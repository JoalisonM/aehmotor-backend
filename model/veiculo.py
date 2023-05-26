from flask_restful import fields
from helpers.database import db

veiculo_fields={
    'id':fields.Interger,
    'cidade':fields.String,
    'qtdPassageiros':fields.Interger,
    'tipoVeiculo':fields.String,
    'placa':fields.String,
}

class Veiculo(db.Model):
    id=db.Colum(db.Interger,primary_key=True)
    cidade=db.Column(db.String, nullable=False)
    qtdPassageiros=db.Colum(db.Interger,nullable=False)
    tipoVeiculo=db.Column(db.String, nullable=False)
    placa=db.Colum(db.String,nullable=False)
    rota_id = db.Column(db.String, db.ForeignKey('rota.id'))
    
    
    def __init__(self,id,cidade,qdtPassageiros,tipoVeiculo,placa):
        self.id=id
        self.cidade=cidade
        self.qtdPassageiros=qdtPassageiros
        self.tipoVeiculo=tipoVeiculo
        self.placa=placa
        
    def __repr__(self):
        return f'<Veiculo {self.id}>'
        