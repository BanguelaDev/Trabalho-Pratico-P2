from flask import Blueprint, render_template, request, redirect, url_for, session
from src.database.models import add_user, get_user, add_player

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/")
def index():
    return redirect(url_for('auth.login'))

@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    session.pop('user_id', None)
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = get_user(username)
        
        if user:
            if user[2] == password:
                session['user_id'] = user[0]
                return redirect(url_for('game.ticket'))
            else:
                return render_template('login_register.html', register = False, error = "Senha incorreta! Tente novamente.", label = "password")
        else:
            return render_template('login_register.html', register = False, error = "Nenhum usuário encontrado com esse nome!", label = "username")
    
    return render_template('login_register.html', register = False)

@auth_bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_username = request.form.get('new-username')
        new_password = request.form.get('new-password')

        user = get_user(new_username)
            
        if user:
            return render_template('login_register.html', register = True, error = "Já existe um usuário com esse nome!", label = "username")
        else:
            user_id = add_user(new_username, new_password)
            add_player(user_id, new_username)
            session['user_id'] = user_id
            return redirect(url_for('game.tutorial', page='0'))

    return render_template('login_register.html', register = True)

@auth_bp.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))
