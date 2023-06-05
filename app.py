from flask_restful import Api
from flask import Flask, Blueprint

from helpers.cors import cors
from helpers.database import db, migrate
from resources.funcionario import Funcionarios, FuncionarioById
from resources.passageiro import Passageiros, PassageiroById
from resources.cidade import Cidades,CidadeById
from resources.endereco import Enderecos, EnderecoById
from resources.aluno import Alunos, AlunoById
from resources.pessoa import Pessoas, PessoaById

# create the app
app = Flask(__name__)

# restful
api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix="/api")

DB_URL = "postgresql://postgres:1234@localhost:5432/aehmotor"
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the app with the extension
db.init_app(app)
cors.init_app(app)
migrate.init_app(app, db)

api.add_resource(Funcionarios,'/funcionarios')
api.add_resource(FuncionarioById,'/funcionarios/<int:id>')
api.add_resource(Passageiros, '/passageiros')
api.add_resource(PassageiroById,'/passageiros/<int:id>')
api.add_resource(Alunos, '/alunos')
api.add_resource(AlunoById, '/alunos/<int:idPessoa>')
api.add_resource(Pessoas, '/pessoas')
api.add_resource(PessoaById, '/pessoas/<int:id>')
api.add_resource(Cidades,'/cidades')
api.add_resource(CidadeById,'/cidades/<int:id>')
api.add_resource(Enderecos,'/enderecos')
api.add_resource(EnderecoById,'/enderecos/<int:id>')


# Blueprints para Restful
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
