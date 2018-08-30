#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

background_image_filename = 'a.jpg'
 
import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
screen = pygame.display.set_mode((620, 388), 0, 32)
background = pygame.image.load(background_image_filename).convert()
 
Fullscreen = False
 
while True:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if event.type == KEYDOWN:
        if event.key == K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode((620, 388), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((620, 388), 0, 32)
 
    screen.blit(background, (0,0))
    pygame.display.update()