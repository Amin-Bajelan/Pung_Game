from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)

    def go_up(self):
        y = self.ycor() + 30
        self.sety(y)

    def go_down(self):
        y = self.ycor() - 30
        self.sety(y)
