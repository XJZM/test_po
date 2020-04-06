# # -- coding: utf-8 --
# # 如果不导入这2个模块和下边这条语句，则会报错：找不到当前模块
# import allure
# import pytest
# import os, sys
#
#
# sys.path.append(os.getcwd())
# from page import Page
# from base import init_driver
# from base import analyses_file
#
#
# def analyses_file_with_key(key):
#     """
#     为了统一文件解析入口，所以编写了该方法
#     为了以免长时间不用数据导致往后看不懂数据，所以把yaml中以列表形式编写的数据改成了以字典形式，
#     但是@pytest.mark.parametrize()方法在需要输入多参数时，需要传入[(a,b),(c,d)]这样的格式，
#     所以此方法的另外一个作用就是：对yaml数据文件中的字典形式的数据进行处理，
#     最后返回@pytest.mark.parametrize()方法可以识别的列表形式
#     :param key: 传入对应文件对应某条测试用例的key
#     :return:
#     """
#     file_dict = analyses_file("setting_data")[key]
#     file_single_list = list()
#     for i in file_dict.values():
#         file_single_list.append(i)
#     return file_single_list
#
#
# class TestDisplay:
#     """
#     调用page提供的动作，专注以何种顺序去调用某个动作
#     注意：测试步骤不应该写在测试脚本里，而应该写在对应的page页面的独立的动作上，这里只为了学习
#     """
#     def setup(self):
#         self.driver = init_driver()
#         self.page = Page(self.driver)
#
#     @allure.severity(allure.severity_level.BLOCKER)
#     # @nose.allure.severity(nose.allure.severity_level.BLOCKER)
#     # @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
#     @allure.step('我是一个测试步骤')
#     def test_click_display(self):
#         self.page.setting.click_display()
#
#     @allure.severity(allure.severity_level.CRITICAL)
#     # @nose.allure.severity(nose.allure.severity_level.CRITICAL)
#     # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
#     @allure.step('我是一个测试步骤')
#     @pytest.mark.parametrize("dict_data", analyses_file_with_key("test_input_search"))
#     def test_input_search(self, dict_data):
#         username = dict_data["username"]
#         password = dict_data["password"]
#         print(password)
#         self.page.setting.click_search()
#         self.page.setting.input_search(username)
#
#     @allure.severity(allure.severity_level.NORMAL)
#     # @nose.allure.severity(nose.allure.severity_level.NORMAL)
#     # @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
#     @allure.step('我是一个测试步骤')
#     def test_click_wlan(self):
#         self.page.setting.click_wlan()
#         # 这个描述也应该写在page页面单独的动作之上
#         # 可配合参数化对单独的步骤进行描述，例如登录
#         allure.attach('描述', '我是测试步骤001的描述～～～')
#
#     @allure.severity(allure.severity_level.MINOR)
#     # @nose.allure.severity(nose.allure.severity_level.MINOR)
#     # @pytest.allure.severity(pytest.allure.severity_level.MINOR)
#     def test_click_more(self):
#         self.page.setting.click_more()
#
#     @allure.severity(allure.severity_level.TRIVIAL)
#     # @allure.severity('critical')
#     # @nose.allure.severity(nose.allure.severity_level.TRIVIAL)
#     # @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
#     def test_click_memory(self):
#         self.page.setting.click_memory()
