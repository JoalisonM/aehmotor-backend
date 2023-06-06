from flask_restful import Resource, reqparse, marshal

from model.aluno import *
from model.instituicaoEnsino import *
from model.endereco import *
from model.cidade import *
from model.uf import *
from model.prefeitura import *
from model.funcionario import *
from model.passageiro import *
from model.motorista import *
from model.pessoa import *
from model.veiculo import *
from model.rota import *
from model.message import *
from helpers.database import db
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('idMotorista', type=str, help='Problema no id do motorista', required=True)
parser.add_argument('idVeiculo', type=str, help='Problema no id do veiculo', required=True)
parser.add_argument('idInstituicaoEnsino', type=str, help='Problema no id do instituicao', required=True)
parser.add_argument('idPrefeitura', type=str, help='Problema no id do prefeitura', required=True)
parser.add_argument('cidadeOrigem', type=str, help='Problema na cidade de origem', required=True)
parser.add_argument('cidadeDestino', type=str, help='Problema na cidade de destino', required=True)
parser.add_argument('qtdAlunos', type=str, help='Problema na quantidade de alunos', required=True)
parser.add_argument('horarioSaida', type=str, help='Problema no horario da saida', required=True)
parser.add_argument('horarioChegada', type=str, help='Problema no horario da entrada', required=True)



class Rotas(Resource):
    def get(self):
        logger.info("Ufs listados com sucesso!")
        rotas = Rota.query.all()
        return marshal(rotas, rota_fields), 200

    def post(self):
        args = parser.parse_args()
        try:
            idMotorista = args["idMotorista"]
            idVeiculo = args["idVeiculo"]
            idInstituicaoEnsino = args["idInstituicaoEnsino"]
            idPrefeitura = args["idPrefeitura"]
            cidadeOrigem = args["cidadeOrigem"]
            cidadeDestino = args["cidadeDestino"]
            qdtAlunos = args["qdtAlunos"]
            horarioSaida = args["horarioSaida"]
            horarioChegada = args["horarioChegada"]

            rota = Rota(idMotorista, idVeiculo, idInstituicaoEnsino, idPrefeitura, cidadeOrigem, cidadeDestino, qdtAlunos, horarioSaida, horarioChegada )

            db.session.add(rota)
            db.session.commit()

            logger.info("Rota cadastrada com sucesso!")

            return marshal(rota, rota_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao cadastrar a rota", 2)
            return marshal(message, message_fields), 404

class RotaById(Resource):
    def get(self, id):
        rota = rota.query.get(id)

        if rota is None:
            logger.error(f"Rota {id} não encontrado")

            message = Message(f"Rota {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Rota {id} encontrado com sucesso!")
        return marshal(rota, rota_fields)

    def put(self, id):
        args = parser.parse_args()

        try:
            rota = Rota.query.get(id)

            if rota is None:
                logger.error(f"Rota {id} não encontrado")
                message = Message(f"Rota{id} não encontrado", 1)
                return marshal(message, message_fields)

            rota.idMotorista = args["idMotorista"]
            rota.idVeiculo = args["idVeiculo"]
            rota.idInstituicaoEnsino = args["idInstituicaoEnsino"]
            rota.idPrefeitura = args["idPrefeitura"]
            rota.cidadeOrigem = args["cidadeOrigem"]
            rota.cidadeDestino = args["cidadeDestino"]
            rota.qdtAlunos = args["qdtAlunos"]
            rota.horarioSaida = args["horarioSaida"]
            rota.horarioChegada = args["horarioChegada"]

            db.session.add(rota)
            db.session.commit()

            logger.info("Rota cadastrado com sucesso!")
            return marshal(rota, rota_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao atualizar a Uf", 2)
            return marshal(message, message_fields), 404

    def delete(self, id):
        rota = Rota.query.get(id)

        if rota is None:
            logger.error(f"Rota {id} não encontrado")
            message = Message(f"Rota {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(rota)
        db.session.commit()

        message = Message("Rota deletado com sucesso!", 3)
        return marshal(message, message_fields), 200