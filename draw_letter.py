

filename = "glyph_A.xml"

from xml.dom import minidom

doc = minidom.parse(filename)

pendown = False
import turtle
wn = turtle.Screen()
bob = turtle.Turtle()
bob.penup()

contours = doc.getElementsByTagName("contour")
for c in contours:
	pts = c.getElementsByTagName("pt")
	for pt in pts:
		x = pt.attributes["x"].value
		y = pt.attributes["y"].value
		on = pt.attributes["on"].value
		print(x,y,on)

		if int(on)==1:
			bob.goto(int(x)*0.25,int(y)*0.25)
			if pendown == False:
				pendown = True
				bob.pendown()


wn.mainloop()