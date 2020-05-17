from selenium import webdriver
import time
import requests as rq
from bs4 import BeautifulSoup as bs

board_list = ["https://everytime.kr/370444",
              "https://everytime.kr/370445",
              "https://everytime.kr/375132",
              "https://everytime.kr/375128"]
main_url = "https://everytime.kr"

def login(my_id, my_pass):
    global driver
    driver = webdriver.Chrome("./chromedriver")
    driver.get(main_url)
    login_btn = driver.find_element_by_xpath('/html/body/aside/div[1]/a[2]')
    login_btn.click()
    time.sleep(0.1)
    input_id =driver.find_element_by_xpath('//*[@id="container"]/form/p[1]/input')
    input_pass = driver.find_element_by_xpath('//*[@id="container"]/form/p[2]/input')
    input_id.send_keys(my_id)
    input_pass.send_keys(my_pass)
    enter_btn = driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input')
    enter_btn.click()
    driver.get("https://everytime.kr/lecture")

    return driver

def notfirst():
    global driver
    driver.get("https://everytime.kr/lecture")
    return driver