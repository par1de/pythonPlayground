import pyautogui
import time

time.sleep(3)
# f = open("sorgente", "r")
# for word in f:
# 	pyautogui.typewrite(word)
# 	pyautogui.press("enter")
#  time.sleep(3)
# f.close()
for i in range(10):
	pyautogui.typewrite("ciao")
	pyautogui.press("enter")
	pyautogui.press("enter")
