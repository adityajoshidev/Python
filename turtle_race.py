import turtle,random

screen=turtle.Screen()
screen.setup(width=500,height=400)

colors=["violet","indigo","blue","green","yellow","orange","red"]
pos_x=-230
pos_y=-70
user_bet=screen.textinput("Bet on the race!",f"Which turtle do you think will win the race? {colors}: ").lower()
turtles={}

for color in colors:
    turtles[f"{color}_turtle"]=turtle.Turtle(shape="turtle")
    turtles[f"{color}_turtle"].color(color)
    turtles[f"{color}_turtle"].penup()
    turtles[f"{color}_turtle"].setpos(pos_x,pos_y)
    pos_y+=30

drawer=turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.setpos(230,-90)
drawer.pendown()
drawer.setpos(230,130)

race_on=True
while race_on:
    for color in colors:
        turtles[f"{color}_turtle"].forward(random.randint(1,10))
        if turtles[f"{color}_turtle"].pos()[0]>230:
            if color==user_bet:
                print("You won")
            else:
                print(f"You lose")
            print(f"{color.capitalize()} won.")
            race_on=False
            break

screen.exitonclick()
