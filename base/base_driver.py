# -- coding: utf-8 --
from appium import webdriver


def init_driver(ports='4723'):
    # server 启动参数
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    # desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['deviceName'] = '192.168.56.107:5555'

    # 设置
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'

    # 设置锁屏
    # desired_caps['appPackage'] = 'com.android.settings'
    # desired_caps['appActivity'] = '.ChooseLockPattern'

    # 文件管理器
    # desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
    # desired_caps['appActivity'] = '.activities.NavigationActivity'

    # 解决输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # toast
    desired_caps['automationName'] = 'Uiautomator2'

    # 声明我们的driver对象
    driver = webdriver.Remote('http://localhost:%s/wd/hub' % ports, desired_caps)

    # 获取当前会话中的上下文
    # NATIVE_APP：安卓原生应用
    # WEBVIEW_开头：对应网页
    print("driver.contexts：", driver.contexts)

    # 涉及到混合应用时，需要用switch_to.context()切换到对应的原生应用或者网页
    # driver.switch_to.context("")
    return driver

#
# def init_driver_ios(ports='4723'):
#     # server 启动参数
#     desired_caps = dict()
#     # 设备信息
#     desired_caps['platformName'] = 'iOS'
#     desired_caps['platformVersion'] = '12.0'
#     # desired_caps['deviceName'] = '192.168.56.101:5555'
#     desired_caps['deviceName'] = 'iPhone 8 Plus'
#
#     # 如果已经安装了app，则直接填入app的信息
#     # 如果没有安装，则填入app的路径
#     desired_caps['app'] = 'com.android.settings'
#
#     # 声明我们的driver对象
#     driver = webdriver.Remote('http://localhost:%s/wd/hub' % ports, desired_caps)
#
#     # 获取当前会话中的上下文
#     # NATIVE_APP：安卓原生应用
#     # WEBVIEW_开头：对应网页
#     print("driver.contexts：", driver.contexts)
#
#     # 涉及到混合应用时，需要用switch_to.context()切换到对应的原生应用或者网页
#     # driver.switch_to.context("")
#     return driver
