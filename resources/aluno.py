from sqlalchemy import or_
from flask_restful import Resource, reqparse, marshal
from helpers.auth.token_handler.token_verificador import token_verifica
from model.aluno import *
from model.instituicaoEnsino import *
from model.passageiro import *
from model.message import *
from model.pretensao import *
from helpers.database import db
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('nome', type=str, help='Problema no nome', required=True)
parser.add_argument('email', type=str, help='Problema no email', required=True)
parser.add_argument('nascimento', type=str, help='Problema no nascimento', required=True)
parser.add_argument('telefone', type=str, help='Problema no telefone', required=True)
parser.add_argument('senha', type=str, help='Problema na senha', required=True)
parser.add_argument('matricula', type=str, help='Problema na matrícula', required=False)
parser.add_argument('curso', type=str, help='Problema no curso', required=False)
parser.add_argument('turno', type=str, help='Problema no turno', required=False)
parser.add_argument('id_instituicao_ensino', type=int, help='Problema na faculdade', required=False)


class Alunos(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Alunos listados com sucesso!")
        alunos = Aluno.query.all()
        return marshal(alunos, aluno_fields), 200

    def post(self):
        args = parser.parse_args()
        try:
            nome = args["nome"]
            email = args["email"]
            nascimento = args["nascimento"]
            telefone = args["telefone"]
            senha = args["senha"]
            matricula = args["matricula"]
            curso = args["curso"]
            turno = args["turno"]
            id_instituicao_ensino = args["id_instituicao_ensino"]

            aluno = Aluno(nome, email, nascimento, telefone, senha, matricula, curso, turno, id_instituicao_ensino)

            db.session.add(aluno)
            db.session.commit()

            logger.info("Aluno cadastrado com sucesso!")

            return marshal(aluno, aluno_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao cadastrar o aluno", 2)
            return marshal(message, message_fields), 404

class AlunoById(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo, idPessoa):
        aluno = Aluno.query.get(idPessoa)

    #     if aluno is None:
    #         logger.error(f"Aluno {idPessoa} não encontrado")

    #         message = Message(f"Aluno {idPessoa} não encontrado", 1)
    #         return marshal(message), 404

    #     logger.info(f"Aluno {idPessoa} encontrado com sucesso!")
    #     return marshal(aluno, aluno_fields)

    @token_verifica
    def put(self,refresh_token, token_tipo, idPessoa):
        args = parser.parse_args()

        try:
            aluno = Aluno.query.get(idPessoa)

            if aluno is None:
                logger.error(f"Aluno {idPessoa} não encontrado")
                message = Message(f"Aluno {idPessoa} não encontrado", 1)
                return marshal(message, message_fields)

            aluno.nome = args["nome"]
            aluno.email = args["email"]
            aluno.nascimento = args["nascimento"]
            aluno.telefone = args["telefone"]
            aluno.senha = args["senha"]
            aluno.matricula = args["matricula"]
            aluno.curso = args["curso"]
            aluno.turno = args["turno"]
            aluno.id_instituicao_ensino = args["id_instituicao_ensino"]

            db.session.add(aluno)
            db.session.commit()

            logger.info("Aluno cadastrado com sucesso!")
            return marshal(aluno, aluno_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao atualizar o aluno", 2)
            return marshal(message, message_fields), 404

    @token_verifica
    def delete(self, refresh_token, token_tipo, idPessoa):
        aluno = Aluno.query.get(idPessoa)

        if aluno is None:
            logger.error(f"Aluno {idPessoa} não encontrado")
            message = Message(f"Aluno {idPessoa} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(aluno)
        db.session.commit()

        message = Message("Aluno deletado com sucesso!", 3)
        return marshal(message, message_fields), 200

class AlunoByNome(Resource):
    def get(self, query):
        try:
            queryInt = int(query)
            alunos = Aluno.query.filter(
                or_(
                    Aluno.id_pessoa == queryInt,
                    Aluno.id_instituicao_ensino == queryInt,
                    Aluno.telefone == query,
                    Aluno.matricula == query,
                )
            ).all()
        except ValueError:
            alunos = Aluno.query.filter(
                or_(
                    Aluno.nome.ilike(f"%{query}%"),
                    Aluno.curso.ilike(f"%{query}%"),
                    Aluno.email.ilike(f"%{query}%"),
                    Aluno.turno.ilike(f"%{query}%"),
                )
            ).all()

        if not alunos:
            logger.error(f"Aluno {query} não encontrado")

            message = Message(f"Aluno {query} não encontrado", 1)
            return marshal(message, message_fields), 404

        logger.info(f"Aluno {query} encontrado com sucesso!")
        return marshal(alunos, aluno_fields), 200
