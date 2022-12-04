import turtle
import numpy as np
import random
import time


def main(speed=0, bg_color="grey"):
    # create Turtle object
    turtle_screen = turtle.Screen()
    myTurtle = turtle.Turtle()
    
    # set speed to 'fastest = 0'
    myTurtle.speed(speed)

    # change background color
    turtle_screen.bgcolor(bg_color)

    """TODO: define different colors here"""
    turtle.colormode(255)

    for _ in range(10):
        # define some params
        size = 18
        pos = [np.random.randint(-300, 300), np.random.randint(-300, 300)]

        """TODO: set snowflakecreate color here (one of the colors defined above)"""

        R = random.randint(0, 255)
        B = random.randint(0, 255)
        G = random.randint(0, 255)
        myTurtle.color(R, G, B)

        # Go to the start position of the snowflakecreate
        myTurtle.penup()
        myTurtle.goto(pos[0], pos[1])
        myTurtle.pendown()

        # draw the snowflakecreate
        for _ in range(8):
            snowflake_branch(size, myTurtle)
            myTurtle.left(45)


def snowflake_branch(size, myTurtle):
    # This function draws one branch of the snowflakecreate.
    for _ in range(3):
        for _ in range(3):
            myTurtle.forward(size / 3)
            myTurtle.backward(size / 3)
            myTurtle.right(45)
        myTurtle.left(90)
        myTurtle.backward(size / 3)
        myTurtle.left(45)
    myTurtle.right(90)
    myTurtle.forward(size)


if __name__ == "__main__":
    main()
    time.sleep(20)
