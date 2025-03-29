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
    # If board is empty - X's turn
    if board_empty(board):
         return 'X'
    
    # Count the number of X's and O's: 
    counts = count_pieces(board)
    if counts['X'] > counts['O']: 
        return 'O'
    else: 
        return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3): 
        for j in range(3): 
            if board[i][j] == EMPTY: 
                actions.add((i,j))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Make a deep copy
    result_board = copy.deepcopy(board)

    # Check the action is valid
    cell_contents = board[action[0]][action[1]]
    if cell_contents != EMPTY: 
        raise Exception("Invalid action")

    # Otherwise, implement the action and return the board
    
    else: 
        result_board[action[0]][action[1]] = player(board)
    
    return result_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

def board_empty(board): 
    for row in board: 
        for cell in row: 
            if cell != EMPTY: return False 
    return True

def count_pieces(board): 
    counts = {"X": 0, "O": 0}
    
    for row in board:
        for cell in row:
            if cell in counts:
                counts[cell] += 1
                
    return counts
