import pickle
print(dir(pickle))

n=int(input("enter how many students u have:"))
if(n<=0):
	print(f"{n} is invalid input")
else:
	for i in range(n+1):
		print("-"*50)
		print(f"Enter {n} student details:")
		sno=int(input("Enter student no:"))
		sname=input("Enter student name:")
		smarks=input("Enter the student marks:")
		cname=input("Enter the student college marks:")
		print("-"*50)
		lst=list()
		lst.append(sno)
		lst.append(sname)
		lst.append(smarks)
		lst.append(cname)
		pickle.dumps(lst,wp)
		print(f"{i} student record saved in file:")

