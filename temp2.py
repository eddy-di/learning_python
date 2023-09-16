import turtle as t


def chess(length, size):
    t.hideturtle()
    t.speed(0)
    for i in range(size):
        if i % 2 == 0:
            t.penup()
            t.goto(-length * (size * 0.5), length * (size * 0.5) + (-length * i))
            t.pendown()
            for j in range(size): # even row
                if j % 2 == 0:
                    t.begin_fill()
                    for _ in range(4):
                        t.forward(length)
                        t.right(90)
                    t.end_fill()
                    t.forward(length)
                else:
                    t.pendown()
                    for _ in range(4):
                        t.forward(length)
                        t.right(90)
                    t.forward(length)
            t.penup()
        else:
            t.penup()
            t.goto(-length * (size * 0.5), length * (size * 0.5) + (-length * i))
            t.pendown()
            for k in range(size): # odd row
                if k % 2 != 0:
                    t.begin_fill()
                    for _ in range(4):
                        t.forward(length)
                        t.right(90)
                    t.end_fill()
                    t.forward(length)
                else:
                    for _ in range(4):
                        t.forward(length)
                        t.right(90)
                    t.forward(length)
            t.penup()
        
        
chess(10, 20)