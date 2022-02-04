#list are mutable they are easy to modify
message=['Hello', 'Hi', 'am', 'good']
greeting=["Hey","Bye"]
print(message[0:2])
message.append("Karthi")
print(message[0:5])
message.insert(0,"Dhachu")
print(message[0:5])
message.append(greeting)
print(message)
message.extend(greeting)
print(message)
message.remove(["Hey","Bye"])
print(message)
removed=message.pop(1)
print(message)
print(removed)

#in operator

print("Hi" in message)

for i in message:
	print(i,end=" ")
print("\n")


for index,value in enumerate(message):
	print(index,end=" ")
	print(value,end=" ")
print("\n")

if False:
	print("Mall gate should be open...so i can access any shops")

greeting=['hello','hi','Ram']	
greeting_str='!'.join(greeting) # string to list with speration !
print(greeting_str)
print(type(greeting_str))
greeting_lst=greeting_str.split("!") #list to string
print(greeting_lst)
print(type(greeting_lst))
#mutable
list_1=["Hello","Hi","Bye"]
list_2=list_1
print(list_1)
print(list_2)
list_1[0]='Hey'
print(list_1)
print(list_2)

#immutable tuple
tuple_1=("Hello","Hi","Bye")
for i in tuple_1:
	print(i)
tuple_2=tuple_1
print(tuple_1)
print(tuple_2)
tuple_1[0]='Hey'
print(tuple_1)
print(tuple_2)
 
#sets(unordered everytime set order change)
sets={"Hello","Hi","Bye","hello"}
print(sets)
#betterway to use with membership operator
print('bye')

#empty list:

empty_list=[]
empty_list=list()

#empty_tuple
empty_tuple=()
empty_tuple=tuple()

#empty_set
empty_set={} # we use this for creating dictionary
#empty_set=set{}

emp={'first':['John','Ravi','Jake'],'age':['28','24','23'],'prog-lang':'python'}

print(emp.get['first'])

