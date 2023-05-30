from flask_restful import Api
from flask import Flask, Blueprint

from helpers.cors import cors
from helpers.database import db, migrate
from resources.pessoa import *
#from resources.aluno import Alunos, AlunoById
from resources.pessoa import Pessoas, PessoaById
from resources.uf import Ufs, UfById
from resources.instituicaoEnsino import InstituicoesDeEnsino, InstituicaoDeEnsinoById

# create the app
app = Flask(__name__)

# restful
api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix="/api")

DB_URL = "postgresql://postgres:12345@localhost:5432/aehmotor"
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the app with the extension
db.init_app(app)
cors.init_app(app)
migrate.init_app(app, db)

api.add_resource(PessoaResource, '/pessoas')
# api.add_resource(PeopleResource, '/pessoas/<int:person_id>')
#api.add_resource(Alunos, '/alunos')
#api.add_resource(AlunoById, '/alunos/<int:idPessoa>')
api.add_resource(Pessoas, '/pessoas')
api.add_resource(PessoaById, '/pessoas/<int:id>')
api.add_resource(Ufs, '/ufs')
api.add_resource(UfById, '/ufs/<int:id>')
api.add_resource(InstituicoesDeEnsino, '/instituicoesDeEnsino')
api.add_resource(InstituicaoDeEnsinoById, 'instituicoesDeEnsino/<int:id>')


# Blueprints para Restful
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
