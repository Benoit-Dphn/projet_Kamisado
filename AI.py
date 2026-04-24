from utile import gameOver
from evaluation import evaluation_kamisado


def negamaxWithPruning(state, player, alpha=float("-inf"), beta=float("inf")):
    if gameOver(state):
        return -evaluation_kamisado(state, player), None

    theValue, theMove = float("-inf"), None
    for move in moves(state):
        successor = apply(state, move)
        value, _ = negamaxWithPruning(successor, player % 2 + 1, -beta, -alpha)
        if value > theValue:
            theValue, theMove = value, move
        alpha = max(alpha, theValue)
        if alpha >= beta:
            break
    return -theValue, theMove
