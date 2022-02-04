def square(x):
	return x*x

# result=square(7)
# print(result)

# result=square
# print(result(4))


# def square(x):
# 	return x*x

# def cube(x):
# 	return x*x*x

# #[1,2,3,4]=[2,4,6,8]

# lst=[1,2,3,4]

# def my_sq(func,lst_args):
# 	result=[]
# 	for i in lst_args:
# 		result.append(func(i))
# 	return result

# print(my_sq(cube,lst))


# def outer_func():
# 	message='hi'

# 	def inner_func():
# 		print(message)
# 	return inner_func

# #outer_func()
# result = outer_func()
# result()
# print(result)

def outer_func(message):
	def inner_func():
		print(message)
	return inner_func

#outer_func("b")

hello_result = outer_func("Hello")
hi_result=outer_func("hello")
hello_result()
hi_result()
print(hello_result.__name__)
print(hello_result.__name__)
