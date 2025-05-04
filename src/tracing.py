import logging
from time import time

from fastapi.concurrency import iterate_in_threadpool
from opentelemetry.metrics import get_meter
from opentelemetry.trace import get_tracer
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Match
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from starlette.types import ASGIApp

meter = get_meter("my.meter")


req_count = meter.create_counter(
    name="request_counter_total",
    description="qtd total requests",
)

err_count = meter.create_counter(
    name="error_counter_total",
    description="qtd errors total",
)

active_count = meter.create_up_down_counter(
    name="active_requests",
    description="qtd active requests.",
)

total_time = meter.create_histogram(name="total_request_time", description="time to response a request.")


class TempoMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)
        self.app_name = "great app"

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        method = request.method
        path, is_handled_path = self.get_path(request)

        base_attributes = {"method": method, "path": path}

        if not is_handled_path or path == "/metrics":
            return await call_next(request)

        active_count.add(1, attributes=base_attributes)
        start_time = time()

        tracer = get_tracer(__name__)
        with tracer.start_as_current_span(name="endpoint_tracer") as span:
            try:
                body = await request.body()
                request_body = body.decode("utf-8")
                span.set_attribute("endpoint.request.path", path)
                span.set_attribute("endpoint.request.body", request_body)
                span.set_attribute("endpoint.request.method", method)

                logging.warning(f"request.path {path}")


                response = await call_next(request)

                status_code = response.status_code
                response_body = b""
                async for chunk in response.body_iterator:
                    response_body += chunk
                response.body_iterator = iterate_in_threadpool([response_body])  # Needs to be async

                span.set_attribute("endpoint.response.body", response_body.decode())
                span.set_attribute("endpoint.response.status_code", status_code)
                attributes = base_attributes | {
                    "status_code": status_code,
                }
                req_count.add(1, attributes=attributes)

            except BaseException as e:
                attributes = base_attributes | {
                    "exception_type": type(e).__name__,
                    "status_code": 500,
                }
                req_count.add(1, attributes=attributes)
                err_count.add(1)

                span.set_attribute("endpoint.response.exception", str(e))
                span.set_attribute("endpoint.response.status_code", HTTP_500_INTERNAL_SERVER_ERROR)

                logging.error(f"Error in request: {e}")

                raise e from None

            active_count.add(-1, attributes=base_attributes)
            total_time.record(time() - start_time, attributes=base_attributes)

            return response

    @staticmethod
    def get_path(request: Request) -> tuple[str, bool]:
        for route in request.app.routes:
            match, child_scope = route.matches(request.scope)
            if match == Match.FULL:
                return route.path, True

        return request.url.path, False
