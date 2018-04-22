from random import randint

class Die():
    """骰子"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回骰子随机值"""
        return randint(1, self.num_sides)
