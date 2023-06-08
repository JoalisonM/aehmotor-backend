from flask_restful import fields
from helpers.database import db

prefeitura_fields={
  'id': fields.Integer,
  'nome': fields.String,
  'secretario': fields.Integer,
  'id_endereco': fields.Integer,
}

class Prefeitura(db.Model):
  __tablename__ = "prefeitura"

  id = db.Column(db.Integer, primary_key=True)
  nome=db.Column(db.String, nullable=False)
  secretario = db.Column(db.Integer, db.ForeignKey('funcionario.id_pessoa'), nullable=False)
  id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'), nullable=False)

  rota = db.relationship("Rota", uselist=False, backref="prefeitura")

  def __init__ (self, secretario, id_endereco):
    self.secretario=secretario
    self.id_endereco=id_endereco


  def __repr__(self):
    return f'<Prefeitura secretario:{self.secreatario}>'