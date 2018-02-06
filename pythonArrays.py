#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

i=0
for i in range (n):
    #print ("i:{} n:{}".format(i,n-i-1))
    x=n-i-1
    sys.stdout.write(str(arr[x])+" ")
    
