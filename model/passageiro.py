from flask_restful import fields
from helpers.database import db

passageiro_fields = {
  'id': fields.Integer,
  'idAluno': fields.Integer,
  'cidadeOrigem': fields.String,
  'cidadeDestino' : fields.String,
}

class Passageiro(db.Model):
  __tablename__ = "passageiro"

  id = db.Column(db.Integer, primary_key=True)
  id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id_pessoa'))
  cidade_origem = db.Column(db.String, nullable=False)
  cidade_destino = db.Column(db.String, nullable=False)

  def __init__(self, idAluno, cidadeOrigem, cidadeDestino):
    self.idAluno = idAluno
    self.cidadeOrigem = cidadeOrigem
    self.cidadeDestino = cidadeDestino

  def __repr__(self):
    return f'<Passageiro {self.idAluno}>'