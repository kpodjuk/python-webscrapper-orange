from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import sched, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')


driver = webdriver.Chrome("C:/Users/kamil/Desktop/prog/python/chromedriver.exe", chrome_options=chrome_options)
driver.get("http://192.168.1.1/home/index.html")
content = driver.page_source

driver.implicitly_wait(5)

button = driver.find_elements_by_xpath('/html/body/div[10]/div[2]/div/div/ul/li[5]/a')[0]
button.click()
value = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/article[1]/div/div[2]/ul[2]/li[3]')[0]



s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print(value.get_attribute("innerHTML"))
    # do your stuff
    s.enter(1, 1, do_something, (sc,))

s.enter(1, 1, do_something, (s,))
s.run()