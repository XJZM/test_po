# -- coding: utf-8 --
from appium import webdriver


def init_driver():
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
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
