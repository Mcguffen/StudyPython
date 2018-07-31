# 这是一个Matplotlib的的字体管理类
# 1.加载front文件夹里面的字体数据
#   1).字体名字 相对位置
# 2.字体用数组显示
#   1)返回字体的名字和路径
# 3.
import os
import glob
from utils import log


l = []


def get_py(path, l):
    # fileList = os.listdir(path)   #获取path目录下所有文件
    filelist = os.getcwd()
    for filename in filelist:
        pathTmp = os.path.join(path,filename)   #获取path与filename组合后的路径
        if os.path.isdir(pathTmp):   #如果是目录
           log("meiy")
            # get_py(pathTmp,l)        #则递归查找
        elif filename[-3:].upper()== '.ttf':   #不是目录,则比较后缀名
            l.append(pathTmp)


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        log('root =({}) \n dirs =({})\n files = ({})'.format(root, dirs, files))


def find_front_by_windows():
    fronts = glob.glob(r'C:/Windows/Fonts/**.ttf')
    log("windows front=({})".format(fronts))

    pass


def find_file():
    # 获取当前目录下所有的.ttf文件
    # 1.打开当前目录

    suf = '*'+'.ttf'
    ttfs = []
    log('debug findfile')
    for suffile in glob.glob(os.path.join('front', '.', '*.ttf')):
        ttfs.append(suffile)
        log("debug suffile @@@@@ ({}) \n ({})".format(suffile, ttfs))
        # workbook.close()


def test_get_by():
    path = input('请输入路径:').strip()
    get_py(path,l)
    print('在%s目录及其子目录下找到%d个,ttf文件\n分别为：\n'%(path, len(l)))
    for filepath in l:
        print(filepath+'\n')
    pass


def test():
    # test_get_by()
    find_file()
    find_front_by_windows()
    # c = 'source_code_pro'
    # file_name(c)
    pass


if __name__ == '__main__':
    test()
    pass
