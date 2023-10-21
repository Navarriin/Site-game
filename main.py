from flask import Flask
# importando a Blueprint
from game import game_bp

# comando basico para startar o flask
app = Flask(__name__)

# registrando a bp
app.register_blueprint(game_bp)

# rota com debug ativado 
if __name__ == '__main__':
    app.run(port=5000,host='localhost',debug=True)