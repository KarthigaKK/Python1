# wp=open("test.txt","r")

# print(wp.read())
# print(wp.closed)

# wp.close()
# print(wp.closed)

with open("test.txt","r") as f:
	for line in f:
		content=f.readline()
		print(content,end="")

