import datetime
import sys
import unittest

sys.path.append('../01_hello_world')
import genetic

class OneMaxTests(unittest.TestCase):
    def test(self, length = 100):
        gene_set = [0, 1]
        
