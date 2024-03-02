#!/usr/bin/env python

# Displays the Berlin clock
# 2020-06-13

import pygame

import sys, time, datetime

ORANGE = 192, 0, 0
YELLOW = 192, 192, 0
BACKGROUND = 0, 0 , 0
GRAY = 50, 50, 50
BORDER = 1
RES = 220,250

def mainprog(win, res):
    box4, box11, boxy = res[0] // 4, res[0] // 11, res[1] // 5
    b11rest = res[0] - 11 * box11

    now = datetime.datetime.now()
    for x in range(4):
        h1, h2 = divmod(now.hour, 5)
        mm = now.minute % 5
        if x < h1: c1 = ORANGE
        else: c1 = GRAY
        if x < h2: c2 = ORANGE
        else: c2 = GRAY
        if x < mm: c3 = YELLOW
        else: c3 = GRAY
        pygame.draw.rect(win, c1, [x * box4 + BORDER, boxy + BORDER,
            box4 - 2 * BORDER, boxy - 2 * BORDER])
        pygame.draw.rect(win, c2, [x * box4 + BORDER, 2 * boxy + BORDER,
            box4 - 2 * BORDER, boxy - 2 * BORDER])
        pygame.draw.rect(win, c3, [x * box4 + BORDER, 4 * boxy + BORDER,
            box4 - 2 * BORDER, boxy - 2 * BORDER])
    for x in range(11):
        m5 = now.minute // 5
        if x < m5:
            if (x + 1) % 3 == 0: c = ORANGE
            else: c = YELLOW
        else: c = GRAY
        if x == 10:
            pygame.draw.rect(win, c, [x * box11 + BORDER, 3 * boxy + BORDER,
                box11 - 2 * BORDER + b11rest, boxy - 2 * BORDER])
        else:
            pygame.draw.rect(win, c, [x * box11 + BORDER, 3 * boxy + BORDER,
                box11 - 2 * BORDER, boxy - 2 * BORDER])
    if now.second % 2 == 0: c = YELLOW
    else: c = GRAY
    pygame.draw.circle(win, c, (2 * box4, boxy // 2), boxy // 2 - BORDER)

class Berlin:
    def __init__(self):
        pygame.init()
        self.res = RES
        self.screen = pygame.display.set_mode(self.res, pygame.RESIZABLE)
        pygame.display.set_caption('Berlin')
        self.screen.fill(BACKGROUND)
        self.clock = pygame.time.Clock()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.running = False
            if event.type == pygame.VIDEORESIZE:
                self.res = event.w, event.h
                self.last = 0
                self.screen = pygame.display.set_mode(self.res, pygame.RESIZABLE)

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(10)
            self.events()
            self.update()
        pygame.quit()

    def update(self):
        self.screen.fill(BACKGROUND)
        mainprog(self.screen, self.res)
        pygame.display.flip()

c = Berlin()
c.run()

