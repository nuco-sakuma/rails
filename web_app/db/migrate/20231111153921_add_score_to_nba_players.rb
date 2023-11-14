class AddScoreToNbaPlayers < ActiveRecord::Migration[7.0]
  def change
    add_column :nba_players, :score, :integer
  end
end
