import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request
from flask_restful import Resource

class EnviarEmailResource(Resource):
    def post(self):
        # Obter dados do formulário da solicitação POST
        data = request.get_json()
        #ome = data.get('nome')
        destinatarios = data.get('destinatarios')
        mensagem = data.get('mensagem')

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


