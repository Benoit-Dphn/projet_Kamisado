import copy

board = []
player = 0
color = ""
r = 0
c = 0

def parse_board(state) :
    board = state["board"]
    player = state["current"]
    color = state["color"]

    return board, player, color

def get_pion_position(board,player, color):
    player = "dark" if player == 0 else "light"
    for r in range(len(board)):
        for c in range(len(board[r])):
            tile = board[r][c]
            pion = tile[1]
            if pion is not None :
                if pion[0] == color and pion[1] == player :
                    return(r, c)             
    return None
             
def get_legal_moves(board, player, color):
    
    get_pion_position(board, player, color)
    moves = []
    direction = 1 if player == "light" else -1

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

            if board[r][c][1] is not None :
                return dr, dc
            
            if board[new_r][new_c][1] is not None:
                break
            
            dest_color = board[new_r][new_c][0]
            moves.append((new_r, new_c, dest_color))

    return moves

def apply_move(board, player, start_pos, end_pos):
    BOARD = copy.deepcopy(board)


def get_next_color(board, end_pos):
    return board[end_pos][0]

def is_winning(board, player):
    if player == 0 :
        for i in range(8):
            if board[7][i][color, player] == True :
                end_game(player)
            else : return None
    else :
        for i in range(8):
            if board[0][i][color, player] == True :
                end_game(player)
            else : return None