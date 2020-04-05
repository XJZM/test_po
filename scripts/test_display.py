# -- coding: utf-8 --
# 如果不导入这2个模块和下边这条语句，则会报错：找不到当前模块
import allure
import pytest
import os, sys
sys.path.append(os.getcwd())
from page import Page
from base import init_driver
from base import analyses_file


def analyses_file_with_key(key):
    """
    为了统一文件解析入口，所以编写了该方法
    为了以免长时间不用数据导致往后看不懂数据，所以把yaml中以列表形式编写的数据改成了以字典形式，
    但是@pytest.mark.parametrize()方法在需要输入多参数时，需要传入[(a,b),(c,d)]这样的格式，
    所以此方法的另外一个作用就是：对yaml数据文件中的字典形式的数据进行处理，
    最后返回@pytest.mark.parametrize()方法可以识别的列表形式
    :param key: 传入对应文件对应某条测试用例的key
    :return:
    """
    file_dict = analyses_file("setting_data")[key]
    file_single_list = list()
    for i in file_dict.values():
        file_single_list.append(i)
    return file_single_list


class TestDisplay:
    """
    调用page提供的动作，专注以何种顺序去调用某个动作
    """
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # def test_click_display(self):
    #     self.page.setting.click_display()
    #     assert 1

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("dict_data", analyses_file_with_key("test_input_search"))
    def test_input_search(self, dict_data):
        username = dict_data["username"]
        password = dict_data["password"]
        print(password)
        self.page.setting.click_search()
        self.page.setting.input_search(username)
        assert 1

