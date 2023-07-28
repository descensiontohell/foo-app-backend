"""Create Item

Revision ID: c254dcb938f9
Revises: 
Create Date: 2023-07-22 12:17:40.984265

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c254dcb938f9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "item",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("item")
