from turtle import Turtle
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

class Snake:

    """has been declared an empy list to save the objects created in the fun CREATE()"""

    def __init__(self):
        self.a = 3
        self.b = 2
        self.objects = []
        self.create()
        self.head = self.objects[0]

    def get_pos(self, i):

        """the function returns a tupple value in each object is calculated the coord"""

        x = self.objects[i].xcor()
        y = self.objects[i].ycor()
        value_returned = (x, y)
        return value_returned

    def motion_body(self):

        """here we move the body from the snake, we need the position from the item next to firt one an the rest reply the move"""
        for i in range(1, len(self.objects)):
            pos = self.get_pos(self.b-i)
            self.objects[self.a-i].goto(pos)
        self.objects[0].forward(20)

    def right_motion(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left_motion(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down_motion(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up_motion(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def add_item(self, position):

        self.objects.append(Turtle("square"))
        self.objects[-1].color("white")
        self.objects[-1].penup()
        self.objects[-1].goto(position)

    def extend(self):
        self.a += 1
        self.b += 1
        pos = self.get_pos(-1)
        self.add_item(pos)


    def create(self):

        for i in range(0, 3):
            self.objects.append(Turtle("square"))
            self.objects[i].color("white")
            self.objects[i].penup()
            self.objects[i].goto(i * 20 * -1, 0)





