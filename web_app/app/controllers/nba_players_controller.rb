class NbaPlayersController < ApplicationController
  def index
    @nba_players = NbaPlayer.all
  end

  def show
    @nba_player= NbaPlayer.find(params[:id])
  end

  def edit
    @nba_player= NbaPlayer.find(params[:id])
  end

  def update
    @nba_player = NbaPlayer.find(params[:id])
    #文字列を数字に変換
    new_sum_score = params[:nba_player][:sum_score].to_i
    @nba_player.sum_score += new_sum_score
    
    
    # 認可されたパラメータ:sum_score(private以下)に現在の@nba_player.sum_scoreを追加している
    if @nba_player.update(nba_player_params.merge(sum_score: @nba_player.sum_score))
      @nba_player.increment!(:post_count)
      if @nba_player.post_count>0
        @nba_player.score =@nba_player.sum_score / @nba_player.post_count
      else
        @nba_player.score = @nba_player.sum_score
      end
      flash[:success] = "Profile updated"
      redirect_to @nba_player
    else
      render 'edit', status: :unprocessable_entity
    end
  end

  private

    def nba_player_params
      params.require(:nba_player).permit(:sum_score)
    end

end
