from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from os import system

mess = input("Input the message you want to spam: ")
driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
time.sleep(1)


system("cls")
input("Type anything in this command line to start the spam: ")

count = 0

while True:   
    count +=1
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys (f"{mess}")
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]/button').click()  
    print(count)
