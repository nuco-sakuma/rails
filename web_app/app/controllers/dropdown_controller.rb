class DropdownController < ApplicationController
  def index
    @users = User.paginate(page: params[:page])
    @player_names = NbaPlayer.all

  end
end
