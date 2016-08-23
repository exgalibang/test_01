from selenium import webdriver

#登录
def login():
    driver.find_element_by_name('email').clear()
    driver.find_element_by_name('email').send_keys(username)
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('dologin').click()


#退出
def logout():
    driver.find_element_by_link_text('退出').click()
    #driver.quit()


#当前用户信息
username = 'galibang_001'
password = 'galibang001'


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://mail.163.com')
driver.switch_to.frame("x-URS-iframe")
login()  #调用登录模块


#收信、写信、删除信件模块
#...


logout()  #调用退出模块
