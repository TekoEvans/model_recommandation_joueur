from typing import Union
from fastapi import FastAPI
from models import PlayerInfo
from services import get_recommandation_fine_tunig, get_recommandation_prompt_tunig
import time
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")



@app.post("/recommandation")
def prompt_recommandation(player_info: PlayerInfo):
    """
     mMust receive a Json form who contains :
    - age
    - position :  ["Gardien de but", "Défenseur central", "Arrière droit", "Arrière gauche", "Latéral droit", "Latéral gauche", "Libéro", "Milieu défensif", "Milieu central", "Milieu offensif", "Milieu droit", "Milieu gauche", "Ailier droit", "Ailier gauche", "Deuxième attaquant", "Avant-centre", "Attaquant"]
    - nbr_matchs_played
    - nbr_assist
    - nbr_scored_goals
    """
    time_start = time.time()
    message = get_recommandation_fine_tunig(player_info)
    time_ellapsed = time.time() - time_start
    return {"Assiatant": message, "time": time_ellapsed}


@app.post("/recommandation/prompt_tunig")
def prompt_recommandation(player_info: PlayerInfo):
    """
    Json form who contains :
    - age
    - position 
    - nbr_matchs_played
    - nbr_assist
    - nbr_scored_goals
    """
    time_start = time.time()
    message = get_recommandation_prompt_tunig(player_info)
    time_ellapsed = time.time() - time_start
    return {"Assiatant": message, "time": time_ellapsed}