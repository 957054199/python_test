# 安装selenium：pip install selenium
# 查看是否安装成功：pip show selenium
# webdriver驱动

from selenium import webdriver

# 通过webdriver驱动调用谷歌浏览器
browser = webdriver.Firefox()
url = "https://www.baidu.com"
browser.get(url)
