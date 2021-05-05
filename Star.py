import turtle
turtle.speed(10)
turtle.color("green","azure")
turtle.begin_fill()
while True:
	turtle.forward(500)
	turtle.left(170)
	if abs(turtle.position())<1:
		break
turtle.end_fill()
turtle.done()