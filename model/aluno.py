from flask_restful import fields
from helpers.database import db
from model.pessoa import *
#from model.instituicaoEnsino import *

aluno_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'nascimento': fields.DateTime,
  'email': fields.String,
  'telefone': fields.String,
  'endereco': endereco_fields,
  'matricula' : fields.String,
  'curso' : fields.String,
  'turno' : fields.String,
  #'instituicaoEnsino': instituicaoEnsino_fields,
}

class Aluno(Pessoa, db.Model):

  __mapper_args__ = {'polymorphic_identify': 'aluno'}

  #id = db.Column(db.Integer, db.ForeignKey('pessoa.id'))
  matricula = db.Column(db.String, unique=True, nullable=False, primary_key=True)
  curso = db.Column(db.String, unique=True, nullable=False)
  turno = db.Column(db.String, unique=True, nullable=False)
  #idInstituicaoEnsino =  db.Column(db.Integer, db.ForeignKey('instituicaoEnsino.id'))
  #aluno = db.relationship("Aluno", uselist=False, backref="instituicaoEnsino")
  passageiro = db.relationship("Passageiro", uselist=False, backref="aluno")

  def __init__(self, nome, nascimento, email, telefone, idEndereco, matricula, curso, turno, idInstituicaoEnsino):
    super().__init__(nome, nascimento, email, telefone, idEndereco)
    self.idInstituicaoEnsino = idInstituicaoEnsino
    self.curso = curso
    self.turno = turno
    self.matricula = matricula

  def __repr__(self):
    return f'<Aluno {self.matricula}>'