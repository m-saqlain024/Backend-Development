import sys
locaation = sys.path


for i in locaation:
    print(i)

import calendar

leakdays = calendar.leapdays(2000,2050)
# print(leakdays)

isleap = calendar.isleap(2000)
print(isleap)