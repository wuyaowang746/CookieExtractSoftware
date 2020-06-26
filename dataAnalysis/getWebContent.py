import os
import sqlite3
import urllib.request

from lxml import etree
import requests
import urllib.parse

from requests import RequestException
import extract_chrome_cookie
import get_other_cookie
"""
错误码
"""
READ_ERROR = "ERROR"
NETWORK_ERROR = "NETWORK_ERROR"
CHROME_ERROR = "CHROME_FILE_NOT_EXISTS"
FIREFOX_ERROR = "FIREFOX_FILE_NOT_EXISTS"
NO_DANGDANGCOOKIE = "NO_DANGDANGCOOKIE"

"""
爬取网页上的内容，如书名，分类等等
"""
def getPage(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            # res.encoding = 'GBK'
            # 解决中文显示异常的问题
            root = etree.HTML(res.text.encode(res.encoding).decode(res.apparent_encoding, errors='ignore'))
            name = root.xpath('//*[@id="product_info"]/div[1]/h1/@title')
            classification = root.xpath('//*[@id="detail-category-path"]/span/a[1]/text()')[0]
            print(name)

    except RequestException as e:
        print(e)


def getURL():
    temp = getDangDangCookieFromChrome()
    if temp == -1:
        return -1
    historyHtml = []
    try:
        if temp is not -1:
            historyPage = temp.split(',')
            for each in historyPage:
                historyHtml.append('http://product.dangdang.com/' + each + '.html')
            return historyHtml
    except Exception as e:
        print(e)


"""
从chrome获取当当网的cookie浏览历史
"""
def getDangDangCookieFromChrome():
    sql_exe = 'select name, encrypted_value as value from cookies where host_key like ".dangdang.com"'
    filename = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\default\Cookies')
    # 错误测试
    # filename = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\defaul\Cookies')
    # 文件路径正确时提取解密数据
    try:
        if sqlite3.connect(filename):
            con = sqlite3.connect(filename)
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute(sql_exe)
            flag = -1
            for each in cur:
                if each['name'] == 'producthistoryid':
                    value = extract_chrome_cookie.chrome_decrypt(each['value'])
                    flag = 1
            # 当前数据库内存在浏览历史的记录
            if flag == 1:
                # 对数据进行urldecode操作
                tempValue = urllib.parse.unquote(value)
                return tempValue
            else:
                return -1
    # 文件路径不正确时抛出错误
    except Exception as e:
        return e

def analysisPage():
    historyHtml = getURL()
    dataList = ["NETWORK_ERROR"]
    if historyHtml == -1:
        return []
    shopHistory = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
    for each in historyHtml:
        try:
            res = requests.get(each, headers=headers)
            if res.status_code == 200:
                root = etree.HTML(res.text.encode(res.encoding).decode(res.apparent_encoding, errors='ignore'))
                # 先获取商品大的分类，如果是图书则获取出版社，作者，出版日期等信息
                # 如果是非图书的商品，只需要获取商品名称和分类
                firstClass = root.xpath('//*[@id="breadcrumb"]/a[1]/b/text()')[0]
                imgSrc = root.xpath('//*[@id="largePic"]/@src')[0]
                if firstClass == '图书':
                    # 商品名称
                    goodsName = '书名: ' + root.xpath('//*[@id="product_info"]/div[1]/h1/@title')[0]
                    # 作者姓名
                    authorName = root.xpath('//*[@id="author"]/a[1]/text()')[0]
                    authorName = '作者: ' + authorName
                    # 出版社名称
                    publisher = root.xpath('//*[@id="product_info"]/div[2]/span[2]/a/text()')[0]
                    publisher = '出版社: ' + publisher
                    # 二级分类
                    secondClass = root.xpath('//*[@id="breadcrumb"]/a[2]/text()')[0]
                    # 三级分类
                    thirdClass = root.xpath('//*[@id="breadcrumb"]/a[3]/text()')[0]
                    classification = '分类: ' + firstClass + '->' + secondClass + '->' + thirdClass
                    shopHistory.append([imgSrc, goodsName, classification, authorName, publisher])
                else:
                    goodsName = '商品名称: ' + root.xpath('//*[@id="product_info"]/div[1]/h1/@title')[0]
                    # 二级分类
                    secondClass = root.xpath('//*[@id="breadcrumb"]/a[2]/text()')[0]
                    # 三级分类
                    thirdClass = root.xpath('//*[@id="breadcrumb"]/a[3]/text()')[0]
                    classification = '分类: ' + firstClass + '->' + secondClass + '->' + thirdClass
                    shopHistory.append([imgSrc, goodsName, classification])
        except RequestException:
            return dataList
    return shopHistory


if __name__ == "__main__":
    # getPage('http://product.dangdang.com/28530739.html')
    # getURL()
    # getDangDangCookieFromChrome()
    analysisPage()
