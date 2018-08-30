#coding:utf-8

#book
#http://hyry.dip.jp/tech/book/page/scipy/matplotlib.html

#demo material
#http://blog.csdn.net/ywjun0919/article/details/8692018

import numpy as np
import matplotlib.pyplot as plt
plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
ax1 = plt.subplot(211) # 在图表2中创建子图1
ax2 = plt.subplot(212) # 在图表2中创建子图2
x = np.linspace(0, 3, 100)
for i in xrange(5):
    plt.figure(1)  #❶ # 选择图表1
    plt.plot(x, np.exp(i*x/3))
    plt.sca(ax1)   #❷ # 选择图表2的子图1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i*x))
plt.show()


#import numpy as np
import pylab as pl
x = [1, 2, 3, 4, 5]# Make an array of x values
y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
pl.plot(x, y)# use pylab to plot x and y
pl.show()# show the plot on the screen

from pylab import *

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plot(X,C)
plot(X,S)
show()

#import numpy as np
import pylab as pl
# Use numpy to load the data contained in the file
# 'fakedata.txt' into a 2-D array called data
data = np.loadtxt("fakedata.txt")
# plot the first column as x, and second column as y
pl.plot(data[:,0], data[:,1], 'ro')
#character, color
#b        , blue
#g        , green
#r        , red
#e        , eyan
#m        , magenta
#y        , yellow
#k        , black
#w        , white

#linestyle, description
#'-'      , solid
#'--'     , dashed
#'-.'     , dash_dot
#':'      , dotted
#'None'   , draw nothing
#' '      , draw nothing
#''       , draw nothing


pl.xlabel('x')
pl.ylabel('y')
pl.xlim(0.0, 10.)
pl.show()


import numpy as np
# Let's make 2 arrays (x, y) which we will write to a file
# x is an array containing numbers 0 to 10, with intervals of 1
x = np.arange(0.0, 10., 1.)
# y is an array containing the values in x, squared
y = x*x
print 'x = ', x
print 'y = ', y
# Now open a file to write the data to
# 'w' means open for 'writing'
file = open('testdata.txt', 'w')
# loop over each line you want to write to file
for i in range(len(x)):
    # make a string for each line you want to write
    # '\t' means 'tab'
    # '\n' means 'newline'
    # 'str()' means you are converting the quantity in brackets to a string type
    txt = str(x[i]) + '\t' + str(y[i]) + ' \n'
    # write the txt to the file
    file.write(txt)
# Close your file
file.close()