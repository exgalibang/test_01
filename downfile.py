from selenium import webdriver
import os

fp = webdriver.FirefoxProfile()

fp.set_preference('browser.download.folderList',0)
fp.set_preference('browser.download.manager.showWhenStarting',True)
fp.set_preference('browser.download.dir',os.getcwd())
fp.set_preference('browser.helperApps.neverAsk.saveToDisk','application/octet-stream')

driver = webdriver.Firefox(firefox_profile=fp)
driver.get('http://pypi.Python.org/pypi/selenium#downloads')
driver.find_element_by_partial_link_text('selenium-3').click()
