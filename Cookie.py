from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import random

import threading

import time

driver = webdriver.Chrome("C:\\Users\\inspiron\\Downloads\\chromedriver_win32\\chromedriver")

url = "http://orteil.dashnet.org/cookieclicker/"

driver.get(url)


def investingClicks(browser):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='bigCookie']")))

    cookie = browser.find_element_by_xpath("//div[@id='bigCookie']")
    while True:
        try:
            cookie.click()

            for i in browser.find_elements_by_xpath("//div[@class='product unlocked enabled']"):
                probability = random.randint(0,100)
                
                if "Tower" in i.text:
                    cookie.click()
                    if probability < 71:
                        i.click()
                        print(i.text)
                    elif probability == 1:
                        time.sleep(300)
                elif "Mine" in i.text:
                    cookie.click()
                    if probability < 61:
                        i.click()
                        print(i.text)
                    elif probability == 1:
                        time.sleep(300)
                elif "Bank" in i.text:
                    cookie.click()
                    if probability < 61:
                        i.click()
                        print(i.text)
                    elif probability == 1:
                        time.sleep(300)
                elif "Factory" in i.text:
                    cookie.click()
                    if probability < 61:
                        i.click()
                        print(i.text)
                    elif probability == 1:
                        time.sleep(300)
                elif "Farm" in i.text:
                    cookie.click()
                    if probability < 61:
                        i.click()
                        print(i.text)
                    elif probability == 1:
                        time.sleep(300)
                elif "Grandma" in i.text:
                    cookie.click()
                    if probability < 41:
                        i.click()
                        print(i.text)
                    elif probability == 1:
                        time.sleep(300)
                elif "Cursor" in i.text:
                    cookie.click()
                    if probability < 20:
                        i.click()
                        print(i.text)
                    elif probability == 1:
                        time.sleep(300)
                
                
                
                
                else:
                    i.click()
                    cookie.click()
        except:
            pass

def constantClicks(browser):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='bigCookie']")))
    cookie = browser.find_element_by_xpath("//div[@id='bigCookie']")
    while True:
        try:
            cookie = browser.find_element_by_xpath("//div[@id='bigCookie']")

            cookie.click()
        except:
            pass

def constantClicks2(browser):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='bigCookie']")))
    cookie = browser.find_element_by_xpath("//div[@id='bigCookie']")
    while True:
        try:
            cookie = browser.find_element_by_xpath("//div[@id='bigCookie']")

            cookie.click()
        except:
            pass

def constantClicks3(browser):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='bigCookie']")))
    cookie = browser.find_element_by_xpath("//div[@id='bigCookie']")
    while True:
        try:
            cookie = browser.find_element_by_xpath("//div[@id='bigCookie']")

            cookie.click()
        except:
            pass


def constantUpgrades(browser):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='bigCookie']")))
    #upgrade = browser.find_elements_by_xpath("//div[@class='crate upgrade enabled']")
    while True:
        upgrade = browser.find_elements_by_xpath("//div[@class='crate upgrade enabled']")
    
        
        for i in upgrade:

            i.click()     
        time.sleep(10)        
    

thread1 = threading.Thread(target = investingClicks(driver))

thread2 = threading.Thread(target = constantClicks(driver))
thread3 = threading.Thread(target = constantClicks2(driver))
thread4 = threading.Thread(target = constantClicks3(driver))
thread5 = threading.Thread(target = constantUpgrades(driver))




thread2.start()
thread3.start()
thread4.start()

time.sleep(30)
thread1.start()
thread5.start()
