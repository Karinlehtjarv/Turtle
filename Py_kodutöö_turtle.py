#ITT-20
#Karin Leht-Järv
#Turtle kujund 14

import turtle

def draw_square(some_turtle):

    for i in range (1,5):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    #Turtle Brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(6)
    brad.pensize(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #Turtle Angie
    angie = turtle.Screen()
    angie.shape("turtle")
    angie.color("blue")
    angie.speed(5)
    angie.pensize(2)
    size=1
    while (True):
        angie.forward(size)
        angie.right(91)
        size = size + 1

    window.exitonclick()

draw_art()
# import turtle
# turtle.bgcolor("black")
#                    for i in range(5):
#                          for colours in ("red" ,"magenta","white","cyan","green","yellow","blue","purple","pink"):
#                                  turtle.color(colours)
#                                  turtle.pensize(3)
#                                  turtle.left(12)
#                                  turtle.forward(200)
#                                  turtle.left(90)
#                                  turtle.forward(200)
#                                  turtle.left(90)
#                                  turtle.forward(200)
#                                  turtle.left(90)
#                                  turtle.forward(200)
#                                  turtle.left(90)
# 
# import turtle
# window = turtle.Screen()
# window.bgcolor("lightblue")
# brandom = turtle.Turtle()
# brandom.fillcolor('red')
# brandom.pencolor('red')
# brandom.pensize(3)
# 
# def drawsq(t, s):
#     for i in range(4):
#         t.forward(s)
#         t.left(90)
#     
# for i in range(1,9):
#     brandom.left(360/i)
#     drawsq(brandom, 50)