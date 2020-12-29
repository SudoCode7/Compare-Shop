from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import  time
import pyautogui
from selenium.webdriver.common.keys import Keys
browser = webdriver.Edge()
p ="trest"
browser.get("https://www.grofers.com/")
time.sleep(7)
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/header/div[2]/div/div/div[1]/input').send_keys(p)
#browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/header/div[2]/div/div/div[1]/input').click()
for i in p:
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/header/div[2]/div/div/div[1]/input').send_keys(Keys.BACKSPACE)