import draw
import pygame as pg
import time

pg.init()

LIMIT = 10000
SIZE_WINDOW = 900

print("############# Welcome ############")
print("What mode do you want to choose for drawing your spiral ?")
print("For the probabilistic algorithm: (p)")
print("For the deterministic algorithm: (d)")
CHOICE = input("")


# Fenêtre
window = pg.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))
pg.display.set_caption("Prime spiral")
window.fill((0,0,0))

draw.draw_spiral(window, LIMIT, CHOICE)

time.sleep(20)
pg.quit()
