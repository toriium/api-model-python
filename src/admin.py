from starlette_admin.contrib.sqla import Admin, ModelView

from src.data.db_orm.connection import writing_engine
from src.data.db_orm.tables.tbl_books import TblBooks
from src.settings import APP_NAME

STARLETTE_ADMIN = Admin(writing_engine, title=APP_NAME)


# class HomeView(CustomView):
#     async def render(self, request: Request, templates: Jinja2Templates) -> Response:
#         return templates.TemplateResponse(
#             request,
#             name="admin_home.html",
#             context={"latest_posts": ..., "top_users": ...},
#         )


# STARLETTE_ADMIN.add_view(HomeView(label="Home", icon="fa fa-home", path="/"))

STARLETTE_ADMIN.add_view(ModelView(TblBooks, icon="fa fa-home"))
