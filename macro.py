import time
from selenium import webdriver
import pyautogui
import clipboard
from selenium.webdriver.common.by import By

driver=webdriver.Chrome('chromedriver.exe')
driver.get("https://www.naver.com")
driver.execute_script("window.open('https://www.naver.com');")
driver.switch_to.window(driver.window_handles[-1])
element=driver.find_element(By.ID,"query")
element.send_keys("CONTEMENT")
element.send_keys("\n")

input()
driver.switch_to.window(driver.window_handles[-1])
driver.fullscreen_window()
pyautogui.mouseInfo()