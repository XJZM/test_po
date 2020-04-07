# -- coding: utf-8 --
# 如果不导入这2个模块和下边这条语句，则会报错：找不到当前模块
import allure
import pytest
import os, sys
sys.path.append(os.getcwd())
from page import Page
from base import init_driver
from base import analyses_file_get_data


class TestSetting:
    """
    调用page提供的动作，专注以何种顺序去调用某个动作
    """
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("dict_data", analyses_file_get_data("test_input_search"))
    def test_demo(self, dict_data):
        print(dict_data)
        assert 1
