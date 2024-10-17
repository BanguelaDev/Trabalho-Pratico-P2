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
    'pontos de vida': 3,
    
    'atributos': {
        'força': 3, # O professor pediu pra deixar tudo em 1, mas no desafio dos monstros o personagem tem q ter 3 de força..
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
    
def desafioDoCofre():
    print("Começando o desafio do cofre!\n")
    print("O enigma funcionará da seguinte maneira, o cofre terá um numero aleatório de 3 a 18, e você terá 3 dados de 6 faces, jogue os 3 dados e tenha a sorte do total dos números ser o número do cofre escolhido. \nBoa sorte aventureiro!\n")
    
    
        
def desafioDosMonstros():
    print("Começando o desafio dos monstros!\n")
    
    
def main():
    
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
            
            for i in range(4): # Looping de 1 a 4
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