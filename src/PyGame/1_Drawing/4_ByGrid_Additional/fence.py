# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Fence")

# -*- acsection: main -*-
canvas.fill(pg.Color("skyblue")) # paint background
pg.draw.rect(canvas, pg.Color("green"), (0, 200, 300, 100))  # grass

pg.draw.line(canvas, pg.Color('brown'), ( 10, 100), (290, 100), 10)
pg.draw.line(canvas, pg.Color('brown'), ( 10, 250), (290, 250), 10)
pg.draw.polygon(canvas, pg.Color('brown'), [( 20, 80), ( 30,  70), ( 40, 80), ( 40, 270), ( 20, 270)])
pg.draw.polygon(canvas, pg.Color('brown'), [( 60, 80), ( 70,  70), ( 80, 80), ( 80, 270), ( 60, 270)])
pg.draw.polygon(canvas, pg.Color('brown'), [(100, 80), (110,  70), (120, 80), (120, 270), (100, 270)])
pg.draw.polygon(canvas, pg.Color('brown'), [(140, 80), (150,  70), (160, 80), (160, 270), (140, 270)])
pg.draw.polygon(canvas, pg.Color('brown'), [(180, 80), (190,  70), (200, 80), (200, 270), (180, 270)])
pg.draw.polygon(canvas, pg.Color('brown'), [(220, 80), (230,  70), (240, 80), (240, 270), (220, 270)])
pg.draw.polygon(canvas, pg.Color('brown'), [(260, 80), (270,  70), (280, 80), (280, 270), (260, 270)])

# -*- acsection: after-main -*-
pygamebg.wait_loop()
