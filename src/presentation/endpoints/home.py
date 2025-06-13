from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.application.token.token_service import cookie_token_validation, create_access_token, token_validation
from src.application.user.user_error import UserError
from src.application.user.user_service import UserService
from src.settings import TEMPLATES_DIR

home_router = APIRouter()

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@home_router.get(
    path="/",
    status_code=200,
    tags=["home"],
    description="/",
)
async def home(request: Request):
    user = request.session.get("user")
    logged_in = bool(user)

    return templates.TemplateResponse(request=request, name="home.html",
                                      context={"logged_in": logged_in})

@home_router.get("/login")
async def get_login(request: Request):
    user = request.session.get("user")
    token = request.cookies.get("token")
    if user and token:
        return RedirectResponse(url="/dashboard", status_code=status.HTTP_302_FOUND)

    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@home_router.post("/login")
async def post_login(request: Request, username: str = Form(...), password: str = Form(...)):
    user, error = UserService.get_user_by_username(username=username)
    if error:
        if error == UserError.user_not_found:
            error_message = "This user doesn't exist in our base"
        elif error == UserError.incorrect_password:
            error_message = "Incorrect password"
        else:
            error_message = "An unexpected error occurred"
        return templates.TemplateResponse("login.html", {"request": request, "error": error_message})

    # Add user to cookie "session"
    request.session["user"] = user.username

    token = create_access_token(username=user.username)

    response = RedirectResponse(
        url="/dashboard",
        status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="token", value=token, httponly=True)
    return response


@home_router.get(
    path="/dashboard",
    response_class=HTMLResponse,
    status_code=200,
    tags=["dashboard"],
    dependencies=[Depends(cookie_token_validation)]
)
async def dashboard(request: Request):
    user = request.session.get("user")
    if not user:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})


@home_router.get("/logout")
async def logout(request: Request):
    request.session.clear()

    response = RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    response.delete_cookie("token")
    return response
