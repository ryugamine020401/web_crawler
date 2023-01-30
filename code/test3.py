


st = "3.14159 26535 89793 23846 26433 83279 50288 41971 69399 37510 58209 74944 59230 78164 06286 20899 86280 34825 34211 70679 82148 08651 32823 06647 09384 46095 50582 23172 53594 08128 48111 74502 84102 70193 85211 05559 64462 29489 54930 38196"
# print(st.split())
#st = "3.14159 26535 89793 23846 26433 83279 50288 41971 69399 37510 58209 74944"
k = st.split()
str_ = "".join(k)
# print(str_)

import time
import pyautogui
#
# #目前滑鼠坐標
#
# #目前螢幕解析度=
# pyautogui.size()
# #(x,y)是否在螢幕上
# x, y = pyautogui.position()
# print(pyautogui.position())
# print(x, y)
num_seconds = 0.1
cnt = 0
print(str_)
while 1:
    #ctrl + f2 exitHello world!11455
    #pyautogui.moveTo(1185, 439, duration=num_seconds)
    if(cnt == 1):
        time.sleep(2)
        pyautogui.leftClick(1111, 511)  #點進去
        pyautogui.hotkey('ctrl', 'a')  # 快捷鍵組合
        pyautogui.hotkey('right')  # 快捷鍵組合
        pyautogui.hotkey('backspace')
        #pyautogui.typewrite(str_)
        time.sleep(2)
        pyautogui.leftClick(1185, 511)   #送出
        # tmp = str_[::-1]
        # tmp = tmp[1:]
        # str_ = tmp[::-1]
        # print(str_)

    else:
        pyautogui.leftClick(1111, 442)
        #pyautogui.typewrite(str_)
        pyautogui.leftClick(1185, 442)
        cnt += 1