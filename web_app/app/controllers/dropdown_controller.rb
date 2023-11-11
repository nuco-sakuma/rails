class DropdownController < ApplicationController
  def index
    @users = User.paginate(page: params[:page])
    @player_name =NbaPlayer.all
  end
end
