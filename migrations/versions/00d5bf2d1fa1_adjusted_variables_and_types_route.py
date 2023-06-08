"""adjusted variables and types route

Revision ID: 00d5bf2d1fa1
Revises: acc5f06bf81f
Create Date: 2023-06-07 19:57:34.710326

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '00d5bf2d1fa1'
down_revision = 'acc5f06bf81f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cidade', schema=None) as batch_op:
        batch_op.alter_column('latitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=8),
               existing_nullable=False)
        batch_op.alter_column('longitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=8),
               existing_nullable=False)

    with op.batch_alter_table('rota', schema=None) as batch_op:
        batch_op.alter_column('horario_saida',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Time(),
               existing_nullable=False)
        batch_op.alter_column('horario_chegada',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Time(),
               existing_nullable=False)

    with op.batch_alter_table('uf', schema=None) as batch_op:
        batch_op.alter_column('latitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=8),
               existing_nullable=False)
        batch_op.alter_column('longitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=8),
               existing_nullable=False)
        batch_op.drop_column('11')
        batch_op.drop_column('norte')
        batch_op.drop_column('-63.34')
        batch_op.drop_column('-10.83')
        batch_op.drop_column('rondônia')
        batch_op.drop_column('ro')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('uf', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ro', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('rondônia', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('-10.83', sa.REAL(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('-63.34', sa.REAL(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('norte', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('11', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.alter_column('longitude',
               existing_type=sa.Float(precision=8),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('latitude',
               existing_type=sa.Float(precision=8),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('rota', schema=None) as batch_op:
        batch_op.alter_column('horario_chegada',
               existing_type=sa.Time(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
        batch_op.alter_column('horario_saida',
               existing_type=sa.Time(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)

    with op.batch_alter_table('cidade', schema=None) as batch_op:
        batch_op.alter_column('longitude',
               existing_type=sa.Float(precision=8),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('latitude',
               existing_type=sa.Float(precision=8),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
