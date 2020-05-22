import pygame
from pygame.locals import *
import sys
from slider import *
import time

vec = pygame.Vector2
color = pygame.color.Color
red = color(222, 45, 33)
orange = color(232, 131, 27)

font = "Arial"


class Branch(object):
    def __init__(self, surface, start_pos, dir, length, color, width=2,
                 growing_angle1=45, growing_angle2=45):

        self.surface = surface
        self.start_pos = start_pos
        self.dir = dir
        self.length = length
        self.color = color
        self.width = width
        self.growing_angle1 = growing_angle1
        self.growing_angle2 = growing_angle2

        self.end_pos = self.dir * self.length + self.start_pos

    def draw(self):
        pygame.draw.line(
            self.surface, self.color, self.start_pos, self.end_pos, self.width)

    def grow(self):
        dir_1 = self.dir.rotate(self.growing_angle1)
        dir_2 = self.dir.rotate(-self.growing_angle2)
        clr = self.color + color(20, 20, 20)

        b1 = Branch(self.surface, self.end_pos, dir_1, self.length * 0.7,
                    clr, self.width, self.growing_angle1, self.growing_angle2)

        b2 = Branch(self.surface, self.end_pos, dir_2, self.length * 0.7,
                    clr, self.width, self.growing_angle1, self.growing_angle2)
        return([b1, b2])


class Tree(object):
    def __init__(self, root, depth):
        self.root = root
        self.tree = []
        self.depth = depth

    def grow(self, branch=None, depth=0):
        if depth >= self.depth:
            return

        if depth == 0:
            new_branches = [self.root]
        else:
            new_branches = branch.grow()

        self.tree.extend(new_branches)

        for new_branch in new_branches:
            self.grow(new_branch, depth+1)


WINDOW_SIZE = (400, 600)
BG_COLOR = color(42, 42, 42)
FPS = 60
DEPTH = 10
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

root = Branch(screen, vec(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] -
                          200), vec(0, -1), 100, orange)
tree = [root]
angle1 = Slider(screen, (150, 450), 100, 180, red, orange)
angle2 = Slider(screen, (150, 500), 100, 180, red, orange)

font = pygame.font.SysFont(font, 12)
text_1 = font.render('Angle 1 :', True, color(255, 255, 255))
text_2 = font.render('Angle 2 :', True, color(255, 255, 255))

while True:
    clock.tick(FPS)
    angle1.update()
    angle2.update()
    screen.blit(text_1, (100, 450))
    screen.blit(text_2, (100, 500))
    # Set new angle
    root.growing_angle1 = angle1.value
    root.growing_angle2 = angle2.value

    tree = Tree(root, DEPTH)
    tree.grow()

    for i in range(len(tree.tree)):
        tree.tree[i].draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    pygame.display.update()
    screen.fill(BG_COLOR)
