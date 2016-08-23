from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://manhua.163.com")
driver.find_element_by_name('key').send_keys('黑执事')

