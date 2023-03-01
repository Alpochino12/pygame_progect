from entities.entity import Entity
import entities.warrior as warrior


class Skeleton(Entity):
    def __init__(self, screen, board, clock, x, y, idles):
        self.flag = -1
        super().__init__(screen, board, clock, x, y, idles)
        self.health = 3

    def get_damage(self, damage: int):
        super(Skeleton, self).get_damage(damage)

    def idle(self, x, y):
        if self.health == 0:
            return
        super(Skeleton, self).idle(x, y)

    def get_player(self):
        for e in self.board.entities:
            if isinstance(e, warrior.Warrior):
                return self.board.entities[e]

    def move(self):
        if self.health == 0:
            return
        pl = self.get_player()
        if not pl:
            return
        step = 1
        if abs(pl[0] - self.cell_x) <= 1 and abs(pl[1] - self.cell_y <= 1):
            self.board.board[pl[1]][pl[0]].get_damage(1)

        if self.flag == -1:
            if pl[0] > self.cell_x:
                if self.board.board[self.cell_y][self.cell_x + 1]:
                    return
                self.cell_x += 1
            elif pl[0] == self.cell_x:
                if pl[1] > self.cell_y:
                    self.cell_y += 1
                elif pl[1] < self.cell_y:
                        self.cell_y += 1
            elif pl[0] < self.cell_x:
                if self.board.board[self.cell_y][self.cell_x - 1]:
                    return
                self.cell_x -= 1
        elif self.flag == 1:
            if pl[1] > self.cell_y:
                if self.board.board[self.cell_y + 1][self.cell_x]:
                    return
                self.cell_y += 1
            elif pl[1] == self.cell_y:
                if pl[0] > self.cell_x:
                    if self.board.board[self.cell_y][self.cell_x + 1]:
                        return
                    self.cell_x += 1
                elif pl[0] < self.cell_x:
                    if self.board.board[self.cell_y][self.cell_x - 1]:
                        return
                    self.cell_x -= 1
            elif pl[1] < self.cell_y:
                if self.board.board[self.cell_y - 1][self.cell_x]:
                    return
                self.cell_y -= 1
        self.flag *= -1
