class Entity:
    def __init__(self, screen, board, clock, x, y, idles):
        self.screen = screen
        self.clock = clock
        self.board = board
        self.cell_x = x
        self.cell_y = y
        self.idles = idles
        board.add_entity(self.cell_x, self.cell_y, self)
        self.health = 3

        self.idle(x, y)

    def idle(self, x, y):
        idle_anim_count = 0
        self.board.move_entity(x, y, self)
        cords = x, y = 260 + self.cell_x * 70, 100 + self.cell_y * 70
        self.screen.blit(self.idles[idle_anim_count], (x, y))

    def get_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.board.delete_entity(self)
