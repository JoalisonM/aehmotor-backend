from flask_restful import fields
from helpers.database import db

prefeitura_fields={
  'id': fields.Integer,
  'secretario': fields.Integer,
  'idEndereco': fields.Integer,
}

class Prefeitura(db.Model):
  __tablename__ = "prefeitura"

  id = db.Column(db.Integer, primary_key=True)
  secretario = db.Column(db.Integer, db.ForeignKey('funcionario.id'))
  idEndereco = db.Column(db.Integer, db.ForeignKey('endereco.id'))

  rota = db.relationship("Rota", uselist=False, backref="prefeitura")

  def __init__ (self, secretario, idEndereco):
    self.secretario=secretario
    self.idendereco=idEndereco


  def __repr__(self):
    return f'<Prefeitura secretario:{self.secreatario}>'