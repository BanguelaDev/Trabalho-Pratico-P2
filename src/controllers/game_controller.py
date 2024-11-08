import random

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
    elif drope <= 89:
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
