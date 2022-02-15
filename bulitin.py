ddef demo_func(greeting,name='Jay'):
	return f"{greeting} - {name}"

print(demo_func('hello'))
#keyword arg--dicto
def emp_info(*args,**kwarg):
	print(args)
	print(kwarg)


emp_info('hello','hi','Ram',name='karthi',age=27)

lst=['hello','bye','hey','hi']
def find_index():
	for index,value in enumerate(lst):
		if index==1:
			print(value)


find_index()

greetings=['hello','bye','hey','hi']

def find_index1(greetings,target):
	for index,value in enumerate(greetings):
		if value == target:
			return value
	return -1


print(find_index1(greetings,'bye'))