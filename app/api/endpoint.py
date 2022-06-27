from . import api
from .config import STEAM_API_KEY
from flask import jsonify
from flask import request
import requests
from .errors import bad_request


@api.get("/")
def get_owned_games():
    data = request.get_json() or {}

    print(data)
    if "steam_id" not in data:
        return bad_request("Steam ID must be supplied")

    steam_id = data["steam_id"]

    response = requests.get(
        f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={STEAM_API_KEY}&steamid={steam_id}&include_appinfo=true&include_played_free_games=true&format=json")

    return response.json()
