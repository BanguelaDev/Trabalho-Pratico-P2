import time
import os
import random

os.system('cls')

raças = ('Humano', 'Guerreiro')

jogador = {
    'nome': "Desconhecido",
    'raça': "Desconhecida",
    
    'nível': 1,
    'experiência': 0,
    'pontos de vida': 3,
    
    'atributos': {
        'força': 3, # Vc pediu pra deixar tudo em 1, mas no desafio dos monstros o personagem tem q ter 3 de força..
        'defesa': 1,
        'agilidade': 1,
        'inteligencia': 1,
        'carisma': 1,
        'sabedoria': 1,
    },
    
    'moedas' : {
        'bronze': 0,
        'prata': 0,
        'ouro': 0
    }
}

# fiz um dicionátio para cada monstro (OBS: o monstro tem esquiva determinada, mas, o personagem vai fazer um teste D20)
monstro_facil = {
    'pontos de vida': 8,
    'defesa': 1,
    'esquiva': 2,
}

monstro_médio = {
    'pontos de vida':  12,
    'defesa': 1,
    'esquiva': 4,
}

monstro_dificil = {
    'ponto de vida': 20,
    'defesa': 2,
    'esquiva': 6,
}

boss = {
    'pontos de vida': 45,
    'defesa': 10,
    'esquiva': 8
}
    
def desafioDoCofre():
    print("Começando o desafio do cofre!\n")
    print("O enigma funcionará da seguinte maneira, o cofre terá um numero aleatório de 3 a 18, e você terá 3 dados de 6 faces, jogue os 3 dados e tenha a sorte do total dos números ser o número do cofre escolhido. \nBoa sorte aventureiro!\n")
    numero_do_cofre = random.randint(3,18)

    # pensei dessa forma, quem quiser arrumar fica a vontade
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
    
    
def main():
    
    def imprimirFicha():
        print("-" * 20)
        
        for estatistica, valor in jogador.items():
            if type(valor) is dict: # Não achei outra forma, ent pensei nisso (se o tipo do valor é um dicionário)
                print(f"• {estatistica.capitalize()}:")
                for atributo, valor in valor.items():
                    print(f"•    {atributo.capitalize()}: {valor}")
            else:
                print(f"• {estatistica.capitalize()}: {valor}")
            
        print("-" * 20, "\n")
        
    def escolherRaça():
        print("-" * 20)
        
        print("Raças:")
        
        for i in range(len(raças)):
            raça = raças[i]
            print(f"{i + 1} - {raça}")
            
        print("-" * 20)
            
        index = int(input("Escolha sua raça: "))
        
        if index < 0 or index > len(raças):
            print("Opção inválida\n")
            exit()
        
        raça = raças[index - 1]
        jogador["raça"] = raça
    
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
            
            for i in range(4):
                os.system('cls')
                print(f"Iniciando o jogo{'.' * i}")
                time.sleep(.5)
                
            os.system('cls')
            
            valorRandom = random.randint(1, 8)
            print(f"Um valor aleatório foi gerado, e caiu em: {valorRandom} \n")
            
            if valorRandom >= 1 or valorRandom <= 2:
                desafioDoCofre()
                
            elif valorRandom >= 3 or valorRandom <= 8:
                desafioDosMonstros()
            
        elif opção == "2":
            imprimirFicha()
            exit()
            
        else:
            continue
        
main()