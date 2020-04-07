# -- coding: utf-8 --
import inspect

import yaml


def analyses_file(key):
    """
    v1.3: 解决当测试脚本为test_demo_demo_demo.py时，对于测试数据名为demo_demo_demo_data.yml时，此方法无法正常处理的问题
    :param key: 字典的key，具体查阅对应yaml文件的结构，确定要哪个key的值
    :return:
    """
    try:
        file_name = ""
        previous_method_path = inspect.stack()[1].filename
        print("previous_method_path：", previous_method_path)
        # 输出：/learn/learn_pytest_po/scripts/test_setting.py
        # 多层级命名：/learn/learn_pytest_po/scripts/test_setting_demo_demo.py'

        # 根据得到的路径，从右开始寻找第一个斜杆，斜杆右边一个就是调用文件名的起始下标
        test_scripts_name_start_index = previous_method_path.rfind('/') + 1

        # 根据得到的路径，从右开始寻找第一个点，就是调用文件名的最终下标
        test_scripts_name_end_index = previous_method_path.rfind('.')

        # 利用起始和最终下标截取previous_method_path，获得调用文件名的名字
        test_scripts_name = previous_method_path[test_scripts_name_start_index:test_scripts_name_end_index]

        # 以下划线作为分隔符对test_scripts_name进行切片，获得一个列表
        test_scripts_name_list = test_scripts_name.split("_")

        # 遍历整个列表，去除test，拼接剩余部分
        for file_name_for in test_scripts_name_list:
            # 判断：如果为test就直接跳过
            if "test" == file_name_for:
                continue

            # 然后拼接_data前面的部分
            file_name += "_" + file_name_for

        # 最后与_data拼接成第二个调用该方法的测试用例对应的页面的对应yml文件名
        # file_name的输出为：_setting_demo_demo，所以要从第1个下标开始取值
        file_name_last = file_name[1:] + "_data"
        print("file_name_last：", file_name_last)

        file_path = "./data/" + file_name_last + ".yml"  # 外部调用的路径为：./data；内部：../data
        with open(file_path, "r") as f:
            # yaml 5.1版本后弃用了yaml.load(file)这个用法，因为觉得很不安全，5.1版本之后就修改了需要指定Loader，
            # 通过默认加载​​器（FullLoader）禁止执行任意函数
            print("上一个调用我的人是：", inspect.stack()[1].filename)
            data = yaml.load(f, Loader=yaml.FullLoader)
            file_dict = data[key]
            file_single_list = list()
            for i in file_dict.values():
                file_single_list.append(i)
            return file_single_list
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 如果在当前文件调用的话，因为上个人调用，其实就是自己调用自己，所以输出的值是：analyses_data，但是并没有这个名字的文件
    print(analyses_file("test_input_search"))
