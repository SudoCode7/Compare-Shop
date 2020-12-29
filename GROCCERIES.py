"""
ENTER YOUR LOCATION IN THE TWO PLACES DOWN COMMENTED BELOW AND ENJOY!!!
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import  time
import pyautogui
from selenium.webdriver.common.keys import Keys

pincode = 122009     #ENTER YOUR PINCODE HERE
place = "gurgaon"    #ENTER YOUR CITY HERE IN INVERTED QUOTES
browser = webdriver.Edge()
browser.get("https://www.bigbasket.com/")
browser.find_element_by_xpath("/html/body/div[1]/div[1]/header/div/div/div/div/ul/li[2]/div/a/span/span[3]").click()
browser.find_element_by_xpath("/html/body/div[1]/div[1]/header/div/div/div/div/ul/li[2]/div/div/div[2]/form/div[1]/div/div/span").click()
browser.find_element_by_xpath("/html/body/div[1]/div[1]/header/div/div/div/div/ul/li[2]/div/div/div[2]/form/div[1]/div/input[1]").send_keys(place)
browser.find_element_by_xpath("/html/body/div[1]/div[1]/header/div/div/div/div/ul/li[2]/div/div/div[2]/form/div[1]/div/ul[1]/li/div[3]/a").click()
browser.find_element_by_xpath("/html/body/div[1]/div[1]/header/div/div/div/div/ul/li[2]/div/div/div[2]/form/div[2]/input[1]").send_keys(pincode)
browser.find_element_by_xpath("/html/body/div[1]/div[1]/header/div/div/div/div/ul/li[2]/div/div/div[2]/form/div[3]/button").click()
browser.execute_script("window.open('https://grofers.com/');")
time.sleep(1)
browser.execute_script("window.open('https://jiomart.com/');")
random= input("\n\nEnter the location in Grofers and Jiomart, when done press enter")
product = input("\nEnter the product you want to search and press 'e' to exit \n")
while product!='e':
    browser.switch_to.window(browser.window_handles[0])
    browser.find_element_by_xpath('//*[@id="input"]').send_keys(product)
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[8]/div/div[3]/div/div[1]/button').click()
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/header/div[2]/div/div/div[1]/input').send_keys(product)
    pyautogui.press('enter')
    time.sleep(2)
    for i in product:
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/header/div[2]/div/div/div[1]/input').send_keys(Keys.BACKSPACE)
        pyautogui.press("esc")
    browser.switch_to.window(browser.window_handles[2])
    browser.find_element_by_xpath('//*[@id="search"]').send_keys(product)
    pyautogui.press('enter')
    product = input("\nEnter next product ")