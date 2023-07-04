from flask_restful import Resource, fields, marshal
from helpers.database import db
from model.aluno import *
from model.alunoRota import *
from model.instituicaoEnsino import *
from model.rota import *


class AlunoRota(Resource):
    def get(self, id):
        query = db.session.query(
            Rota.turno,
            Rota.cidade_destino,
            Rota.horario_saida,
            Rota.horario_chegada,
            InstituicaoEnsino.nome
        )\
        .join(Rota, Aluno.id_instituicao_ensino == Rota.id_instituicao_ensino)\
        .join(InstituicaoEnsino, Rota.id_instituicao_ensino == InstituicaoEnsino.id)\
        .filter(Aluno.id_pessoa == id).all()

        result = []
        for tupla in query:
            aluno_rota_dict = {
                'turno': tupla[0],
                'cidade_origem': tupla[1],
                'horario_saida': tupla[2],
                'horario_chegada': tupla[3],
                'nome_instituicao_ensino': tupla[4]
            }
            result.append(aluno_rota_dict)

        return(marshal(result, aluno_rota_fields))
