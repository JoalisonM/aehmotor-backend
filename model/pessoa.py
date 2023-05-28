from flask_restful import fields
from helpers.database import db

pessoa_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'nascimento': fields.DateTime,
  'email': fields.String,
  'telefone': fields.String,
  'senha': fields.String,
  'idEndereco': fields.Integer,
}

class Pessoa(db.Model):
  __tablename__ = "pessoa"

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  nascimento = db.Column(db.Date, nullable=False)
  telefone = db.Column(db.String, unique=True, nullable=False)
  senha = db.Column(db.String, nullable=False)
  idEndereco = db.Column(db.Integer, db.ForeignKey('endereco.id'))
  tipo = db.Column(db.String, nullable=False)

  __mapper_args__ = {
    "polymorphic_identity": "pessoa",
    "polymorphic_on": tipo
  }

  def __init__(self, nome, email, nascimento, telefone, senha, idEndereco):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.telefone = telefone
    self.nascimento = nascimento
    self.idEndereco = idEndereco

  def __repr__(self):
    return f'<Pessoa {self.nome}>'