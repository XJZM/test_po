# # -- coding: utf-8 --
# from selenium.webdriver.remote import webdriver
# from selenium.webdriver.common.by import By
#
# # 提供元素定位
# # 提供元素动作
#
#
# class DisplayPage:
#     # 把元素的定位方式提取出来
#     display_button = "//*[contains(@text, '显示')]"
#     search_button = "com.android.settings:id/search"
#     search_edit_text = "android:id/search_src_text"
#     back_button = "android.widget.ImageButton"
#
#     def __init__(self, driver):
#         # 当scripts/test开头的测试脚本开始运行后，setup()方法会创建一个driver的对象
#         # 把setup()创建的这个对象传给__init__()的形参driver，并且重新赋值给self.driver
#         # 这样就能保证当运行scripts下的测试脚本和page下的测试页面的时候，用的是同一个driver对象
#         self.driver = driver
#
#     def click_display(self):
#         """
#         第二个版本：把方法中实现功能的共同点提取出来，比如定位元素的方式："//*[contains(@text, '显示')]"
#         把它定义成类变量，这样代码可阅读性提高，耦合也变弱了
#         :return:
#         """
#         self.driver.find_element_by_xpath(self.display_button).click()
#
#     def click_search(self):
#         self.driver.find_element_by_id(self.search_button)
#
#     def input_keyword(self, content):
#         self.driver.find_element_by_id("android:id/search_src_text").send_keys(content)
#
#     def click_back(self):
#         self.driver.find_element_by_class_name("android.widget.ImageButton").click()
#
