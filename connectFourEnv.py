import numpy as np

class ConnectFour:
    
    def __init__(self):

        # A connect 4 game is a board with 6 rows and 7 columns with initial state wherein all slots are empty 
        # Thus, using numpy.zeros to initialise the board :
            
        self.rows = 6  
        self.columns = 7
        self.board = np.zeros((self.rows, self.columns), dtype=int)
        
        # Usually this game is played by 2 people so say Player 1 and Player 2 with Player 1 starting the game :
        self.player = 1 
        
 
        
    # for function to insert a coin into empty slot I need a helper function to tell me if a column has empty slots or not 
    # and if it has empty slots then fetch their location:
    
    def isLegalMove(self,column):
        
        boardCondition = self.board[0][column]
        
        if boardCondition == 0:
            return True
        
        return False
    
    def fetchLegalMoves(self):
        legalMoves = []
        columns = self.columns
        for location in range(columns):
            if self.isLegalMove(location):
                legalMoves.append(location)
        
        return legalMoves
    
    def insertCoin(self,board,column,player):
        # checking before inserting coin and then inserting it by 
        # initialising that position equal to the Player number:
        
        rows = self.rows

        if self.isLegalMove(column):
            for row in range(rows-1,-1,-1):
                if board[row][column] == 0:
                    board[row][column] = player
                    break
            
        
                
        
    # A function to check if the board is completely occupied :
    
    def isCompOccupied(self):
        return not np.any(self.board == 0)
    
    
    # A function to change player turn is also needed, 
    # so as this game is played amongst 2 players :
    
    def changePlayer(self):
        
        player = self.player = 2 if self.player == 1 else 1
            
        return player
        
        
    # Now to check which player won the game :
    
    # In connect 4 a player wins if :
    # i. if there are 4 coins placed one after the other in a horizontal row 
    # ii. if there are 4 coins placed one after the other in a vertical column 
    # iii. if there are 4 coins placed one after the other across any diagonal
    
    def winner(self,board,player):
        rows = self.rows
        columns = self.columns
        
        # checking for condition i :
        for row in range(rows):
            for column in range(columns-3):
                if board[row][column] == player and \
                   board[row][column + 1] == player and \
                   board[row][column + 2] == player and \
                   board[row][column + 3] == player:
                    return True
        
        # checking for condition ii :
        for row in range(rows-3):
            for column in range(columns):
                if board[row][column] == player and \
                   board[row + 1][column] == player and \
                   board[row + 2][column] == player and \
                   board[row + 3][column] == player:
                    return True
        
        # checking diagonal 1 i.e from top left to bottom right [condition iii] :
        for row in range(rows-3):
            for column in range(columns-3):
                if board[row][column] == player and \
                   board[row + 1][column + 1] == player and \
                   board[row + 2][column + 2] == player and \
                   board[row + 3][column + 3] == player:
                    return True
        
        # checking diagonal 2 i.e from top right to bottom left [condition iii] :
        for row in range(3,rows):
            for column in range(columns-3):
                if board[row][column] == player and \
                   board[row - 1][column + 1] == player and \
                   board[row - 2][column + 2] == player and \
                   board[row - 3][column + 3] == player:
                       return True
                
        
        return False
        
    # Now for evaluating the score its better to break it down into 2 parts
    # one function will keep track of score based on playerNumber and board conidtion
    # and another function to compute score for the player:
    
    def computeScore(self,player,setOfSlots):
        
        score = 0
        opponent = 2 if player == 1 else 1
        
        # In case where there are 4 in a set
        if setOfSlots.count(player) == 4:
            score += 100
        
        # In case where there are only 3 in a set
        elif setOfSlots.count(player) == 3 and setOfSlots.count(0) == 1:
            score+=10
        
        # In case where there are only 2 in a set
        elif setOfSlots.count(player) == 2 and setOfSlots.count(0) == 1:
            score+=5
        
        # In case where the opponent has 3 in a set
        if setOfSlots.count(opponent) == 3 and setOfSlots.count(0) == 1:
            score -= 8
        
        return score
    
    # now in connect 4 if we start inserting coins 
    # from the center it is more likely to lead to victory
    # because better connection opportunities :
    
    def totalScore(self, board, player):
        score = 0
        rows = self.rows
        columns = self.columns
        midCol = columns // 2

        # Center column heuristic
        midBoard = [board[row][midCol] for row in range(rows)]
        score += midBoard.count(player) * 6

        # Horizontal score
        for row in range(rows):
            rowList = list(board[row, :])
            for column in range(columns - 3):  # Ensure we don't go out of bounds
                setOfSlot = rowList[column:column + 4]
                score += self.computeScore(player, setOfSlot)

        # Vertical score
        for column in range(columns):
            colList = [board[row][column] for row in range(rows)]
            for row in range(rows - 3):  # Ensure we don't go out of bounds
                setOfSlot = colList[row:row + 4]
                score += self.computeScore(player, setOfSlot)

        # Diagonal (top-left to bottom-right)
        for row in range(rows - 3):
            for column in range(columns - 3):
                setOfSlot = [board[row + i][column + i] for i in range(4)]
                score += self.computeScore(player, setOfSlot)

        # Diagonal (bottom-left to top-right)
        for row in range(3, rows):
            for column in range(columns - 3):
                setOfSlot = [board[row - i][column + i] for i in range(4)]
                score += self.computeScore(player, setOfSlot)

        return score

                
                
    
    # A function to reset the game i.e all slots empty and Player 1 starts the game:
    def resetGame(self):
        rows = self.rows
        columns = self.columns
        self.board = np.zeros(rows,columns)
        self.player = 1
        
    # debug board 
    def debugBoard(self):
        board = self.board
        print(board)
    
    