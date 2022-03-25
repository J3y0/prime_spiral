import pygame as pg
import prime_test as prime
from math import cos, sin, pi
import time

SIZE_WINDOW = 900
STEP = 15 # (en pixel)
WIDTH = 3
COLOR = (255,255,255)


def refresh():
    pg.display.update()

def draw_line(window, x_start, y_start, x_end, y_end, width_line, color_line = (255,255,255)):
    pg.draw.line(
                window,
                start_pos = (x_start, y_start),
                end_pos = (x_end, y_end),
                width = width_line,
                color = color_line
                )

def draw_spiral(window, LIMIT, CHOICE):
    """Tous les deux virages, on doit augmenter de un le nombre de pas fait"""

    x_init, y_init = 450,450
    number_step = 0
    nbre_virage = 0
    compteur = 0

    angle = [0, pi/2, pi, 3*pi/2]

    while compteur < LIMIT:
        if nbre_virage%2 == 0:
            number_step += 1

        for j in range(number_step):
            compteur += 1
            if compteur > LIMIT:
                break

            x_end, y_end = x_init + STEP*cos(angle[nbre_virage%4]), y_init - STEP*sin(angle[nbre_virage%4]) # Minus because (0,0) is at the top right of the screen

            draw_line(window, x_init, y_init, x_end, y_end, WIDTH, COLOR)
            
            if CHOICE == 'd':
                if compteur > 1 and prime.is_prime_div(compteur):
                    draw_point(window, (x_end+x_init)/2, (y_end+y_init)/2, WIDTH + 2, COLOR)
           
            elif CHOICE == 'p':
                if compteur > 1 and prime.is_prime_fermat(compteur):
                    draw_point(window, (x_end+x_init)/2, (y_end+y_init)/2, WIDTH + 2, COLOR)

            x_init, y_init = x_end, y_end
            time.sleep(0.005)
            refresh()
        nbre_virage += 1





def draw_point(window, x, y, radius = 1, color_point = (255,255,255)):
    pg.draw.circle(window, color_point, (x,y) , radius)


if __name__ == '__main__':
    pg.init()

    # Fenêtre
    window = pg.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))
    pg.display.set_caption("Prime spiral")
    window.fill((0,0,0))

    draw_spiral(window, 200,'p')

    time.sleep(20)
    pg.quit()
