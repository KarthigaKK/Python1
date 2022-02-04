
def decorate_function(func):
	def wrapper_function(**kwargs):
		print("hello")
		return func(**kwargs)
	return wrapper_function

@decorate_function
def display():
	print("Display function ran")
@decorate_function
def display_info(name,age):
	print(f"Display_info func ran with name:{name} and age:{age}")

display()
display_info(name="Ram",age="45")

# display()
# @decorate_function 
    #or
#decorate_display=decorate_function(display)
#decorate_display()

# #display()
#print(dir(logging))

# import logging
# logging.basicConfig(filename="test.txt",level=logging.INFO)

# def logger_func(func):
# 	def log_file(*args):
# 		logging.info(f"Running func:{func.__name__} with argument:{args}")
# 		print(func(*args))
# 	return log_file


# #@logger_func
# def add(x,y):
# 	return x+y 

# def sub(x,y):
# 	return x-y


#add(4,6)
# logger_output=logger_func(add)
# logger_output(2,6)
# print(logger_output.__name__)

