from utile import gameOver, get_legal_moves, get_pos, apply
from evaluation import evaluation_kamisado
import time
import random

bool_random = True


class TimeOutError(Exception):
    pass


def board_to_key(board):
    """Convert the board into a fully hashable nested tuple for cache keys."""
    return tuple(
        tuple(
            (cell[0], tuple(cell[1]) if cell[1] is not None else None) for cell in row
        )
        for row in board
    )


def state_to_key(state):
    """Full state key: board + current player + required color."""
    return (board_to_key(state["board"]), state["current"], state["color"])


if bool_random:

    def negamaxWithPruningIterativeDeepening(state, player, timeout=2.6):
        cache: dict = {}  # state_key -> (depth, value, move)
        start = time.time()
        best_move = None
        best_value = 0
        total_over = False

        def get_moves_and_successors(state):
            board = state["board"]
            player = state["current"]
            color = state["color"]

            if color is None:
                camp = "light" if player == 1 else "dark"
                successors = []
                for r in range(8):
                    for c in range(8):
                        piece = board[r][c][1]
                        if piece is not None and piece[1] == camp:
                            piece_color = piece[0]
                            for move in get_legal_moves(
                                board, player, r, c, piece_color
                            ):
                                successor = apply(state, r, c, player, move)
                                end_l, end_c, _ = move
                                formatted = [[r, c], [end_l, end_c]]
                                successors.append((formatted, successor))
                return successors

            pos = get_pos(board, player, color)
            if pos is None:
                return []

            start_l, start_c = pos
            successors = []
            for move in get_legal_moves(board, player, start_l, start_c, color):
                end_l, end_c, _ = move
                formatted = [[start_l, start_c], [end_l, end_c]]
                successor = apply(state, start_l, start_c, player, move)
                successors.append((formatted, successor))

            return successors

        def negamax(state, depth, alpha, beta):
            if time.time() - start > timeout:
                raise TimeOutError()

            key = state_to_key(state)

            if key in cache:
                cached_depth, cached_val, cached_move = cache[key]
                if cached_depth >= depth:
                    return cached_val, cached_move, False

            over = gameOver(state)
            if over:
                val = -evaluation_kamisado(state, state["current"])
                return val, None, True

            if depth == 0:
                val = -evaluation_kamisado(state, state["current"])
                return val, None, False

            possibilities = get_moves_and_successors(state)

            if not possibilities:
                val = -evaluation_kamisado(state, state["current"])
                return val, None, True

            possibilities.sort(
                key=lambda poss: cache.get(state_to_key(poss[1]), (0, 0, None))[1]
            )

            best_val = float("-inf")
            best_mv = possibilities[-1][0]
            all_over = True

            for move, successor in reversed(possibilities):
                val, _, child_over = negamax(successor, depth - 1, -beta, -alpha)
                val = -val

                all_over = all_over and child_over

                if val > best_val:
                    best_val = val
                    best_mv = move

                alpha = max(alpha, best_val)
                if alpha >= beta:
                    break

            cache[key] = (depth, best_val, best_mv)
            return best_val, best_mv, all_over

        # Fallback garanti : on calcule les coups légaux avant la recherche
        # pour ne jamais renvoyer None au serveur si le timeout frappe trop tôt
        first_possibilities = get_moves_and_successors(state)
        if not first_possibilities:
            print("Aucun coup légal disponible.")
            return 0, None
        best_move = first_possibilities[0][0]

        depth = 1
        try:
            while not total_over:
                val, mov, ov = negamax(state, depth, float("-inf"), float("inf"))
                best_value = val
                best_move = mov
                total_over = ov
                print(
                    f"Profondeur {depth} terminée. Meilleur coup : {best_move}, valeur : {best_value}"
                )
                depth += 1

        except TimeOutError:
            print(
                f"Temps écoulé à la profondeur {depth}. Meilleur coup retenu : {best_move}"
            )

        return best_value, best_move

else:

    def negamaxWithPruningIterativeDeepening(
        state,
        player,
    ):
        return get_legal_moves(state, player)[
            random.randint(len(get_legal_moves(state, player)))
        ]
