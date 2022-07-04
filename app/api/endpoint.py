from . import api
import os
from .config import STEAM_API_KEY
from flask import jsonify
from flask import request
import requests
from .errors import bad_request


@api.get("/test")
def test():
    return "hello world"


@api.get("/owned-games")
def get_owned_games():
    steam_id = request.args.get("steam_id")
    if not steam_id:
        return bad_request("Steam ID must be supplied")

    response = requests.get(
        f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={STEAM_API_KEY}&steamid={steam_id}&include_appinfo=true&include_played_free_games=true&format=json")

    return response.json()


@api.get("/user")
def get_user_info():
    pass


@api.get("/player-count")
def get_player_count():
    app_id = request.args.get("app_id")

    if not app_id:
        return bad_request("app_id must be supplied")

    url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1?appid={app_id}"
    response = requests.get(url)
    data = response.json()

    return data
