from flask_restful import Resource, reqparse, marshal

from model.motorista import *
from model.pessoa import *
from model.message import *
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('nome', type=str, help='Problema no nome', required=True)
parser.add_argument('email', type=str, help='Problema no email', required=True)
parser.add_argument('nascimento', type=str, help='Problema no nascimento', required=True)
parser.add_argument('telefone', type=str, help='Problema no telefone', required=True)
parser.add_argument('idEndereco', type= int, help='Problema no id do endereço', required=True)
parser.add_argument('senha', type=str, help='Problema na senha', required=True)
parser.add_argument('cargo', type=str, help='Problema no cargo', required=True)
parser.add_argument('idVeiculo', type=int, help='Problema no id de veículo')



class Motoristas(Resource):
    def get(self):
        logger.info("Motoritas listados com sucesso!")
        motoristas = Motorista.query.all()
        return marshal(motoristas, motorista_fields), 200

    def post(self):
        args = parser.parse_args()
        try:
            nome = args["nome"]
            email = args["email"]
            nascimento = args["nascimento"]
            telefone = args["telefone"]
            idEndereco = args["idEndereco"]
            senha = args["senha"]
            cargo = args["cargo"]
            idVeiculo = args["idVeiculo"]
            

            motorista = Motorista(nome, email, nascimento, telefone,idEndereco, senha,cargo,idVeiculo)

            db.session.add(motorista)
            db.session.commit()

            logger.info("Motorista cadastrado com sucesso!")

            return marshal(motorista, motorista_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao cadastrar motorista", 2)
            return marshal(message, message_fields), 404

class MotoristaById(Resource):
    def get(self, id):
        motorista = Motorista.query.get(id)

        if motorista is None:
            logger.error(f"Motorista {id} não encontrado")

            message = Message(f"Motorista {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Motorista {id} encontrado com sucesso!")
        return marshal(motorista, motorista_fields)

    def put(self, id):
        args = parser.parse_args()

        try:
            motorista = Motorista.query.get(id)

            if motorista is None:
                logger.error(f"Motorista {id} não encontrado")
                message = Message(f"Motorista {id} não encontrado", 1)
                return marshal(message, message_fields)

            motorista.nome = args["nome"]
            motorista.email = args["email"]
            motorista.nascimento = args["nascimento"]
            motorista.telefone = args["telefone"]
            motorista.idEndereco = args["idEndereco"]
            motorista.senha = args["senha"]
            motorista.cargo = args["cargo"]
            motorista.idVeiculo = args["idVeiculo"]
            

            db.session.add(motorista)
            db.session.commit()

            logger.info("Motorista cadastrado com sucesso!")
            return marshal(motorista, motorista_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao atualizar motorista", 2)
            return marshal(message, message_fields), 404

    def delete(self, id):
        motorista = Motorista.query.get(id)

        if motorista is None:
            logger.error(f"Motorista {id} não motorista")
            message = Message(f"Motorista {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(motorista)
        db.session.commit()

        message = Message("Motorista deletado com sucesso!", 3)
        return marshal(message, message_fields), 200