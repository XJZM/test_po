# # -- coding: utf-8 --
#
# import pytest
#
#
# class TestABC:
#     """
#     预期失败：condition条件为True时
#     预期成功：condition条件为False时
#     当用例a失败的时候，如果用例b和用例c都是依赖于第一个用例的结果，那可以直接跳过用例b和c的测试，直接给他标记失败xfail
#     用到的场景，登录是第一个用例，登录之后的操作b是第二个用例，登录之后操作c是第三个用例，很明显三个用例都会用到登录操作。
#     如果登录都失败了，那后面2个用例就没测试的必要了，直接跳过，并且标记为失败用例，这样可以节省用例时间。
#     """
#
#     def setup_class(self):
#         print("------->setup_class")
#
#     def teardown_class(self):
#         print("------->teardown_class")
#
#     # 预期失败，实际成功：XPassed，测试报告显示为：红色
#     # 该场景即为有bug
#     @pytest.mark.xfail(2 > 1, reason="标注为预期失败")
#     def test_fail_pass(self):
#         print("------->预期失败，实际成功")
#         assert 1
#
#     # 预期失败，实际失败：XFailed，测试报告显示为：橙色
#     # 即虽然实际失败了，但是原因不是因为有bug，而是由于比如：前置条件没有成功导致的失败、功能暂时还没有实现等等
#     # 使用场景：b用例的运行需要a用例成功的运行，但是a用例失败了，那b用例自然也会失败。那么如果a用例已经失败了，就没有必要再去运行b用例了
#     # 所以在b用例上根据a用例是否运行成作为条件标记预期失败，在测试报告体现为XFailed
#     @pytest.mark.xfail(2 > 1, reason="标注为预期失败")
#     def test_fail_fail(self):
#         print("------->预期失败，实际失败")
#         assert 0
#
#     # 预期成功，实际成功：Passed，测试报告显示为：绿色
#     # 使用场景：
#     @pytest.mark.xfail(1 > 2, reason="标注为预期成功")
#     def test_pass_pass(self):
#         print("------->预期成功，实际成功")
#         assert 1
#
#     # 预期成功，实际失败：Failed，测试报告显示为：红色
#     # 该场景即为有bug
#     @pytest.mark.xfail(1 > 2, reason="标注为预期成功")
#     def test_pass_fail(self):
#         print("------->预期成功，实际失败")
#         assert 0
