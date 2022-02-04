
# x='global x'
# # print(x)
#LEGB rule--local,enclosing,global and builtin

# x='global x'

# def demo(z):
# 	#global x
# 	x='local x'
# 	print(z)


# demo('local z')	
# print(x)

# import builtins

# print(dir(builtins))

# def max():
# 	pass

# num=[1,2,4,7,9]

# print(max(num))
# #print(help(max))

# x='global x'
# def outer():
# 	x='outer x'

# 	def inner():
# 		nonlocal x
# 		x='inner x'
# 		print(x)
# 	inner()	
# 	print(x)


# outer()
# print(x)
