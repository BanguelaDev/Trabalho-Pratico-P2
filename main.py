import os
from flask import Flask, render_template, request, redirect, url_for, session
import random
import copy

os.system('cls')

raças = ('Humano', 'Guerreiro') # Raças disponíveis
app.secret_key = 'tads'

jogador = {
    'nome': "Desconhecido",
    'raça': "Desconhecida",
    
    'nível': 1,
    'experiência': 0,
    
    'atributos': {
        'ataque': 2,
        'defesa': 1,
        'vida': 8,
        'esquiva': 1,
    },
    
    'moedas' : {
        'bronze': 0,
        'prata': 0,
        'ouro': 0
    }
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
        accounts[username] = {'password': password, 'player': copy.deepcopy(jogador)}
        accounts[username]['player']['name'] = username
        session['username'] = username
        return redirect(url_for('ticketRegister'))
    
def desafioDoCofre():
    print("Começando o desafio do cofre!\n")
    print("O enigma funcionará da seguinte maneira, o cofre terá um numero aleatório de 3 a 18, e você terá 3 dados de 6 faces, jogue os 3 dados e tenha a sorte do total dos números ser o número do cofre escolhido. \nBoa sorte aventureiro!\n")
    
    numero_do_cofre = random.randint(3,18)

    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    dado3 = random.randint(1,6)
    somar_os_dados = dado1 + dado2 + dado3

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
    



    
    
def imprimirFicha():
    print("-" * 20)
        
    for estatistica, valor in jogador.items(): # Pegando o nome e o valor de dentro do dicionario "jogador"
        if type(valor) is dict: # Se o tipo do valor é um dicionário
            print(f"• {estatistica.capitalize()}:")
            for atributo, valor in valor.items(): # Pegando o nome (atributo) e o valor de dentro do dicionario "valor"
                print(f"•    {atributo.capitalize()}: {valor}")
        else: # Se não for um dicionário
            print(f"• {estatistica.capitalize()}: {valor}")
       
    print("-" * 20, "\n")
        
def escolherRaça():
    print("-" * 20)
        
    print("Raças:")
        
    for i in range(len(raças)): # Looping de 1 até a quantidade de raças disponiveis (dicionario)
        raça = raças[i] # Pegando o nome da raça usando o numero como índice (i)
        print(f"{i + 1} - {raça}") # Mostrando a raça em ordem (1 a x)
            
    print("-" * 20)
            
    index = int(input("Escolha sua raça: "))
        
    if index < 0 or index > len(raças): # Se o indice for menor que 0 ou o indice for maior que a quantidade de raças disponíveis no dicionario "raças"
         print("Opção inválida\n")
         exit()
        
    raça = raças[index - 1] # A raça é igual ao indice (numero escolhido) - 1
    jogador["raça"] = raça # Definindo a raça do jogador pra raça escolhida
    


if __name__ == "__main__":
    app.run(debug=True)