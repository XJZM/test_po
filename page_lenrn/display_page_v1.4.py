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
#         第五个版本：认真分析发现，每个动作还是有一些重复率高的功能，比如click()，send_keys()等
#         这时候我们可以像封装自己的find_element()一样去封装它们，然后直接返回定位元素操作元素一系列操作。
#         而我们定义的操作元素的方法的功能就很清晰了，要么点击，要么输入文字，至于是怎么实现的，交给统一的方法。如下：
#         :return:
#         """
#         self.click(self.display_button)
#
#     def click_search(self):
#         # 自己定义的动作就很清晰，只需要关注是点击还是输入文字，或者别的动作
#         self.click(self.search_button)
#
#     def input_keyword(self, content):
#         self.input(self.search_edit_text, content)
#
#     def click_back(self):
#         self.click(self.back_button)
#
#     def find_element(self, feature):  # feature：特征
#         by = feature[0]
#         value = feature[1]
#         return self.driver.find_element(by, value)
#
#     def click(self, feature):
#         # 进一步封装自己的click()，在这里边实现定位元素点击元素
#         return self.find_element(feature).click()
#
#     def input(self, feature, content):
#         # 进一步封装自己的input()，在这里边实现定位元素然后输入信息
#         return self.find_element(feature).send_keys(content)
#
#
#
