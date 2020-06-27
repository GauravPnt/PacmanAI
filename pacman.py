from character import *


class Pacman(Character):
    """
    pacman class
    """
    def __init__(self, board):
        super().__init__(board)
        # noinspection PyArgumentList
        self.pos = vec(13, 29)
        self.allowed = ['C', 'E']
