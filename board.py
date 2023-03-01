import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.entities = {}
        self.flag = -1
        self.set_view()

    def set_view(self, left=300, top=140, cell_size=70):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.board_right_point = left + cell_size * self.width
        self.board_bottom_point = top + cell_size * self.height

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                rect = (self.left + x * self.cell_size, self.top + y * self.cell_size,
                        self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)

    def is_mouse_on_board(self, x, y):
        return self.left <= x <= self.board_right_point \
               and self.top <= y <= self.board_bottom_point

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if not self.is_mouse_on_board(x, y):
            return None
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        return x, y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def add_entity(self, x, y, entity):
        self.entities[entity] = (x, y)
        self.board[y][x] = entity

    def move_entity(self, x, y, entity):
        self.board[self.entities[entity][1]][self.entities[entity][0]] = 0
        self.entities[entity] = (x, y)
        self.board[y][x] = entity

    def delete_entity(self, entity):
        x, y = self.entities[entity]
        self.board[y][x] = 0
        del self.entities[entity]
