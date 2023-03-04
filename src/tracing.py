from functools import wraps

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


class OTLPProvider:
    def __init__(self):
        # set the service name to show in traces
        resource = Resource(attributes={"service.name": "service_fastapi"})

        # set the tracer provider
        self.__tracer_provider = TracerProvider(resource=resource)
        trace.set_tracer_provider(tracer_provider=self.__tracer_provider)

        # set the processor
        otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
        span_processor = BatchSpanProcessor(otlp_exporter)
        self.__tracer_provider.add_span_processor(span_processor=span_processor)

    @property
    def tracer_provider(self) -> TracerProvider:
        return self.__tracer_provider


def tracer_endpoint():
    def handler_func(function):
        @wraps(function)
        async def wrapper(*args, **kwargs):
            with tracer.start_as_current_span(name='endpoint_tracer') as span:
                func_return = await function(*args, **kwargs)
                if isinstance(func_return, JSONResponse):
                    span.set_attribute("endpoint.response.body", func_return.body)
                    span.set_attribute("endpoint.response.status_code", func_return.status_code)
                elif isinstance(func_return, HTTPException):
                    span.set_attribute("endpoint.response.body", str(func_return.detail))
                    span.set_attribute("endpoint.response.status_code", func_return.status_code)
                else:
                    raise ValueError("Response must be [JSONResponse,HTTPException] object")

                return func_return

        return wrapper

    return handler_func


def start_instrumentation(app: FastAPI):
    FastAPIInstrumentor.instrument_app(app, tracer_provider=tracer_provider)
    RedisInstrumentor().instrument()


tracer_provider = OTLPProvider().tracer_provider
tracer = tracer_provider.get_tracer(__name__)
