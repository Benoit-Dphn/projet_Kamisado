from utile import get_legal_moves


def evaluation_kamisado(etat, mon_index):
    board = etat["board"]
    mon_camp = "light" if mon_index == 1 else "dark"
    score = 0

    W_PROGRESSION = [
        0,
        10,
        30,
        70,
        150,
        300,
        600,
        10000,
    ]
    W_MOBILITY = 10
    W_BLOCK_PENALTY = 500
    W_WIN_THREAT = 1500
    W_WIN_ACHIEVED = 500000

    for r in range(8):
        for c in range(8):
            piece = board[r][c][1]
            if piece is None:
                continue

            p_color, p_camp = piece
            p_player_idx = 1 if p_camp == "light" else 0

            dist = r if p_camp == "light" else 7 - r

            valeur_piece = 0

            if dist == 7:
                valeur_piece = W_WIN_ACHIEVED
            else:
                valeur_piece += W_PROGRESSION[dist]

                moves = get_legal_moves(board, p_player_idx, r, c, p_color)
                nb_moves = len(moves)

                if nb_moves == 0:
                    valeur_piece -= W_BLOCK_PENALTY
                else:
                    valeur_piece += nb_moves * W_MOBILITY

                    for m_r, m_c, _ in moves:
                        if (p_camp == "light" and m_r == 7) or (
                            p_camp == "dark" and m_r == 0
                        ):
                            valeur_piece += W_WIN_THREAT
                            break

            if p_camp == mon_camp:
                score += valeur_piece
            else:
                score -= valeur_piece

    return score
