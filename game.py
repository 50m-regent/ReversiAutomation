import numpy as np

# 00 00 00 10 08 00 00 00
# 00 00 00 08 10 00 00 00

DEFAULT_BOARD = (
    0x0000001008000000,
    0x0000000810000000
)

class Player:
    agents = {
        'human': HumanAgent,
        'random': RandomAgent,
        'dqn': DQNAgent,
    }

    def __init__(self, source='human'):
        self.agent = agents[source]

    def action(self, enable_actions):
        pass

class Game:
    def __init__(self, data=DEFAULT_BOARD):
        self.board = Board()
        self.board.load(data)

        self.players = [
            None,
            Player(input('Player1 Mode<< ')),
            Player(input('Player2 Mode<< '))
        ]

        self.turn = 1

    def enable_actions(self):


    def action(self):
        self.players[self.turn].action(self.enable_actions())

    def update(self):
        
        self.turn = 0 - self.turn

    def play(self):
        while self.winner == None:
            self.action()
            self.update()
            self.debug()

if __name__ == '__main__':
    game = Game()
    game.play()
