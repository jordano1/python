import unittest

class TestGame(unittest.TestCase):
   def test_input(self):
        test_param = 10
        #        main is referencing the file name
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
