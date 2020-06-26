import os
import sqlite3
import re
import numpy
import pandas

"""
错误码
"""
CHROME_ERROR = "CHROME_FILE_NOT_EXISTS"
FIREFOX_ERROR = "FIREFOX_FILE_NOT_EXISTS"

READ_ERROR = "ERROR"
'''
得到Firefox存储cookies文件的绝对路径
处理逻辑是如果Profiles文件夹下同时存在"xxx.default"和"xxx.default-release"，进入后者寻找cookies，否则进入前者
@:param folds_arr:列出在当前文件夹下所有的文件或者文件夹
@:param folds_end:取当前文件夹下所有文件的后缀名
@:param cookie_path:cookies文件完整的路径
'''


def get_firefox_cookie_path():
    cookiepath_common = os.environ['APPDATA'] + r"\Mozilla\Firefox\Profiles"
    folds_arr = os.listdir(cookiepath_common)
    folds_end = [os.path.splitext(file)[-1][1:] for file in folds_arr]  # 将文件名和后缀分开
    flag = -1
    for each in folds_end:
        if 'default-release' in each:
            flag = folds_end.index(each)
        elif 'default' in each:
            flag = folds_end.index('default')
        if flag is not -1:
            break
    # 当没有这两个文件夹的时候返回READ_ERROR错误
    if flag == -1:
        return READ_ERROR
    # 否则返回拼接正确的文件路径
    else:
        cookie_fold_index = flag
        cookie_fold = folds_arr[cookie_fold_index]
        cookie_path = os.path.join(cookiepath_common, cookie_fold)
        return os.path.join(cookie_path, 'cookies.sqlite')


'''
读取cookie文件
@:param sql_exe:SQL语句
@:param cursor:数据库查询指针

'''
def get_cookie_from_firefox():
    data_list = []
    cookie_file = get_firefox_cookie_path()
    # 如果没有找到正确的文件路径，返回-1
    if cookie_file == READ_ERROR:
        return data_list
    # 在正确的文件路径上操作文件
    else:
        con = sqlite3.connect(cookie_file)
        con.row_factory = sqlite3.Row
        sql_exe = "select host, name, value , path from moz_cookies"
        df = pandas.read_sql(sql_exe, con)
        df1 = numpy.array(df)
        return df1.tolist()

    # try:
    #     if cursor.execute(sql_exe):
    #         for each in cursor:
    #             host = each['host']
    #             name = each['name']
    #             value = each['value']
    #             path = each['path']
    #            # print("host:" + host + " path:" + path + " name:" + name + " value:" + value)
    # except Exception as e:
    #     print(e)


if __name__ == '__main__':
    # get_firefox_cookie_path()
    get_cookie_from_firefox()
