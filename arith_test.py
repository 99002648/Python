import unittest
from arith import add,sub,mul,div

 
class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(add(5,7), 12)
        #self.assertEqual(add(5,7), 15)
        self.assertEqual(sub(7,5), 2)
        #self.assertEqual(sub(7,5), 4)
        self.assertEqual(mul(5,7), 35)
        #self.assertEqual(mul(5,7), 25)
        self.assertEqual(div(35,7), 5)
        #self.assertEqual(div(35,7), 15)
        
        
if __name__ == '__main__':
    unittest.main()
