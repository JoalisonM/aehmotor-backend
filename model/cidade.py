from flask_restful import fields

from helpers.database import db

cidade_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'sigla': fields.String,
  'idUf':fields.Integer,
}

class Cidade(db.Model):
  __tablename__ = "cidade"

  codigo_ibge = db.Column(db.Integer, primary_key=True, nullable=False)
  nome = db.Column(db.String(100), nullable=False)
  latitude = db.Column(db.Float(8), nullable=False)
  longitude = db.Column(db.Float(8), nullable=False)
  capital = db.Column(db.Boolean, nullable=False)
  codigo_uf = db.Column(db.Integer, db.ForeignKey('uf.codigo_uf'), nullable=False)
  siafi_id = db.Column(db.String(4), nullable=False)
  ddd = db.Column(db.Integer, nullable=False)
  fuso_horario = db.Column(db.String, nullable=False)

  endereco = db.relationship("Endereco", uselist=False, backref="cidade")

  def __init__(self, nome, sigla, idUf):
    self.nome = nome
    self.sigla = sigla
    self.idUf = idUf

  def __repr__(self):
    return f'<Cidade>'