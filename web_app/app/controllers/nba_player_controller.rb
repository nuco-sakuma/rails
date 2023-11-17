class NbaPlayerController < ApplicationController
  def index
    @player_names= NbaPlayer.all
    @users = User.all
    # @users = User.paginate(page: params[:page])
  end

  def show
    @player_name = NbaPlayer.find(params[:id])

  end
end
