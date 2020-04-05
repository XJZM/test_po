# # -- coding: utf-8 --
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# class BaseAction:
#     """
#     """
#     def __init__(self, driver):
#         self.driver = driver
#
#     def find_element(self, feature):
#         """
#         加入显示等待
#         :param feature:
#         :return:
#         """
#         by = feature[0]
#         value = feature[1]
#         return WebDriverWait(self.driver, 5, 1).until(lambda driver: driver.find_element(by, value))
#
#     def find_elements(self, feature):
#         """
#         加入定位多个元素的方法
#         :param feature:
#         :return:
#         """
#         by = feature[0]
#         value = feature[1]
#         return WebDriverWait(self.driver, 5, 1).until(lambda driver: driver.find_elements(by, value))
#
#     def click(self, feature):
#         return self.find_element(feature).click()
#
#     def input(self, feature, content):
#         return self.find_element(feature).send_keys(content)
