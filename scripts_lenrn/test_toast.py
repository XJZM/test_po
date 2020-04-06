# # -- coding: utf-8 --
# import time
# import os, sys
#
# from selenium.webdriver.common.by import By
#
# sys.path.append(os.getcwd())
#
# from base import init_driver
# from page import Page
#
#
# class TestFileManager:
#     """
#     调用page提供的动作，专注以何种顺序去调用某个动作
#     """
#     def setup(self):
#         self.driver = init_driver()
#         self.page = Page(self.driver)
#
#     def test_return_desktop(self):
#         # print(self.driver == self.page.driver)
#         toast_text = "退出"
#         time.sleep(1)
#         self.driver.press_keycode(4)
#         time.sleep(1)
#         self.driver.press_keycode(4)
#         time.sleep(1)
#         self.driver.press_keycode(4)
#         # demo = self.driver.find_toast(toast_text)
#         demo = self.page.setting.find_toast(toast_text)
#         # demo = self.driver.find_element_by_xpath("//*[contains(@text, '退出')]")
#         print(demo)
#
