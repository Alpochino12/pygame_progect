import os
import random
import sys

import pygame
from board import Board
from entities.warrior import Warrior
from entities.skeleton import Skeleton

pygame.init()
pygame.key.set_repeat(200, 70)
clock = pygame.time.Clock()
board = Board(10, 8)

FPS = 50
WIDTH = 1280
HEIGHT = 720

clock = pygame.time.Clock()
size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('fon.xcf'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


# warrior
cords = x, y = 260, 100

warrior_idles = [pygame.image.load('data/idle/image_part_001.xcf')]

skeleton_idles = [pygame.image.load('data/idle_sk/image_part_001.png')]
flag = -1


def main():
    pygame.init()
    pygame.display.set_caption('rimfantastic')

    start_screen()
    running = True
    bg = pygame.image.load('data/bg.png')
    warrior_x, warrior_y = 0, 0
    skeleton_x, skeleton_y = 1, 0
    warrior = Warrior(screen, board, clock, warrior_x, warrior_y, warrior_idles)
    skeletons = [
        Skeleton(screen, board, clock, random.randint(8, 9), random.randint(0, 7), skeleton_idles)
        for i in range(5)]
    flag = -1
    # музыка
    pygame.mixer.init()
    pygame.mixer.music.load('data/music/xDeviruchi - Decisive Battle.wav')
    pygame.mixer.music.play()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.get_cell(event.pos) == None or flag == 1:
                    pass
                else:
                    warrior_x, warrior_y = board.get_cell(event.pos)
                    flag *= -1

        if warrior.health == 0:
            screen.blit(load_image('youlose.xcf'), (0, 0))
            pygame.display.update()
            continue
        if not warrior.get_enemy():
            screen.blit(load_image('youwin.xcf'), (0, 0))
            pygame.display.update()
            continue

        pygame.display.update()
        screen.blit(bg, (0, 0))
        board.render(screen)

        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(str(warrior.health), 1, (180, 0, 0))
        screen.blit(text1, (10, 50))
        screen.blit(pygame.image.load('data/heart.png'), (9, 80))
        for e in list(board.entities):
            if isinstance(e, Warrior):
                warrior.idle(warrior_x, warrior_y)
            elif isinstance(e, Skeleton):
                if flag == 1:
                    e.move()
                e.idle(e.cell_x, e.cell_y)
        if flag == 1:
            flag *= -1
        pygame.display.update()
        clock.tick(10)
    pygame.quit()


if __name__ == '__main__':
    main()
