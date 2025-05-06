from typing import Annotated
from pydantic import AfterValidator, BaseModel , Field, ValidationError

players_posts = { 
    "GB": "Gardien de but",
    # Defeneurs
    "DC": "Défenseur central", 
    "AD": "Arrière droit", 
    "AG": "Arrière gauche", 
    "LD": "Latéral droit",
    "LG": "Latéral gauche", 
    "SW": "Libéro", 
    # Milieux :
    "MDF": "Milieu défensif",
    "MC": "Milieu central",
    "MO": "Milieu offensif",
    "MD": "Milieu droit",
    "MG": "Milieu gauche",
    # Attaquants :
    "AD": "Ailier droit",
    "AG": "Ailier gauche",
    "SA": "Deuxième attaquant",
    "AC": "Avant-centre",
    "AT": "Attaquant" 
}

def validate_player_post(value):
    if value not in players_posts.values():
        raise ValueError(f"player post must be one of {list(players_posts.values())}.")
    return value

class PlayerInfo(BaseModel):
    age: int = Field(gt=0) 
    nbr_matchs_played: int = Field(ge=0) 
    nbr_assist: int = Field(ge=0) 
    nbr_scored_goals: int = Field(ge=0) 
    position: Annotated[str, AfterValidator(validate_player_post)]
    
