import turtle

my_turtle=turtle.Turtle()
my_turtle.speed(0)

# my_turtle.forward(100)
# my_turtle.right(90)

# my_turtle.forward(100)
# my_turtle.right(90)

# my_turtle.forward(100)
# my_turtle.right(90)

# my_turtle.forward(100)
# my_turtle.right(90)

 

def square(length,angle):
	for i in range(4):
		my_turtle.forward(100)
		my_turtle.right(90)
#360/10=36 (exact circle to get circle withour overlapping)
for i in range(36):
	square(100,90)
	my_turtle.right(10)

turtle.done()
