import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()


# browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
#
# print(input_first)
# print(input_second)
# print(input_third)
#
# browser.close()

# browser.get('https://www.taobao.com')
# input_nodes = browser.find_elements_by_css_selector('.service-bd li')
# print(input_nodes)
# browser.close()
# 淘宝搜索iPhone，ipad
# input = browser.find_element_by_id('q')
# input.send_keys('iphone')
# time.sleep(1)
# input.clear()
# input.send_keys('ipad')
# button = browser.find_element_by_class_name('btn-search')
# print(button)
# button.click()


# 动作链

# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()


# 执行Javascript 下拉进度条
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')



# 获取节点信息

# browser.get('https://www.zhihu.com/explore')
# logo = browser.find_element_by_id('special')
# print(logo)
# print(logo.get_attribute('class'))


# 获取文本值
url = 'https://www.zhihu.com/explore'
browser.get(url)
# input = browser.find_element_by_class_name('Entry-body')
# print(input.text)

#












