import draw
import pygame as pg
import time

pg.init()

LIMIT = 2000
SIZE_WINDOW = 900

# Fenêtre
window = pg.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))
pg.display.set_caption("Prime spiral")
window.fill((0,0,0))

draw.draw_spiral(window, LIMIT)

time.sleep(20)
pg.quit()
