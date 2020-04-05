# # -- coding: utf-8 --
#
#
# import pytest
#
#
# class TestSingleParametrize:
#     """
#     函数数据参数化：方便测试函数对测试数据的获取
#     单个参数：
#     """
#     def setup_class(self):
#         print("------->setup_single_class")
#
#     def teardown_class(self):
#         print("------->teardown_single_class")
#
#     @pytest.mark.parametrize("a", [3, 6])  # a参数被赋予两个值，函数会运行两遍
#     def test_a(self, a):  # 参数必须和parametrize里面的参数一致
#         print("test data:a=%d" % a)
#         assert a % 3 == 0
#
#
# class TestDoubleParametrize:
#     """
#     多个参数：
#     """
#
#     def setup_class(self):
#         print("------->setup_double_class")
#
#     def teardown_class(self):
#         print("------->teardown_double_class")
#
#     @pytest.mark.parametrize("a, b", [(1, 2), (0, 3)])  # 参数a,b均被赋予两个值，函数会运行两遍
#     def test_a(self, a, b):  # 参数必须和parametrize里面的参数一致
#         print("test data:a=%d,b=%d" % (a, b))
#         assert a + b == 3
#
#
#
#
#
# def return_test_data():
#     return [(1, 2), (0, 3)]
#
#
# class TestReturnParametrize:
#     """
#     # 函数返回值类型示例
#     """
#     def setup_class(self):
#         print("------->setup_return_class")
#
#     def teardown_class(self):
#         print("------->teardown_return_class")
#
#     @pytest.mark.parametrize("a,b", return_test_data())  # 使用函数返回值的形式传入参数值
#     def test_a(self, a, b):
#         print("test data:a=%d,b=%d" % (a, b))
#         assert a + b == 3
