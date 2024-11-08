from flask import Flask
from src.routes.auth_routes import auth_bp
from src.routes.game_routes import game_bp
from src.database.db_config import init_db

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
app.secret_key = 'tads'

# Inicializar o banco de dados
init_db()

# Registrar blueprints (Blueprint basicamente divide as rotas em categorias, nesse caso uma p autenticação e outra pro resto, que seria o jogo em si)
app.register_blueprint(auth_bp, url_prefix='/') # Blueprint da parte de autenticação (Login, Logout, Registro...)
app.register_blueprint(game_bp, url_prefix='/game') # Blueprint do jogo em si

if __name__ == "__main__":
    app.run(debug=True)
