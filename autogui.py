import pyautogui as pg
import time
print("start 5 sec")
time.sleep(5)
for i in range(30):
    pg.write("HEllo")
    pg.press("enter")