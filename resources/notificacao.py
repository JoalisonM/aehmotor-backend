import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import request
from flask_restful import Resource
from helpers.auth.token_handler.token_verificador import token_verifica
from helpers.database import db
from model.aluno import *
from model.motorista import * 
from model.viagem import *
from model.pretensao import *

class EnviarEmailResource(Resource):
    @token_verifica
    def post(self, refresh_token, token_id):
        # Obter dados do formulário da solicitação POST
        #nome = data.get('nome')
        destinatarios = db.session.query(Aluno.email)\
            .join(Motorista, Motorista.id_funcionario==Viagem.id_funcionario)\
            .join(Viagem, Viagem.id==Pretensao.id_viagem)\
            .join(Pretensao, Pretensao.id_aluno==Aluno.id_pessoa)\
            .filter(Motorista.id_funcionario==token_id).all()
        mensagem = "Ei, o ônibus chegou !!!"

        if not all([destinatarios, mensagem]):
            return {'message': 'Erro: Todos os campos são obrigatórios'}, 400

        try:
            enviar_email(destinatarios, mensagem)
            return {'message': 'E-mail enviado com sucesso'}
        except Exception as e:
            return {'message': f'Erro ao enviar o e-mail: {str(e)}'}, 500

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
                mensagem_mime['To'] = destinatario
                mensagem_mime['Subject'] = assunto          
                mensagem_mime.attach(MIMEText(corpo, 'plain'))

                server.sendmail(remetente, destinatario, mensagem_mime.as_string())


