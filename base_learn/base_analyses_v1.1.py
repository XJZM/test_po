# -- coding: utf-8 --
import yaml


def analyses_file(file_name, key):
    """
    把test脚本中的analyses_file_with_key()方法的功能合并到解析yaml文件的方法中
    这样，用文件名把yaml文件解析成字典格式，用key拿到某个脚本需要的值
    :param file_name: data目录下yaml文件的文件名
    :param key: 字典的key，具体查阅对应yaml文件的结构，确定要哪个key的值
    :return:
    """
    try:
        file_path = "./data/" + file_name + ".yml"  # 外部调用的路径为：./data；内部：../data
        with open(file_path, "r") as f:
            # yaml 5.1版本后弃用了yaml.load(file)这个用法，因为觉得很不安全，5.1版本之后就修改了需要指定Loader，
            # 通过默认加载​​器（FullLoader）禁止执行任意函数
            data = yaml.load(f, Loader=yaml.FullLoader)
            file_dict = data[key]
            file_single_list = list()
            for i in file_dict.values():
                file_single_list.append(i)
            return file_single_list

    except Exception as e:
        print(e)


if __name__ == '__main__':
    print(analyses_file("setting_data", "test_input_search"))
