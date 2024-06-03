import random
import turtle
t=turtle.Turtle()
scr=turtle.Screen()
t.shape("turtle")
def Ukraine():
    t.fillcolor("yellow")
    t.begin_fill()
    t.pencolor("Black")
    for i in range(2):
        t.fd(300)
        t.rt(90)
        t.fd(100)
        t.rt(90)
    t.end_fill()
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.fd(300)
        t.lt(90)
        t.fd(100)
        t.lt(90)
    t.end_fill()
def Poland():
    t.fillcolor("red")
    t.begin_fill()
    t.pencolor("Black")
    for i in range(2):
        t.fd(300)
        t.rt(90)
        t.fd(100)
        t.rt(90)
    t.end_fill()
    for i in range(2):
        t.fd(300)
        t.lt(90)
        t.fd(100)
        t.lt(90)
def India():
    t.fillcolor("orange")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.lt(90)
        t.fd(50)
        t.lt(90)
    t.end_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(50)
        t.rt(90)
    t.end_fill()
    t.rt(90)
    t.fd(50)
    t.fillcolor("green")
    t.begin_fill()
    t.fd(50)
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.fd(50)
    t.end_fill()
def Germany():
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.lt(90)
        t.fd(50)
        t.lt(90)
    t.end_fill()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(50)
        t.rt(90)
    t.end_fill()
    t.rt(90)
    t.fd(50)
    t.fillcolor("yellow")
    t.begin_fill()
    t.fd(50)
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.fd(50)
    t.end_fill()
def Russia():
    for i in range(2):
        t.fd(150)
        t.lt(90)
        t.fd(50)
        t.lt(90)
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(50)
        t.rt(90)
    t.end_fill()
    t.rt(90)
    t.fd(50)
    t.fillcolor("red")
    t.begin_fill()
    t.fd(50)
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.fd(50)
    t.end_fill()
flags= [Ukraine, Poland, India, Germany, Russia]
lives=3
points=0
t.speed(100)
while lives>0 and len(flags)>0:
    t.reset()
    flag=random.choice(flags)
    flag()
    answer=input("Which country is this flag?")
    if answer==flag.__name__:
        flags.remove(flag)
        print("Bravo")
        points+=1
        print("Your points", points)
    else:
        flags.remove(flag)
        print("Wrong")
        lives-=1
        print("Your lives", lives)
if points==5:
    print("You won")
else:
    print("You lose")
turtle.exitonclick()