# -- coding: utf-8 --
from page import SettingPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def setting(self):
        return SettingPage(self.driver)

