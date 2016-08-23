from selenium import webdriver
from public import Login
from time import sleep
import csv

file = 'C:\\Users\\hzluye\\Desktop\\info.csv'
data = csv.reader(open(file,'r'))

class LoginTest():

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get('http://mail.163.com')

    def test_login(self):        
        #username = data[0]
        #password = data[1]
        Login().user_login(self.driver,username,password)
        user = self.driver.find_element_by_id('spnUid').text
        print(user)
        sleep(2)
        self.driver.quit()

    #def test_logout(self):
        #Login.user_logout(self.driver)

for user in data:
    username = user[0]
    password = user[1]
    LoginTest().test_login()
    
