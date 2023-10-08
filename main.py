import colorgram
import random
import turtle as t


t.colormode(255)
color_list = [(176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89), (124, 218, 207), (120, 43, 71), (94, 158, 65), (227, 170, 187), (131, 184, 161), (48, 187, 202), (172, 187, 222), (232, 173, 164), (154, 209, 219), (100, 51, 43), (34, 64, 115), (44, 80, 79), (215, 207, 37), (52, 58, 66), (31, 87, 90), (76, 51, 43), (40, 67, 65), (84, 37, 55)]
random_color = random.choice(color_list)
t.hideturtle()
t.penup()
t.setheading(220)
t.forward(320)
t.setheading(0)
t.speed(0)
dot_number = 100

for dot in range(1,dot_number + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    
    if dot % 10 == 0:
        t.penup()
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

    
    






screen = t.Screen()
screen.exitonclick()