import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
clock = turtle.Turtle()
clock.shape("turtle")
clock.color("blue")
for i in range(12):
    clock.penup()
    clock.forward(120)
    clock.stamp()
    clock.backward(10)
    clock.pendown()
    clock.backward(10)
    clock.penup()
    clock.backward(100)
    
    clock.left(30)

 
 