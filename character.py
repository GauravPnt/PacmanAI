from settings import *
import pygame
import math

vec = pygame.math.Vector2


class Character:
    """
    general behaviour of the player
    """

    def __init__(self, board: [[]]):
        self.pos = ORIGIN
        self.speed = 0.1
        self.board = board
        self.update_dir = RIGHT
        self.direction = RIGHT
        self.allowed = []

    def can_move(self, coord: vec, direction: vec):
        """
        :param coord: resultant pixel we want to move to
        :param direction: direction in which we are moving
        :return: is move feasible
        """
        # noinspection PyArgumentList
        coord = vec(round(coord.x, 1), round(coord.y, 1))
        if 1 <= coord.x <= COLS - 1 and 1 <= coord.y <= ROWS - 1:
            if direction == LEFT:
                return self.board[int(coord.y)][math.ceil(coord.x - 0.9)] in self.allowed
            if direction == UP:
                return self.board[math.ceil(coord.y - 0.9)][int(coord.x)] in self.allowed
            if direction == RIGHT:
                return self.board[int(coord.y)][int(coord.x + 0.9)] in self.allowed
            if direction == DOWN:
                return self.board[int(coord.y + 0.9)][int(coord.x)] in self.allowed
        return False

    def can_change_dir(self, direction: vec):
        """
        :param direction: direction we want to move to
        :return: is changing direction possible
        """
        coord = self.pos + self.speed * direction
        return (round(self.pos.x, 2).is_integer() and
                round(self.pos.y, 2).is_integer() and
                self.can_move(coord, direction))

    def update(self):
        """
        updates direction when possible
        :return:
        """
        new_pos = self.pos + self.speed * self.direction
        if self.can_move(new_pos, self.direction):
            self.pos += self.speed * self.direction
        if self.can_change_dir(self.update_dir):
            self.direction = self.update_dir

    def change_direction(self, direction: vec):
        """
        stores the keyboard event, updates direction when possible
        :param direction: direction to change to
        :return:
        """
        self.update_dir = direction

    def get_pos(self):
        """
        :return: converts cell coordinates to pixel position
        """
        return (int(self.pos.x * CELL_WIDTH) + CELL_WIDTH // 2,
                int(self.pos.y * CELL_HEIGHT) + CELL_HEIGHT // 2)
