class CreateNbaPlayers < ActiveRecord::Migration[7.0]
  def change
    create_table :nba_players do |t|
      t.string :player_name
      t.integer :sum_score
      t.integer :post_count
      t.integer :score

      t.timestamps
    end
  end
end
