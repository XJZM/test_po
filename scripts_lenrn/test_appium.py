# # -- coding: utf-8 --
#
#
# # 如果不导入这2个模块和下边这条语句，则会报错：找不到base模块
# import os, sys, time
# sys.path.append(os.getcwd())
# from base.base_driver import init_driver
# from selenium.webdriver.support.wait import WebDriverWait
#
#
#
# class TestAppium:
#
#     def setup(self):
#         self.driver = init_driver()
#
#     def tst_base_appium_api(self):
#         # 获取包名
#         current_package = self.driver.current_package
#         print("包名为：", current_package)
#
#         # 获取启动名
#         current_activity = self.driver.current_activity
#         print("启动名为：", current_activity)
#
#         # 获取手机当前时间
#         current_time = self.driver.device_time
#         print("手机当前时间为：", current_time)
#
#         # 获取手机的像素
#         phone_size = self.driver.get_window_size()
#         print("手机的像素为", phone_size)
#
#         # 获取手机当前网络
#         # Value(Alias)       | Data | Wifi | Airplane Mode
#         # 0(None)            | 0    | 0    | 0
#         # 1(Airplane Mode)   | 0    | 0    | 1
#         # 2(Wifi only)       | 0    | 1    | 0
#         # 4(Data only)       | 1    | 0    | 0
#         # 6(All network on)  | 1    | 1    | 0
#         phone_net = self.driver.network_connection
#         print("手机的网络为：", phone_net)
#
#         # 设置手机网络
#         self.driver.set_network_connection(6)
#
#         # 获取当前屏幕内元素结构
#         cur_page_source = self.driver.page_source
#         print("屏幕内元素结构有", cur_page_source)
#         time.sleep(2)
#
#         # 脚本内启动其他app
#         # com.taptap / com.play.taptap.ui.MainAct
#         self.driver.start_activity("com.taptap", "com.play.taptap.ui.MainAct")
#
#         # 应用置于后台事件
#         self.driver.background_app(5)
#
#         # 判断app是否安装
#         print("taptap是否安装：", self.driver.is_app_installed("com.taptap"))
#
#         # 关闭当前操作的app，不会关闭驱动对象
#         self.driver.close_app()
#
#         # 操作手机通知栏，然后点击返回，返回的android keycode是4
#         self.driver.open_notifications()
#         time.sleep(2)
#         self.driver.press_keycode(4)
#
#         # 手机截图
#         time_now = time.strftime("%Y_%m_%d %H_%M_%S")
#         image_name = ('./image/%s_screen.png' % time_now)
#         self.driver.get_screenshot_as_file(os.getcwd() + os.sep + image_name)
#
#     def tst_op_file(self):
#         # 发送文件到手机
#         # Python3.x中字符都为unicode编码，而b64encode函数的参数为byte类型，需要先转码；生成的数据为byte类型，需要将byte转换回去
#         import base64
#         data = "text_123"
#         data = str(base64.b64encode(data.encode('utf-8')), 'utf-8')
#         self.driver.push_file('/sdcard/test.txt', data)
#
#         # 从手机中拉取文件
#         data = self.driver.pull_file('/sdcard/test.txt')  # 返回数据为base64编码
#         print(str(base64.b64decode(data), 'utf-8'))  # base64解码
#
#     def tst_op_apk(self):
#         # 安装APK到手机
#         apk_path = "/Users/alppe/Downloads/com.taptap_2.4.1_d.apk"
#         try:
#             self.driver.install_app(apk_path)
#         except Exception as e:
#             print(e)
#
#         time.sleep(5)
#         # 手机中移除APP
#         self.driver.remove_app("com.taptap")
#
#     def tst_element_location(self):
#         # 通过id方式定位一个元素
#         # self.driver.find_element_by_id("com.android.settings:id/title").click()
#
#         # 通过id方式定位一组元素
#         # elements_id = self.driver.find_elements_by_id("com.android.settings:id/title")
#         # print(elements_id)
#
#         # 通过class方式定位一个元素
#         # self.driver.find_element_by_class_name("android.widget.FrameLayout")
#
#         # 通过class方式定位一组元素
#         # elements_class = self.driver.find_elements_by_class_name("android.widget.FrameLayout")
#         # print(type(elements_class))
#         # elements_class[4].click()
#
#         # xpath定位
#         # 如果是用text的值进行定位，则要注意如果定位的元素是一个输入框：
#         # 还没有在输入之前该输入框的text的值为默认，例如搜索框的默认值为搜索。输入任意内容之后，text的值则会变为刚输入的值，
#         # 那么如果还用text的值进行定位，则会报错
#         # self.driver.find_element_by_xpath("//*[contains(@text, 'WLAN')]").click()
#
#         # 显示等待：在一个超时时间范围内，每隔一段时间去搜索一次元素是否存在，
#         # 如果存在返回定位对象，如果不存在直到超时时间到达，报超时异常错误
#         # 1.实例化WebDriverWait类，传入driver对象，之后driver对象被赋值给WebDriverWait的一个类变量：self._driver
#         # 2.until为WebDriverWait类的方法，until传入method方法(即匿名函数)，之后method方法会被传入self._driver
#         # 3.搜索到元素后until返回定位对象，没有搜索到函数until返回超时异常错误.
#         wait_element = WebDriverWait(self.driver, 10, 1)\
#             .until(lambda x: x.find_element_by_id("com.android.settings:id/title"))
#         wait_element.click()
#
#     def tst_op_element(self):
#         # 点击元素
#         # self.driver.find_element_by_xpath("//*[contains(@content-desc, '搜索')]").click()
#         # time.sleep(1)
#         #
#         # # 输入框输入信息，如果不能输入中文，则需要在启动参数中加入这2行：
#         # # desired_caps['unicodeKeyboard'] = True
#         # # desired_caps['resetKeyboard'] = True
#         # self.driver.find_element_by_xpath("//*[contains(@text, '搜索')]").send_keys('中国')
#         #
#         # # 清空输入框内容
#         # time.sleep(1)
#         # self.driver.find_element_by_id("android:id/search_src_text").clear()
#
#         # # 获取元素的文本内容
#         # text_value = self.driver.find_elements_by_class_name("android.widget.TextView")
#         # for i in text_value:
#         #     print(i.text)
#
#         # 获取元素的属性值
#         element = self.driver.find_element_by_xpath("//*[contains(@text, 'WLAN')]")
#         # value = 'text'返回text的属性值
#         print(element.get_attribute('text'))
#         # value = 'name'返回content-desc / text属性值
#         print(element.get_attribute('name'))
#         # value = 'className'返回class属性值，只有API = > 18才能支持
#         print(element.get_attribute('className'))
#         # value = 'resourceId' 返回 resource-id属性值，只有API = > 18才能支持
#         print(element.get_attribute('resourceId'))
#
#         # 获取元素在屏幕上的坐标
#         print(element.location)
#
#     def tst_swipe_scroll_drag(self):
#         # swipe：从一个坐标位置滑动到另一个坐标位置, 只能是两个点之间的滑动。
#         # swipe(start_x, start_y, end_x, end_y, duration=None)
#         # start_x：起点X轴坐标
#         # start_y：起点Y轴坐标
#         # end_x：  终点X轴坐标
#         # end_y,： 终点Y轴坐标
#         # duration： 滑动这个操作一共持续的时间长度，单位：ms，时间越大，滑动的惯性越小
#         # self.driver.swipe(300, 800, 300, 200, 5000)
#
#
#
#         # scroll：从一个元素滑动到另一个元素，直到页面自动停止，惯性很大，跟机子是否运行流畅有关系
#         # scroll(origin_el, destination_el)
#         # origin_el：滑动开始的元素
#         # destination_el：滑动结束的元素
#         # element_ori = self.driver.find_element_by_xpath("//*[contains(@text, '存储')]")
#         # element_dest = self.driver.find_element_by_xpath("//*[contains(@text, 'WLAN')]")
#         # self.driver.scroll(element_ori, element_dest)
#
#
#
#         # drag：从一个元素滑动到另一个元素,第二个元素替代第一个元素原本屏幕上的位置，没有惯性
#         # drag_and_drop(origin_el, destination_el)
#         # origin_el：滑动开始的元素
#         # destination_el：滑动结束的元素
#         element_ori = self.driver.find_element_by_xpath("//*[contains(@text, '存储')]")
#         element_dest = self.driver.find_element_by_xpath("//*[contains(@text, 'WLAN')]")
#         self.driver.drag_and_drop(element_ori, element_dest)
#
#     def tst_TouchAction(self):
#         from appium.webdriver.common.touch_action import TouchAction
#         element_ori = self.driver.find_element_by_xpath("//*[contains(@text, '存储')]")
#         element_dest = self.driver.find_element_by_xpath("//*[contains(@text, 'WLAN')]")
#         # TouchAction是AppiumDriver的辅助类，主要针对手势操作，比如滑动、长按、拖动等，
#         # 原理是将一系列的动作放在一个链条中发送到服务器，服务器接受到该链条后，解析各个动作，逐个执行。
#         # 注意：所有手势都要通过执行perform()函数才会运行
#
#         # 模拟手指轻敲一下屏幕操作
#         # tap(element=None, x=None, y=None)
#         # element：被定位到的元素
#         # x：相对于元素左上角的坐标，通常会使用元素的X轴坐标
#         # y：通常会使用元素的Y轴坐标
#
#         # 轻敲某个元素，相当于click()
#         # TouchAction(self.driver).tap(element_dest).perform()
#
#         # 轻敲某个坐标
#         # TouchAction(self.driver).tap(x=300, y=800).perform()
#
#         # 如果tap()方法同时传入元素和坐标，则只有元素所在的位置会被轻敲
#         # TouchAction(self.driver).tap(element_dest, x=300, y=800).perform()
#
#
#
#         # 模拟手指按下和抬起操作
#         # press(el=None, x=None, y=None)
#         # release()  # 结束动作，手指离开屏幕
#         # element：被定位到的元素
#         # x：通常会使用元素的X轴坐标
#         # y：通常会使用元素的Y轴坐标
#         # 按下某个元素不松手
#         # TouchAction(self.driver).press(element_dest).perform()
#
#         # 按下某个元素松手，相当于click()和tap()
#         # TouchAction(self.driver).press(element_dest).release().perform()
#
#         # 按下某个坐标松手
#         # TouchAction(self.driver).press(x=300, y=800).release().perform()
#
#
#
#         # 等待操作
#         # wait(ms=0)
#         # ms：暂停的毫秒数
#
#         # 按下后等待一段时间松手，模拟长按
#         # TouchAction(self.driver).press(x=300, y=800).wait(3000).release().perform()
#
#
#
#         # 模拟手指长按操作
#         # long_press(el=None, x=None, y=None, duration=1000)
#         # element：被定位到的元素
#         # x：通常会使用元素的X轴坐标
#         # y：通常会使用元素的Y轴坐标
#         # duration：持续时间，默认为1000ms
#         # TouchAction(self.driver).long_press(element_dest, duration=2000).perform()
#
#
#
#         # 模拟手机的滑动操作
#         # move_to(el=None, x=None, y=None)
#         # el: 定位的元素
#         # x: 相对于前一个元素的X轴偏移量
#         # y: 相对于前一个元素的Y轴偏移量
#
#         # 元素方式滑动，注意：移动完记得放手，也就是调用release()
#         # 可以模拟scroll()滑动，惯性很大
#         # TouchAction(self.driver).press(element_ori).move_to(element_dest).release().perform()
#
#         # 坐标方式滑动
#         # TouchAction(self.driver).press(x=90, y=280).move_to(x=180, y=0).move_to(x=180, y=180).release().perform()
