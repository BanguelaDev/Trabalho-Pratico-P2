from flask import Blueprint, render_template, session, redirect, url_for, request
from src.database.models import get_player_by_user_id, update_player

game_bp = Blueprint('game', __name__)

races = {
    "Anão": {"health": 10, "defense": 2},
    "Elfo": {"dodge": 3, "attack": 1},
    "Humano": {"health": 8, "attack": 2}
}

vocations = {
    "Guerreiro": {"attack": 2, "defense": 3},
    "Arqueiro": {"dodge": 2, "attack": 2},
    "Paladino": {"health": 5, "defense": 2}
}

@game_bp.route("/race-vocation-selector", methods=['GET'])
def race_vocation_selector():
    player = get_player_by_user_id(session.get('user_id'))
        
    if player and (player['race'] != 'Unknown' or player['vocation'] != 'Unknown'):
        return redirect(url_for('game.tutorial'))

    return render_template("race_vocation_selector.html", races = races, vocations = vocations)

@game_bp.route("/tutorial/<int:page>", methods=['GET', 'POST'])
def tutorial(page):
    player = get_player_by_user_id(session.get('user_id'))
    
    if player:
        return render_template("tutorial.html", player=player, page=page)
    
    return redirect(url_for('auth.homepage'))
    
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
            return render_template("ticket.html", player = player)
    
    return redirect(url_for('auth.homepage'))
