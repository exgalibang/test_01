from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://manhua.163.com')
print('设置浏览器宽480、高800显示')
driver.set_window_size(480,800)
driver.quit()
