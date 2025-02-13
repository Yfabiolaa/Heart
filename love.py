import math
from turtle import *
def love(e):
    return 15*math.sin(e)**3
def main(e):
    return 12*math.cos(e)-5*\
    math.cos(2*e)-2*\
    math.cos(3*e)-\
    math.cos(4*e)
speed(0)
bgcolor("black")
for i in range(6000):
    goto(love(i)*20,main(i)*20)
    for j in range (5):
        color("crimson")
    goto(0,0)
done() 
