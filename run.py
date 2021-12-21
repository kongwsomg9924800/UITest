import os
import sys
import pytest
from common.action import get_path, del_file, set_config, send_hock, get_time


def choose_env():
    dev_url = 'https://www.baidu.com'
    test_url = 'http://1.117.156.17:8090/admin'
    pre_url = 'https://www.qq.com'
    path = get_path('/config.ini')
    arg = sys.argv
    if len(arg) == 2:
        if arg[1] == 'test':
            set_config(path=path, section='ui_info', key='url', value=test_url)
        elif arg[1] == 'dev':
            set_config(path=path, section='ui_info', key='url', value=dev_url)
        elif arg[1] == 'pre':
            set_config(path=path, section='ui_info', key='url', value=pre_url)
        else:
            print('请输入环境名称：dev、test、pre')
            sys.exit(1)

    elif len(arg) == 1:
        set_config(path=path, section='ui_info', key='url', value=test_url)

    else:
        print('请输入环境名称：dev、test、pre')
        sys.exit(1)


if __name__ == '__main__':  # 程序入口，运行整个项目
    choose_env()
    allure_path = get_path('/reports/allure/')
    case_path = get_path('/testcase/')
    html_path = get_path('/reports/html/' + get_time() + '.html')
    del_file(allure_path)
    pytest.main(['-s', '--alluredir', allure_path, case_path, '--html={}'.format(html_path),
                 '--self-contained-html'])  # pytest的内置方法 -s 参数是打印详细信息
    send_hock(html_path)
    os.system('allure serve ' + allure_path + ' -p 61375')  # 运行allure服务

