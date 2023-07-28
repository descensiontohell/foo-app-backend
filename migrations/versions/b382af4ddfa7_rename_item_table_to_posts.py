"""rename item table to posts

Revision ID: b382af4ddfa7
Revises: c254dcb938f9
Create Date: 2023-07-28 17:03:32.332126

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "b382af4ddfa7"
down_revision = "c254dcb938f9"
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table("item", "posts")


def downgrade():
    op.rename_table("posts", "item")
