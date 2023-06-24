import time
import clipboard
import pyautogui
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver="chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.get("https://www.google.com/search?q=abcd")