# # -- coding: utf-8 --
# import inspect
#
#
# class Page:
#     """
#     优化原因：由于page页面统一入口的特性，按照普通的方法，每增加一个页面，就要导入一次那个页面的类，当有100个页面的时候，
#             就要导入100此页面，光导入的语句就要100条
#     新思路：那么是谁要调用page里的方法呢？就是test中每个单独的测试脚本，那么就可以利用stack()获取调用的文件名，然后进行拼接
#             最后通过eval()和exec()两个方法实现动态获取
#     """
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def page_object(self):
#         """
#         解决当页面命名为demo_demo_demo_page这种多级名字时导致此方法不能正常运行的问题
#         :return:
#         """
#         # 第一个调用stack()这个方法的方法就是本方法page_object，调用page_object()的方法即为第二个，也就是下标为1的方法，
#         # 也就是对应的某个页面，例如setting
#         method_name = inspect.stack()[1].function
#         print("method_name", method_name)
#
#         # 把找到的method_name用下划线进行分割，获得一个列表
#         method_name_list = method_name.split("_")
#         class_name = ""
#
#         # 遍历这个列表，处理每一个demo的首字母（假设文件名为demo_demo_demo_page.py），然后进行拼接
#         for method_name in method_name_list:
#             class_name += method_name[0].upper() + method_name[1:]
#
#         # 最后与字符串Page拼接完整的页面类名
#         class_name += "Page"
#
#         # 利用exec()方法运行导入语句，即每次要return某个类时，就先导入这个类
#         exec("from page import %s" % class_name)
#
#         # 利用eval()方法去执行
#         return eval("%s(self.driver)" % class_name)
#
#     @property
#     def setting(self):
#         return self.page_object()
#
#     # 以后不管有多少个页面，都直接返回page_object()
#     def login(self):
#         return self.page_object()
#
#     def login_demo_demo(self):
#         return self.page_object()
#
#     def login_2(self):
#         return self.page_object()
#
#     def login_3(self):
#         return self.page_object()
#
#
#
