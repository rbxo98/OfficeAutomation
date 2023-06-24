from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import clipboard
e=Exception()
import time

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")

while True:
    driver=webdriver.Chrome('chromedriver.exe')
    driver.execute_script("window.open('https://tm.aliyun.com/?spm=a1z1w.8511710.0.0.icT0AW');")
    result=[]
    driver.switch_to.window(driver.window_handles[-1])
    element=driver.find_element(By.CSS_SELECTOR,"#search > div:nth-child(4) > div.search-input > span > span.ace-input.ace-medium.ace-input-group-auto-width > input")
    key=input("keyword: ").rstrip()
    driver.execute_script(f"window.open('https://www.google.com/search?q={key}');")
    element.send_keys(key)
    element.send_keys("\n")
    driver.switch_to.window(driver.window_handles[-1])
    try:
        productlist=driver.find_elements(By.CLASS_NAME,"next-row.trademark-row")
        print(productlist)
        driver.execute_script("window.open('https://naver.com');")
        driver.switch_to.window(driver.window_handles[-1])
        element=driver.find_element(By.ID,"query")
        element.send_keys(key)
        element.send_keys("\n")
        print("있으면 번째, 없고 홈페이지면 0")
        num=int(input())-1
        print(num)
        if num==-3:
            ...
        elif num>=0:
            driver.switch_to.window(driver.window_handles[2])
            for w in productlist[num].text.split():
                c=w.split("：")
                print(c)
                if c[0]=="注册号":
                    companyid=c[1]
            companyhref=productlist[num].find_element(By.CSS_SELECTOR,f"div:nth-child({num+1}) > div:nth-child(2) > div:nth-child(1) > a").get_attribute("href")
            clipboard.copy(companyhref)
            driver.quit()
            pos = pyautogui.position()
            pyautogui.moveTo(1, 1)
            pyautogui.click()
            print(1)
            pyautogui.hotkey("ctrlleft", "t")
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press('enter')
            pyautogui.moveTo(pos)
            input("로딩, 번역제거")
            print("")

            # 스크린샷
            print("스샷")
            pyautogui.moveTo(2, 44)
            time.sleep(0.2)
            pyautogui.screenshot("C:/Users/rbxo9/Desktop/새 폴더 (2)/1.png", region=(11, 233, 920, 783))
            time.sleep(0.2)

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
            time.sleep(.2)

            # 출원번호
            print("출원번호")
            clipboard.copy(companyid)
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

            input("등록 대기, 요청이랑 등록번호 입력")
            clipboard.copy(companyid)
        else:
            print("스샷")
            time.sleep(0.2)
            pyautogui.screenshot("C:/Users/rbxo9/Desktop/새 폴더 (2)/1.png", region=(4, 47, 900, 960))
            time.sleep(0.2)

            driver.quit()
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
            clipboard.copy(key)
            pyautogui.hotkey("ctrl","v")

            #국가 선택
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