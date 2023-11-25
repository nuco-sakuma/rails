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
        # players_nameをデータベースに挿入前に全てのレコードを削除
        cursor.execute('DELETE FROM nba_players;')

        # idの初期値を設定
        last_id = 0

        for player_name in players_list:
            cursor.execute('SELECT * FROM nba_players WHERE player_name = %s', (player_name,))
            result = cursor.fetchone()

            if not result:
                # プレイヤー名が存在しない場合に挿入（idはAUTO_INCREMENTで自動で割り振られる）
                last_id += 1
                cursor.execute('INSERT INTO nba_players (id, player_name, created_at, updated_at, sum_score, post_count, score) VALUES (%s, %s, %s, %s, 0, 0, 0)',
                               (last_id, player_name, datetime.now(), datetime.now()))

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
