from flask import Flask, render_template, request, redirect, url_for, session
import random
import copy

app = Flask(__name__)
app.secret_key = 'tads'

player_template = {
    'name': 'Unknown',
    'vocation': 'Unknown',
    'race': 'Unknown',
    'exp': 0,
    'level': 0,
    'attributes': {'attack': 2, 'defense': 1, 'health': 8, 'dodge': 1},
}

vocations = {
    'warrior': {'attack': 2, 'defense': 1, 'dodge': -1},
    'archer': {'attack': 2, 'dodge': 1, 'defense': -1, 'health': -1},
    'paladin': {'attack': 1, 'dodge': -1, 'defense': 1, 'health': 1},
}

races = {
    'dwarf': {'defense': 1, 'health': 2},
    'elf': {'attack': 1, 'dodge': 2},
    'human': {'attack': 1, 'dodge': 1, 'defense': 1, 'health': 1},
}

# to fazendo aqueles requisitos inicias que o professor mandou fazer, o sistema e os testes e assim adiante

monstros = {
    'fraco': {'ataque':3, 'defesa':1, 'vida':8, 'esquiva':2},
    'medio': {'ataque':4, 'defesa':1, 'vida':12, 'esquiva':4,},
    'dificil': {'ataque':6, 'defesa':2, 'vida':20, 'esquiva':6,},
    'chefe': {'ataque':10, 'defesa':5, 'vida':45, 'esquiva':8,},
}
# o sistema de D20
def D20():
    return random.randint(1,20)

def escolha_do_monstro():# usando o D100 pra ver qual monstro vai dropar 
    drope = random.randint(0,100)
    if drope <= 39:
        return monstros['fraco']
    elif drope <= 69:
        return monstros['medio']
    elif drope <=89:
        return monstros['dificil']
    else:
        return monstros['chefe']

# teste ataque (pedido de socorro: to entendendo nada)
# depois lanço o english cabuloso, se não vou me confundir 
def teste_de_ataque(ataque_usuario, defesa_inimigo):
    rolar_dado = D20()  
    ataque_final = rolar_dado + ataque_usuario
    critico = rolar_dado == 20  
    return ataque_final >= defesa_inimigo, critico

# calcular o dano
def calcular_dano(ataque_usuario, defesa_inimigo, dano_critico):
    dano_inicial = max(0, ataque_usuario - defesa_inimigo)
    if dano_critico:
        return dano_inicial * 2
    return dano_inicial

# Simulando um banco de dados com um dicionário, trocar por sql (não faço ideia de como funciona)
accounts = {}

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/loginRegister", methods=['POST'])
def loginRegister():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in accounts: # Caso a conta ja exista
        if accounts[username]['password'] == password: # Se a senha for correta
            session['username'] = username
            return redirect(url_for('ticket')) # Levar pra ficha
        else:
            return "Senha incorreta! Tente novamente.", 401
    else:
        accounts[username] = {'password': password, 'player': copy.deepcopy(player_template)}
        accounts[username]['player']['name'] = username
        session['username'] = username
        return redirect(url_for('ticketRegister'))
    
@app.route("/ticketRegister", methods=['GET'])
def ticketRegister():
    username = session.get('username')
    
    if username in accounts and \
       accounts[username]['player']['race'] != 'Unknown' or \
       accounts[username]['player']['vocation'] != 'Unknown':
        return redirect(url_for('ticket'))

    return render_template("ticketRegister.html", races=races, vocations=vocations)

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('homepage'))

@app.route("/ticket", methods=['GET', 'POST'])
def ticket():
    username = session.get('username')
    if username and username in accounts:
        player_info = accounts.get(username, {}).get('player')
        if player_info:
            return render_template("ticket.html", player=player_info)
    
    return redirect(url_for('homepage'))

# tinha esquecido da route
@app.route("/teste_de_ataque", methods=['POST'])
def ataque_route():
    username = session.get('username')
    if not username:
        return redirect(url_for('homepage'))
    
    player = accounts[username][player] if username in accounts else None
    monstros = escolha_do_monstro()

    if not player or not monstros:
        return "Erro ao carregar dados do player ou monstro.", 500
    
    dano = 0
    
    ataque, critico = teste_de_ataque(player['attributes']['attack'], monstros['defesa'])
    if ataque:
        dano = calcular_dano(player['attributes']['attack'], monstros['defesa'], critico)
        resultado = f"Ataque Bem-Sucedido!!! {'Dano Crítico!!!' if critico else 'Dano Normal.'} Dano causado: {dano}"
    else:
        resultado = "O ataque falhou"

    return render_template("resultado_ataque.html", resultado = resultado)  
    



    
    
    


if __name__ == "__main__":
    app.run(debug=True)
