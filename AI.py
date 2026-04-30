from utile import gameOver, get_legal_moves, apply, get_pos
from evaluation import evaluation_kamisado
from collections import defaultdict
import time


class TimeOutError(Exception):
    pass


def negamaxWithPruningIterativeDeepening(state, player, timeout=2.6):
    cache = defaultdict(lambda: 0)
    start = time.time()
    best_move = None
    best_value = 0
    total_over = False

    def cachedNegamaxWithPruningLimitedDepth(
        state, player, depth, alpha=float("-inf"), beta=float("inf")
    ):
        if time.time() - start > timeout:
            raise TimeOutError()

        over = gameOver(state)
        if over or depth == 0:
            return -evaluation_kamisado(state, player), None, over

        theValue, theMove, theOver = float("-inf"), None, True
        board = state["board"]
        player = state["current"]
        color = state["color"]
        pos = get_pos(board, player, color)
        starting_l, starting_c = pos[0], pos[1]
        possibilities = [
            (move, apply(state, move))
            for move in get_legal_moves(board, player, starting_l, starting_c, color)
        ]

        possibilities.sort(key=lambda poss: cache[tuple(poss[1])])

        for move, successor in reversed(possibilities):
            value, _, over = cachedNegamaxWithPruningLimitedDepth(
                successor, player % 2 + 1, depth - 1, -beta, -alpha
            )
            value = -value

            theOver = theOver and over
            if value > theValue:
                theValue, theMove = value, move

            alpha = max(alpha, theValue)
            if alpha >= beta:
                break

        cache[tuple(tuple(tuple(row) for row in state["board"]))] = theValue
        return theValue, theMove, theOver

    depth = 1
    try:
        while not total_over:
            val, mov, ov = cachedNegamaxWithPruningLimitedDepth(state, player, depth)
            best_value = val
            best_move = mov
            total_over = ov

            print(f"Profondeur {depth} terminée. Meilleur coup : {best_move}")
            depth += 1

    except TimeOutError:
        print(f"Temps écoulé ! Arrêt à la profondeur {depth}.")

    return best_value, best_move
