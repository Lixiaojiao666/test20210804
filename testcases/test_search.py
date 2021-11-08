import unittest

class Search:

    def search(self):
        print('search')
        return True

class TestSearch(unittest.TestCase):
    '''
    @classmethod
    def setUpClass(cls) -> None:
        cls.search = Search()
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')
    '''
    def setUp(self) -> None:
        print('setup')
        self.search = Search()

    def tearDown(self) -> None:
        print('tearDown')

    def test_search1(self):
        print('test_search1')
        #实例化Search类
        #mysearch1 = Search()
        #实例调用search方法
        assert True == self.search.search()

    def test_search2(self):
        print('test_search2')
        #实例化Search类
        #mysearch2 = Search()
        #实例调用search方法
        assert True == self.search.search()

    def test_search3(self):
        print('test_search3')
        #实例化Search类
        #mysearch3 = Search()
        #实例调用search方法
        assert True == self.search.search()
class TestSearch1(unittest.TestCase):

    #@classmethod
    #def setUpClass(cls) -> None:
    #    cls.search = Search()
    #    print('setUpClass')

    #@classmethod
    #def tearDownClass(cls) -> None:
    #    print('tearDownClass')

    def setUp(self) -> None:
        print('setup_方法级别1')
        self.search = Search()

    def tearDown(self) -> None:
        print('tearDown_方法级别1')

    def test_search11(self):
        print('test_search11')
        #实例化Search类
        #mysearch1 = Search()
        #实例调用search方法
        assert True == self.search.search()

    def test_search22(self):
        print('test_search22')
        #实例化Search类
        #mysearch2 = Search()
        #实例调用search方法
        assert True == self.search.search()

    def test_search33(self):
        print('test_search33')
        #实例化Search类
        #mysearch3 = Search()
        #实例调用search方法
        assert True == self.search.search()

    def test_equal(self):
        print('断言相等')
        self.assertEqual(1,1,'判断1=1') #断言相等

    def test_notequal(self):
        print('断言不相等')
        self.assertNotEqual(1,2,'判断1 ！= 2 ') #断言不相等

    def test_assertTure(self):
        print('断言表达式为Ture')
        self.assertTrue(1==2,'判断1==1为真')#断言表达式为真

    def test_assertFalse(self):
        print('断言表达式为假')
        self.assertFalse(1==1,'判断1==2为假')#断言表达式为假

class TestSearch2(unittest.TestCase):
     def test_case1(self):
         print('***********************')


if __name__ == '__main__':
     #执行测试用例方法一，执行当前文件所有的unittest测试用例
     #unittest.main()#可以调用所有unittest的所有模块来运行，也就是通过这个unittest.main()可以运行当前模块的所有的测试类和测试用例
     '''
     #执行测试用例方法二，执行指定的测试用例，将要执行的测试用例添加到测试套件里面，批量执行
     #创建一个测试套件，然后加载测试用例，然后执行
     suite = unittest.TestSuite()
     suite.addTest(TestSearch("test_search1"))
     suite.addTest(TestSearch1("test_search11"))
     unittest.TextTestRunner().run(suite)
     '''
     #执行测试用例方法三，执行指定的测试类
     #创建一个测试套件，然后加载测试类，然后批量执行测试类
     suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
     suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
     suite = unittest.TestSuite([suite1,suite2])
     unittest.TextTestRunner(verbosity=2).run(suite)