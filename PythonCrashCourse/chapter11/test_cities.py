"""
测试city_functions模块
"""
import unittest

from city_functions import city_country

class CityFunctionTest(unittest.TestCase):
    """测试类"""
    def test_city_functions(self):
        city = "beijing"
        country = 'china'
        formatted_info = city_country(city, country)
        self.assertEqual("Beijing, China - Population ", formatted_info)

unittest.main()
