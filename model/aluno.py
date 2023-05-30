from flask_restful import fields
from helpers.database import db
from model.pessoa import Pessoa

aluno_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'nascimento': fields.String,
  'email': fields.String,
  'telefone': fields.String,
  'senha' : fields.String,
  'matricula' : fields.String,
  'curso' : fields.String,
  'turno' : fields.String,
  'idInstituicaoEnsino': fields.Integer,
}

class Aluno(Pessoa):
  __tablename__ = "aluno"

  idPessoa = db.Column(db.Integer ,db.ForeignKey("pessoa.id"), primary_key=True)
  matricula = db.Column(db.String, unique=True, nullable=True)
  curso = db.Column(db.String, nullable=True)
  turno = db.Column(db.String, nullable=True)
  idInstituicaoEnsino =  db.Column(
    db.Integer, db.ForeignKey('instituicaoEnsino.id'), nullable=True
  )

  passageiro = db.relationship("Passageiro", uselist=False, backref="aluno")

  __mapper_args__ = {"polymorphic_identity": "aluno"}

  def __init__(self, nome, email, nascimento, telefone, senha, matricula, curso, turno, idInstituicaoEnsino):
    super().__init__(nome, email, nascimento, telefone, senha)
    self.curso = curso
    self.turno = turno
    self.matricula = matricula
    self.idInstituicaoEnsino = idInstituicaoEnsino

  def __repr__(self):
    return f'<Aluno {self.matricula}>'