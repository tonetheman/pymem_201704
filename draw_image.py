
from PIL import Image

img = Image.open("ball_image_32x32.png")

import turtle
turtle.colormode(255)

# trying to speed it up
turtle.hideturtle()

turtle.speed("fastest")

for i in range(img.width):
	for j in range(img.height):
		t = (i,j)
		color = img.getpixel(t)
		turtle.setpos(t)
		turtle.dot(2,color)


