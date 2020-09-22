# see test1 for more info
import unittest
# import main file
import script

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        #        main is referencing the file name
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asdfdasf'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'pls enter num')
        
    def test_do_stuff4(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'pls enter num')
        
if __name__=='__main__': 
    unittest.main()
