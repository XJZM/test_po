# # -- coding: utf-8 --
# # 如果不导入这2个模块和下边这条语句，则会报错：找不到当前模块
# import os, sys
# import threading
# from appium import webdriver
# sys.path.append(os.getcwd())
#
#
# def init_driver(ports='4723'):
#     # server 启动参数
#     desired_caps = dict()
#     # 设备信息
#     desired_caps['platformName'] = 'Android'
#     desired_caps['platformVersion'] = '5.1'
#     # desired_caps['deviceName'] = '192.168.56.101:5555'
#     desired_caps['deviceName'] = '192.168.56.107:5555'
#
#     # 设置
#     desired_caps['appPackage'] = 'com.android.settings'
#     desired_caps['appActivity'] = '.Settings'
#
#     # 设置锁屏
#     # desired_caps['appPackage'] = 'com.android.settings'
#     # desired_caps['appActivity'] = '.ChooseLockPattern'
#
#     # 文件管理器
#     # desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
#     # desired_caps['appActivity'] = '.activities.NavigationActivity'
#
#     # 解决输入中文
#     desired_caps['unicodeKeyboard'] = True
#     desired_caps['resetKeyboard'] = True
#
#     # toast
#     desired_caps['automationName'] = 'Uiautomator2'
#
#     # 声明我们的driver对象
#     driver = webdriver.Remote('http://localhost:%s/wd/hub' % ports, desired_caps)
#     return driver
#
#
# def do(i):
#     driver = init_driver(i)
#     driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
#
#
# def main():
#     """
#     利用多线程对多台设备手机进行并发
#     :return:
#     """
#     ports = ["4723", "4725"]
#     for i in ports:
#         # do为要同时运行的函数，i为do的形参
#         threading.Thread(target=do, args=(i, )).start()
#
#
# if __name__ == '__main__':
#     main()
#
#
# # 第一个终端输入命令：appium -p 4723 -bp 4724 -U 192.168.56.107:5555
# # -p：指定appium端口为4723
# # -bp：指定bootstrap端口为4724
# # -U或者--udid：指定唯一设备号
#
# # 另一个终端输入命令：appium -p 4725 -bp 4726 -U 192.168.56.108:5555
# # 以此类推
