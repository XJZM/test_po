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
#         此写法的优点：
#             动态导包，动态return某个页面类，100个页面，省略100行代码
#         缺点：
#             Page类的方法必须与对应的页面类完全一致，比如一个页面类命名为SettingPage，那么在Page类中的方法命名必须为setting
#             否则本方法作废
#         :return:
#         """
#         # 第一个调用stack()这个方法的方法就是本方法page_object，调用page_object()的方法即为第二个，也就是下标为1的方法，
#         # 也就是对应的某个页面，例如setting
#         method_name = inspect.stack()[1].function
#
#         # 得到某个页面名字后，又由于刚开始的写法是return SettingPage(self.driver)，那么就把得到的setting加以处理、格式化就能
#         # 利用eval()方法去执行
#         class_name = method_name[0].upper() + method_name[1:] + "Page"
#
#         # 利用exec()方法运行一段代码，即每次要return某个类时，就先导入这个类
#         exec("from page import %s" % class_name)
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
#     def login_1(self):
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
