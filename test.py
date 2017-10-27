import unittest
from module import Calculator


class ModuleTest(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator(8, 4)

    def tearDown(self):
        pass

    def test_add(self):
        """

        """
        result = self.cal.add()
        self.assertEqual(result,12)

    def test_div(self):
        result = self.cal.div()
        self.assertEqual(result,2)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest("test_div"))

    runner = unittest.TextTestRunner()
    runner.run(suite)