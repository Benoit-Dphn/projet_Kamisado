from utile import gameOver, get_legal_moves, get_pos, apply
from evaluation import evaluation_kamisado
import time


class TimeOutError(Exception):
    pass


def board_to_key(board):

    return tuple(
        tuple(
            (cell[0], tuple(cell[1]) if cell[1] is not None else None) for cell in row
        )
        for row in board
    )


def state_to_key(state):

    return (board_to_key(state["board"]), state["current"], state["color"])


def negamaxWithPruningIterativeDeepening(state, player, timeout=2.9):

    cache = {}
    start_time = time.time()

    def get_moves_and_successors(s):
        board = s["board"]
        curr_p = s["current"]
        color = s["color"]
        successors = []

        if color is None:
            camp = "light" if curr_p == 1 else "dark"
            for r in range(8):
                for c in range(8):
                    piece = board[r][c][1]
                    if piece is not None and piece[1] == camp:
                        piece_color = piece[0]
                        for move in get_legal_moves(board, curr_p, r, c, piece_color):
                            successor = apply(s, r, c, curr_p, move)
                            end_l, end_c, _ = move
                            successors.append(([[r, c], [end_l, end_c]], successor))
            return successors

        pos = get_pos(board, curr_p, color)
        if pos is None:
            return []

        start_l, start_c = pos
        for move in get_legal_moves(board, curr_p, start_l, start_c, color):
            end_l, end_c, _ = move
            formatted_move = [[start_l, start_c], [end_l, end_c]]
            successor = apply(s, start_l, start_c, curr_p, move)
            successors.append((formatted_move, successor))
        return successors

    def negamax(current_state, depth, alpha, beta):

        if time.time() - start_time > timeout:
            raise TimeOutError()

        key = state_to_key(current_state)

        if key in cache:
            cached_depth, cached_val, _ = cache[key]
            if cached_depth >= depth:
                return cached_val, None, False

        over = gameOver(current_state)
        possibilities = get_moves_and_successors(current_state)

        if over or depth == 0 or not possibilities:
            return (
                evaluation_kamisado(current_state, current_state["current"]),
                None,
                over,
            )

        possibilities.sort(key=lambda p: cache.get(state_to_key(p[1]), (0, 0, 0))[1])

        best_val = float("-inf")
        best_mv = possibilities[-1][0]
        is_terminal_branch = True

        for move, successor in reversed(possibilities):
            val, _, child_over = negamax(successor, depth - 1, -beta, -alpha)
            val = -val

            is_terminal_branch = is_terminal_branch and child_over

            if val > best_val:
                best_val = val
                best_mv = move

            alpha = max(alpha, best_val)
            if alpha >= beta:
                break

        cache[key] = (depth, best_val, best_mv)
        return best_val, best_mv, is_terminal_branch

    best_move_found = None
    best_score_found = 0
    current_depth = 1

    first_list = get_moves_and_successors(state)
    if first_list:
        best_move_found = first_list[0][0]

    try:
        finished = False
        while not finished:
            score, move, finished = negamax(
                state, current_depth, float("-inf"), float("inf")
            )
            if move:
                best_move_found = move
                best_score_found = score

            print(
                f"Profondeur {current_depth} finie. Coup: {best_move_found}, Score: {best_score_found}"
            )

            if best_score_found > 40000:
                break

            current_depth += 1

    except TimeOutError:
        print(
            f"Timeout atteint à la profondeur {current_depth}. Renvoi du meilleur coup."
        )

    return best_score_found, best_move_found
