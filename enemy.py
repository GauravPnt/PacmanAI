from character import *
from settings import *
import queue


class Node:
    """
    represents a cell on the board
    """

    def __init__(self, coord: vec, target: vec):
        self.h = INF
        self.g = INF
        self.f = INF
        self.parent = None
        self.coord = coord
        self.set_heuristics(target)

    def set_heuristics(self, target):
        self.h = abs(self.coord.x - target.x) + abs(self.coord.y - target.y)

    def set_f(self):
        self.f = self.g + self.h

    def check(self):
        return 0 <= self.coord.x < COLS and 0 <= self.coord.y < ROWS

    def relax(self, u: 'Node', d: int):
        """
        :param u: source node
        :param d: distance between the two
        :return:
        """
        if self.g > u.g + d:
            self.g = u.g + d
            self.parent = u


class Enemy(Character):
    """
    generic behaviour of the enemy
    """

    def __init__(self, board: [[]], pacman_pos: vec):
        super().__init__(board)
        self.direction = RIGHT
        self.pos = ORIGIN
        self.pacman_pos = pacman_pos
        self.ds = [UP, LEFT, DOWN, RIGHT]

    def update_pacman_pos(self, pacman_pos: vec):
        self.pacman_pos = pacman_pos

    def a_star(self, target: vec):
        """
        :param target: target position to reach
        :return: shortest path if node is reachable, else loops back to one previous from current node
        """
        pq = queue.PriorityQueue()
        visit = set()
        s = Node(self.pos, target)
        s.g = 0
        pq.put((s.f, s))
        visit.add(s)
        u = None
        while not pq.empty():
            u = pq.get()[1]
            if u.coord == target:
                return u
            for ds in self.ds:
                v = Node(u.coord + ds, target)
                if v in visit:
                    continue
                if not v.check():
                    continue
                if self.board[v.coord.y][v.coord.x] == '1' or \
                        self.board[v.coord.y][v.coord.y].islower() and (ds == UP or ds == DOWN) or \
                        ds == -self.direction:
                    continue
                v.relax(u, 1)
                visit.add(v)
                pq.put((v.f, v))
        return u
