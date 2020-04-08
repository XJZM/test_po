# # -- coding: utf-8 --
#
# import pytest
#
#
# class TestFixture:
#     """
#     fixture修饰器来标记固定的工厂函数，在其他函数，模块，类或整个工程调用它时会被激活并优先执行,
#     通常会被用于完成预置处理和重复操作。
#     方法：fixture(scope="function", params=None, autouse=False, ids=None, name=None)常用参数:
#         scope：被标记方法的作用域
#             function" (default)：作用于每个测试方法，每个test都运行一次
#             "class"：作用于整个类，每个class的所有test只运行一次
#             "module"：作用于整个模块，每个module的所有test只运行一次
#             "session：作用于整个session(慎用)，每个session只运行一次
#         params：(list类型)提供参数数据，供调用标记方法的函数使用
#         autouse：是否自动运行,默认为False不运行，设置为True自动运行
#
#     """
#     pass
#
#
# # class TestFixtureOne:
# #     """
# #     第一种：通过参数引用
# #     """
# #     @pytest.fixture()
# #     def before(self):
# #         print("------->before_One")
# #
# #     # ⚠️ test_a方法传入了被fixture修饰的函数，以变量的形式
# #     # ⚠️ 结果为：每次运行test开头的测试用例都会先运行被fixture修饰的方法
# #     def test_a(self, before):
# #         print("------->test_One_a")
# #         assert 1
# #
# #     # ⚠️ 没有传入被fixture修饰的函数
# #     # ⚠️ 结果为：每次运行test开头的测试用例都不会先运行被fixture修饰的方法
# #     def test_b(self):
# #         print("------->test_One_b")
# #         assert 1
# #
# #
# # # ⚠️ 被fixture修饰的方法在类外面
# # # ⚠️ 默认域为function，使用方式设置为手动使用，即修饰要使用的测试类
# # # ⚠️ 结果：每次运行test开头的测试用例都会先运行被fixture修饰的方法，与第三种和第四种一样
# # @pytest.fixture()
# # def before():
# #     print("------->before_Two")
# #
# # 使用装饰器@pytest.mark.usefixtures()修饰需要运行的用例
# # @pytest.mark.usefixtures("before")
# # class TestFixtureTwo:
# #     """
# #     第二种：通过函数引用
# #     """
# #     def setup(self):
# #         print("------->setup_Two")
# #
# #     def test_a(self):
# #         print("------->test_Two_a")
# #         assert 1
# #
# #     def test_b(self):
# #         print("------->test_Two_b")
# #         assert 1
# #
# #
# # # ⚠️ 被fixture修饰的方法在类外面
# # # ⚠️ 默认域为function，使用方式设置为自动使用
# # # ⚠️ 结果：每次运行test开头的测试用例都会先运行被fixture修饰的方法，与第四种一样
# # @pytest.fixture(autouse=True)
# # def before():
# #     print("------->before_Three")
# #
# #
# # class TestFixtureThree:
# #     """
# #     第三种：设置为默认运行
# #     """
# #     def setup(self):
# #         print("------->setup_Three")
# #
# #     def test_a(self):
# #         print("------->test_Three_a")
# #         assert 1
# #
# #     def test_b(self):
# #         print("------->test_Three_b")
# #         assert 1
# #
# #
# # class TestFixtureFour:
# #     """
# #     第四种：作用域为function
# #     """
# #     # ⚠️ 被fixture修饰的方法在类里面
# #     # ⚠️ 作用域设置为function，使用方式设置为自动使用
# #     # ⚠️ 结果：每次运行test开头的测试用例都会先运行被fixture修饰的方法，与第三种一样
# #     @pytest.fixture(scope='function', autouse=True)
# #     def before(self):
# #         print("------->before_Four")
# #
# #     def setup(self):
# #         print("------->setup_Four")
# #
# #     def test_a(self):
# #         print("------->test_Four_a")
# #         assert 1
# #
# #     def test_b(self):
# #         print("------->test_Four_b")
# #         assert 1
# #
# #
# # # ⚠️ 作用域设置为class，使用方式设置为自动使用
# # # ⚠️ 作用域设置为function，使用方式设置为自动使用
# # # ⚠️ 结果：每次运行test开头的测试类都会先运行被fixture修饰的方法，不管类中有多少测试用例，只运行一次
# # @pytest.fixture(scope='class', autouse=True)
# # def before():
# #     print("------->before_Five")
# #
# #
# # class TestFixtureFive:
# #     """
# #     第五种：作用域为class
# #     """
# #     def setup(self):
# #         print("------->setup_Five")
# #
# #     def test_a(self):
# #         print("------->test_Five_a")
# #         assert 1
# #
# #     def test_b(self):
# #         print("------->test_Five_b")
# #         assert 1
# #
# #
# # class TestFixtureSix:
# #     """
# #     第五种：作用域为module，在当前.py脚本里面所有用例开始前只执行一次
# #     """
# #     pass
# #
# #
# # class TestFixtureSeven:
# #     """
# #     第六种：作用域为session
# #     fixture为session级别是可以跨.py模块调用的，也就是当我们有多个.py文件的用例的时候，如果多个用例只需调用一次fixture，
# #     那就可以设置为scope="session"，并且写到conftest.py文件里。
# #     conftest.py文件名称是固定的，pytest会自动识别该文件。
# #     放到项目的根目录下就可以全局调用了，如果放到某个package下，那就在该package内有效
# #
# #     """
# #     pass
# #
#
#
