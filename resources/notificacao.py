import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_restful import Resource
from helpers.auth.token_handler.token_verificador import token_verifica
from helpers.database import db
from helpers.base_logger import *
from model.aluno import *
from model.motorista import *
from model.viagem import *
from model.funcionario import *
from model.viagem import *
from model.pretensao import *

class EnviarEmailChegada(Resource):
    @token_verifica
    def post(self, refresh_token, token_id):
        try:
            # Obter dados do formulário da solicitação POST
            motorista_alias = db.aliased(Motorista, flat=True)
            destinatarios = db.session.query(Aluno.email)\
                .join(Pretensao, Aluno.id_pessoa==Pretensao.id_aluno)\
                .join(Viagem, Pretensao.id_viagem == Viagem.id)\
                .join(motorista_alias, Viagem.id_funcionario == motorista_alias.id_funcionario)\
                .filter(motorista_alias.id_funcionario==token_id).all()
            mensagem = "Ei, o ônibus chegou!!!"

            logger.info(f"{destinatarios}")

            if not all([destinatarios, mensagem]):
                return {'message': 'Erro: Todos os campos são obrigatórios'}, 400

            enviar_email(destinatarios, mensagem)
            return {'message': 'E-mail enviado com sucesso'}
        except Exception as e:
            logger.error(f"error: {e}")
            return {'message': f'Erro ao enviar o e-mail'}, 404

class EnviarEmailSaida(Resource):
    @token_verifica
    def post(self, refresh_token, token_id):
        try:
            # Obter dados do formulário da solicitação POST
            motorista_alias = db.aliased(Motorista, flat=True)
            destinatarios = db.session.query(Aluno.email)\
                .join(Pretensao, Aluno.id_pessoa==Pretensao.id_aluno)\
                .join(Viagem, Pretensao.id_viagem == Viagem.id)\
                .join(motorista_alias, Viagem.id_funcionario == motorista_alias.id_funcionario)\
                .filter(motorista_alias.id_funcionario==token_id).all()
            mensagem = "Ei, o ônibus está saindo do campus!!!"

            logger.info(f"{destinatarios}")

            if not all([destinatarios, mensagem]):
                return {'message': 'Erro: Todos os campos são obrigatórios'}, 400

            enviar_email(destinatarios, mensagem)
            return {'message': 'E-mail enviado com sucesso'}
        except Exception as e:
            logger.error(f"error: {e}")
            return {'message': f'Erro ao enviar o e-mail'}, 404

def enviar_email(destinatarios, mensagem):
    remetente = 'aehmotorsistemas@gmail.com'
    senha = 'viftwaiwfudjzeat'
    #destinatario = email
    assunto = 'Aehmotor'
    corpo = f'{mensagem}'


    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(remetente, senha)
        #server.sendmail(remetente, destinatario, mensagem_mime.as_string())

        for destinatario in destinatarios:
            #vai pegar o id da instituição e através do nome e vai conferir
            #e filtrar os alunos que estão cadastrados na rota
            mensagem_mime = MIMEMultipart()
            mensagem_mime['From'] = remetente
            mensagem_mime['To'] = destinatario[0]
            mensagem_mime['Subject'] = assunto
            mensagem_mime.attach(MIMEText(corpo, 'plain'))

            server.sendmail(remetente, destinatario, mensagem_mime.as_string())


