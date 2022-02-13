import random
import turtle

turtle.speed(0)
turtle.Screen().bgcolor('black')
def pen(colour):
    (turtle.color(colour))

pen('red')
def firework1(size):
    for num in range(20):
        turtle.forward(size)
        turtle.right(180 - 360 / 20)

firework1(60)
def move():
    turtle.penup()
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    turtle.goto(x, y)
    turtle.pendown()

move()
pen('yellow')
firework1(75)
move()
pen('blue')
firework1(97)
move()
pen('purple')
firework1(86)
move()
pen('lightblue')
firework1(150)
move()
pen('pink')
firework1(78)
move()
pen('orange')
firework1(170)
move()
pen('violet')
firework1(190)
move()
pen('green')
firework1(200)