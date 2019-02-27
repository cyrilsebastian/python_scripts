#!/usr/bin/python3
#by @CyrilSebastian

#usually time and time-formats are very useful while creating scripts

import time

localtime = time.localtime()
print (localtime)

#printing the date in DD-MM-YY
version1 = time.strftime("%d-%m-%y")
print ("printing DD-MM-YY format")
print (version1)

#printing the date in DD-MMM-YYYY
version2 = time.strftime("%d-%b-%Y")
print ("printing DD-MMM-YYYY format")
print (version2)

#printing the date in DDMMYYHHMMSS
version3 = time.strftime("%d%m%y%I%M%S")
print ("printing DDMMYYHHMMSS format")
print (version3)

#printing epoch
version4 = int(time.time())
print ("printing epoch format")
print (version4)
