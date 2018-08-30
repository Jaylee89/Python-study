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
 
x, y = 0, 0
move_x, move_y = 0, 0

my_event = pygame.event.Event(KEYDOWN, {"key":K_DOWN, "mod":0, "unicode":u' '})
pygame.event.post(my_event)
execute_times = 10
init_time=0
while True:
    #if init_time == 10:
    #    exit()
    init_time = init_time + 1
    print 'init_time is %d' % init_time
    #pygame.event.set_allowed([KEYDOWN, KEYUP])
    for event in pygame.event.get():
        if event.type == QUIT:
           exit()
    print event
    if event is not None and event.type == KEYDOWN:
        #键盘有按下？
        if event.key == K_LEFT:
            #按下的是左方向键的话，把x坐标减一
            move_x = -1
        elif event.key == K_RIGHT:
            #右方向键则加一
            move_x = 1
        elif event.key == K_UP:
            move_y = -1
            if init_time % 450 == 0:
                my_event = pygame.event.Event(KEYDOWN, {"key":K_DOWN, "mod":0, "unicode":u' '})
                pygame.event.post(my_event)
                init_time = 0
        elif event.key == K_DOWN:
            move_y = 1
            if init_time % 450 == 0:
                my_event = pygame.event.Event(KEYDOWN, {"key":K_UP, "mod":0, "unicode":u' '})
                pygame.event.post(my_event)
                init_time = 0
    elif event is not None and event.type == KEYUP:
        #如果用户放开了键盘，图就不要动了
        move_x = 0
        move_y = 0

    #计算出新的坐标
    x+= move_x
    y+= move_y

    screen.fill((0,0,0))
    screen.blit(background, (x,y))
    #在新的位置上画图
    pygame.display.update()