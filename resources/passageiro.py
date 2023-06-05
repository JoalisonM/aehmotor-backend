from flask_restful import Resource, reqparse, marshal

from model.aluno import*
from model.passageiro import*
from model.pessoa import*
from model.message import *
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('idAluno', type=int, help= 'Problema no id de aluno', required=True)
parser.add_argument('cidadeOrigem', type=str, help='Problema no campo cidade de origem', required=True)
parser.add_argument('cidadeDestino', type=str, help='Problema no campo  cidade de destino', required=True)

class Passageiros(Resource):
    def get(self):
        logger.info("Passageiros listados com sucesso!")
        passageiros = Passageiro.query.all()
        return marshal(passageiros, passageiro_fields), 200
    
    def post(self,idAluno):
        args = parser.parse_args()
        try:
            idAluno = args["idAluno"]
            cidadeOrigem= args["cidadeOrigem"]
            cidadeDestino = args["cidadeDestino"]
            
            
            passageiro = Passageiro(idAluno, cidadeOrigem, cidadeDestino)
            
            db.session.add(passageiro)
            db.session.commit()
            
            logger.info("Passageiro cadastrado com sucesso!")
            
            return marshal(passageiro, passageiro_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")
            
            message = Message("Erro ao cadastradar passageiro", 2)
            return marshal(message, message_fields), 404
        
class PassageiroById(Resource):
    def get(self, id):
        passageiro = Passageiro.query.get(id)
        
        if passageiro is None:
            logger.error(f"Passageiro {id} não encontrado")
            
            message = Message(f"Passageiro {id} não encotrado", 1)
            return marshal(message), 404
        
        logger.info(f"Passageiro {id} encontrado com sucesso!")
        return marshal(passageiro, passageiro_fields), 200
    
    def put(self, id):
        args = parser.parse_args()
        
        try:
            passageiro = Passageiro.query.get(id)
            if passageiro is None:
                logger.error(f"Passageiro {id} não encontrado")
                message = Message(f"Passageiro {id} não encontrado", 1)
                return marshal(message, message_fields)
            
            passageiro.id = args["id"]
            passageiro.cidadeOrigem = args["cidadeOrigem"]
            passageiro.cidadeDestino = args["cidadeDestino"]
            
            db.session.add(passageiro)
            db.session.commit()
            
            logger.info("Passageiro cadastrado com sucesso!")
            return marshal(passageiro, passageiro_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")
            
            message = Message("Erro ao atualizar passageiro", 2)
            return marshal(passageiro, passageiro_fields), 404
        
    def delete(self, id):
        passageiro = Passageiro.query.get(id)
        
        if passageiro is None:
            logger.error(f"Passageiro {id} não encontrado")
            message = Message(f"Passageiro {id} não encontrado", 1)
            return marshal (message, message_fields)
        
        db.session.delete(passageiro)
        db.session.commit()
        
        message = Message("Passageiro deletada com sucesso!", 3)
        return marshal(message, message_fields), 200        