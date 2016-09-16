#!/usr/bin/python

import time

localTime = time.localtime(time.time())
print localTime

timeStr = time.asctime(localTime)
print timeStr
