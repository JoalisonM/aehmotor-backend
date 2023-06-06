from flask_restful import Resource, reqparse, marshal

from model.funcionario import *
from model.pessoa import *
from model.message import *
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('nome', type=str, help='Problema no nome', required=True)
parser.add_argument('nascimento', type=str, help='Problema no nascimento', required=True)
parser.add_argument('email', type=str, help='Problema no email', required=True)
parser.add_argument('telefone', type=str, help='Problema no telefone', required=True)
parser.add_argument('senha', type=str, help='Problema no senha', required=True)
parser.add_argument('cargo', type=str, help='Problema no cargo', required=True)



class Funcionarios(Resource):
    def get(self):
        logger.info("Funcionários listados com sucesso!")
        funcionarios = Funcionario.query.all()
        return marshal(funcionarios, funcionario_fields), 200

    def post(self):
        args = parser.parse_args()
        try:
            nome = args["nome"]
            nascimento = args["nascimento"]
            email = args["email"]
            telefone = args["telefone"]
            senha = args["senha"]
            cargo = args["cargo"]

            funcionario = Funcionario(nome, nascimento, email, telefone, senha, cargo)

            db.session.add(funcionario)
            db.session.commit()

            logger.info("Funcionário cadastrada com sucesso!")

            return marshal(funcionario, funcionario_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao cadastrar funcionário", 2)
            return marshal(message, message_fields), 404

class FuncionarioById(Resource):
    def get(self, id):
        funcionario = Funcionario.query.get(id)

        if funcionario is None:
            logger.error(f"Funcionário {id} não encontrado")

            message = Message(f"Funcionário {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Funcionário {id} encontrado com sucesso!")
        return marshal(funcionario, funcionario_fields)

    def put(self, id):
        args = parser.parse_args()

        try:
            funcionario = Funcionario.query.get(id)

            if funcionario is None:
                logger.error(f"Funcionário {id} não encontrado")
                message = Message(f"Funcionário {id} não encontrado", 1)
                return marshal(message, message_fields)

            funcionario.nome = args["nome"]
            funcionario.email = args["email"]
            funcionario.nascimento = args["nascimento"]
            funcionario.telefone = args["telefone"]
            funcionario.senha = args["senha"]
            funcionario.cargo = args["cargo"]

            db.session.add(funcionario)
            db.session.commit()

            logger.info("Funcionário cadastrado com sucesso!")
            return marshal(funcionario, funcionario_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao atualizar funcionário", 2)
            return marshal(message, message_fields), 404

    def delete(self, id):
        funcionario = Funcionario.query.get(id)

        if funcionario is None:
            logger.error(f"Funcionário {id} não encontrado")
            message = Message(f"Funcionário {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(funcionario)
        db.session.commit()

        message = Message("Funcionário deletado com sucesso!", 3)
        return marshal(message, message_fields), 200