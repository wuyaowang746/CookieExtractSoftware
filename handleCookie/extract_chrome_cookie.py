import os
import sys
import sqlite3
import http.cookiejar as cookiejar
from urllib.parse import urlencode
import json, base64
import ctypes.wintypes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)
import urllib
"""
错误码
"""
CHROME_ERROR = "CHROME_FILE_NOT_EXISTS"
FIREFOX_ERROR = "FIREFOX_FILE_NOT_EXISTS"

# SQL查询语句，从cookie文件中查询
sql = """
SELECT
    host_key, name, encrypted_value as value, path
FROM
    cookies
"""


# chrome版本低于80.X的使用这个函数进行encrypted_value的解密
def dpapi_decrypt(encrypted):
    class DATA_BLOB(ctypes.Structure):
        _fields_ = [('cbData', ctypes.wintypes.DWORD),
                    ('pbData', ctypes.POINTER(ctypes.c_char))]

    p = ctypes.create_string_buffer(encrypted, len(encrypted))
    blobin = DATA_BLOB(ctypes.sizeof(p), p)
    blobout = DATA_BLOB()
    retval = ctypes.windll.crypt32.CryptUnprotectData(
        ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))
    if not retval:
        raise ctypes.WinError()
    result = ctypes.string_at(blobout.pbData, blobout.cbData)
    ctypes.windll.kernel32.LocalFree(blobout.pbData)
    return result


def get_key_from_local_state():
    jsn = None
    with open(os.path.join(os.environ['LOCALAPPDATA'],
                           r"Google\Chrome\User Data\Local State"), encoding='utf-8', mode="r") as f:
        jsn = json.loads(str(f.readline()))
    return jsn["os_crypt"]["encrypted_key"]

'''
Chrome 版本在80.X以上的使用这个函数对加密的value进行解密
'''
def aes_decrypt(encrypted_txt):
    encoded_key = get_key_from_local_state()
    encrypted_key = base64.b64decode(encoded_key.encode())
    encrypted_key = encrypted_key[5:]
    key = dpapi_decrypt(encrypted_key)
    nonce = encrypted_txt[3:15]
    cipher = Cipher(algorithms.AES(key), None, backend=default_backend())
    cipher.mode = modes.GCM(nonce)
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_txt[15:])

'''
对提取到的cookie分别进行解密
'''
def chrome_decrypt(encrypted_txt):
    if sys.platform == 'win32':
        try:
            if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                decrypted_txt = dpapi_decrypt(encrypted_txt)
                return decrypted_txt.decode()
            elif encrypted_txt[:3] == b'v10':
                decrypted_txt = aes_decrypt(encrypted_txt)
                return decrypted_txt[:-16].decode()
        except WindowsError:
            return None

'''
提取cookie信息
'''
def get_cookies_from_chrome():
    data_list = []
    filename = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\default\Cookies')
    # 错误测试
    # filename = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\default\Cooki')
    # 文件路径正确时提取解密数据
    # 判断是否存在cookie文件
    if os.path.exists(filename):
        try:
            if sqlite3.connect(filename):
                con = sqlite3.connect(filename)
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                cur.execute(sql)

                for each in cur:
                    host = each['host_key']
                    name = each['name']
                    value = chrome_decrypt(each['value'])
                    path = each['path']
                    # print("host:" + host + " path:" + path + " name:" + name + " value:" + value)
                    data_list.append([host, name, value, path])
                return data_list
            # 文件路径不正确时抛出错误
        except Exception as e:
            print(e)
    # 不存在返回空列表
    else:
        return data_list



if __name__ == '__main__':
    get_cookies_from_chrome()
