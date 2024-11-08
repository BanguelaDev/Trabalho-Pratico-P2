from flask import Blueprint, render_template, session, redirect, url_for, request
from src.database.models import get_player_by_user_id, update_player

game_bp = Blueprint('game', __name__)

races = {
    "Anão": {"Vida": 10, "Defesa": 2},
    "Elfo": {"Esquiva": 3, "Ataque": 1},
    "Humano": {"Vida": 8, "Ataque": 2}
}

vocations = {
    "Guerreiro": {"Ataque": 2, "Defesa": 3},
    "Arqueiro": {"Esquiva": 2, "Ataque": 2},
    "Paladino": {"Vida": 5, "Defesa": 2}
}

@game_bp.route("/race-vocation-selector", methods=['GET'])
def race_vocation_selector():
    user_id = session.get('user_id')
    player = get_player_by_user_id(user_id)
        
    if player and (player[3] != 'Unknown' or player[4] != 'Unknown'):
        return redirect(url_for('game.ticket'))

    return render_template("race_vocation_selector.html", races = races, vocations = vocations)

@game_bp.route("/ticket", methods=['GET', 'POST'])
def ticket():
    user_id = session.get('user_id')

    race = request.form.get('race')
    vocation = request.form.get('vocation')
    
    if race and vocation:
        update_player(user_id, {
            'race': race,
            'vocation': vocation
        })

    if user_id:
        player = get_player_by_user_id(user_id)
        if player:
            return render_template("ticket.html", player=player)
    
    return redirect(url_for('auth.homepage'))
