
import turtle

print("pos", turtle.position())

turtle.forward(50)
print("pos", turtle.position())

turtle.back(50)

turtle.right(90)

# set the position of the turtle does not raise the pen!
turtle.setposition(100,100)

turtle.home()

turtle.exitonclick()

