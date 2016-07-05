from turtle import *
wn = Screen()
wn.title('Mickey Mouse')
wn.bgcolor('lightyellow')

shape('turtle')

head = 30
setheading(head)
pensize(6)

penup()
left(90)
forward(120)
right(50)
pendown()
begin_fill()

for i in xrange(150): #Left ear of Micky mouse being drawn
    forward(3)
    left(2)

right(130)

for i in xrange(120):
    forward(5)
    left(2)

right(130)

for i in xrange(150): #right ear of Micky mouse being drawn
    forward(3)
    left(2)

right(134)

for i in xrange(25):
    forward(5)
    left(2)

end_fill()
done()
