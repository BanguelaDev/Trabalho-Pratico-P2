from flask import Flask, render_template, request, redirect, url_for, session
import random

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

# o sistema de D20
def D20():
    return random.randint(1,20)

# teste ataque (pedido de socorro: to entendendo nada)
# depois lanço o english cabuloso, se não vou me confundir 
def teste_de_ataque(ataque_usuario, defesa_inimigo):
    rolar_dado = D20()  
    ataque_final = rolar_dado + ataque_usuario  
    CRITICO = rolar_dado == 20 # isso aqui é em relação ao dano critico

    if ataque_final >= defesa_inimigo:
        return True, CRITICO 
    return False, False 

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
        accounts[username] = {'password': password, 'player': player_template.copy()}
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


if __name__ == "__main__":
    app.run(debug=True)
