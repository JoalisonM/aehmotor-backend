"""alteracoes no passageiro

Revision ID: 193fb16dc8f4
Revises: a80ace0b027f
Create Date: 2023-06-05 16:31:20.037152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '193fb16dc8f4'
down_revision = 'a80ace0b027f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('passageiro', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['idAluno'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('passageiro', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
