# unittest
import unittest

def add(x, y):
    return x + y

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

if __name__ == '__main__':
    unittest.main()

# pytest (which is more popular as it has less boilerplate code)
def add(x, y):
    return x + y

def test_add_positive_numbers():
    assert add(2, 3) == 5
    
def test_add_negative_numbers():
    assert add(-2, -3) == -5

# Common structure when using pytest
#
# project/
# │
# ├── my_module.py        # Actual program code
# ├── test/
# │   ├── test_my_module.py   # Test file for my_module.py
# │   └── test_another_module.py  # Test file for another_module.py
