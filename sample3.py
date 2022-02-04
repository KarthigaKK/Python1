#Dict (Multiple datatypes possible)

#key:value

#{key1:value1,key2:value2}

#emp=[['John','Ram','Ravi'],[28,27,29],'Python']

#print(emp[1][1])

#prog_lang='Python'

#emp={'first':'John','age':27,'prog_lang':['Python','Java']}

emp={'first':['John','Ravi'],'age':27,'prog_lang':['Python','Java']}

emp.update({'first':'jake','email':'logu@yahoo.com'})
print(emp)

del emp['age']
print(emp)
removed=emp.pop('first')
print(removed)
#print(emp['first']):print(emp[1])
print(emp.get('first'))
#print(emp.get('email'))
#print(emp['email'])

#dictionary are mutable
print(emp.get('email','Not found'))
emp['email']='john@yahoo.com'
print(emp['email'])

print(emp.keys())
print(emp.values())
print(emp.items())

for index,values in emp.items():
	print(f'{index}-{values}')

	#storing,Managing,Accessing data in dict is easy and mostly used
	
