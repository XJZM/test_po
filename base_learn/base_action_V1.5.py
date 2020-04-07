# # -- coding: utf-8 --
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# class BaseAction:
#     """
#     V1.5:
#         新增swipe_screen方法，功能为根据想要寻找的文本信息，滑动屏幕，默认从下往上
#     """
#     def __init__(self, driver):
#         self.driver = driver
#
#     def swipe_screen(self, feature, want_to_find_text, direction="down_to_up"):
#         """
#         :param direction: 默认为从下到上进行滑动，其他方向：
#                     从上到下：up_to_down
#                     从左到右：left_to_right
#                     从右到左：right_to_left
#         :return:
#         """
#         # 定义一个用一个屏幕所有元素的text拼接的字符串，默认为空
#         # 定义在外层循环外，确保刚开始的值为空，当开始循环后，每一次外层循环完，都由new_elements_text提供值
#         old_elements_text = ""
#
#         # 外层循环：确保获取一个屏幕的元素后，没有发现要找的元素，能继续滑动屏幕，获取下一个屏幕的元素
#         while True:
#
#             # 定义另一个用当前屏幕所有元素的text拼接的字符串，默认为空
#             # 定义在外层循环里，确保拼接完当前屏幕所有元素的text后，下一次循环滑动后的另外一个屏幕时为空
#             # 然后重新拼接那个屏幕所有元素的text，再与old_elements_text对比
#             new_elements_text = ""
#
#             # 调用自己封装的find_elements()，寻找一组元素
#             elements = self.find_elements(feature)
#
#             # 内层循环：确保当获取到一个屏幕的元素后，对当前屏幕的所有元素逐个遍历，寻找要找的那个元素
#             for element in elements:
#                 print("当前屏幕所有元素的text的值有：", element.text)
#                 # 内层循环每循环一次，都把循环到的元素的text以+=的方式复制给new_elements_text
#                 new_elements_text += element.text
#                 if want_to_find_text == element.text:
#                     # 根据业务需求来处理找到后的元素，具体要怎么处理。目前这点暂时写为找到后点击
#                     element.click()
#                     return
#             print("当前屏幕所有元素的text拼接后的值为：", new_elements_text)
#
#             # 如果相等，说明已经滑到底了，既然已经滑到底了，就没必要继续滑了，直接退出方法
#             if old_elements_text == new_elements_text:
#                 return
#             # 如果不相等，就把当前屏幕获得的元素的text也就是new_elements_text全部复制给old_elements_text
#             else:
#                 old_elements_text = new_elements_text
#
#             # 内层循环完如果没有找到要找到元素，那么就滑动屏幕
#             swipe_time = 5000
#             screen_width = self.driver.get_window_size()["width"]
#             screen_height = self.driver.get_window_size()["height"]
#             start_x, start_y, end_x, end_y = 0, 0, 0, 0
#             if direction in ["down_to_up", "up_to_down"]:
#                 start_x = screen_width * 0.5
#                 start_y = screen_height * 0.75
#                 end_x = screen_width * 0.5
#                 end_y = screen_width * 0.25
#
#             if direction in ["left_to_right", "right_to_left"]:
#                 start_x = screen_width * 0.25
#                 start_y = screen_height * 0.5
#                 end_x = screen_width * 0.75
#                 end_y = screen_width * 0.5
#
#             # 滑动屏幕
#             if direction in ["down_to_up", "left_to_right"]:
#                 self.driver.swipe(start_x, start_y, end_x, end_y, swipe_time)
#             elif direction in ["up_to_down", "right_to_left"]:
#                 self.driver.swipe(end_x, end_y, start_x, start_y, swipe_time)
#             else:
#                 raise Exception("请输入正确的滑动方向，例如从上到下为：'up_to_down'。其他方向同理")
#
#     def find_element(self, feature, timeout=5.0, poll_frequency=1.0):
#         """
#         对于时间设置为浮点数的原因：由于find_toast方法寻找频率时间较短，并且为浮点数，为了统一，就把这个方法的时间也默认为浮点数了
#         根据特征，找元素
#         :param feature: 特征，即定位方式，例如：
#                 (By.ID, "android:id/search_src_text")
#                 或者(By.XPATH, "text,WLAN")
#         :param timeout: 超时时间
#         :param poll_frequency: 寻找频率
#         :return: 一个元素
#         """
#         by = feature[0]
#         value = feature[1]
#         try:
#             if by == By.XPATH:  # 只有以xpath进行定位时才需要进行处理
#                 value = self.__xpath_splicing(feature[1])
#             wait = WebDriverWait(self.driver, timeout, poll_frequency)
#             return wait.until(lambda driver: driver.find_element(by, value))
#         except Exception as e:
#             print("find_element()提示错误信息：", e)
#
#     def find_elements(self, feature, timeout=5.0, poll_frequency=1.0):
#         """
#         根据特征，找元素
#         :param feature: 同find_element()方法
#         :param timeout:
#         :param poll_frequency:
#         :return: 一组元素
#         """
#         by = feature[0]
#         value = feature[1]
#         try:
#             if by == By.XPATH:  # 只有以xpath进行定位时才需要进行处理
#                 value = self.__xpath_splicing(feature[1])
#             wait = WebDriverWait(self.driver, timeout, poll_frequency)
#             return wait.until(lambda driver: driver.find_elements(by, value))
#         except Exception as e:
#             print("find_elements()提示错误信息：", e)
#
#     def find_toast(self, feature):
#         """
#         对于poll_frequency频率默认为0.1秒的原因：toast持续时间短，有时候由于网络与设备配置问题的卡顿，如果设置时间过长会导致找不到
#         预期要获得的toast的文字
#         :param feature: 预期要获得的toast的文字
#         :return:
#         """
#         message_toast = "//*[contains(@text,'%s')]" % feature
#         return self.find_element(feature=(By.XPATH, message_toast), poll_frequency=0.1).text
#
#     def is_toast_exist(self, feature):
#         """
#         判断toast是否存在
#         :param feature:
#         :return:
#         """
#         try:
#             self.find_toast(feature)
#             return True
#         except Exception:
#             return False
#
#     def get_feature_key_t_or_f(self, feature, key="enabled"):
#         """
#         获取某个元素的某个key是true还是false
#         key的值要么为true，要么为false，注意是字符串，不是布尔值
#         :param feature:
#         :param key: 想要查看的那个属性的key，默认查找enabled
#         :return:
#         """
#         if self.find_element(feature).get_attribute(key) == "true":
#             return True
#         else:
#             return False
#
#     def is_feature_exist(self, feature):
#         """
#         判断某个元素是否存在
#         元素的text都有对应的值，尤其是输入框，输入什么，text的值就为什么，
#         所以结合xpath定位text，可以根据这个特点判断输入框中的值是否正常显示，重新输入另外一个值是否正常显示
#         :param feature:
#         :return:
#         """
#         try:
#             self.find_element(feature)
#             return
#         except Exception:
#             return False
#
#     def click(self, feature):
#         """
#         自定义click()方法，用自定义的find_element()调用系统的click()
#         :param feature:
#         :return:
#         """
#         self.find_element(feature).click()
#
#     def input(self, feature, content):
#         """
#         自定义输入信息方法，用自定义的find_element()的send_keys()
#         :param feature:
#         :param content:
#         :return:
#         """
#         self.find_element(feature).send_keys(content)
#
#     @staticmethod
#     def __middle_xpath_splicing(xpath):
#         """
#         拼接自定义传进来的xpath
#         :param xpath:
#         :return:
#         """
#         xpath_middle = ""
#         xpath_no_space = xpath.replace(' ', '')  # 对传进来的xpath信息进行去空格处理
#         xpath_split = xpath_no_space.split(",")  # 对去空格处理后的xpath信息以,号为分割进行切片
#         if len(xpath_split) == 3:  # 判断切片后的信息，如果数量等于3，说明是单条件xpath定位
#             if xpath_split[2] == "1":  # 进一步判断，如果切片后的最后一位是"1"，那么则是单条件精准定位
#                 xpath_middle += "@%s='%s' and " % (xpath_split[0], xpath_split[1])
#             elif xpath_split[2] == "0":  # 进一步判断，如果切片后的最后一位是"0"，那么则是单条件模糊定位
#                 xpath_middle += "contains(@%s, '%s') and " % (xpath_split[0], xpath_split[1])
#         elif len(xpath_split) == 2:  # 如果数量等于2，说明是单条件模糊定位
#             xpath_middle += "contains(@%s, '%s') and " % (xpath_split[0], xpath_split[1])
#         else:
#             raise Exception(("你传的xpath参数有误，请参考正确格式进行传入或者直接用原生xpath的格式进行传入"))
#         return xpath_middle
#
#     def __xpath_splicing(self, xpath):
#         """
#         拼接自定义传进来的xpath
#         :param xpath:
#             第一种：单条件xpath，以字符串的方式传入。例如"text,显示"或者"text,显示,1"或者"text,显示,0"
#                 其中1代表精准定位，0代表模糊定位。默认即为模糊定位，所以0也可不传
#             第二种：多条件xpath，以元组的方式传入。例如("text,显示", "text,显示,1", "text,显示,0")
#             第三种：原生xpath，例如"//*[contains(@text, '显示')]"或者"//*[@text='显示']"
#         :return:
#         """
#         xpath_start = "//*["
#         xpath_end = "]"
#         xpath_middle = ""
#         if isinstance(xpath, str):  # 判断传进来的xpath是什么类型的值，如果是str，说明是单条件xpath定位
#             if xpath.startswith("/"):  # 如果是以原生xpath的格式传进来，我不处理，我直接还给你
#                 return xpath
#             xpath_middle = self.__middle_xpath_splicing(xpath)
#         elif isinstance(xpath, tuple):  # 如果是tuple，说明是多条件xpath定位
#             for feature_for in xpath:
#                 xpath_middle += self.__middle_xpath_splicing(feature_for)  # 多条件要+=
#         xpath_middle = xpath_middle.rstrip(" and ")  # 消除最后一个and以及空格
#         xpath = xpath_start + xpath_middle + xpath_end  # 最后拼接完整的xpath信息
#         return xpath
#
#     def press_key_code(self, key_code):
#         """
#         利用automationName这个key是否在capabilities这个列表中，capabilities即为前置代码中的字典
#         判断是否使用了Uiautomator2框架，如果使用了，那么就用press_keycode(key_code)方法
#         如果没有使用，就使用keyevent(key_code)方法
#         :param key_code:
#         :return:
#         """
#         if "automationName" in self.driver.capabilities.keys():
#             self.driver.press_keycode(key_code)
#         else:
#             self.driver.keyevent(key_code)
