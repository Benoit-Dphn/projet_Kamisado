from projet_Kamisado import utile as u
import random

def rand_play(state):
    pos = u.get_pos(state["board"], state["current"], state["color"])
    moves = u.get_legal_moves(state["board"], state["current"], pos[0], pos[1], state["color"])
    return [pos, random.choice(moves)]