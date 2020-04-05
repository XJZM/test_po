# -- coding: utf-8 --
import yaml


def analyses_file(file_name):
    try:
        file_path = "./data/" + file_name + ".yml"  # 外部调用的路径为：./data；内部：../data
        with open(file_path, "r") as f:
            # yaml 5.1版本后弃用了yaml.load(file)这个用法，因为觉得很不安全，5.1版本之后就修改了需要指定Loader，
            # 通过默认加载​​器（FullLoader）禁止执行任意函数
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data
    except Exception as e:
        print(e)


if __name__ == '__main__':
    pass
