from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import teamandplayersvsplayers
from nba_api.stats.static import players
import mysql.connector
from datetime import datetime

# データベースへの接続とカーソルの生成
connection = mysql.connector.connect(
    host='web_app-mysql',
    user='root',
    passwd='test',
    db='web_app_development')
cursor = connection.cursor()

def save_players_to_database(players_list):
    try:
        # players_nameをデータベースに挿入
        for player_name in players_list:
            cursor.execute('INSERT INTO nba_players (player_name, created_at,updated_at) VALUES (%s, %s,%s)', (player_name, datetime.now(),datetime.now()))


        # 変更を保存
        connection.commit()

        print("Players names saved to the database successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # データベース接続を閉じる
        cursor.close()
        connection.close()

if __name__ == "__main__":
    active_players = players.get_active_players()
    players_name = [player['full_name'] for player in active_players]

    # players_nameをデータベースに保存
    save_players_to_database(players_name)

