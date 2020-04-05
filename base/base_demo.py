# -- coding: utf-8 --
from base import analyses_file



def analyses_file_with_key(key):
    """
    第一种处理办法：
    为了统一文件解析入口，所以编写了该方法
    为了以免长时间不用数据导致往后看不懂数据，所以把yaml中以列表形式编写的数据改成了以字典形式，
    但是@pytest.mark.parametrize()方法在需要输入多参数时，需要传入[(a,b),(c,d)]这样的格式，
    所以次方法的另外一个作用就是：对yaml数据文件中的字典形式的数据进行处理，
    最后返回@pytest.mark.parametrize()方法可以识别的列表形式
    这种方式有一个比较不好的缺点：需要根据参数是单个还是多个进行变换
        单个参数：@pytest.mark.parametrize("自定义参数", analyses_file_with_key("对应字典的根key"))
        多个参数：@pytest.mark.parametrize(("自定义参数1","自定义参数2"), analyses_file_with_key("对应字典的根key"))
    :param key: 传入对应文件对应某条测试用例的key
    :return:
    """
    file_dict = analyses_file("setting_data")[key]
    file_list = list()
    for i in file_dict.values():
        file_single_list = list()
        for j in i.values():
            file_single_list.append(j)
        file_list.append(file_single_list)
    return file_list




def analyses_file_with_key(key):
    """
    # 第二种处理办法：
    这种方式与第一种相比较，可以自定义key的命名，需要用哪个值，直接key['value']就好了，
    并且可以认为加入这条数据属于哪个测试用例，方便后期调试
    参数化的写法为：
        不管是单个数据还是成对数据：
        @pytest.mark.parametrize("自定义参数", analyses_file_with_key("对应字典的根key"))
    :param key: 传入对应文件对应某条测试用例的key
    :return:
    """
    file_dict = analyses_file("setting_data")[key]
    file_single_list = list()
    for i in file_dict.values():
        file_single_list.append(i)
    print(file_single_list)
    return file_single_list


if __name__ == '__main__':
    analyses_file_with_key("test_input_search")
