from flask_restful import fields

from helpers.database import db

institutoEnsino_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'sigla': fields.String,
}


class InstitutoEnsino(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String, nullable=False)
  telefone = db.Column(db.String, nullable=False)
  endereco = db.relationship("Endereco", uselist=False, backref="pessoa")

  def __init__(self, nome, telefone, endereco):
    super().__init__()
    self.nome = nome
    self.telefone = telefone
    self.endereco = endereco

  def __repr__(self):
    return f'<Endereço>'