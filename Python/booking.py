import json
import time
import re
import string
import requests
import bs4
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
def prepare_driver(url):
    '''Returns a Firefox Webdriver.'''
    options = Options()
   # options.add_argument('-headless')
    driver = Firefox(executable_path='geckodriver', options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, 'ss')))
    return driver


driver=prepare_driver('https://www.booking.com') 

driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div[1]").click()


#time.sleep(10)    

#selected the dates
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div[2]/div/div/div[2]").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div[2]/div/div/div[2]").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div[2]/div/div/div[2]").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div[2]/div/div/div[2]").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div[2]/div/div/div[2]").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div[2]/div/div/div[2]").click()

driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[5]/td[5]").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[5]/td[7]").click()
time.sleep(10)   

#time.sleep(10)

driver.find_element_by_xpath('//*[@id="xp__guests__toggle"]').click()
for i in range(28):
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/button[2]").click()
for i in range(29):
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/div/div[3]/div/div[2]/button[2]").click
for i in range(5):
#driver.close()
