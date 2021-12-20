# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/148:38 下午
@DESC :
'''
import configparser
import shutil
import sys
import time

import requests as requests
import yaml
import os


def get_config(item: str):
    """
    获取/config.ini文件下，api_info标题下，指定item键的值
    :param item: 键
    :return:
    """
    config = configparser.ConfigParser()
    config.read(get_path('/config.ini'))
    items = dict(config.items('api_info'))
    return items[item]


def get_yaml(path):
    """
    获取yaml下的所有内容，并转为字典
    :param path: yaml文件路径
    :return:
    """
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)  # safe_load(f) yaml自带的函数，作用是将读取后的yaml内容转为字典
    return data


def get_path(path):
    """
    获取绝对路径，并将传入的path拼接到绝对路径末尾
    :param path: 传入的相对路径
    :return:
    """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + path
    return path


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def set_config(path: str, section: str, key: str, value: str) -> None:
    config = configparser.ConfigParser()  # 调用python的标准库configparser，并实例化
    config.read(path)  # 读取/config.ini文件，get_path('/config.ini')为自定义方法，作用是获取绝对路径
    config.set(section, key, value)  # 将ini文件中的api_info标题下的cookies键赋值为str(cookies)
    config.write(open(path, 'r+'))  # 保存


def send_hock(des):
    data = {"msg_type": "text", "content": {"text": des}}
    res = requests.request(method='POST',
                           url='https://open.feishu.cn/open-apis/bot/v2/hook/179b90d2-4fca-4940-928c-b1119a7e9c95',
                           json=data)
    print(res.text)


def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def get_html_info(path):
    with open(path, 'r', encoding='utf-8') as f:
        a = f.read()
        # todo: 正则表达式


if __name__ == '__main__':
    get_html_info('/Users/kongweicheng/code/linxin_learn/UITestT/report/html_report/2021-12-20 23:21:58.html')
