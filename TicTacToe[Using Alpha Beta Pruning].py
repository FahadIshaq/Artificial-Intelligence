"""GROUP MEMBERS
	FAHAD ISHAQ [FA20-BCS-017] 
 	IDREES AHMED GHAZI [FA20-BCS-025]
"""
import random #imports random module to generate random numbers
import math   #imports math module to use infinity here

#Prints the Board
def printBoard(board):
    print(board[1] + '     |     ' + board[2] + '     |     ' + board[3])
    print('------+-----------+------')
    print(board[4] + '     |     ' + board[5] + '     |     ' + board[6])
    print('------+-----------+------')
    print(board[7] + '     |     ' + board[8] + '     |     ' + board[9])
    


#First Move
def FirstMove():
    x=random.randint(1,2)
    if(x==1):
        return 'human'
    else:
        return 'computer'

#Checks the winning conditions
def winner(board, letter):
	return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
	(board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
	(board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
	(board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
	(board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
	(board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
	(board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
	(board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal
 
 
 
def SpaceFree(board, move):  #checks if the space is free
	return board[move] == ' '



#Human Move
def humanMove(board):
    yourMove=''
    totalPossibleMoves=[1,2,3,4,5,6,7,8,9]
    while yourMove not in totalPossibleMoves or not SpaceFree(board, int(yourMove)):
        print("Enter the position you want to place your move(1-9): ")
        yourMove = int(input())
    return yourMove



#Minmax Algorithm
def MinmaxAlgorithm(board, depth, isMax, alpha, beta, computerLetter): #minimax algorithm with alpha beta pruning 
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'
	if winner(board, computerLetter): #if computer wins
		return 1
	if winner(board, playerLetter): #if player wins
		return -1
	if BoardFull(board): #if board is full
		return 0 

	if isMax: #if it is the computer's turnss
		best = -(math.inf) #best value is -infinity 

		for i in range(1,10): 
			if SpaceFree(board, i):
				board[i] = computerLetter #make the move
				best = max(best, MinmaxAlgorithm(board, depth+1, not isMax, alpha, beta, computerLetter) ) # depth is used to make the computer play more defensively
				alpha = max(alpha, best) #alpha is the best value for the max player 
				board[i] = ' ' #undo the move to check for other moves 

				if alpha >= beta: #pruning
					break

		return best #return the best value 

	else: #if it is the player's turn
		best = math.inf #best value is infinity

		for i in range(1,10): 
			if SpaceFree(board, i): 
				board[i] = playerLetter #make the move
				best = min(best, MinmaxAlgorithm(board, depth+1, not isMax, alpha, beta, computerLetter) ) # depth is used to make the computer play more defensively
				beta = min(beta, best) #beta is the best value for the min player
				board[i] = ' ' #undo the move to check for other moves

				if alpha >= beta: #alpha beta pruning 
					break

		return best



#Computer Move
def ComputerTurn(board, computerLetter):
	bestVal = -(math.inf) #best value is -infinity
	bestMove = -1 #best move is -1 any move is better than -1
	for i in range(1,10):
		if SpaceFree(board, i):
			board[i] = computerLetter #make the move

			moveVal = MinmaxAlgorithm(board, 0, False, -(math.inf), (math.inf), computerLetter) #get the value of the move
			print("moveVal: ", moveVal) #prints the move values 

			board[i] = ' '  #undo the move to check for other moves 	
			if moveVal > bestVal:  #finds the best move
				bestMove = i #best move is i
				bestVal = moveVal
	print("Best Value is ", bestVal) #prints the best value
	return bestMove #returns the best move


#Checks if the board is full or not
def BoardFull(board):
	for i in range(1,10):
		if SpaceFree(board, i):
			return False
	return True


def singlePlayer():
    
    while True:
		# Reset the board
       theBoard = [' '] * 10
       human='X'
       computer='O'
       turn = FirstMove()
       print(turn + ' Will have the first Move')
       Playing = True
       while Playing:
           if turn == 'player':
               printBoard(theBoard)
               move = humanMove(theBoard)
               theBoard[move] = human
               
               if winner(theBoard, human):
                   printBoard(theBoard)
                   print('You won the game')
                   Playing = False
               else:
                   if BoardFull(theBoard):
                       printBoard(theBoard)
                       print('The game is a tie')
                       break
                   else:
                       turn = 'computer'
           else:
               move = ComputerTurn(theBoard, computer)
               theBoard[move] = computer
               if winner(theBoard, computer):
                   printBoard(theBoard)
                   print('You lose the game')
                   Playing = False
               else:
                   if BoardFull(theBoard):
                       printBoard(theBoard)
                       print('The game is a tie')
                       break
                   else:
                       turn = 'player'
       print('Do you want to play again? (yes or no)')
       if not input().lower().startswith('y'):
           exit(0)
       else:
           main()
           break

#AI VS AI
def AIvsAI():
    while True:
		# Reset the board
       theBoard = [' '] * 10
       AI='X'
       computer='O'
       turn = FirstMove()
       print(turn + ' Will have the first Move')
       Playing = True
       while Playing:
           if turn == 'player':
               printBoard(theBoard)
               move = ComputerTurn(theBoard,AI)
               theBoard[move] = AI
               
               if winner(theBoard, AI):
                   printBoard(theBoard)
                   print('AI won the game')
                   Playing = False
               else:
                   if BoardFull(theBoard):
                       printBoard(theBoard)
                       print('The game is a tie')
                       break
                   else:
                       turn = 'computer'
           else:
               move = ComputerTurn(theBoard, computer)
               theBoard[move] = computer
               if winner(theBoard, computer):
                   printBoard(theBoard)
                   print('AI lose the game')
                   Playing = False
               else:
                   if BoardFull(theBoard):
                       printBoard(theBoard)
                       print('The game is a tie')
                       break
                   else:
                       turn = 'player'
       print('Do you want to play again? (yes or no)')
       if not input().lower().startswith('y'):
           exit(0)
       else:
           main()
           break


def main():
    print("---------------------------------------------------------------------------")
    print('\nWelcome to Tic Tac Toe!\n'.center(80))
    print("---------------------------------------------------------------------------")
    print('Reference of numbering on the board')
    printBoard('0 1 2 3 4 5 6 7 8 9'.split())
    print('')
    
    while(True):
        print("Do you want to play Single Player or AI VS AI? (1/2)")
        choice=(input())
        if(choice=='1'):
            print("---------------------------------------------------------------------------")
            print("You have selected Single Player".center(80))
            singlePlayer()
            print("---------------------------------------------------------------------------")
            break
        elif(choice=='2'):
            print("---------------------------------------------------------------------------")
            print("You have selected AI VS AI".center(80))
            print("---------------------------------------------------------------------------")
            AIvsAI()
            break
        else:
            print("Invalid Choice")
            continue

main()
