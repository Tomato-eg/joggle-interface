import os


class PathUtils:
    def get_project_path(self):
        """ 获取项目根路径 """
        """
            1、split()函数
            语法：str.split(str="",num=string.count(str))[n]

            参数说明：
            str:表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
            num:表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量
            [n]:表示选取第n个分片
            
            注意：当使用空格作为分隔符时，对于中间为空的项会自动忽略
            
            2、os.path.split()函数
            语法：os.path.split('PATH')
            
            参数说明：
            
            1.PATH指一个文件的全路径作为参数：
            
            2.如果给出的是一个目录和文件名，则输出路径和文件名
            
            3.如果给出的是一个目录名，则输出路径和为空文件名
        """
        # __file__ 获取当前执行脚本的绝对路径
        # \\ -> \
        """
            os.path.split() -> 返回 ('文件路径', '文件名')
            获取当前绝对路径作为参数 __file__
            路径分割 os.path.split(__file__)[0]
            再分割
        """
        # file:C:\Users\Administrator\Desktop\api_auto\common\path_utils.py
        return os.path.split(os.path.split(__file__)[0])[0] + "\\"


if __name__ == '__main__':
    # 当前目录绝对路径
    print(os.path.realpath(__file__))
    # 返回文件绝对路径 文件名
    print(os.path.split(os.path.realpath(__file__)))
    # 返回文件路径
    print(os.path.split(os.path.realpath(__file__))[0])
    # 返回文件名
    print(os.path.split(os.path.realpath(__file__))[1])
    # 获取当前执行脚本的绝对路径
    print(__file__)

    print('------------------------------')

    print(PathUtils().get_project_path())
    print(os.path.split(__file__)[0])
