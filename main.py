import time

from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="/Users/kongweicheng/utils/selenium/chromedriver")  # 打开Chrome浏览器并实例化，指定chromedriver地址
time.sleep(1)  # 主进程睡眠1秒
driver.get("https://www.baidu.com")  # 打开'https://www.baidu.com'
time.sleep(1)
driver.find_element_by_id("kw").send_keys("kongweisheng")  # 定位到输入框（按id），并对输入框进行操作（在输入框输入kongweisheng）
driver.find_element_by_id("su").click()  # 定位到搜索按钮（按id）并点击该按钮
time.sleep(10)
driver.quit()  # 关闭该浏览器进程
