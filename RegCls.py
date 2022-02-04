class Emp1:

	raise_amt=1.05
	num_of_emps=0
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		

	num_of_emps += 1

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise_amt(self):
		self.pay=self.pay * self.raise_amt
		return self.pay

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amt=amount

	
	def email(self):
		return f"{self.first.lower()}.{self.last.lower()}@company.com"

	@classmethod #Alternate Constructor
	def from_str(cls,emp_str):
		first,last,pay=emp_str.split('-')
		return cls(first,last,pay)

	@staticmethod
	def is_workday(day):
 		if day.weekday()==5 or day.weekday()==6:
 			return False
 		return True


#subclasses--dont repeat the concept

class Developer(Emp1):
	def __init__(self,first,last,pay,prog_lang):
		super().__init__(first,last,pay)
		self.prog_lang=prog_lang

class Manager(Emp1):
	def __init__(self,first,last,pay,employees=None):
		super().__init__(first,last,pay)

		if employees is None:
			self.employees=[]
		else:
			self.employees=employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)
		
	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def display_emp(self):
		for emp in self.employees:
			print(emp.fullname())

print(Emp1.num_of_emps)
emp_1=Emp1('Karthi','Kalyan',9000)
dev_1=Developer('John','K',90000,'python')
print(dev_1.prog_lang)
mgr=Manager('John','K',90000)

mgr.add_emp(emp_1)
mgr.add_emp(dev_1)
mgr.remove_emp(dev_1)
mgr.display_emp()
#print(mgr.display_emp())

print(issubclass(Manager,Emp1))
print(issubclass(Manager,Developer))
print(isinstance(mgr,Manager))
print(isinstance(emp_1,Manager))
import datetime
print(datetime.__dict__)

#print(help(Developer))
# import datetime

# my_date=datetime.date(2022,2,12)
# print(Emp1.is_workday(my_date))

# emp_1=Emp1("Karthi","Kalyan",9000)


# #print(emp_1.first)
# Emp1.set_raise_amt(1.90)
# print(Emp1.raise_amt)

# print(emp_1.fullname())
# emp_1.first="Kirthi"
# print(emp_1.first)
# print(emp_1.email())

# print(emp_1.apply_raise_amt())
# # num_amt=emp_1.set_raise_amt(2)
# # print(num_amt)

# emp_1_str='John - H - 1000'
# first,last,pay=emp_1_str.split('-')
# print(pay)
# #print(emp_1_str.split('-'))

# #Instance/Regular method
# new_emp=emp_1.from_str(emp_1_str)
# print(new_emp.first)

# #class levelmethod called through class name
# new_emp=Emp1.from_str(emp_1_str)
# print(new_emp.first)