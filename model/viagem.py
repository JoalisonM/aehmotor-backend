from flask_restful import fields
import datetime
from helpers.database import db
from model.rota import rota_fields

viagem_fields = {
    'id': fields.Integer,
    'rota': fields.Nested(rota_fields)
}


class Viagem(db.Model):
    __tablename__ = "viagem"

    # SQL
    id = db.Column(db.Integer, primary_key=True)
    id_rota = db.Column(db.Integer, db.ForeignKey('rota.id'))
    data = db.Column(db.DateTime, nullable=False)
    criacao = db.Column(db.DateTime, nullable=False,
                        default=datetime.datetime.utcnow)

    # OO
    rota = db.relationship("Rota", uselist=False)

    def __init__(self, rota):
        self.rota = rota

    def __repr__(self):
        return f'<Viagem data={self.data}>'
