"""
Tic Tac Toe Player
"""

import math, copy

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
    xcount = 0
    ocount = 0
    for i in range (3):
        for j in range (3):
            if board[i][j] == "X":
                xcount += 1
            if board[i][j] == "O":
                ocount += 1
    if xcount > ocount:
        turn = "O"
    elif xcount <= ocount:
        turn = "X"
    return turn

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possactions = []
    for i in range (3):
        for j in range (3):
            if board[i][j] == None:
                action = (i,j)
                possactions.append(action) 
    
    return possactions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    newBoard = copy.deepcopy(board)
    x = action[0]
    y = action[1]
    newBoard[x][y] = turn
    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    xdia = 0    
    x2dia = 0
    odia = 0
    o2dia = 0
    winner = 0
    for i in range (3):
        xrow = 0
        orow = 0
        xcol = 0
        ocol = 0

        #Getting X's and O's in diagonals for a three in a row            
        if board[i][i] == "X":
            xdia += 1
        elif board[i][i] == "O":
            odia += 1       
        if board[i][2-i] == "X":
            x2dia += 1
        elif board[i][2-i] == "O":
            o2dia += 1
        if winner != 0:
            break
        if xdia == 3 or x2dia == 3:
            winner = "X"
            return winner
        elif odia == 3 or o2dia == 3:
            winner = "O"
            return winner

        for j in range (3): 
            #Getting X's and O's in Rows for a three in a row
            if board [i][j] == "X":
                xrow += 1
            elif board[i][j] == "O":
                orow += 1
            
            #Getting X's and O's in Columns for a three in a row
            if board[j][i] == "X":
                xcol += 1
            elif board[j][i] == "O":
                ocol += 1
            
            #Checking if 3 in a row for column and row
            if xrow == 3 or xcol == 3:
                winner = "X"
                return winner
            elif orow == 3 or ocol == 3:
                winner = "O"
                return winner

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    xdia = 0    
    x2dia = 0
    odia = 0
    o2dia = 0
    gameOver = False
    tie = 0
    for i in range (3):
        xrow = 0
        orow = 0
        xcol = 0
        ocol = 0
        #Getting X's and O's in diagonals for a three in a row            
        if board[i][i] == "X":
            xdia += 1
        elif board[i][i] == "O":
            odia += 1       
        if board[i][2-i] == "X":
            x2dia += 1
        elif board[i][2-i] == "O":
            o2dia += 1
        if xdia == 3 or x2dia == 3:
            gameOver = True
            return gameOver
        elif odia == 3 or o2dia == 3:
            gameOver = True
            return gameOver
        for j in range (3): 
            #Getting X's and O's in Rows for a three in a row
            if board[i][j] == "X":
                xrow += 1
            elif board[i][j] == "O":
                orow += 1            
            #Getting X's and O's in Columns for a three in a row
            if board[j][i] == "X":
                xcol += 1
            elif board[j][i] == "O":
                ocol += 1           
            #Checking if 3 in a row for column and row
            if xrow == 3 or xcol == 3:
                gameOver = True
                break
            elif orow == 3 or ocol == 3:
                gameOver = True
                return gameOver            
            #Checking for tie
            if board[i][j] != None:
                tie += 1
            if tie == 9:
                gameOver = True
                return gameOver   
    return gameOver

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    xdia = 0    
    x2dia = 0
    odia = 0
    o2dia = 0
    utility = 0
    for i in range (3):
        xrow = 0
        orow = 0
        xcol = 0
        ocol = 0
        #Getting X's and O's in diagonals for a three in a row            
        if board[i][i] == "X":
            xdia += 1
        elif board[i][i] == "O":
            odia += 1       
        if board[i][2-i] == "X":
            x2dia += 1
        elif board[i][2-i] == "O":
            o2dia += 1
        if utility != 0:
            break
        if xdia == 3 or x2dia == 3:
            utility = 1
            return utility
        elif odia == 3 or o2dia == 3:
            utility = -1
            return utility

        for j in range (3): 
            #Getting X's and O's in Rows for a three in a row
            if board[i][j] == "X":
                xrow += 1
            elif board[i][j] == "O":
                orow += 1
            
            #Getting X's and O's in Columns for a three in a row
            if board[j][i] == "X":
                xcol += 1
            elif board[j][i] == "O":
                ocol += 1
            
            #Checking if 3 in a row for column and row
            if xrow == 3 or xcol == 3:
                utility = 1
                return utility
            elif orow == 3 or ocol == 3:
                utility = -1
                return utility
    return utility

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    OptimalAction = 0    
    if terminal(board):
        return None
    currActions = actions(board)
    if player(board) == "X":
        currScore = -math.inf
        for i in range (len(currActions)):
            bestScore = minValue(result(board,currActions[i]), -math.inf, math.inf)
            if bestScore == "X":
                OptimalAction = currActions[i]
                return OptimalAction
            elif bestScore > currScore:
                currScore = bestScore
                OptimalAction = currActions[i]

    elif player(board) == "O":
        currScore = math.inf
        for i in range (len(currActions)):
            bestScore = maxValue(result(board, currActions[i]), -math.inf, math.inf)
            if bestScore == -1:
                OptimalAction = currActions[i]
                return OptimalAction
            elif bestScore < currScore:
                currScore = bestScore
                OptimalAction = currActions[i]
    return OptimalAction

def maxValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    bestScore = -math.inf
    possibleActions = actions(board)
    for i in range (len(possibleActions)):
        newScore = minValue(result(board, possibleActions[i]), alpha, beta)
        bestScore = max(bestScore, newScore)
        alpha = max(bestScore, alpha)
        if bestScore == 1:
            return bestScore
        #Alpha-Beta Pruning 
        if alpha >= beta:
            break
    return bestScore

def minValue (board, alpha, beta):
    if terminal(board):
        return utility(board)
    bestScore = math.inf
    possibleActions = actions(board)
    for i in range (len(possibleActions)):
        newScore = maxValue(result(board,possibleActions[i]), alpha, beta)
        bestScore = min(bestScore, newScore)
        beta = min(bestScore, beta)
        if bestScore == -1:
            return bestScore
        #Alpha-Beta Pruning
        if beta <= alpha:
            break
    return bestScore
