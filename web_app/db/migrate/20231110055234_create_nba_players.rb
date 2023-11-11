class CreateNbaPlayers < ActiveRecord::Migration[7.0]
  def change
    create_table :nba_players, id: false do |t|
      t.integer :id, auto_increment: true, primary_key: true
      t.string :player_name

      t.timestamps
    end
  end
end
