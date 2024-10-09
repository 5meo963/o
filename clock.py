Here is the cleaned-up version of your code without comments and unnecessary whitespaces:

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import tm1637

try:
    import thread
except ImportError:
    import _thread as thread

Display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)

try:
    Display.StartClock(military_time=False)
    sleep(5)
    Display.ShowDoublepoint(False)
    sleep(5)
    
    loops = 3
    while loops > 0:
        for i in range(10):
            Display.SetBrightness(i / 10.0)
            sleep(0.5)
        loops -= 1
    
    Display.StopClock()
    thread.interrupt_main()

except KeyboardInterrupt:
    Display.cleanup()

