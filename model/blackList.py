from helpers.database import db
from datetime import datetime


class BlackList(db.Model):
    __tablename__ = "tb_blacklist"


    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), unique=True, nullable=True)
    data_expiracao = db.Column(db.DateTime, nullable=False)

    def __init__(self, token, data_expiracao):
        self.token = token
        self.data_expiracao = data_expiracao