# Funções que mexe nos dados dos usuários/jogadores

import sqlite3
from src.database.db_config import DATABASE

def add_user(username, password):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return user_id

def get_user(username):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_player(user_id, name):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO players (user_id, name) VALUES (?, ?)
    ''', (user_id, name))
    conn.commit()
    conn.close()
    
def update_player(user_id, update_fields):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    for field, value in update_fields.items():
        cursor.execute(f'UPDATE players SET {field} = ? WHERE user_id = ?', (value, user_id))

    conn.commit()
    conn.close()

def get_player_by_user_id(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM players WHERE user_id = ?', (user_id,))
    player = cursor.fetchone()
    conn.close()
    return player
