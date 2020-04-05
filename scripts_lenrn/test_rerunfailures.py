# # -- coding: utf-8 --
# import pytest
#
#
# class Test_Rerunfailures:
#     """
#     失败重跑
#     """
#     def setup_class(self):
#         print("------->setup_class")
#
#     def teardown_class(self):
#         print("------->teardown_class")
#
#     def test_a(self):
#         print("------->test_a")
#         assert 1
#
#     # 断言失败的测试用例会失败重复n次，n为命令行指定的失败重跑次数或者pytest.ini配置文件配置的次数
#     def test_b(self):
#         print("------->test_b")
#         assert 0  # 断言失败