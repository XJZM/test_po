# # -- coding: utf-8 --
# from selenium.webdriver.remote import webdriver
# from selenium.webdriver.common.by import By
#
# # 提供元素定位
# # 提供元素动作
#
#
# class DisplayPage:
#     # 进一步把元素的定位方式以元组的方式提取出来
#     # a = 1, 2相当于a = (1, 2)，如下例子：
#     display_button = By.XPATH, "//*[contains(@text, '显示')]"
#     search_button = By.ID, "com.android.settings:id/search"
#     search_edit_text = By.ID, "android:id/search_src_text"
#     back_button = By.CLASS_NAME, "android.widget.ImageButton"
#
#     def __init__(self, driver):
#         # 当scripts/test开头的测试脚本开始运行后，setup()方法会创建一个driver的对象
#         # 把setup()创建的这个对象传给__init__()的形参driver，并且重新赋值给self.driver
#         # 这样就能保证当运行scripts下的测试脚本和page下的测试页面的时候，用的是同一个driver对象
#         self.driver = driver
#
#     def click_display(self):
#         """
#         第三个版本：虽然把共同点提取出来了，但是和第一个版本的区别并不大。这时候可以利用selenium自带的find_element()方法
#         做进一步的提取。这样共同点就可以把定位元素需要的2个参数都提取出来了
#         :return:
#         """
#         self.driver.find_element(self.display_button).click()
#
#     def click_search(self):
#         self.driver.find_element(self.search_button).click()
#
#     def input_keyword(self, content):
#         self.driver.find_element(self.search_edit_text).send_keys(content)
#
#     def click_back(self):
#         self.driver.find_element(self.back_button).click()
#
