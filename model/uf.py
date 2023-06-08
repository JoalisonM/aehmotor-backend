from flask_restful import fields

from helpers.database import db

uf_fields = {
  'codigo_uf': fields.Integer,
  'uf': fields.String,
  'nome': fields.String,
  'latitude': fields.Float,
  'longitude': fields.Float,
  'regiao': fields.String,
}

class Uf(db.Model):
  __tablename__ = "uf"

  codigo_uf = db.Column(db.Integer, primary_key=True)
  uf = db.Column(db.String(2), nullable=False)
  nome = db.Column(db.String(100), nullable=False)
  latitude = db.Column(db.Float(8), nullable=False)
  longitude = db.Column(db.Float(8), nullable=False)
  regiao = db.Column(db.String(12), nullable=False)

  cidade = db.relationship("Cidade", uselist=False, backref="uf")

  def __init__(self, nome, sigla):
    self.nome = nome
    self.sigla = sigla

  def __repr__(self):
    return f'<UF>'