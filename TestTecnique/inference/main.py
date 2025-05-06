from typing import Union
from fastapi import FastAPI
from models import PlayerInfo
from services import get_recommandation_fine_tunig
import time


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



@app.post("/recommandation")
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
    message = get_recommandation_fine_tunig(player_info)
    time_ellapsed = time.time() - time_start
    return {"message": message, "time": time_ellapsed}