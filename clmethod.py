#adding data members through object are called instance data members
#object name,self---Instance data memebrs
#write a python program which will read and display employee data

class Employee:
	cname="IBM" #class/Static data memeber
	addr="HYD,23567"  #class/Static data memeber
	def addEmployeeDetails(self,sno,empname,dept,salary):
#		self.sno = int(input("Enter Employee name:"))
#		self.empname=input("ENter employee name:")
#		self.dept=input("Enter department name:")
#		self.salary=int(input("Enter employee Salary:"))
		self.sno=sno
		self.empname=empname
		self.dept=dept
		self.salary=salary
	def displayEmployeeValues(self):
		print("---------------------------------------------")
		print("Employee details:")
		print("---------------------------------------------")
		print("Employee no:{}".format(self.sno))
		print("Employee name:{}".format(self.empname))
		print("Employee dept:{}".format(self.dept))
		print("Employee salary:{}".format(self.salary))
		print("Employee company:{}".format(self.cname))
		print("Employee pay:{}".format(Employee.pay))
		print("---------------------------------------------")
	@classmethod
	def dispCompanyName(cls):
		print("Employee address:{}".format(cls.addr))
		print("Employee company:{}".format(Employee.cname))


#main program
#create an object
Employee.pay=90000  #class/Static data memeber

emp=Employee()
emp.addEmployeeDetails(10,"Karthi","PAY",800000)
emp.displayEmployeeValues()


#emp.sno  =10
#emp.empname="Kavi"
#emp.dept="Sales"
#emp.salary=100000

print("---------------------------------------------")
print("Employee details:")
print("---------------------------------------------")
print("Employee no:{}".format(emp.sno))
print("Employee name:{}".format(emp.empname))
print("Employee dept:{}".format(emp.dept))
print("Employee salary:{}".format(emp.salary))
print("Employee company:{}".format(emp.cname))
print("Employee pay:{}".format(Employee.pay))
print("---------------------------------------------")

#class level method
emp.dispCompanyName() #using object also possible
Employee.dispCompanyName() #class level method use class name better

print(emp.__dict__)
print(help(Employee))
print(Employee.__dict__)
#print(issubclass.dispCompanyName())