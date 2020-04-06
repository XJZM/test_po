# -- coding: utf-8 --
import inspect

import yaml


def analyses_file_get_data(key):
    """
    把test脚本中的analyses_file_with_key()方法的功能合并该文件中，并且动态获取上一个调用我的方法，也就是测试脚本本身。
    然后通过处理动态获得对应测试脚本的yaml文件名，这样就不用每次都去传了
    :param key: 字典的key，具体查阅对应yaml文件的结构，确定要哪个key的值
    :return:
    """
    try:
        previous_method_path = inspect.stack()[1].filename
        # 输出：/learn/learn_pytest_po/scripts/test_setting.py

        # 利用rfind()方法从又往左找，先找到靠近右边的第一个下划线，获得的就是这个下划线的下标
        # 但是开始的下标应该是这个下划线的后面一个下标，所以要+1
        start_index = int(previous_method_path.rfind('_')) + 1

        # 利用rfind()方法从又往左找，再找到靠近右边的第一个点，获得的就是这个点的下标
        end_index = int(previous_method_path.rfind('.'))

        # 那么这2个下标之间的字符串就是调用analyses_file()方法的那个测试脚本！
        # 最后利用切片和字符串拼接就可以获得完整的以"页面_data"命名的yaml文件名！
        file_name = previous_method_path[start_index:end_index] + "_data"

        file_path = "./data/" + file_name + ".yml"  # 外部调用的路径为：./data；内部：../data
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
    print(analyses_file_get_data("test_input_search"))
