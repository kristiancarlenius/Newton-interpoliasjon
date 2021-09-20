# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:42:33 2021

@author: Kristian
"""
import numpy as np
x = [1976, 1981, 1986, 1991, 1996, 2001];
y = [4017101, 4092340, 4159187, 4249830, 4369957, 4503436];
yx = [0, 0, 0, 0, 0, 0]
y2 = [0, 0, 0, 0, 0, 0]
y3 = [0, 0, 0, 0, 0]
y4 = [0, 0, 0, 0]
y5 = [0, 0, 0]
y6 = [0, 0]
y7 = [0]
yy = [y, y3, y4, y5, y6, y7]

for i in range(len(y3)):
    y3[i]= (y[i+1]-y[i])/(x[i+1]-x[i])
    
for i in range(len(y4)):
    y4[i]= (y3[i+1]-y3[i])/(x[i+2]-x[i])
    
for i in range(len(y5)):
    y5[i]= (y4[i+1]-y4[i])/(x[i+3]-x[i])
    
for i in range(len(y6)):
    y6[i]= (y5[i+1]-y5[i])/(x[i+4]-x[i])

y7[0]= (y6[1]-y6[0])/(x[5]-x[0])

for i in range(len(yx)):
    yx[i] = yy[i][0]

#print(yx)

d = 1
f = np.poly((x[0], x[1]))
g = np.poly((x[0], x[1], x[2]))
h = np.poly((x[0], x[1], x[2], x[3]))
j = np.poly((x[0], x[1], x[2], x[3], x[4]))


y2[0] = d
y2[1] = np.poly1d([1, 1976])
y2[2] = np.poly1d(f)
y2[3] = np.poly1d(g)
y2[4] = np.poly1d(h)
y2[5] = np.poly1d(j)

a = len(yx)
c = len(yx)-1
while c > 0:
    
    while a >= 0:
        y2[c][a] = y2[c][a]*yx[c]
        print(y2[c][a])
        a -= 1
    c -= 1
    a = c + 1
    

l = np.polyadd(np.polyadd(np.polyadd(y2[1], y2[2]), np.polyadd(y2[3], y2[4])), np.polyadd(y2[5], y2[0]))

print(l)