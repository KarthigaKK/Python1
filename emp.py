class Employee:

	raise_amt=1.05

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		
	@property
	def fullname(self):
		return f"{self.first} {self.last}"
	@property	
	def apply_raise_amt(self):
		self.pay =int(self.pay * self.raise_amt)
	

	@property
	def email(self):
		return f"{self.first.lower()}.{self.last.lower()}@company.com"

emp_obj_1=Employee('Logu','Rangan',1000000)

emp_obj_1=Employee('Logu','Rangan',1000000)
emp_obj_2=Employee('Kavi','Ravi',300000)

print(emp_obj_1.pay)
print(emp_obj_2.pay)
emp_obj_1.apply_raise_amt
emp_obj_2.apply_raise_amt

print(emp_obj_1.pay)
print(emp_obj_2.pay)