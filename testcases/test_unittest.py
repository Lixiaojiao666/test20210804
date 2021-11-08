import unittest

class TestStringMethods(unittest.TestCase):

    # 在每条测试用例的前面调用
    def setUp(self) -> None:
        print('setup')

    # 在每条测试用例的后面调用
    def tearDown(self) -> None:
        print('teardown')

    # 在整个类的的前面调用，，因为是类方法，所以要加装饰器@classmethod
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    # 在整个类的的后面调用，因为是类方法，所以要加装饰器@classmethod
    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def test_abc(self):
        print('test abc  111')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print('test_upper  222')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print('test_isupper  333')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
        print('test_split  444')

if __name__ == '__main__':
    unittest.main()