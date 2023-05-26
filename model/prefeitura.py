from flask_restful import fields
from helpers.database import db

prefeitura_fields={
    'id':fields.Interger,
    'secretario':fields.Interger,
    'idEndereco':fields.Interger,
}

class Prefeitura(db.Model):
    id =db.Colum(db.String,primary_key=True)
    secretario=db.Colum(db.Interger,nullable=True)
    idEndereco=db.Colum(db.Interger,nullable=True)
    
def __init__ (self,id,secretario,idEndereco):
    self.id=id
    self.secretario=secretario
    self.idendereco=idEndereco


def __repr__(self):
    return f'<Prefeitura secretario:{self.secreatario}>'