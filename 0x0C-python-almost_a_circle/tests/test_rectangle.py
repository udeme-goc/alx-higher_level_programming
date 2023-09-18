import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        # Test if the constructor initializes attributes correctly
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_str(self):
        # Test if __str__ method returns the expected string format
        r = Rectangle(10, 2)
        pattern = r"\[Rectangle\] \(\d+\) 0/0 - 10/2"
        self.assertRegex(str(r), pattern)

    def test_width_validation(self):
        # Test width attribute validation
        # Test if TypeError is raised for non-integer width
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        # Test if ValueError is raised for width <= 0
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        # Test if ValueError is raised when setting width to a negative value
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

    def test_height_validation(self):
        # Test height attribute validation
        # Test if TypeError is raised for non-integer height
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        # Test if ValueError is raised for height <= 0
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        # Test if ValueError is raised when setting height to a negative value
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.height = -2

    def test_x_validation(self):
        # Test x attribute validation
        # Test if TypeError is raised for non-integer x
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "0", 0)
        # Test if ValueError is raised when setting x to a negative value
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.x = -1

    def test_y_validation(self):
        # Test y attribute validation
        # Test if TypeError is raised for non-integer y
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "0")
        # Test if ValueError is raised when setting y to a negative value
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.y = -1

    def test_area(self):
        # Test area method
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        # Test if display method prints the rectangle with '#' character.
        r = Rectangle(4, 3, 2, 1, 12)
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        expected_output = "\n  ####\n  ####\n  ####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_format(self):
        # Test if __str__ method returns the expected string format.
        r = Rectangle(4, 3, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/3")

        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")

if __name__ == "__main__":
    unittest.main()
