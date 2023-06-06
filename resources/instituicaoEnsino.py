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
parser.add_argument('telefone', type=str, help='Problema no telefone', required=True)
parser.add_argument('idEndereco', type=int, help='Problema no endereço', required=False)


class InstituicoesDeEnsino(Resource):
    def get(self):
        logger.info("Instituições listados com sucesso!")
        instituicoesEnsino = InstituicaoEnsino.query.all()
        return marshal(instituicoesEnsino, instituicaoEnsino_fields), 200

    def post(self):
        args = parser.parse_args()
        try:
            nome = args["nome"]
            telefone = args["telefone"]
            idEndereco = args["idEndereco"]

            instituicaoEnsino = InstituicaoEnsino(nome, telefone, idEndereco)

            db.session.add(instituicaoEnsino)
            db.session.commit()

            logger.info("Instituição cadastrado com sucesso!")

            return marshal(instituicaoEnsino, instituicaoEnsino_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao cadastrar a Instituição", 2)
            return marshal(message, message_fields), 404

class InstituicaoDeEnsinoById(Resource):
    def get(self, id):
        instituicaoEnsino = InstituicaoEnsino.query.get(id)

        if instituicaoEnsino is None:
            logger.error(f"Instituição de Ensino {id} não encontrado")

            message = Message(f"Instituição de Ensino {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Instituição de Ensino {id} encontrado com sucesso!")
        return marshal(instituicaoEnsino, instituicaoEnsino_fields)

    def put(self, id):
        args = parser.parse_args()

        try:
            instituicaoEnsino = Aluno.query.get(id)

            if instituicaoEnsino is None:
                logger.error(f"Instituição de Ensino {id} não encontrado")
                message = Message(f"Instituição de Ensino {id} não encontrado", 1)
                return marshal(message, message_fields)

            instituicaoEnsino.nome = args["nome"]
            instituicaoEnsino.telefone = args["telefone"]
            instituicaoEnsino.idEndereco = args["idEndereco"]

            db.session.add(instituicaoEnsino)
            db.session.commit()

            logger.info("Instituição de Ensino cadastrado com sucesso!")
            return marshal(instituicaoEnsino, instituicaoEnsino_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao atualizar a Instituição de Ensino", 2)
            return marshal(message, message_fields), 404

    def delete(self, id):
        instituicaoEnsino = InstituicaoEnsino.query.get(id)

        if instituicaoEnsino is None:
            logger.error(f"Instituição de Ensino {id} não encontrado")
            message = Message(f"Instituição de Ensino {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(instituicaoEnsino)
        db.session.commit()

        message = Message("Instituição de Ensino deletado com sucesso!", 3)
        return marshal(message, message_fields), 200