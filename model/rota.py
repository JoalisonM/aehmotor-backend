from flask_restful import fields
from helpers.database import db

rota_fields ={
  'id': fields.Integer,
  'id_veiculo':fields.Integer,
  'id_motorista':fields.Integer,
  'id_prefeitura':fields.String,
  'id_instituicao_ensino':fields.Integer,
  'cidade_origem':fields.String,
  'cidade_destino':fields.String,
  'qtd_alunos':fields.Integer,
  'horario_saida':fields.String,
  'horario_chegada':fields.String,
  'turno': fields.String
}

class Rota(db.Model):
  __tablename__ = "rota"

  id = db.Column(db.Integer, primary_key=True)
  id_motorista = db.Column(db.Integer, db.ForeignKey('motorista.id_funcionario'))
  id_veiculo = db.Column(db.Integer, db.ForeignKey('veiculo.id'))
  id_instituicao_ensino = db.Column(db.Integer, db.ForeignKey('instituicao_ensino.id'))
  id_prefeitura = db.Column(db.Integer, db.ForeignKey('prefeitura.id'))
  cidade_origem = db.Column(db.String, nullable=False)
  cidade_destino = db.Column(db.String, nullable=False)
  qtd_alunos = db.Column(db.Integer, nullable=False)
  horario_saida = db.Column(db.Time, nullable=False)
  horario_chegada = db.Column(db.Time, nullable=False)
  turno = db.Column(db.String(20), nullable=False)

  viagem = db.relationship("Viagem", uselist=False, backref="rota")

  def __init__(self, id_motorista, id_veiculo, id_instituicao_ensino,
               id_prefeitura, cidade_origem, cidade_destino, qtd_alunos,
               horario_saida, horario_chegada,turno
  ):
      self.cidade_origem=cidade_origem
      self.cidade_destino=cidade_destino
      self.id_motorista=id_motorista
      self.qtd_alunos=qtd_alunos
      self.id_veiculo=id_veiculo
      self.horario_saida=horario_saida
      self.horario_chegada=horario_chegada
      self.id_prefeitura=id_prefeitura
      self.id_instituicao_ensino=id_instituicao_ensino
      self.turno = turno

  def __repr__(self):
      return f'<Rota>'