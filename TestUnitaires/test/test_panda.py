#coding:utf-8
import sys 
sys.path.append("..")
from src.panda import Panda 
import unittest 


class test_panda(unittest.TestCase):
    def test_panda_is_instance(self):
        p = Panda("kiko", 15)
        self.assertIsInstance(p, Panda)

    def test_panda_age_is_positive(self):
        p = Panda("kiko", 15)
        self.assertGreater(p.age , 0)


if __name__ == "__main__":
    unittest.main()
