import time
import os
import random

os.system('cls')

raças = ('Humano', 'Guerreiro') # Raças disponíveis


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

# fiz um dicionátio para cada monstro (OBS: o monstro tem esquiva determinada, mas, o personagem vai fazer um teste D20)
monstro_facil = {
    'ataque': 3,
    'defesa': 1,
    'vida': 8,
    'esquiva': 2,
}

monstro_médio = {
    'ataque': 4,
    'defesa': 1,
    'vida': 12,
    'esquiva': 4,
}

monstro_dificil = {
    'ataque': 6,
    'defesa': 2,
    'vida': 20,
    'esquiva': 6,
}

boss = {
    'ataque': 10,
    'defesa': 5,
    'vida': 45,
    'esquiva': 8,
}

# funcaozinha p rolar o d20
def rolar_D20():
    for i in range(4):# só pra ficar bonito
        os.system('cls')
        print(f"Rolando um D20{'.' * i}")
        time.sleep(.7)
    return random.randint(1, 20)

def esquivar (esquiva_personagem, ataque_do_monstro): # teste de esquiva
    d20 = rolar_D20()
    result_esquiva = d20 + esquiva_personagem

    print(f"Você tirou {d20} teste de esquiva")
    print(f"Sua esquiva: {result_esquiva}")

    if result_esquiva >= ataque_do_monstro:
        print("VOCÊ SE ESQUIVOU DO ATAQUE!!!")
        return False
    else:
        print("Você não se esquivou a tempo!!!")
        print("Você recebeu um golpe do monstro")
        return False

# adicionei o acerto critico, eu imaginei isso em forma de função 
def calcular_o_dano (ataque_personagem, defesa_monstro):
    d20 = rolar_D20()
    print(f"Você rolou {d20} no do D20")

    if d20 == 20:
        print("ACERTO CRÍTICO!!!")
        dano = (ataque_personagem * 2) - defesa_monstro
    else:
        dano = ataque_personagem - defesa_monstro
    if dano < 0:# não sei se era necessário, mas add para não ter a possibiladade de dano negativo
        dano = 0 
        return dano
    
def desafioDoCofre():
    print("Começando o desafio do cofre!\n")
    print("O enigma funcionará da seguinte maneira, o cofre terá um numero aleatório de 3 a 18, e você terá 3 dados de 6 faces, jogue os 3 dados e tenha a sorte do total dos números ser o número do cofre escolhido. \nBoa sorte aventureiro!\n")
    
    numero_do_cofre = random.randint(3,18)

    # pensei dessa forma, quem quiser arrumar fica a vontade
    # vamo deixar mais bonitinho, usar o time.sleep pra n ir tudo de uma vez só, vou deixar com outra pessoa
    
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    dado3 = random.randint(1,6)
    somar_os_dados = dado1 + dado2 + dado3

    print(f"Você rolou os dados e essas foram suas seguintes faces: {dado1}, {dado2} e {dado3}")
    print(f"A soma dos dados é: {somar_os_dados}")

    if somar_os_dados == numero_do_cofre:
        print("Parabéns Aventureiro!!! Você conseguiu decifrar o enigma do cofre!!!\n")
    else:
        print("Você não conseguiu decifrar o enigma do cofre, tente novamente Aventureiro!!!")
          
def desafioDosMonstros():
    print("Começando o desafio dos monstros!\n")
    
def imprimirFicha():
    print("-" * 20)
        
    for estatistica, valor in jogador.items(): # Pegando o nome e o valor de dentro do dicionario "jogador"
        if type(valor) is dict: # Se o tipo do valor é um dicionário
            print(f"• {estatistica.capitalize()}:")
            for atributo, valor in valor.items(): # Pegando o nome (atributo) e o valor de dentro do dicionario "valor"
                print(f"•    {atributo.capitalize()}: {valor}")
        else: # Se não for um dicionário
            print(f"• {estatistica.capitalize()}: {valor}")
            gfhffdg
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
    
jogador["nome"] = input("Qual o nome do seu personagem: ").capitalize()
os.system('cls')
        
print(f"Olá jogador {jogador["nome"]}, seja bem vindo ao jogo!!\n")
escolherRaça()

os.system('cls')

print("Tudo pronto para começar, mas antes aqui está sua ficha\n")
imprimirFicha()

while True:
    opção = input("1 - Entrar na caverna e dar inicio ao jogo\n2 - Voltar para a pusada e finalizar o jogo \nO que deseja fazer: ")

    if opção == '1':
            
        print("\nIniciando o jogo.")
        time.sleep(2)
                
        os.system('cls')
            
        d20 = rolar_D20()
        print(f"Você rolou {d20} no D20\n") 
            
        if d20 <= 4: # igual ou menor a 4 é o cofre
            desafioDoCofre()
                
        else: # de 5 pra frente é monstro meu parceiro 
            desafioDosMonstros()
            
    elif opção == "2":
        imprimirFicha()
        exit()
            
    else:
        continue 
