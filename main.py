import turtle as t
import random
t.colormode(255)
co = [
(220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222), (203, 134, 157),(180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52), (213, 87, 61),
(197, 85, 112), (208, 223, 231), (229, 199, 114), (57, 166, 135), (141, 33, 42), (8, 104, 80),
(47, 158, 182), (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157), (126, 38, 34),(156, 210, 197), (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47)
]

tim = t.Turtle()
src = t.Screen()
tim.speed(0)
tim.up()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
n = 10
while n > 0:
    for _ in range(10):
        tim.dot(20, random.choice(co))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(360)
    n -= 1
src.exitonclick()

