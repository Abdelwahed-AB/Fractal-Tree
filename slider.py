import pygame as pg


class Slider():
    def __init__(self, Surface, position, width, max_value, nob_color, bg_color):
        # Slider properties
        self.surface = Surface
        self.position = position
        self.nob_position = (position[0] + 10, position[1] + 10)
        self.width = width
        self.max_value = max_value
        self.nob_color = nob_color
        self.bg_color = bg_color
        self.value = 0

        self.isHeld = False
    # Draw the necessary graphics

    def draw(self):
        rail_rect = pg.Rect(self.position[0], self.position[1] + (20//3), self.width, 20//3)
        rail = pg.draw.rect(self.surface, (125, 126, 124), rail_rect)
        nob = pg.draw.circle(self.surface, self.nob_color, self.nob_position, 10)

    # Get the user input
    def user_input(self):
        if pg.mouse.get_pressed()[0] == 1:
            if (self.nob_position[0] - 10 < pg.mouse.get_pos()[0] < self.nob_position[0] + 10) and (self.nob_position[1] - 10 < pg.mouse.get_pos()[1] < self.nob_position[1] + 10):
                self.isHeld = True
            if self.isHeld:
                mposX = pg.mouse.get_pos()[0]
                self.nob_position = (
                    clamp(mposX, self.position[0] + 10, self.position[0] + self.width - 10), self.nob_position[1])
        else:
            self.isHeld = False

    def update(self):
        self.draw()
        self.user_input()
        self.value = ((self.nob_position[0] - self.position[0] -
                       10)/(self.width - 20)) * self.max_value


def clamp(x, minVal, maxVal):
    if x > maxVal:
        return maxVal
    elif x < minVal:
        return minVal
    else:
        return x
