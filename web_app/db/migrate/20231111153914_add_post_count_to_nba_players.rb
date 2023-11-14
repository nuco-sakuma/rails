class AddPostCountToNbaPlayers < ActiveRecord::Migration[7.0]
  def change
    add_column :nba_players, :post_count, :integer
  end
end
