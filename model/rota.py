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
  idMotorista = db.Column(db.Integer, db.ForeignKey('motorista.idFuncionario'))
  idVeiculo = db.Column(db.Integer, db.ForeignKey('veiculo.id'))
  idInstituicaoEnsino = db.Column(db.Integer, db.ForeignKey('instituicaoEnsino.id'))
  idPrefeitura = db.Column(db.Integer, db.ForeignKey('prefeitura.id'))
  cidadeOrigem = db.Column(db.String, nullable=False)
  cidadeDestino = db.Column(db.String, nullable=False)
  qdtAlunos = db.Column(db.Integer, nullable=False)
  horarioSaida = db.Column(db.DateTime, nullable=False)
  horarioChegada = db.Column(db.DateTime, nullable=False)

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