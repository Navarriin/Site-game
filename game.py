from flask import Blueprint, render_template, request
from random import randint

# cria um Bp com a logica 
game_bp = Blueprint('game', __name__)

# pagina principal com joginho
@game_bp.route('/', methods=['GET', 'POST'])
def index():
    # conferindo se o metodo e get ou post
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # gera um numero aleatorio e o armazena
        numero = randint(1,10)
        # em caso de erro, chama a funcao (error)
        try:
            palpite = int(request.form.get("name"))
        except ValueError:
            return error()
        # compara se o numero digitado e igual o aleatorio
        if palpite == numero:
            return render_template('vitoria.html')
        else:
            return render_template('derrota.html')

# rota para um possivel erro
@game_bp.route('/error')
def error():
    return render_template('error.html')