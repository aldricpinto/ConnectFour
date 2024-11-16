import numpy as np
import random
import math
from connectFourEnv import *


class MiniMaxAgent:
    
    def __init__(self):
        self.cfe = ConnectFour()
        
    
        
    def minimax(self,alpha,beta,depth,maxPlayer,board,playerNumber):
        
        
        fetchLegalMoves = self.cfe.fetchLegalMoves()

        opponent = 2 if playerNumber == 1 else 1
        
        # Evaluating terminal conditions :
        
        if depth == 0 or self.cfe.isCompOccupied() or not fetchLegalMoves :
            return None,self.cfe.totalScore(board,playerNumber)
        
        
        if self.cfe.winner(board,playerNumber):
            return None, math.inf if maxPlayer else -math.inf
        
        
        if maxPlayer:
            
            value = -math.inf
            bestLoc = None
            
            for move in fetchLegalMoves:
                interimBoard = board.copy()
                self.cfe.insertCoin(interimBoard,move,playerNumber)
            
                value = max(self.minimax(alpha,beta,depth-1,False,interimBoard,opponent)[1],value)
                
                if value == self.minimax(alpha,beta,depth-1,False,interimBoard,opponent)[1]:
                    bestLoc = move
                    
                alpha = max(alpha,value)
                
                if value>=beta:
                    break
                
            bestLoc = bestLoc if bestLoc is not None else fetchLegalMoves[0]
            return bestLoc,value
                
        else:
           
            value = math.inf
            bestLoc = None
            
            for move in fetchLegalMoves:
                interimBoard = board.copy()
                self.cfe.insertCoin(interimBoard,move,opponent)
            
                value = min(self.minimax(alpha,beta,depth-1,True,interimBoard,playerNumber=1)[1],value)
                
                if value == self.minimax(alpha,beta,depth-1,True,interimBoard,playerNumber=1)[1]:
                    bestLoc = move
                    
                beta = min(beta,value)
                
                if value<=alpha:
                    break
            bestLoc = bestLoc if bestLoc is not None else fetchLegalMoves[0]
            return bestLoc,value


    
    def warpperMiniMax(self, board, valid_moves, depth, player):
        if not valid_moves:
            return None
        bestLoc,bestScore = self.minimax(-math.inf, math.inf,depth, True,board, player)
        
        return bestLoc




