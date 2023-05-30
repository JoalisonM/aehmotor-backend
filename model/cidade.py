from flask_restful import fields

from helpers.database import db

cidade_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'sigla': fields.String,
}

class Cidade(db.Model):
  __tablename__ = "cidade"

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String, nullable=False)
  sigla = db.Column(db.String, nullable=False)
  idUf = db.Column(db.Integer, db.ForeignKey('uf.id'))

  endereco = db.relationship("Endereco", uselist=False, backref="cidade")

  def __init__(self, nome, sigla, idUf):
    self.nome = nome
    self.sigla = sigla
    self.idUf = idUf

  def __repr__(self):
    return f'<Cidade>'