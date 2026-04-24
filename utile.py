from inscription import handle_server_requests as hsr
from AI import negamaxWithPruning


def parse_board(state):
    pass


def get_moves(board, r, c, camp):
    moves = []
    direction = 1 if camp == "light" else -1

    vectors = [
        (direction, 0),
        (direction, -1),
        (direction, +1),
    ]

    for dr, dc in vectors:
        for i in range(1, 8):
            new_r = r + dr * i
            new_c = c + dc * i

            if not (0 <= new_r <= 7 and 0 <= new_c <= 7):
                break

            if board[new_r][new_c][1] is not None:
                break

            dest_color = board[new_r][new_c][0]
            moves.append((new_r, new_c, dest_color))

    return moves


def send_moves(state, move):
    pass


def gameOver(state, player):
    pass


def get_pos(board, player, color):

    indx = "dark" if player == 0 else "light"
    for l in range(8):
        for c in range(8):
            if board[l][c][1] is not None:
                if (board[l][c][1][0] == color) and (board[l][c][1][1]) == indx:
                    return l, c

    return None


def get_legal_moves(board, player, starting_l, color):
    legal_moves = []
    colision = [
        0,
        0,
        0,
    ]  # [diag_gauche,vertical,diag droite]  0 is on a pas croiser un pion 1 si oui
    dl_gauche = 0
    dl_droite = 0

    # je vais juste avnacer pour faire le verticale avec la boucle mais a chaque fois je frais de check avec dl_gauche et droite comme ca on parcour tous les chemin vrtica aussi , le seul probleme c est , la boucle sera while on a pas dep
