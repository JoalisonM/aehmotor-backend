from flask_restful import fields
from helpers.database import db

pessoa_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'nascimento': fields.String,
  'email': fields.String,
  'telefone': fields.String,
  'senha': fields.String,
  'tipo': fields.String,
}

class Pessoa(db.Model):
  __tablename__ = "pessoa"

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  nascimento = db.Column(db.Date, nullable=False)
  telefone = db.Column(db.String, unique=True, nullable=False)
  senha = db.Column(db.String, nullable=False)
  tipo = db.Column(db.String, nullable=False)

  endereco = db.relationship("Endereco", uselist=False, backref="pessoa")

  __mapper_args__ = {
    "polymorphic_identity": "pessoa",
    "polymorphic_on":tipo
  }

  def __init__(self, nome, email, nascimento, telefone, senha):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.telefone = telefone
    self.nascimento = nascimento

  def __repr__(self):
    return f'<Pessoa {self.nome}>'