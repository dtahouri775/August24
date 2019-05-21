import sys
#import pyautogui

import time

try:
    print(sys.version)
    import pyautogui
    # import gw_utility.Book
except:
    import pyautogui
print(pyautogui.size())

print('Press Ctrl-C to quit.')
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print positionStr,
        print '\b' * (len(positionStr) + 2),
        sys.stdout.flush()
        time.sleep(1)
        print('x=',x)
        print('y=',y)
        time.sleep(3)
except KeyboardInterrupt:
    print 'KeyboardInterrupt!!\n'