from starlette_admin.contrib.sqla import Admin, ModelView

from src.data.db_orm.connection import writing_engine
from src.data.db_orm.tables.tbl_books import TblBooks

# Create admin
STARLETTE_ADMIN = Admin(writing_engine, title="Example: SQLAlchemy")

# Add view
STARLETTE_ADMIN.add_view(ModelView(TblBooks))