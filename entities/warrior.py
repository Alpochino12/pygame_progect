from entities.entity import Entity
import entities.skeleton as skeleton


class Warrior(Entity):
    def __init__(self, screen, board, clock, x, y, idles):
        super(Warrior, self).__init__(screen, board, clock, x, y, idles)
        self.health = 5
        self.steps_without_damage = 0

    def idle(self, cell_x, cell_y):
        enemies = self.get_enemy()
        for en in enemies:
            if abs(en[0] - self.cell_x) <= 1 and abs(en[1] - self.cell_y <= 1):
                self.attack(en)
        if abs(self.cell_x - cell_x) <= 3 and abs(self.cell_y - cell_y) <= 3\
                and self.board.board[cell_y][cell_x] == 0:
            self.steps_without_damage += 1
            if cell_x != self.cell_x or cell_y != self.cell_y:
                if self.steps_without_damage >= 5:
                    if self.health < 3:
                        self.health += 1
            self.cell_x = cell_x
            self.cell_y = cell_y
        self.board.move_entity(self.cell_x, self.cell_y, self)
        super().idle(cell_x, cell_y)

    def get_damage(self, damage: int):
        self.steps_without_damage = 0
        super(Warrior, self).get_damage(damage)

    def get_enemy(self):
        enemies = []
        for e in self.board.entities:
            if isinstance(e, skeleton.Skeleton):
                enemies.append(self.board.entities[e])
        return enemies

    def attack(self, en):
        self.board.board[en[1]][en[0]].get_damage(1)
