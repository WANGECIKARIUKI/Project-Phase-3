"""Renaming customers to customer

Revision ID: 8ed0733c76f9
Revises: 1b8fbf1d0c22
Create Date: 2023-11-06 09:49:42.313524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ed0733c76f9'
down_revision = '1b8fbf1d0c22'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('customers', 'customer')


def downgrade():
    op.rename_table('customers', 'customer')
