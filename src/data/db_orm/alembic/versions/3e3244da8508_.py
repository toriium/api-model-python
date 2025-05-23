"""empty message

Revision ID: 3e3244da8508
Revises: 
Create Date: 2025-03-01 23:25:23.065994

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '3e3244da8508'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_books',
    sa.Column('isbn', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('author', sa.String(length=200), nullable=False),
    sa.Column('publisher', sa.String(length=500), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('pages', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isbn'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tbl_logs',
    sa.Column('log_message', sa.Text(), nullable=False),
    sa.Column('log_date', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbl_users',
    sa.Column('username', sa.String(length=500), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_users')
    op.drop_table('tbl_logs')
    op.drop_table('tbl_books')
    # ### end Alembic commands ###
