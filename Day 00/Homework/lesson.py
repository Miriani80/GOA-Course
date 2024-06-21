from turtle import *

#square
color("red")
begin_fill()
width(5)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill() 

penup()
goto(200,200)
pendown()


#roof
color("green")
begin_fill()
right(135)
forward(141)
left(90)
forward(141)
end_fill()


penup()
goto(75,0)
pendown()



#door
color("blue")
begin_fill()
right(135)
forward(75)
right(90)
forward(50)
right(90)
forward(75)
end_fill()

penup()
goto(20,180)
pendown()

#window1
color('purple')
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()



penup()
goto(180,180)
pendown()

#window2
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

exitonclick()
