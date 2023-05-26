from flask_restful import fields
from helpers.database import db



rota_fields ={
    'cidadeOrigem':fields.String,
    'cidadeDestino':fields.String,
    'idMotorista':fields.String,
    'qdtAlunos':fields.Integer,
    'veiculo':fields.Integer,
    'horarioSaida':fields.DateTime,
    'horarioChegada':fields.DateTime,
    'instituicaoEnsino':fields.String,
    'idPrefeitura':fields.String,
    'idInstituicaoEnsino':fields.String,
}

class Rota(db.Model):
    cidadeOrigem=db.Column(db.String,primary_key=True)
    cidadeDestino=db.Column(db.String, nullable=False)
    idMotorista=db.Colum(db.String,nullable=False)
    qdtAlunos=db.Colum(db.Interger,nullable=False)
    idVeiculo=db.relationship("Veiculo",uselist=False,backref="rota")
    horarioSaida=db.Colum(db.Time,nullable=False)
    horarioChegada=db.Colum(db.Time,nullable=False)
    idPrefeitura=db.Colum(db.String,nullable=False)
    idInstituicaoEnsino=db.Colum(db.String,nullable=False)    

def __init__(self,cidadeOrigem,cidadeDestino,motorista,qdtAlunos,veiculo,horarioSaida,horarioChegada,prefeitura,idInstituicaoEnsino):
    
    self.cidadeOrigem=cidadeOrigem
    self.cidadeDestino=cidadeDestino
    self.idMotorista=motorista
    self.qdtAlunos=qdtAlunos
    self.idVeiculo=veiculo
    self.horarioSaida=horarioSaida
    self.horarioChegada=horarioChegada
    self.idPrefeitura=prefeitura
    self.idInstituicaoEnsino=idInstituicaoEnsino
    
    
def __repr__(self):
    return f'<Rota cidadeOrigem:{self.cidadeOrigem} cidadeDestino:{self.cidadeDestino} motorista:{self.motorista} >'