import turtle as trtl

painter = trtl.Turtle()

painter.pencolor('red')
painter.left(180)
painter.fd(90)
painter.right(90)
painter.fd(200)
painter.right(90)
painter.fd(90)
painter.right(90)
painter.fd(200)
painter.pencolor('blue')
painter.left(90)
painter.fd(50)
painter.left(135)
painter.fd(71)
painter.penup()
painter.goto(-90,0)
painter.setheading(180)
painter.pendown()
painter.fd(50)
painter.right(135)
painter.fd(71)
painter.penup()
painter.goto(-90,200)
painter.pendown()
painter.setheading(270)
painter.right(30)
painter.pencolor('black')
painter.bk(90)
painter.right(120)
painter.bk(90)
painter.penup()
painter.goto(-30,100)
painter.pendown()
painter.pencolor('blue')
painter.circle(15)
painter.penup()
painter.goto(10,10)
painter.pendown()
painter.fillcolor('blue')
painter.begin_fill()




window = trtl.Screen()
window.mainloop()