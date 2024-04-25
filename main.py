from fastapi import FastAPI
from nba_api.stats.endpoints import scoreboardv2
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players as ply
import json


app = FastAPI()

# Returns information about the upcoming games
@app.get('/games')
async def games():
    try:
        scoreboard = scoreboardv2.ScoreboardV2()
        data = scoreboard.get_normalized_dict()
        return json.dumps(data)
    
    except Exception as error:
        return json.dumps({'error': str(error)})

# Returns information about a specific player
@app.get('/player/{player}')
async def player(player: str):
    try:
        player_ = ply.find_players_by_full_name(player)
        return json.dumps(player_)
    
    except Exception as error:
        return json.dumps({'error': str(error)})

# Returns inactive players
@app.get('/inactive_players')
async def inactive_players():
    try:
        players_ = ply.get_players()
        return json.dumps(players_)

    except Exception as error:
        return json.dumps({'error': str(error)})

# Returns active players
@app.get('/active_players')
async def active_players():
    try:
        players_ = ply.get_active_players()
        return json.dumps(players_)
    
    except Exception as error:
        return json.dumps({'error': str(error)})
    