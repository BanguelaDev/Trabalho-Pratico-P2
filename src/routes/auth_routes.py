from flask import Blueprint, render_template, request, redirect, url_for, session
from src.database.models import add_user, get_user, add_player

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/")
def homepage():
    return render_template("homepage.html")

@auth_bp.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = get_user(username)
        
    if user:
        if user[2] == password:
            session['user_id'] = user[0]
            return redirect(url_for('game.ticket'))
        else:
            return "Senha incorreta! Tente novamente.", 401
    else:
        user_id = add_user(username, password)
        add_player(user_id, username)
        session['user_id'] = user_id
        return redirect(url_for('game.race_vocation_selector'))

@auth_bp.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.homepage'))
