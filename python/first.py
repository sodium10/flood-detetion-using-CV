import pyautogui as p
from time import sleep

# while True:c
#     print(p.position())
p.moveTo(44,68,duration=.5)
p.sleep(1)
p.click()
# p.dragTo(25,68,duration=.6,button="left")

sleep(.5)

# x = 0

# while x != 80:
#     p.click()
#     x += 1ok 



# obj = p.locateOnScreen("test.png")
# p.moveTo(obj,duration=3)


# p.dragTo(426,213,duration=3,button="left")
p.moveTo(515,615,duration=.5)
p.click()
# p.hotkey("command","a",interval=3)
# sleep(1)
# p.hotkey("command","c")
# p.click()


# p.hotkey("command","v")

i = 0
while i<20:
    p.write("hmmmmm ")
    p.press("enter")
    i += 1
