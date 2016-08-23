from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://mail.163.com')
driver.implicitly_wait(10)

print('begin')
driver.switch_to.frame("x-URS-iframe")
print('switch frame')

#当前用户信息
username = 'galibang_001'
password = 'galibang001'

#打印当前页title
title = driver.title
print(title)

#打印当前页URL
url = driver.current_url
print(url)

#执行163邮箱登录
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys(username)
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_id('dologin').click()
sleep(3)

#再次打印当前页title
title = driver.title
print(title)

#打印当前页URL
url = driver.current_url
print(url)

#获得登录的用户名
user = driver.find_element_by_id('spnUid').text
print(user)

#点击收信
driver.find_element_by_id('_mail_component_59_59').click()
sleep(3)






'''
driver.quit()

'''
