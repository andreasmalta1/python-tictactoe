# TicTacToe game
# Line up three in row - horizontal, vertical and diagonally to win in a 3x3 grid
# This match can be played between two humans or compete against the computer
# The computer has two modes - random or unbeatable.

import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    # Creating the board
    @staticmethod
    def make_board():
        return [" " for _ in range(9)]

    # Printing the board as a 3x3 grid
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    # Give a value to each slot from 0 to 8
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    # Assign the letter if the chosen slot is empty
    # If not empty return False
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # After each move check for a winner
    def winner(self, square, letter):
        # Check if the values in the chosen row are all the same
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        # Check if the values in the chosen column are all the same
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True

        # Check if the values in the two diagonal lines are the same
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    # Defining the empty slots
    def empty_squares(self):
        return " " in self.board

    # Checking the number of empty slots
    def num_empty_squares(self):
        return self.board.count(" ")

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


# Gameplay function
def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    # X players starts the game and player rotates with each move
    letter = "X"
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + " makes a move to square {}".format(square))
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # If there is a winner exit the game
            letter = 'O' if letter == 'X' else 'X'  # Switch player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    # Defining the players and their letters
    # Select HumanPlayer for a human player
    # Select SmartComputerPlayer for an unbeatable computer
    # Select RandomComputer player for a computer playing at random
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
