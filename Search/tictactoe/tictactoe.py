"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count=0
    o_count=0
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==X:
                x_count+=1
            elif board[i][j]==O:
                o_count+=1
    
    if x_count>o_count:
        return O
    else:
        return X 
    
    
def actions(board):
    
    """Returns set of all possible actions (i, j) available on the board"""
    
    return {(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == EMPTY}


def result(board, action):
    
    #Returns the board that results from making move (i, j) on the board?.
    i, j = action
    new_board = [row.copy() for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY or \
           board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[i][0]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY or \
       board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
    