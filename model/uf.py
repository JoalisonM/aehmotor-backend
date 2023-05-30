from flask_restful import fields

from helpers.database import db

uf_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'sigla': fields.String,
}

class Uf(db.Model):
  __tablename__ = "uf"

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String, nullable=False)
  sigla = db.Column(db.String, nullable=False)

  cidade = db.relationship("Cidade", uselist=False, backref="uf")

  def __init__(self, nome, sigla):
    self.nome = nome
    self.sigla = sigla

  def __repr__(self):
    return f'<UF>'