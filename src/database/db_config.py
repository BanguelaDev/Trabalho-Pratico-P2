# Configuração e inicialização do banco de dados

import sqlite3

DATABASE = 'rpg_game.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            vocation TEXT DEFAULT 'Unknown',
            race TEXT DEFAULT 'Unknown',
            exp INTEGER DEFAULT 0,
            level INTEGER DEFAULT 0,
            attack INTEGER DEFAULT 2,
            defense INTEGER DEFAULT 1,
            health INTEGER DEFAULT 8,
            dodge INTEGER DEFAULT 1,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized")
