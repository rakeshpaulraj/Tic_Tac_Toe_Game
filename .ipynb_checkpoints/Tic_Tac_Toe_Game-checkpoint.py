###################################################################################################
## Following function intializes the values for a new game 
###################################################################################################
def initialize():
    global board, count, player, marker1, marker2, exitgame, error, replay, gameover
    board = ['-'] * 9
    count = 1
    marker1 = 'x'
    marker2 = 'o'  
    exitgame = False
    error = False
    replay = False
    gameover = False
    displayboard(board)
    

###################################################################################################
## Following function displays the title of game 
###################################################################################################
def displaytitle():
    print('\n')
    print('*********************************************************'.center(80))
    print('TIC TAC TOE GAME'.center(80))
    print('*********************************************************\n'.center(80))
    print('Welcome to Tic Tac Toe game!'.center(80))
    print('(Player-1 is denoted by x and Player-2 is denoted by o)\n'.center(80))
    
###################################################################################################
## Following function gets input for board position 
###################################################################################################
def getinput(player):
    board_position = input(player + " : Please enter a number between 1 to 9 for the board position (or enter 0 to quit) : ")
    return board_position

###################################################################################################
## Following function checks whether the player wants to exit the game or not
###################################################################################################
def checkexit(board_position):
    if board_position == '0':
        exitgame = True
        print("Current game terminated!")
        return exitgame
    
###################################################################################################
## Following function validates the board position input and returns if any error found
###################################################################################################
def validateinput(board_position):
    error = False           
    if not board_position.isdigit():
        print("**Error : " + board_position + " is not an integer. Please enter a valid integer between 1 to 9.")
        error = True
            
    elif int(board_position) > 9:
        print("**Error : Board has only 9 positions. Please enter an integer between 1 to 9.")
        error = True 
            
    elif board[int(board_position) - 1] != '-':
        print("**Error : Number " + str(board_position) + " you entered is already used. Please enter another number.")
        error = True   
        
    return error

def updateboard(board, board_position, player):
    board_position = int(board_position)
    if player == 'PLAYER-1':
        board[board_position - 1] = marker1
    else:
        board[board_position - 1] = marker2
        
###################################################################################################
# Following function checks the result of the board and returns whether player won the game or not 
###################################################################################################
def checkresult(board):
    result = ''
    if (board[0] == board[1] == board[2] == marker1) or (board[0] == board[3] == board[6] == marker1) \
    or (board[6] == board[7] == board[8] == marker1) or (board[2] == board[5] == board[8] == marker1) \
    or (board[1] == board[4] == board[7] == marker1) or (board[3] == board[4] == board[5] == marker1) \
    or (board[0] == board[4] == board[8] == marker1) or (board[ 2] == board[4] == board[6] == marker1):
        print("Player-1 is the winner!".center(50))
        result = 'win'
    elif (board[0] == board[1] == board[2] == marker2) or (board[0] == board[3] == board[6] == marker2) \
    or (board[6] == board[7] == board[8] == marker2) or (board[2] == board[5] == board[8] == marker2) \
    or (board[1] == board[4] == board[7] == marker2) or (board[3] == board[4] == board[5] == marker2) \
    or (board[0] == board[4] == board[8] == marker2) or (board[2] == board[4] == board[6] == marker2):
        print("Player-2 is the winner!".center(50))
        result = 'win' 
    elif len([i for i in board if i == '-']) == 0:
        print("Game tied!".center(50))
        result = 'tie'
    return result


###################################################################################################
# Following function clears the output and displays the board with updated player positions
###################################################################################################
def displayboard(board):
    clear_output() 
    displaytitle()
    a = ''
    for i in range(9):
        if i == 0:
            print('============='.center(80))
        a = a + '| ' + board[i] + ' '
        if (i + 1)%3 == 0:    
            print((a + '|').center(80))
            a = ''
        if i == 8:
            print('============='.center(80))
    print('\n')
    
    
def checkreplay():
    replaygame = input("Do you want to play again? Enter Yes or No: ").lower()
    return replaygame

#def getreplay():
#    replaygame = input("Do you want to play again? : ")
#    return replaygame

###################################################################################################
### Main While loop
###################################################################################################

while True:
    initialize()

    while not exitgame and not gameover:
        
        ## Determine the player for current iteration. Turns 1, 3, 5, 7, 9 are for Player 1 and rest for Player 2
        if count%2 != 0:
            player = 'PLAYER-1'  
        else:
            player = 'PLAYER-2'

        ## get input from player
        board_position = getinput(player)
        
        ## check if player wants to exit game
        exitgame = checkexit(board_position)
        if exitgame:
            break

        ## Validate the inputs and if any error skip the iteration and get the input again
        error = validateinput(board_position)
        if error:
            continue
       
        ## Update the board with the new positions
        updateboard(board, board_position, player)
        
        ## Display the board
        displayboard(board)
        count += 1

        ## Check win or tie result
        result = checkresult(board)
        if result == 'win' or result == 'tie':
            gameover = True

    replaygame = checkreplay()
    if not replaygame == 'yes':
        print("Thanks for playing!")
        break
