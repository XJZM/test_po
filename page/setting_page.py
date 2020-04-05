# -- coding: utf-8 --
import allure
from selenium.webdriver.common.by import By
from base import BaseAction


# 提供元素动作


class SettingPage(BaseAction):
    # display_button = By.XPATH, "//*[contains(@text, '显示')]"
    display_button = By.XPATH, "text,显示"  # 正确写法
    search_button = By.XPATH, "content-desc,搜索"
    input_box = By.ID, "android:id/search_src_text"
    wlan_button = By.XPATH, "text,WLAN"
    more_button = By.XPATH, "text,更多"
    memory_button = By.XPATH, "text,存储"
    # init方法可以省略不写，因为父类已经有init方法类
    # def __init__(self, driver):
    #     super().__init__(driver)

    @allure.step('点击显示按钮')
    def click_display(self):
        allure.attach('点击显示按钮', '我是点击显示按钮的描述～～～')
        self.click(self.display_button)

    @allure.step('点击搜索按钮')
    def click_search(self):
        allure.attach('点击Wi-点击搜索按钮', '我是点击搜索按钮的描述～～～')
        self.click(self.search_button)

    @allure.step('点击Wi-Fi按钮')
    def click_wlan(self):
        allure.attach('点击Wi-Fi按钮', '我是点击Wi-Fi按钮的描述～～～')
        self.click(self.wlan_button)

    @allure.step('点击更多按钮')
    def click_more(self):
        allure.attach('点击更多按钮', '我是点击更多按钮的描述～～～')
        self.click(self.more_button)

    @allure.step('点击存储按钮')
    def click_memory(self):
        allure.attach('点击存储按钮', '我是点击存储按钮的描述～～～')
        self.click(self.memory_button)

    @allure.step('搜索输入框输入信息')
    def input_search(self, content):
        try:
            allure.attach(content, '搜索输入框输入信息')
            self.input(self.input_box, content)
        except Exception as e:
            print("报错：", e)
