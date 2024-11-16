from connectFourEnv import *
from agents import *
import math

def main():
    
    # For testing Human vs. MiniMax :
    
    game = ConnectFour()
    mm = MiniMaxAgent()
    depth = 4

    while True:
        game.debugBoard()

        if game.player == 1:  # Minimax Agent
            print("Player 1's turn (Minimax):")
            valid_moves = game.fetchLegalMoves()
            bestLoc = mm.warpperMiniMax(game.board, valid_moves, depth, game.player)
        else:  # Human
            print("Player 2's turn (Human):")
            try:
                bestLoc = int(input("Enter your column (0-6): "))
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 6.")
                continue

        # Validate the move
        if bestLoc not in game.fetchLegalMoves():
            print("Invalid move. Try again.")
            continue

        # Make the move
        game.insertCoin(game.board,bestLoc, game.player)

        # Check for a winner
        if game.winner(game.board, game.player):
            game.debugBoard()
            print(f"Player {game.player} wins!")
            break

        # Check for a draw
        if game.isCompOccupied():
            game.debugBoard()
            print("It's a draw!")
            break

        # Switch to the next player
        game.changePlayer()


if __name__ == "__main__":
    main()
