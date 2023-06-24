import time

import clipboard
import pyautogui
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
'''
cd C:\Program Files\Google\Chrome\Application
chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\job\chromedata"

'''
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver="chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.get("https://tm.aliyun.com/?spm=a1z1w.8511710.0.0.icT0AW")
while True:
    try:
        key=input("keyword: ").rstrip()
        driver.switch_to.window(driver.window_handles[0])
        element=driver.find_element(By.CSS_SELECTOR,"#search > div:nth-child(4) > div.search-input > span > span.ace-input.ace-medium.ace-input-group-auto-width > input")
        element.send_keys(Keys.CONTROL + "A")
        element.send_keys(key)
        element.send_keys("\n")
        print(driver.window_handles)
        driver.execute_script(f"window.open('https://www.google.com/search?q={key}');")
        print(driver.window_handles)
        num=int(input("num: "))-1
        comid,owner = "",""
        if num >= 0:
            print(driver.current_window_handle)
            driver.switch_to.window(driver.window_handles[1])
            print(driver.current_window_handle)
            search=driver.find_elements(By.CLASS_NAME,"next-row.trademark-row")
            print(search)
            data=search[num].text.split("\n")
            print(data)
            for w in data:
                c = w.split("：")
                print(c)
                if c[0] == "注册号":
                    comid = c[1]
                    print(comid)
                if c[0]=="申请人":
                    owner=c[1]
                    print(owner)
            companyhref = search[num].find_element(By.CSS_SELECTOR, f"div:nth-child({num + 1}) > div:nth-child(2) > div:nth-child(1) > a").get_attribute("href")
            driver.get(companyhref)
            input("로딩대기")
            print("스샷")
            pyautogui.screenshot("C:/Users/rbxo9/Desktop/새 폴더 (2)/1.png", region=(10, 200, 920, 800))
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()

            # 등록페이지 이동
            print("등록페이지 이동")
            pyautogui.moveTo(1400, 133)
            pyautogui.click()
            time.sleep(1)

            # 영문명 입력
            print("영문명")
            pyautogui.moveTo(1472, 384)
            pyautogui.click()
            clipboard.copy(key)
            pyautogui.hotkey("ctrl", "v")

            # 출원번호
            print("출원번호")
            clipboard.copy(comid)
            time.sleep(0.1)
            pyautogui.moveTo(1204, 547)
            pyautogui.click()
            pyautogui.hotkey("ctrl", "v")
            time.sleep(.2)

            # 사진등록
            print("사진등록")
            pyautogui.moveTo(1097, 687)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1224, 133)
            pyautogui.click()
            pyautogui.press('enter')

            pyautogui.scroll(-1000)
            pyautogui.moveTo(1224, 707)
            pyautogui.click()
            clipboard.copy(owner)
            pyautogui.hotkey("ctrl", "v")

            clipboard.copy("요청")
            input("등록 대기, 요청이랑 등록번호 입력")
            clipboard.copy(comid)
        else:

            print("스샷")
            time.sleep(0.2)
            pyautogui.screenshot("C:/Users/rbxo9/Desktop/새 폴더 (2)/1.png", region=(1, 50, 900, 960))
            time.sleep(0.2)

            # 등록페이지 이동
            print("등록페이지 이동")
            pyautogui.moveTo(1400, 133)
            pyautogui.click()
            time.sleep(1)

            # 미등록상표 이동
            print("미등록상표 이동")
            pyautogui.moveTo(1076, 260)
            pyautogui.click()
            time.sleep(.2)

            # 영문명 입력력
            print("미등록상표 이동")
            pyautogui.moveTo(1500, 352)
            pyautogui.click()
            pyautogui.hotkey("ctrl", "v")

            # 국가 선택
            print("국가 선택")
            pyautogui.moveTo(1181, 482)
            pyautogui.click()
            pyautogui.moveTo(1181, 542, duration=0.5)
            pyautogui.scroll(-2300)
            pyautogui.click()
            time.sleep(.2)

            pyautogui.moveTo(1070, 832)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1224, 133)
            pyautogui.click()
            pyautogui.press('enter')
            clipboard.copy("요청")
    except:
        print("except")
    for win in reversed(driver.window_handles[1:]):
        driver.switch_to.window(win)
        driver.close()
