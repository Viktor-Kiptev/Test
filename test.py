import unittest

import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('it is possible to set something before each test')

    def test_do_stuff_valid(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_str(self):
        test_param = 'asd'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff_none(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')


    def test_do_stuff_empty(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')

    def tearDown(self):
        print('cleaninng up')


if __name__ == '__main__':
    unittest.main()
