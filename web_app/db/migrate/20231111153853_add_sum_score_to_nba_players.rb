class AddSumScoreToNbaPlayers < ActiveRecord::Migration[7.0]
  def change
    add_column :nba_players, :sum_score, :integer
  end
end
