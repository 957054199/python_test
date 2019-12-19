# 认识元素定位
# Ctrl + / 注释
# find_element_by_id 通过网页标签ID获取属性
# find_element_by_name 通过网页标签name
# find_element_by_class_name 通过页面的class获取元素
# find_element_by_xpath
# find_element_by_css_selector 通过页面css样式获取元素
# click 点击 clear 清空 time 时间

# 第一步导驱动webdriver
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

browser = webdriver.Firefox()
url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
browser.get(url)

# time 休眠一下
time.sleep(1)

# 输入出发地
# fromStationText 拿到出发地的ID值
start_city = browser.find_element_by_id("fromStationText")

# 点击输入框
start_city.click()

# 清除输入框里面的内容
start_city.clear()

# 输入出发地址 send_keys() 在里面添加数据
start_city.send_keys("北京\n")

# 输入目的地 toStationText
end_city = browser.find_element_by_id("toStationText")

# 点击输入框
end_city.click()

# 清空输入框里面的内容
end_city.clear()

# 输入目的地址 send_keys()
end_city.send_keys("石家庄\n")

time.sleep(2)

# 下拉框技术点 select cc_start_time
times = Select(browser.find_element_by_id("cc_start_time"))

# 获取文本
times.select_by_visible_text("12:00--18:00")

time.sleep(2)

# 选择周日
date = browser.find_element_by_css_selector("#date_range li:nth-child(4)")
date.click()
