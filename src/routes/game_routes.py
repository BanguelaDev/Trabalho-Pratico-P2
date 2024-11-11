from flask import Blueprint, render_template, session, redirect, url_for, request
from src.database.models import get_player_by_user_id, update_player

game_bp = Blueprint('game', __name__)

races = {
    "Humano": {"health": 8, "attack": 2},
    "Anão": {"health": 10, "defense": 2},
    "Elfo": {"dodge": 3, "attack": 1},
}

vocations = {
    "Guerreiro": {"attack": 2, "defense": 3},
    "Arqueiro": {"dodge": 2, "attack": 2},
    "Mago": {"health": 5, "defense": 2}
}

@game_bp.route("/race-vocation-selector", methods=['GET'])
def race_vocation_selector():
    player = get_player_by_user_id(session.get('user_id'))
            
    if player and (player['race'] != 'Unknown' or player['vocation'] != 'Unknown'):
        return redirect(url_for('game.ticket'))

    return render_template("race_vocation_selector.html", races = races, vocations = vocations)

@game_bp.route("/tutorial/<int:page>", methods=['GET'])
def tutorial(page):
    
    user_id = session.get('user_id')
    player = get_player_by_user_id(user_id)
    
    if player:
        return render_template("tutorial.html", player=player, page=page)
    
    return redirect(url_for('auth.login_register'))
    
@game_bp.route("/ticket", methods=['GET', 'POST'])
def ticket():
    user_id = session.get('user_id')
    
    if user_id:
        player = get_player_by_user_id(user_id)
        if player:
            if request.method == "POST":
                race = request.form.get('race')
                vocation = request.form.get('vocation')
                                
                if race and vocation and player['race'] == "Unknown" and player['vocation'] == "Unknown":
                    
                    print(race, vocation)
                    
                    player = update_player(user_id, {
                        'race': race,
                        'vocation': vocation
                    })
                                        
                return render_template("ticket.html", player = player)

    return redirect(url_for('auth.login'))
