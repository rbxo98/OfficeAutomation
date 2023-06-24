import time
import clipboard
import pyautogui

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
clipboard.copy("재요청")
