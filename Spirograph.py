from turtle import Turtle, Screen

t = Turtle()
t.speed("fastest")
def draw_circle(size_of_gap):

    for _ in range(int(360/size_of_gap)):
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)
draw_circle(5)
screen = Screen()


screen.exitonclick()