# Defining the players

import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


# Human Player that gets a move depending on the user entry
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


# Random computer players that gets a move by random
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


# Smart computer player
class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # If the smart computer is playing first it chooses the first slot at random
    # If not we use the minimax so that we can find the best possible move
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = "O" if player == "X" else "X"

        # We check if the previous move is a winner
        if state.current_winner == other_player:
            return {"position": None, "score": 1 * (state.num_empty_squares() + 1) if other_player == max_player else
                                                                                -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}  # Each score should be maximized
        else:
            best = {"position": None, "score": math.inf}  # Each score should minimized
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # Simulate a game after making that move

            # Undo the move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move  # This represents the most optimal next move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
