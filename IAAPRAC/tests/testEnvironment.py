import unittest

# Environment imports to be tested
from sklearn import preprocessing
from scipy import linalg
import numpy

class EnvironmentTestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testPython3(self):
        self.assertEqual(1/2, 0.5, "Python 3 test case")
    
    def testNumPy(self):
        self.assertEqual(numpy.mean([1,2,5]), 8/3, "NumPy dependency test")

    def testSciPy(self):
        self.assertEqual(linalg.det([[1,2],[3,4]]), -2, "Scipy dependency test")
        
    def testSkLearn(self):
        scaler = preprocessing.StandardScaler().fit([[1.,2.],[3.,4.]])
        self.assertEqual(scaler.mean_[0], 2., "SKLearn dependency test")
        self.assertEqual(scaler.mean_[1], 3., "SKLearn dependency test")

if __name__ == '__main__':
    unittest.main()