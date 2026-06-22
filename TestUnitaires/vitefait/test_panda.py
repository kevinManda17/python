#coding:utf-8

# import sys 
# sys.path.append("../")

from panda import Panda 
import unittest 


class test_panda(unittest.TestCase):

    def setUp(self):
        self.p = Panda("kiko",21)

    def test_panda_is_instance(self):
        self.assertIsInstance(self.p, Panda)

    def test_panda_age_is_positive(self):
        self.assertGreater(self.p.age , 0)


if __name__ == "__main__":
    unittest.main()
