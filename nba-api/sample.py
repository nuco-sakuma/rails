from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import teamandplayersvsplayers
from nba_api.stats.static import players

nba_players = players.get_players()

def say_hello():
    big_fundamental = [player for player in nba_players if player["full_name"] == "Tim Duncan"][0]
    return big_fundamental

if __name__ == "__main__":
    print(say_hello())
