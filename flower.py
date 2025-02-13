from turtle import *
import colorsys

speed(0)
bgcolor('black')
h = 0

for i in range(6):
    for j in range(16):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.05
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    rt(60)
done()