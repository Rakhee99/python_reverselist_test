import unittest
from calc.lst import lst1
class testcalc(unittest.TestCase):
    def testrev1(self):
        lst = lst1()
        result = lst.rev(l=[1,2,3,4,5])
        self.assertEqual(result, [5,4,3,2,1], "reverse failed")
    def testrev2(self):
        lst = lst1()
        result = lst.rev(l=[10,20,30])
        self.assertEqual(result, [30,20,10], "reverse failed")
        