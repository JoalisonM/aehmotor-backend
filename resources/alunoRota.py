from flask_restful import Resource, fields, marshal
from helpers.database import db
from model.aluno import *
from model.alunoRota import *
from model.instituicaoEnsino import *
from model.rota import *
from model.rotaInstituicaoEnsino import *


class AlunoRotas(Resource):
    def get(self, id):
        query = db.session.query(
            Rota.turno,
            Rota.cidade_destino,
            Rota.horario_saida,
            Rota.horario_chegada,
            InstituicaoEnsino.nome
        )\
        .select_from(Aluno)\
        .join(RotaInstituicaoEnsino, Aluno.id_instituicao_ensino == RotaInstituicaoEnsino.id_instituicao_ensino)\
        .join(Rota, RotaInstituicaoEnsino.id_rota == Rota.id)\
        .join(InstituicaoEnsino, RotaInstituicaoEnsino.id_instituicao_ensino==InstituicaoEnsino.id)\
        .filter(Aluno.id_pessoa == id).all()

        result = []
        for tupla in query:
            aluno_rota_dict = {
                'turno': tupla[0],
                'cidade_destino': tupla[1],
                'horario_saida': tupla[2],
                'horario_chegada': tupla[3],
                'nome_instituicao_ensino': tupla[4]
            }
            result.append(aluno_rota_dict)

        return(marshal(result, aluno_rota_fields))