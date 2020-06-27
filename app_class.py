from pacman import *
from settings import *

pygame.init()


class App:
    """
    app class
    """

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.board = []
        self.background = None
        self.pacman = None
        self.load()

    def run(self):
        """
        check for events
        update players, enemies, and boards state
        draw the player, enemies and board on screen
        :return:
        """
        while self.running:
            self.events()
            self.update()
            self.draw()

    def load(self):
        """
        initialize the background and the grid
        :return:
        """
        self.background = pygame.image.load('maze.png')
        with open("walls.txt") as file:
            self.board = [[x for x in ''.join(line.split())] for line in file]
        # print(self.board)
        self.pacman = Pacman(self.board)

    def draw_grid(self):
        """
        draw grid corresponding to the maze on the screen
        :return:
        """
        for _x in range(COLS):
            pygame.draw.line(self.background, GREY,
                             (_x * CELL_WIDTH, 0), (_x * CELL_HEIGHT, HEIGHT))
        for _y in range(ROWS):
            pygame.draw.line(self.background, GREY,
                             (0, _y * CELL_HEIGHT), (WIDTH, _y * CELL_HEIGHT))

    def draw_character(self):
        """
        draw pacman and the enemies
        :return:
        """
        pygame.draw.circle(self.screen, PACMAN_COLOR,
                           self.pacman.get_pos(), CELL_WIDTH // 2)

    def events(self):
        """
        listen for keyboard events
        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.pacman.change_direction(LEFT)
                if event.key == pygame.K_RIGHT:
                    self.pacman.change_direction(RIGHT)
                if event.key == pygame.K_DOWN:
                    self.pacman.change_direction(DOWN)
                if event.key == pygame.K_UP:
                    self.pacman.change_direction(UP)

    def update(self):
        """
        update pacman, enemies and the board
        :return:
        """
        self.pacman.update()
        pygame.display.update()

    def draw(self):
        """
        draw the player, enemies and board on screen
        :return:
        """
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, 0))
        # self.draw_grid()
        self.draw_character()
