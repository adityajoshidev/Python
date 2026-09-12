import random
import turtle

timmy=turtle.Turtle()
screen=turtle.Screen()
turtle.colormode(255)
timmy.speed(0)

def draw_square():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)

def draw_dashed_line():
    for i in range(25):
        timmy.forward(10)
        timmy.up()
        timmy.forward(10)
        timmy.down()

def generate_random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

def draw_diff_shapes():
    for i in range(3,11):
        angle=360/i
        for j in range(i):
            timmy.color(generate_random_color())
            timmy.right(angle)
            timmy.forward(100)

def generate_random_walk():
    timmy.pensize(7)
    turn={"left":timmy.left,
          "right":timmy.right,
          }
    move={"forward":timmy.forward,
          "backward":timmy.backward,
          }
    while True:
        timmy.color(generate_random_color())
        random.choice(list(turn.values()))(90)
        random.choice(list(move.values()))(15)

def draw_spirograph():
    i=0
    while i<360:
        timmy.color(generate_random_color())
        timmy.setheading(i)
        timmy.circle(75)
        i+=5

screen.exitonclick()
