 #copy content of one file to other

# with open("test.txt","r") as rf:
# 	with open("test_copy.txt","w") as wf:
# 		for line in rf:
# 			wf.write(line)


#copy content of binary file to other binary file

with open("screenshot.png","rb") as rf:
	with open("screenshot_copy.png","wb") as wf:
		for line in rf:
			wf.write(line)
