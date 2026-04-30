import copy


def copy_board(state):
    copied_board = copy.deepcopy(state["board"])
    return copied_board


def gameOver(state):
    board = copy_board(state)

    for i in range(8):
        top_piece = board[0][i][1]
        if top_piece is not None and top_piece[1] == "dark":
            return True

        bottom_piece = board[7][i][1]
        if bottom_piece is not None and bottom_piece[1] == "light":
            return True

    return False


def get_pos(board, player, color):

    indx = "dark" if player == 0 else "light"
    for row in range(8):
        for c in range(8):
            if board[row][c][1] is not None:
                if (board[row][c][1][0] == color) and (board[row][c][1][1]) == indx:
                    return [row, c]

    return None


def get_legal_moves(board, player, starting_l, starting_c, color):
    legal_moves = []

    direction = 1 if player == 0 else -1
    current_camp = "light" if player == 0 else "dark"

    # False => on continue d'explorer la direction, True => direction bloquee.
    blocked = {
        "diag_left": False,
        "vertical": False,
        "diag_right": False,
    }

    for step in range(1, 8):
        next_l = starting_l + direction * step

        if next_l < 0 or next_l > 7:
            break

        directions = [
            ("diag_left", starting_c - step),
            ("vertical", starting_c),
            ("diag_right", starting_c + step),
        ]

        for name, next_c in directions:
            if blocked[name]:
                continue

            if next_c < 0 or next_c > 7:
                blocked[name] = True
                continue

            square = board[next_l][next_c]
            piece = square[1]

            if piece is None:
                legal_moves.append((next_l, next_c, square[0]))
                continue

            # Collision: si pion adverse, on ajoute la case puis on bloque la direction.
            if piece[1] != current_camp:
                legal_moves.append((next_l, next_c, square[0]))

            blocked[name] = True

        if blocked["diag_left"] and blocked["vertical"] and blocked["diag_right"]:
            break

    return legal_moves


def apply(state, move):
    start_l, start_c, end_l, end_c, player = move
    board = copy_board(state)
    pion = board[start_l][start_c][1]
    board[start_l][start_c][1] = None
    board[end_l][end_c][1] = pion
    new_state = copy.deepcopy(state)
    new_state["board"] = board
    new_state["current"] = 1 - player
    new_state["color"] = new_state["board"][end_l][end_c][0]
    return new_state
