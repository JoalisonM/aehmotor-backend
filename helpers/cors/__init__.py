from flask_cors import CORS

cors = CORS(resources={r"/api/*": {"origins": "*"}})
