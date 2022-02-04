import unittest
#from calcfunc import add
import calcfunc

class TestCalcFunc(unittest.TestCase):

	def test_add(self):
		#result=calcfunc.add(10,5)
		self.assertEqual(calcfunc.add(10,5),15)
		self.assertEqual(calcfunc.add(15,-5),10)
		self.assertEqual(calcfunc.add(-1,-1),-2)
		self.assertEqual(calcfunc.add(5,-5),0)

	def test_sub(self):
		#result=calcfunc.add(10,5)
		self.assertEqual(calcfunc.sub(10,5),5)
		self.assertEqual(calcfunc.sub(15,-5),20)
		self.assertEqual(calcfunc.sub(-1,-1),0)
		self.assertEqual(calcfunc.sub(5,-5),10)

	def test_multiply(self):
		#result=calcfunc.add(10,5)
		self.assertEqual(calcfunc.multiply(10,5),50)
		self.assertEqual(calcfunc.multiply(15,-5),-75)
		self.assertEqual(calcfunc.multiply(-1,-1),1)
		self.assertEqual(calcfunc.multiply(5,-5),-25)

	def test_divide(self):
		self.assertEqual(calcfunc.divide(0,1),0)
		self.assertEqual(calcfunc.divide(5,2),2.5)
		self.assertEqual(calcfunc.divide(-4,2),-2)
		self.assertEqual(calcfunc.divide(20,-4),-5)

if __name__  == '__main__':
	unittest.main()

