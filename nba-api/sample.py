from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import teamandplayersvsplayers
from nba_api.stats.static import players

active_players = players.get_active_players()
players_name = [player['full_name'] for player in active_players]

def say_hello():
    return players_name[:4]

if __name__ == "__main__":
    print(say_hello())
