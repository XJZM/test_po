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
#         第四个版本：把共同点提取出来之后，发现其实和第一个版本区别还是不太大，每个方法实现的功能还是太多，
#         这个时候就可以自己定义一个find_element()，在自己定义的find_element()中返回selenium的find_element()
#         让selenium帮我们定位元素，定位好后返回给我们，我们只需要传入一个共同点就可以了
#         这时候要注意：自己定义的find_element()是直接调用的，而不是用driver去调用
#         因为自己定义的find_element()方法内部就是用driver去调用selenium的find_element()
#         :return:
#         """
#
#         # 此时要定位元素就只要调用自己封装的find_element()
#         # 然后把提取出来的某个元素的定位方式传进去，就能定位到元素了
#         # ⚠️ 注意：调用自己封装的find_element()时，这个方法已经返回了完整的元素，
#         # （方法里已经用driver去调用了selenium的find_element()），直接调用即可，不要在用driver去调用
#         self.find_element(self.display_button).click()
#
#     def click_search(self):
#         self.find_element(self.search_button).click()
#
#     def input_keyword(self, content):
#         self.find_element(self.search_edit_text).send_keys(content)
#
#     def click_back(self):
#         self.find_element(self.back_button).click()
#
#     # 把元素的定位方式传给自己定义的find_element()，然后返回selenium的find_element()
#     # 这样就相当于返回了要定位的元素
#     # 这样就不用每次都去调用selenium提供的find_element()，输入烦人的参数了
#     def find_element(self, feature):  # feature：特征
#         by = feature[0]
#         value = feature[1]
#         return self.driver.find_element(by, value)
#
