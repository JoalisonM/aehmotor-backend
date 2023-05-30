from flask_restful import fields

from helpers.database import db

instituicaoEnsino_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'telefone': fields.String,
  'idEndereco': fields.Integer,
}


class InstituicaoEnsino(db.Model):
  __tablename__ = "instituicaoEnsino"

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String, nullable=False)
  telefone = db.Column(db.String, nullable=False)
  idEndereco = db.Column(db.Integer, db.ForeignKey('endereco.id'))

  rota = db.relationship("Rota", uselist=False, backref="instituicaoEnsino")
  aluno = db.relationship("Aluno", uselist=False, backref="instituicaoEnsino")

  def __init__(self, nome, telefone, idEndereco):
    super().__init__()
    self.nome = nome
    self.telefone = telefone
    self.idEndereco = idEndereco

  def __repr__(self):
    return f'<Endereço>'