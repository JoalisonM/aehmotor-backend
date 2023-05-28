"""adjusted relationships

Revision ID: e855b69e6289
Revises: e8ed3c5a3d18
Create Date: 2023-05-27 21:30:39.021211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e855b69e6289'
down_revision = 'e8ed3c5a3d18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('veiculo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cidade', sa.String(), nullable=False),
    sa.Column('qtdPassageiros', sa.Integer(), nullable=False),
    sa.Column('tipoVeiculo', sa.String(), nullable=False),
    sa.Column('placa', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instituicaoEnsino',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('telefone', sa.String(), nullable=False),
    sa.Column('idEndereco', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idEndereco'], ['endereco.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('aluno',
    sa.Column('idPessoa', sa.Integer(), nullable=False),
    sa.Column('matricula', sa.String(), nullable=False),
    sa.Column('curso', sa.String(), nullable=False),
    sa.Column('turno', sa.String(), nullable=False),
    sa.Column('idInstituicaoEnsino', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idInstituicaoEnsino'], ['instituicaoEnsino.id'], ),
    sa.ForeignKeyConstraint(['idPessoa'], ['pessoa.id'], ),
    sa.PrimaryKeyConstraint('idPessoa'),
    sa.UniqueConstraint('matricula')
    )
    op.create_table('funcionario',
    sa.Column('idPessoa', sa.Integer(), nullable=False),
    sa.Column('cargo', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['idPessoa'], ['pessoa.id'], ),
    sa.PrimaryKeyConstraint('idPessoa')
    )
    op.create_table('motorista',
    sa.Column('idFuncionario', sa.Integer(), nullable=False),
    sa.Column('idVeiculo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idFuncionario'], ['funcionario.idPessoa'], ),
    sa.ForeignKeyConstraint(['idVeiculo'], ['veiculo.id'], ),
    sa.PrimaryKeyConstraint('idFuncionario')
    )
    op.create_table('passageiro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idAluno', sa.Integer(), nullable=True),
    sa.Column('cidadeOrigem', sa.String(), nullable=False),
    sa.Column('cidadeDestino', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['idAluno'], ['aluno.idPessoa'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prefeitura',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('secretario', sa.Integer(), nullable=True),
    sa.Column('idEndereco', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idEndereco'], ['endereco.id'], ),
    sa.ForeignKeyConstraint(['secretario'], ['funcionario.idPessoa'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rota',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idMotorista', sa.Integer(), nullable=True),
    sa.Column('idVeiculo', sa.Integer(), nullable=True),
    sa.Column('idInstituicaoEnsino', sa.Integer(), nullable=True),
    sa.Column('idPrefeitura', sa.Integer(), nullable=True),
    sa.Column('cidadeOrigem', sa.String(), nullable=False),
    sa.Column('cidadeDestino', sa.String(), nullable=False),
    sa.Column('qdtAlunos', sa.Integer(), nullable=False),
    sa.Column('horarioSaida', sa.DateTime(), nullable=False),
    sa.Column('horarioChegada', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['idInstituicaoEnsino'], ['instituicaoEnsino.id'], ),
    sa.ForeignKeyConstraint(['idMotorista'], ['motorista.idFuncionario'], ),
    sa.ForeignKeyConstraint(['idPrefeitura'], ['prefeitura.id'], ),
    sa.ForeignKeyConstraint(['idVeiculo'], ['veiculo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('instituto_ensino')
    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.alter_column('numero',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False)

    with op.batch_alter_table('pessoa', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('tipo', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pessoa', schema=None) as batch_op:
        batch_op.drop_column('tipo')
        batch_op.drop_column('senha')

    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.alter_column('numero',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)

    op.create_table('instituto_ensino',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('telefone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('idEndereco', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['idEndereco'], ['endereco.id'], name='instituto_ensino_idEndereco_fkey'),
    sa.PrimaryKeyConstraint('id', name='instituto_ensino_pkey')
    )
    op.drop_table('rota')
    op.drop_table('prefeitura')
    op.drop_table('passageiro')
    op.drop_table('motorista')
    op.drop_table('funcionario')
    op.drop_table('aluno')
    op.drop_table('instituicaoEnsino')
    op.drop_table('veiculo')
    # ### end Alembic commands ###
