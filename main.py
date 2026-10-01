from turtle import *
import os

flavors = {
        "chocolate": "#663B2A",
        "vanilla": "#d2a679",
        "mint": "#66ffcc",
        "strawberry": "#ff4d4d",
        "banana": "#EBD35F",
        "coffee": "#A15A36",
        "bubble gum": "#CC65AF"
    }

def clear_Terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def begining():
    penup()
    color("#000000")
    home()

def set_Up():
    # set up
    clear_Terminal()
    screen = Screen()
    screen.setup(width=962, height=850)
    bgcolor("#f25a5a")
    pensize(2.5)
    speed(0)
    hideturtle()
    begining()


def draw_Lines():
    color("#972121")
    x =481
    penup()
    right(90)
    goto(x,425)
    for i in range(7):
        pendown()
        forward(850)
        penup()
        x-=137.428571429
        goto(x, 425)
    begining()

def flavor_Menu():
    penup()
    color("#000000")
    goto(-220.5, 176.5)
    pendown()
    begin_fill()
    for i in range(2):
        right(90)
        forward(425)
        right(90)
        forward(240.5)
    color("#ffffff")
    end_fill()
    begining()


def write_Flavor():
    color("#CE0303")
    y=135
    goto(-340.25,y)
    for word in flavors:
        write(word, align="center", font=("Arial", 14, "bold"))
        y -= 60
        goto(-340.25, y)
    begining()

def ice_Cone():
    penup()
    goto(60, -176)
    color("#D2B48C")
    pendown()

    begin_fill()
    for i in range(3):
        right(120)
        forward(120)
    end_fill()
    # draw lines on the cone
    penup()
    goto(50, -198)
    color("#835212")
    setheading(0)
    pendown()

    forward(100)





set_Up()
draw_Lines()
ice_Cone()
done()
# penup()
# goto(0, 0)
# pendown()
# color("#FFB6C1")
# begin_fill()
# circle(55)
# end_fill()
 