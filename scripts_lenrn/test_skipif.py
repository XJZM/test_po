# # -- coding: utf-8 --
#
# import pytest
# class TestSkipif:
#
#     """
#     跳过条件为真的测试用例
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
#     # 如果condition为真，则跳过该测试用例
#     @pytest.mark.skipif(condition=2>1,reason = "跳过该函数")
#     def test_b(self):
#         print("------->test_b")
#         assert 0