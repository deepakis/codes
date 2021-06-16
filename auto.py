import pyautogui as a
import selenium
import time
import webbrowser
webbrowser.open ("https://youtube.com")
time.sleep(7)
# a.write("channel/UCrDbjaPcywlgTRUbbrcK0xg")
# a.keyDown("return")
time.sleep (4)
a.moveTo(700,150)
a.keyDown("return")
a.typewrite("channel/UCrDbjaPcywlgTRUbbrcK0xg")
a.keyDown("return")
time.sleep(1)
a.moveTo(1700,460)
a.leftClick()

