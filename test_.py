import utile
import copy
import evaluation

state3 = {
    "players": ["Les Infernales", "ilyes et benoit contre le reste du monde "],
    "current": 1,
    "color": "orange",
    "board": [
        [
            ["orange", ["pink", "light"]],
            ["blue", ["orange", "light"]],
            ["purple", ["green", "light"]],
            ["pink", ["red", "light"]],
            ["yellow", ["purple", "light"]],
            ["red", ["blue", "light"]],
            ["green", ["brown", "light"]],
            ["brown", ["yellow", "light"]],
        ],
        [
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
        ],
        [
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
        ],
        [
            ["pink", None],
            ["purple", None],
            ["blue", None],
            ["orange", None],
            ["brown", None],
            ["green", None],
            ["red", None],
            ["yellow", None],
        ],
        [
            ["yellow", None],
            ["red", None],
            ["green", None],
            ["brown", None],
            ["orange", None],
            ["blue", None],
            ["purple", None],
            ["pink", None],
        ],
        [
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
        ],
        [
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
        ],
        [
            ["brown", ["yellow", "dark"]],
            ["green", ["green", "dark"]],
            ["red", ["orange", "dark"]],
            ["yellow", ["purple", "dark"]],
            ["pink", ["red", "dark"]],
            ["purple", ["brown", "dark"]],
            ["blue", ["blue", "dark"]],
            ["orange", ["pink", "dark"]],
        ],
    ],
}
state2 = {
    "players": ["Les Infernales", "ilyes et benoit contre le reste du monde "],
    "current": 1,
    "color": "orange",
    "board": [
        [
            ["orange", ["pink", "light"]],
            ["blue", ["orange", "light"]],
            ["purple", ["green", "light"]],
            ["pink", ["red", "light"]],
            ["yellow", ["purple", "light"]],
            ["red", ["blue", "light"]],
            ["green", ["brown", "light"]],
            ["brown", ["yellow", "light"]],
        ],
        [
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
        ],
        [
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
        ],
        [
            ["pink", None],
            ["purple", None],
            ["blue", None],
            ["orange", None],
            ["brown", None],
            ["green", None],
            ["red", None],
            ["yellow", None],
        ],
        [
            ["yellow", None],
            ["red", None],
            ["green", None],
            ["brown", None],
            ["orange", None],
            ["blue", None],
            ["purple", None],
            ["pink", None],
        ],
        [
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
        ],
        [
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
        ],
        [
            ["brown", ["yellow", "dark"]],
            ["green", ["green", "dark"]],
            ["red", ["orange", "dark"]],
            ["yellow", ["purple", "dark"]],
            ["pink", ["red", "dark"]],
            ["purple", ["brown", "dark"]],
            ["blue", ["blue", "dark"]],
            ["orange", ["pink", "dark"]],
        ],
    ],
}
state = {
    "players": ["Les Infernales", "ilyes et benoit contre le reste du monde "],
    "current": 1,
    "color": "orange",
    "board": [
        [
            ["orange", ["green", "light"]],
            ["blue", ["red", "light"]],
            ["purple", ["pink", "dark"]],
            ["pink", ["orange", "light"]],
            ["yellow", ["brown", "light"]],
            ["red", ["yellow", "light"]],
            ["green", ["purple", "light"]],
            ["brown", ["blue", "light"]],
        ],
        [
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
        ],
        [
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
        ],
        [
            ["pink", None],
            ["purple", None],
            ["blue", None],
            ["orange", None],
            ["brown", None],
            ["green", None],
            ["red", None],
            ["yellow", None],
        ],
        [
            ["yellow", None],
            ["red", None],
            ["green", ["pink", "light"]],
            ["brown", None],
            ["orange", ["brown", "dark"]],
            ["blue", None],
            ["purple", None],
            ["pink", None],
        ],
        [
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
        ],
        [
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
        ],
        [
            ["brown", ["green", "dark"]],
            ["green", None],
            ["red", ["red", "dark"]],
            ["yellow", ["orange", "dark"]],
            ["pink", None],
            ["purple", ["purple", "dark"]],
            ["blue", ["yellow", "dark"]],
            ["orange", ["blue", "dark"]],
        ],
    ],
}
board = utile.copy_board(state)
player = copy.deepcopy(state["current"])
color = copy.deepcopy(state["color"])


def test_copy_board():
    assert utile.copy_board(state) == [
        [
            ["orange", ["green", "light"]],
            ["blue", ["red", "light"]],
            ["purple", ["pink", "dark"]],
            ["pink", ["orange", "light"]],
            ["yellow", ["brown", "light"]],
            ["red", ["yellow", "light"]],
            ["green", ["purple", "light"]],
            ["brown", ["blue", "light"]],
        ],
        [
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
        ],
        [
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
        ],
        [
            ["pink", None],
            ["purple", None],
            ["blue", None],
            ["orange", None],
            ["brown", None],
            ["green", None],
            ["red", None],
            ["yellow", None],
        ],
        [
            ["yellow", None],
            ["red", None],
            ["green", ["pink", "light"]],
            ["brown", None],
            ["orange", ["brown", "dark"]],
            ["blue", None],
            ["purple", None],
            ["pink", None],
        ],
        [
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
        ],
        [
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
        ],
        [
            ["brown", ["green", "dark"]],
            ["green", None],
            ["red", ["red", "dark"]],
            ["yellow", ["orange", "dark"]],
            ["pink", None],
            ["purple", ["purple", "dark"]],
            ["blue", ["yellow", "dark"]],
            ["orange", ["blue", "dark"]],
        ],
    ]


def test_eval():
    assert evaluation.evaluation_kamisado(state, 0) == 9255
    assert (
        evaluation.evaluation_kamisado(state, 0)
        == evaluation.evaluation_kamisado(state, 1) * -1
    )


def test_send_move():
    pass


def test_gameOver():
    assert utile.gameOver(state)


def test_get_pos():
    assert utile.get_pos(board, player, color) == [0, 3]


def test_get_legal_moves():
    pass


def test_aplly():
    pass


def test_AI():
    pass
