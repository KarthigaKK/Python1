import unittest
from emp import Employee

class TestEmployee(unittest.TestCase):
	#prerequisite to test all the below test methods.
	def setUp(self):
		#to test email we want first and last name so created instance
		self.emp_1=Employee('Logu','Rangan',1000000)
		self.emp_2=Employee('Kavi','Ravi',300000)

	def tearDown(Self):
		print("Test completed")

	def test_email(self):
		try:
			self.assertEqual(self.emp_1.email,'logu.rangan@company.com')
			self.assertEqual(self.emp_2.email,'kavi.ravi@company.com')
		
		#update first name
			self.emp_1.first='L'
			self.emp_2.first='K'

			self.assertEqual(self.emp_1.email,'l.rangan@company.com')
			self.assertEqual(self.emp_2.email,'k.ravi@company.com')
		except Exception as e:
			print(e)


	def test_fullname(self):
		try:
			self.assertEqual(self.emp_1.fullname,'Logu Rangan')
			self.assertEqual(self.emp_2.fullname,'Kavi Ravi')
			
			#update first name
			self.emp_1.first='L'
			self.emp_2.first='K'

			self.assertEqual(self.emp_1.fullname,'L Rangan')
			self.assertEqual(self.emp_2.fullname,'K Ravi')
		except Exception as e:
			print(e)


	def test_apply_raise_amt(self):
		try:
			self.emp_1.apply_raise_amt
			self.emp_2.apply_raise_amt

			self.assertEqual(self.emp_1.pay,1050000)
			self.assertEqual(self.emp_2.pay,315000)
		except Exception as e:
			print(e)	
		
#main 

if __name__ == '__main__' :
	unittest.main()