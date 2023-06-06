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

            message = Message("Error ao cadastrar o Funcionário", 2)
            return marshal(message, message_fields), 404

class FuncionarioById(Resource):
    def get(self, id):
        funcionario = Funcionario.query.get(id)

        if funcionario is None:
            logger.error(f"Funcionario {id} não encontrado")

            message = Message(f"Funcionario {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Funcionario {id} encontrado com sucesso!")
        return marshal(funcionario, funcionario_fields)

    def put(self, id):
        args = parser.parse_args()

        try:
            funcionario = Funcionario.query.get(id)

            if funcionario is None:
                logger.error(f"Funcionario {id} não encontrado")
                message = Message(f"Funcionario {id} não encontrado", 1)
                return marshal(message, message_fields)

            funcionario.nome = args["nome"]
            funcionario.nascimento = args["nascimento"]
            funcionario.email = args["email"]
            funcionario.telefone = args["telefone"]
            funcionario.senha = args["senha"]
            funcionario.cargo = args["cargo"]


            db.session.add(funcionario)
            db.session.commit()

            logger.info("Funcionario cadastrado com sucesso!")
            return marshal(funcionario, funcionario_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao atualizar o Funcionário", 2)
            return marshal(message, message_fields), 404

    def delete(self, id):
        funcionario = Funcionario.query.get(id)

        if funcionario is None:
            logger.error(f"Funcionario {id} não encontrado")
            message = Message(f"Funcionario {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(funcionario)
        db.session.commit()

        message = Message("Funcionario deletado com sucesso!", 3)
        return marshal(message, message_fields), 200