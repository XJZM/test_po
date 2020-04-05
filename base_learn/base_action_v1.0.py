# # -- coding: utf-8 --
#
#
# # 对应page_learn/display_page_v1.5.py
# class BaseAction:
#     """
#     当把这些公共方法统一移到这个文件时，会产生一个问题，
#     那就是，我要怎么拿到driver呢？
#     答案是：利用init方法拿到driver
#     这里涉及到一个知识点：page页面继承了BaseAction类，那么page页面的init方法就不能像之前那样写了
#     有3种方式：
#         第一种：page页面不写init方法，当page页面创建一个对象时，由于继承了BaseAction，
#         它在自己的类中没有找到init方法，那么就会自动来找父类的init，这时候从test测试脚本创建的原始driver对象
#         就会直接传给BaseAction，从而让page页面能正常创建对象
#         第二种：page页面的init写上：super().__init__(driver)
#         第三种：page页面的init写上：BaseAction.__init__(self, driver)
#     """
#     def __init__(self, driver):
#         self.driver = driver
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
