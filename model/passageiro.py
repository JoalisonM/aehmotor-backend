from flask_restful import fields
from helpers.database import db
from model.aluno import aluno_fields

passageiro_fields = {
  'idAluno': fields.Integer,
  'cidadeOrigem': fields.String,
  'cidadeDestino' : fields.String,
}

class passageiro(db.Model):
  __mapper_args__ = {'polymorphic_identify': 'passageiro'}

  idAluno = db.Column(db.Integer, db.ForeignKey('aluno.id'))
  cidadeOrigem = db.Column(db.String, unique=True, nullable=False)
  cidadeDestino = db.Column(db.String, unique=True, nullable=False)
 
  def __init__(self, idAluno, cidadeOrigem, cidadeDestino):
    self.idAluno = idAluno
    self.cidadeOrigem = cidadeOrigem
    self.cidadeDestino = cidadeDestino
    

  def __repr__(self):
    return f'<Passageiro {self.idAluno}>'