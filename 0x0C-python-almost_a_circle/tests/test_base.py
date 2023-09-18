import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_constructor(self):
        b = Base()
        self.assertEqual(b.id, 1)

        b = Base()
        self.assertEqual(b.id, 2)

        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_private_attribute(self):
        base_instance = Base()
        with self.assertRaises(AttributeError):
            print(base_instance.__nb_objects)

if __name__ == "__main__":
    unittest.main()
