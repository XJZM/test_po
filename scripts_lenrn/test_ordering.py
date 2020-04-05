# # -- coding: utf-8 --
#
# import pytest
#
#
# class TestDefault:
#     """
#     默认情况下，pytest默认按照从上到下执行
#     """
#     def setup_class(self):
#         print("------->setup_default_class")
#
#     def teardown_class(self):
#         print("------->teardown_default_class")
#
#     # 该测试用例第一个执行
#     def test_default_a(self):
#         print("------->test_default_a")
#         assert 1
#
#     # 该测试用例第二个执行
#     def test_default_b(self):
#         print("------->test_default_b")
#         assert 0
#
#
# class TestOrdering:
#     """
#     通过第三方插件包改变运行顺序
#     """
#     def setup_class(self):
#         print("------->setup_ordering_class")
#
#     def teardown_class(self):
#         print("------->teardown_ordering_class")
#
#     # 333：该测试用例第三个被执行
#     @pytest.mark.run(order=2)
#     def test_ordering_a(self):
#         print("------->test_ordering_a")
#         assert 1
#
#     # 222：该测试用例第二个被执行
#     @pytest.mark.run(order=1)
#     def test_ordering_b(self):
#         print("------->test_ordering_b")
#         assert 0
#
#     # 111：该测试用例第一个被执行
#     @pytest.mark.run(order=0)
#     def test_ordering_c(self):
#         print("------->test_ordering_c")
#         assert 1
#
#     # 555：该测试用例第五个被执行
#     @pytest.mark.run(order=-1)
#     def test_ordering_d(self):
#         print("------->test_ordering_d")
#         assert 0
#
#     # 444：该测试用例第四个被执行
#     @pytest.mark.run(order=-2)
#     def test_ordering_e(self):
#         print("------->test_ordering_e")
#         assert 0
