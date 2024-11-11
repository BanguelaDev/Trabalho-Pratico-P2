# Funções que mexe nos dados do usuário/jogador
# Usuario e Jogador sao diferentes, o usuário armazena a autenticação (nome e senha), enquanto o jogador armazena o restante do jogo, seus atributos, etc.

import sqlite3
from src.database.db_config import DATABASE

def add_user(username, password): # Adicionar o usuário no banco de dados, com seu respectivo nome e senha
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return user_id

def get_user(username): # Verificar se o usuário existe no banco de dados
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_player(user_id, name): # Adicionar o jogador no banco de dados, com o respectivo id do usuário e nome (que pode ser diferente do nome do usuário)
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO players (user_id, name) VALUES (?, ?)
    ''', (user_id, name))
    conn.commit()
    conn.close()
    
def update_player(user_id, update_fields): # Atualizando os dados do jogador que está dentro do dicionário
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    for field, value in update_fields.items():
        cursor.execute(f'UPDATE players SET {field} = ? WHERE user_id = ?', (value, user_id))

    conn.commit()
    conn.close()
    
    return get_player_by_user_id(user_id)


def get_player_by_user_id(user_id): # Pegando o jogador usando o respectivo id do usuário
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM players WHERE user_id = ?', (user_id,))
    player_data = cursor.fetchone()
    conn.close()

    if player_data:
        columns = [desc[0] for desc in cursor.description]  # Pega os nomes das colunas
        player_dict = dict(zip(columns, player_data))  # Cria um dicionário
        
        return player_dict # Fiz isso pois o player_data é uma tupla, dificultando bastante a manipulação, então achei melhor transformar em um dicionário
    return None
