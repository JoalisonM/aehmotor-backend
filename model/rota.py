from flask_restful import fields
from helpers.database import db

rota_fields ={
  'id': fields.Integer,
  'idVeiculo':fields.Integer,
  'idMotorista':fields.Integer,
  'idPrefeitura':fields.String,
  'idInstituicaoEnsino':fields.Integer,
  'cidadeOrigem':fields.String,
  'cidadeDestino':fields.String,
  'qdtAlunos':fields.Integer,
  'horarioSaida':fields.DateTime,
  'horarioChegada':fields.DateTime,
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
  qdt_alunos = db.Column(db.Integer, nullable=False)
  horario_saida = db.Column(db.DateTime, nullable=False)
  horario_chegada = db.Column(db.DateTime, nullable=False)

  def __init__(self, cidadeOrigem, cidadeDestino, idMotorista, qdtAlunos, idVeiculo, horarioSaida, horarioChegada, idPrefeitura, idInstituicaoEnsino):
      self.cidadeOrigem=cidadeOrigem
      self.cidadeDestino=cidadeDestino
      self.idMotorista=idMotorista
      self.qdtAlunos=qdtAlunos
      self.idVeiculo=idVeiculo
      self.horarioSaida=horarioSaida
      self.horarioChegada=horarioChegada
      self.idPrefeitura=idPrefeitura
      self.idInstituicaoEnsino=idInstituicaoEnsino

  def __repr__(self):
      return f'<Rota>'