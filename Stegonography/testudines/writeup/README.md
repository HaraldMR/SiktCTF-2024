# Writeup

To solve this challenge you need to look at the two images with strings or other steg tools.
using strings command in linux will show you that there is some code appended to each of the jpeg files.
Googling this type of code will show that it python turtle script. Putting each of the code bits into a python script as functions and running them gives you the flag.


```python
from turtle import *

def drawPre(t):
    t.penup()
    t.left(180)
    t.goto(-200, -10)
    t.left(180)
    t.pendown()
    
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    
    t.penup()
    t.forward(10)
    t.right(90)
    t.pendown()
    
    t.forward(40)
    
    t.penup()
    t.left(90)
    t.forward(10)
    t.pendown()
    
    t.left(90)
    t.forward(40)
    t.backward(20)
    t.right(45)
    t.forward(30)
    t.backward(30)
    t.right(90)
    t.forward(30)
    t.backward(30)
    t.right(45)
    t.forward(20)
    
    t.penup()
    t.left(90)
    t.forward(40)
    t.left(90)
    t.pendown()
    
    t.forward(40)
    t.left(90)
    t.forward(15)
    t.backward(30)
    
    t.penup()
    t.backward(25)
    t.pendown()
    
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    
    t.penup()
    t.forward(20)
    t.left(90)
    t.pendown()
    
    t.forward(40)
    t.left(90)
    t.forward(15)
    t.backward(30)
    
    t.penup()
    t.backward(25)
    t.pendown()
    
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.backward(25)
    t.left(90)
    t.forward(15)

    t.penup()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(15)
    t.pendown()

    t.backward(3)
    t.right(90)
    t.forward(18)
    t.right(45)
    t.forward(2)
    t.left(90)
    t.forward(2)
    t.right(45)
    t.forward(18)
    t.left(90)
    t.forward(3)

    t.penup()
    t.goto(142, -10)
    t.setheading(0)
    t.pendown()

    t.forward(3)
    t.left(90)
    t.forward(18)
    t.right(45)
    t.forward(2)
    t.left(90)
    t.forward(2)
    t.right(45)
    t.forward(18)
    t.left(90)
    t.forward(3)

    t.penup()
    t.goto(180, -10)


def drawTutel(t):
    t.penup()
    t.goto(12,-10)
    t.setheading(90)
    t.pendown()

    t.forward(40)
    t.left(90)
    t.forward(15)
    t.backward(30)

    t.penup()
    t.backward(5)
    t.left(90)
    t.pendown()

    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)

    t.penup()
    t.right(90)
    t.forward(5)
    t.pendown()

    t.forward(30)
    t.backward(15)
    t.right(90)
    t.forward(40)

    t.penup()
    t.left(90)
    t.forward(40)
    t.pendown()

    t.backward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.backward(15)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)

    t.penup()
    t.forward(10)
    t.right(90)
    t.pendown()

    t.forward(40)
    t.left(90)
    t.forward(15)

    t.penup()
    t.goto(-230,-10)
    t.setheading(180)


screen = Screen()
screen.setup(width=500, height=150)

t1 = Turtle()
t2 = Turtle()

t1.speed(6)
t1.shape("turtle")
t1.color("green")

t2.speed(6)
t2.shape("turtle")
t2.color("blue")

drawPre(t1)
drawTutel(t2)

done()
```