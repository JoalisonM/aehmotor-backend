from flask_restful import fields
from helpers.database import db
from model.rota import rota_fields
from model.instituicaoEnsino import instituicaoEnsino_fields

rota_instituicao_fields = {
  'rota': fields.Nested(rota_fields),
  'instituicao_ensino': fields.Nested(instituicaoEnsino_fields),
}

class RotaInstituicaoEnsino(db.Model):
  __tablename__ = "rota_instituicao"

  id = db.Column(db.Integer, primary_key=True)
  id_rota = db.Column(db.Integer, db.ForeignKey('rota.id'))
  id_instituicao_ensino = db.Column(db.Integer, db.ForeignKey('instituicao_ensino.id'))

  rota = db.relationship(
    'Rota', uselist=False,
    backref=db.backref('rota_instituicao', cascade="all, delete")
  )
  instituicao_ensino = db.relationship(
    'InstituicaoEnsino',
    uselist=False
  )

  def __init__(self, id_rota, id_instituicao_ensino):
    self.id_rota = id_rota
    self.id_instituicao_ensino = id_instituicao_ensino

  def __repr__(self):
    return f"<RotaInstituicaoEnsino>"