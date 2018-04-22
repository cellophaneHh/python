import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_give_default_raise(self):
        """测试默认涨薪"""
        employee = Employee('zh', '2683', 1000)
        employee.give_raise()
        self.assertEqual(6000, employee.salary)

    def test_give_other_raise(self):
        """测试非默认涨薪"""
        employee = Employee('zh', '2683', 1000)
        employee.give_raise(1000)
        self.assertEqual(2000, employee.salary)

unittest.main()
