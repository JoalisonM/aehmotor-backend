from flask_restful import Resource, reqparse, marshal
from helpers.auth.token_handler.token_verificador import token_verifica
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
from model.rotaInstituicaoEnsino import *
from helpers.database import db
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('nome', type=str, help='Problema no nome', required=True)
parser.add_argument('telefone', type=str, help='Problema no telefone', required=True)
parser.add_argument('endereco', type=dict, help='Problema no endereço', required=False)


class InstituicoesDeEnsino(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Instituições listados com sucesso!")
        instituicoesEnsino = InstituicaoEnsino.query.all()
        return marshal(instituicoesEnsino, instituicaoEnsino_fields), 200

    @token_verifica
    def post(self, refresh_token, token_tipo):
        args = parser.parse_args()
        try:
            nome = args["nome"]
            telefone = args["telefone"]
            enderecoResponse = args["endereco"]

            #Criar endereço 
            endereco = Endereco(
                cep=enderecoResponse["cep"],
                numero=enderecoResponse["numero"],
                complemento=enderecoResponse["complemento"],
                referencia=enderecoResponse["referencia"],
                logradouro=enderecoResponse["logradouro"],
                id_cidade=enderecoResponse["id_cidade"],
                id_pessoa=enderecoResponse["id_pessoa"]
            )

            db.session.add(endereco)
            db.session.commit()

            instituicaoEnsino = InstituicaoEnsino(nome, telefone, id_endereco=endereco.id)

            db.session.add(instituicaoEnsino)
            db.session.commit()

            logger.info("Instituição de Ensino cadastrado com sucesso!")

            return marshal(instituicaoEnsino, instituicaoEnsino_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao cadastrar a Instituição", 2)
            return marshal(message, message_fields), 404

class InstituicaoDeEnsinoById(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo, id):
        instituicaoEnsino = InstituicaoEnsino.query.get(id)

        if instituicaoEnsino is None:
            logger.error(f"Instituição de Ensino {id} não encontrado")

            message = Message(f"Instituição de Ensino {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Instituição de Ensino {id} encontrado com sucesso!")
        return marshal(instituicaoEnsino, instituicaoEnsino_fields)

    @token_verifica
    def put(self,refresh_token, token_tipo, id):
        args = parser.parse_args()

        try:
            instituicaoEnsino = InstituicaoEnsino.query.get(id)

            if instituicaoEnsino is None:
                logger.error(f"Instituição de Ensino {id} não encontrado")
                message = Message(f"Instituição de Ensino {id} não encontrado", 1)
                return marshal(message, message_fields)

            instituicaoEnsino.nome = args["nome"]
            instituicaoEnsino.telefone = args["telefone"]
            instituicaoEnsino.id_endereco = args["id_endereco"]

            db.session.add(instituicaoEnsino)
            db.session.commit()

            logger.info("Instituição de Ensino cadastrado com sucesso!")
            return marshal(instituicaoEnsino, instituicaoEnsino_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao atualizar a Instituição de Ensino", 2)
            return marshal(message, message_fields), 404

    @token_verifica
    def delete(self, refresh_token, token_tipo, id):
        instituicaoEnsino = InstituicaoEnsino.query.get(id)

        if instituicaoEnsino is None:
            logger.error(f"Instituição de Ensino {id} não encontrado")
            message = Message(f"Instituição de Ensino {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(instituicaoEnsino)
        db.session.commit()

        message = Message("Instituição de Ensino deletado com sucesso!", 3)
        return marshal(message, message_fields), 200
    
class InstituicaoDeEnsinoByNome(Resource):
    def get(self, nome):
        instituicaoEnsino = InstituicaoEnsino.query.filter(
            InstituicaoEnsino.nome.ilike(f"%{nome}%")
        ).all()

        if instituicaoEnsino is None:
            logger.error(f"Instituição de Ensino {id} não encontrado")

            message = Message(f"Instituição de Ensino {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Instituição de Ensino {id} encontrado com sucesso!")
        return marshal(instituicaoEnsino, instituicaoEnsino_fields), 200