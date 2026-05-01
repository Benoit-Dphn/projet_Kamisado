from utile import get_legal_moves


def evaluation_kamisado(etat, mon_index):
    board = etat["board"]
    mon_camp = "light" if mon_index == 1 else "dark"

    score = 0

    W_PROGRESSION = 20
    W_MOBILITY = 5
    W_BLOCK = 150
    W_WIN_THREAT = 800
    W_WIN_ACHIEVED = 10000

    for r in range(8):
        for c in range(8):
            piece = board[r][c][1]
            if piece is None:
                continue

            p_color, p_camp = piece
            player = 0 if p_camp == "light" else 1

            dist_parcourue = r if p_camp == "light" else 7 - r
            valeur_piece = dist_parcourue * W_PROGRESSION

            if (p_camp == "light" and r == 7) or (p_camp == "dark" and r == 0):
                valeur_piece += W_WIN_ACHIEVED
            else:
                moves = get_legal_moves(board, player, r, c, p_color)
                nb_moves = len(moves)

                if nb_moves == 0:
                    valeur_piece -= W_BLOCK
                else:
                    valeur_piece += nb_moves * W_MOBILITY
                    for move_r, move_c, _ in moves:
                        if (p_camp == "light" and move_r == 7) or (
                            p_camp == "dark" and move_r == 0
                        ):
                            valeur_piece += W_WIN_THREAT
                            break

            score += valeur_piece if p_camp == mon_camp else -valeur_piece

    if etat["current"] == mon_index and etat["color"] is not None:
        ma_piece_coincee = True
        found = False
        for r in range(8):
            for c in range(8):
                p = board[r][c][1]
                if p and p[1] == mon_camp and p[0] == etat["color"]:
                    player = 0 if mon_camp == "light" else 1
                    if len(get_legal_moves(board, player, r, c, p_color)) > 0:
                        ma_piece_coincee = False
                    found = True
                    break
            if found:
                break

        if ma_piece_coincee:
            if p_camp == mon_camp:
                score -= 500
            else:
                score += 500

    return score
