"""
RUN THE PROGRAM AND ENTER THE FIELDS REQUIRED
"""
from selenium import webdriver
import pyautogui
import time
product = input("Enter the product you want to search and press 'e' to exit the program  ")
browser = webdriver.Edge()
browser.get("https://www.flipkart.com/")
browser.switch_to.window(browser.window_handles[0])
browser.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys(product)
pyautogui.press('enter')
browser.execute_script("window.open('https://www.snapdeal.com/')")
browser.switch_to.window(browser.window_handles[1])
browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div[2]/input').send_keys(product)
pyautogui.press("enter")
browser.execute_script("window.open('https://www.amazon.in/');")
browser.switch_to.window(browser.window_handles[2])
browser.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').send_keys(product)
pyautogui.press('enter')





