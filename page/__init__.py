# -- coding: utf-8 --
# 如果不导入这2个模块和下边这条语句，则会报错：找不到当前模块
import os, sys
sys.path.append(os.getcwd())
from .setting_page import SettingPage
from .page import Page

