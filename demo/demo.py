#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a = [1,2,3,4,5]
b = [5,4,3,2,1]

def sum(x, y):
    return x + y

zip(a, b) #[(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]

map(lambda x:x[0]*x[1], zip(a,b)) #[5, 8, 9, 8, 5]

reduce(sum, map(lambda x:x[0]*x[1], zip(a,b)))
reduce((lambda x,y: x+y), map(lambda x:x[0]*x[1], zip(a,b)))



