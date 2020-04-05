# # -- coding: utf-8 --
# from selenium.webdriver.remote import webdriver
# from selenium.webdriver.common.by import By
# from base import BaseAction
# # 提供元素定位
# # 提供元素动作
#
#
# class DisplayPage(BaseAction):
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
#         # ⚠️ 这里会遇到两个问题：
#         # ⚠️ 第一个：当把这些方法移到base_action.py文件后，我们应该要怎么调用这些公共方法呢？
#         # ⚠️ 答案是page页面继承BaseAction类！
#         # ⚠️ 第二个：注释在base_action.py中
#         # 第一种是不写init
#         # 第二种：
#         # super().__init__(driver)
#         # 第三种
#         # 三种写法效果相同，所以可以不写这个init
#         BaseAction.__init__(self, driver)
#
#     def click_display(self):
#         """
#         第六个版本：再仔细分析，发现自己封装的click()/input()/find_element()这些方法用的很多
#         一旦页面多了，每个页面都有这些方法，就会造成代码冗余。
#         这个时候就应该把这些公用的方法统一提取到基类中，哪个页面的元素的要用，它去调用就好了
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
#
#
#
#
