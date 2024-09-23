from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        self.goto(0, 0)
        self.x_move = 7
        self.y_move = 7

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_pedal(self):
        self.x_move *= -1

    def reset_position(self):
        self.clear()
        self.goto(0, 0)
