# # -- coding: utf-8 --
# from selenium.webdriver.remote import webdriver
# from selenium.webdriver.common.by import By
#
# # 提供元素定位
# # 提供元素动作
#
#
# class DisplayPage:
#
#     def __init__(self, driver):
#         # 当scripts/test开头的测试脚本开始运行后，setup()方法会创建一个driver的对象
#         # 把setup()创建的这个对象传给__init__()的形参driver，并且重新赋值给self.driver
#         # 这样就能保证当运行scripts下的测试脚本和page下的测试页面的时候，用的是同一个driver对象
#         self.driver = driver
#
#     def click_display(self):
#         """
#         第一个版本：直接在click_display()方法去定位元素，并且去点击该元素，以供test脚本直接调用，
#         但是，这个方法做的事情太多了，不仅做了定位元素的操作，还做了点击操作，还要传入各种参数，
#         耦合度太强，不利于扩展和修改。每个页面有很多的点击或者输入动作，当这个功能一多，就更加难扩展和修改
#         :return:
#         """
#         self.driver.find_element_by_xpath("//*[contains(@text, '显示')]").click()
#
#     def click_search(self):
#         self.driver.find_element_by_id("com.android.settings:id/search")
#
#     def input_keyword(self, content):
#         self.driver.find_element_by_id("android:id/search_src_text").send_keys(content)
#
#     def click_back(self):
#         self.driver.find_element_by_class_name("android.widget.ImageButton").click()
#
