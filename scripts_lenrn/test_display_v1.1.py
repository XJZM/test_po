# # -- coding: utf-8 --
#
# # 如果不导入这2个模块和下边这条语句，则会报错：找不到base模块
# import os, sys, time
#
# from page.page import Page
#
# sys.path.append(os.getcwd())
# from base import init_driver
# from page.display_page import DisplayPage
#
#
# class TestDisplay:
#     """
#     调用page提供的动作，注重以何种顺序去调用某个动作
#     """
#     def setup(self):
#         self.driver = init_driver()
#         # 当创建来page统一入口后，则不需要创建每个页面的对象来
#         # 然后把driver对象传给统一入口Page，Page类在把driver传给每个页面对象
#         self.page = Page(self.driver)
#
#     def test_click_display(self):
#         self.page.display().click_display()
