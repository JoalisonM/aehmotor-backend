"""mergeando dois heads

Revision ID: c545b07ad068
Revises: 8a76e59fd3bc, cab188b640a1
Create Date: 2023-07-03 17:01:12.627516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c545b07ad068'
down_revision = ('8a76e59fd3bc', 'cab188b640a1')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
