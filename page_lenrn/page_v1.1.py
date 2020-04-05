# # -- coding: utf-8 --
#
# # 例子：操作个人资料页面时需要登录，此时需要先点击登录跳转到登录页面，然后才能操作个人资料页面
# # 旧写法：
# #   test脚本中setup方法需要创建个人资料页面的对象，也需要创建登录页面的对象，这是2行代码。随着页面的增多，就要创建相应页面的对象，代码行数也就增多
# #   test脚本调用2个页面对象，这是2行代码。随着调用页面对象的增多，代码行数也就增多
# # 新写法：
# #   test脚本中setup方法创建一个统一的页面入口的对象（这个统一的page入口就由本页面实现），不管有多少也页面，只有一行代码，就是创建统一page入口对象
# #   test脚本调用的对象与旧写法一致
# #   page统一入口，有多少个页面，就有多少行代码。
# # 比较：
# #   旧写法：创建页面对象和调用对象都会随着页面对象的增多而增多
# #   新写法：page统一入口的代码行数固定，只有调用页面对象时才会增加代码行数，创建页面对象只需要一行
# from page import DisplayPage
#
#
# class Page:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     # 加了这个装饰器后的作用：调用方法变成调用属性。就是调用这个方法不需要带小括号了
#     # 比较：
#     #   原来调用方式：page.display()
#     #   现在调用方式：page.display，如果加了()会提示找不到类的错误信息：TypeError: 'DisplayPage' object is not callable
#     @property
#     def display(self):
#         return DisplayPage(self.driver)
