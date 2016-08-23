from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

cookies = driver.get_cookies()
print(cookies)

driver.quit()
