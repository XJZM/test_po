# # -- coding: utf-8 --
#
#
# # display_button = "//*[contains(@text, '显示')]"
# # display_button_1 = "//*[@text='显示']"
# # display_button_1 = "//*[@text='显示' and contains(@text, '显示') and contains(@text, '显示')]"
#
#
# def xpath_splicing(xpath):
#     """
#     拼接自定义传进来的xpath
#     :param xpath:
#     :return:
#     """
#     xpath_middle = ""
#     xpath_no_space = xpath.replace(' ', '')  # 对传进来的xpath信息进行去空格处理
#     xpath_split = xpath_no_space.split(",")  # 对去空格处理后的xpath信息以,号为分割进行切片
#     if len(xpath_split) == 3:  # 判断切片后的信息，如果数量等于3，说明是单条件xpath定位
#         if xpath_split[2] == "1":  # 进一步判断，如果切片后的最后一位是"1"，那么则是单条件精准定位
#             xpath_middle += "@%s='%s' and " % (xpath_split[0], xpath_split[1])
#         elif xpath_split[2] == "0":  # 进一步判断，如果切片后的最后一位是"0"，那么则是单条件模糊定位
#             xpath_middle += "contains(@%s, '%s') and " % (xpath_split[0], xpath_split[1])
#     elif len(xpath_split) == 2:  # 如果数量等于2，说明是单条件模糊定位
#         xpath_middle += "contains(@%s, '%s') and " % (xpath_split[0], xpath_split[1])
#     else:
#         raise Exception(("你传的xpath参数有误，请参考正确格式进行传入或者直接用原生xpath的格式进行传入"))
#     return xpath_middle
#
#
# def make_xpath(xpath):
#     """
#     :param xpath:
#         第一种：单条件xpath，以字符串的方式传入。例如"text,显示"或者"text,显示,1"或者"text,显示,0"
#             其中1代表精准定位，0代表模糊定位。默认即为模糊定位，所以0也可不传
#         第二种：多条件xpath，以元组的方式传入。例如("text,显示", "text,显示,1", "text,显示,0")
#         第三种：原生xpath，例如"//*[contains(@text, '显示')]"或者"//*[@text='显示']"
#     :return:
#     """
#     xpath_start = "//*["
#     xpath_end = "]"
#     xpath_middle = ""
#     if isinstance(xpath, str):  # 判断传进来的feature是什么类型的值，如果是str，说明是单条件xpath定位
#         if xpath.startswith("/"):  # 如果是以原生xpath的格式传进来，我不处理，我直接还给你
#             return xpath
#         xpath_middle = xpath_splicing(xpath)
#     elif isinstance(xpath, tuple):  # 如果是tuple，说明是多条件xpath定位
#         for feature_for in xpath:
#             xpath_middle += xpath_splicing(feature_for)  # 多条件要+=
#     xpath_middle = xpath_middle.rstrip(" and ")  # 消除最后一个and以及空格
#     xpath = xpath_start + xpath_middle + xpath_end
#     print(xpath)
#
#
# if __name__ == '__main__':
#     # value = "text, 显示", "text, 显示,1", "text, 显示,0",
#     value = "text"
#     make_xpath(value)
