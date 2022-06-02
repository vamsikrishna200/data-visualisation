#line plots

import matplotlib.pyplot as plt
import numpy as np
# define data values
x = np.array([1, 2, 3, 4]) # X-axis points
y = x*2 # Y-axis points
plt.plot(x, y) # Plot the chart
plt.show() # display
plt.savefig('plt1.jpg')


import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4])
y = x*2
plt.plot(x, y, '-.')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Any suitable title")
plt.show() # show first chart
plt.savefig('plt2.jpg')

import matplotlib.pyplot as pltimport numpy as np
x = np.array([1, 2, 3, 4])
y = x*2
# first plot with X and Y data
plt.plot(x, y)
x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]
# second plot with x1 and y1 data
plt.plot(x1, y1, '-.')
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')
plt.savefig('plt3.jpg')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4])
y = x*2plt.plot(x, y)
x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]
plt.plot(x, y1, '-.')
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')
plt.fill_between(x, y, y1, color='green', alpha=0.5)
plt.show()

import matplotlib.pyplot as plt
import random as random
students = ["a","b","c","d","e",
"f","g","h","i","j",
"k","l","m","n","oe",
"p","q","r","s","t"]
marks=[]for i in range(0,len(students)):
marks.append(random.randint(0, 101))
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("CLASS RECORDS")
plt.plot(students, marks, color = 'green',
linestyle = 'solid', marker = 'o',
markerfacecolor = 'red', markersize = 12)
plt.savefig('plt5.jpg')
plt.show()

#BAR PLOTS

plt.bar(x, height, width, bottom, align)Code 1:
import numpy as np
import matplotlib.pyplot as plt
# creating the dataset
data = {'C':20, 'C++':15, 'Java':30,
'Python':35}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 5))
# creating the bar plot
plt.bar(courses, values, color ='maroon',
width = 0.4)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.savefig('plt6.jpg')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
# set height of bar
IT = [12, 30, 1, 8, 22]
ECE = [28, 6, 16, 5, 10]
CSE = [29, 3, 24, 25, 17]
# Set position of bar on X axis
br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]# Make the plot
plt.bar(br1, IT, color ='r', width = barWidth,
edgecolor ='grey', label ='IT')
plt.bar(br2, ECE, color ='g', width = barWidth,
edgecolor ='grey', label ='ECE')
plt.bar(br3, CSE, color ='b', width = barWidth,
edgecolor ='grey', label ='CSE')
# Adding Xticks
plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(IT))],
['2015', '2016', '2017', '2018', '2019'])
plt.legend()
plt.savefig('plt7.jpg')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
N = 5
boys = (20, 35, 30, 35, 27)
girls = (25, 32, 34, 20, 25)
boyStd = (2, 3, 4, 1, 2)
girlStd = (3, 5, 2, 3, 3)
ind = np.arange(N)
width = 0.35
fig = plt.subplots(figsize =(10, 7))
p1 = plt.bar(ind, boys, width, yerr = boyStd)
p2 = plt.bar(ind, girls, width,
bottom = boys, yerr = girlStd)
plt.ylabel('Contribution')
plt.title('Contribution by the teams')
plt.xticks(ind, ('T1', 'T2', 'T3', 'T4', 'T5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('boys', 'girls'))
plt.savefig('plt8.jpg')
plt.show()


#ERROR PLOTS

import numpy as np
import matplotlib.pyplot as plt
# example dataxval = np.arange(0.1, 4, 0.5)
yval = np.exp(-xval)
plt.errorbar(xval, yval, xerr = 0.4, yerr = 0.5)
plt.title('matplotlib.pyplot.errorbar() function Example')
plt.savefig('plt9.jpg')
plt.show()

#SCATTER PLOTS

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
# Creating dataset
z = np.random.randint(100, size =(50))
x = np.random.randint(80, size =(50))
y = np.random.randint(60, size =(50))
# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
# Creating plot
ax.scatter3D(x, y, z, color = "green")
plt.title("simple 3D scatter plot")
# show plot
plt.savefig('plt10.jpg')
plt.show()


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
# Creating dataset
z = 4 * np.tan(np.random.randint(10, size =(500))) + np.random.randint(100, size
=(500))
x = 4 * np.cos(z) + np.random.normal(size = 500)
y = 4 * np.sin(z) + 4 * np.random.normal(size = 500)
# Creating figure
fig = plt.figure(figsize = (16, 9))
ax = plt.axes(projection ="3d")
# Add x, y gridlines
ax.grid(b = True, color ='grey',
linestyle ='-.', linewidth = 0.3,
alpha = 0.2)# Creating color map
my_cmap = plt.get_cmap('hsv')
# Creating plot
sctt = ax.scatter3D(x, y, z,
alpha = 0.8,
c = (x + y + z),
cmap = my_cmap,
marker ='^')
plt.title("simple 3D scatter plot")
ax.set_xlabel('X-axis', fontweight ='bold')
ax.set_ylabel('Y-axis', fontweight ='bold')
ax.set_zlabel('Z-axis', fontweight ='bold')
fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)
# show plot
plt.savefig('plt11.jpg')
plt.show()


#KDE PLOTS

import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(500)
res = sn.kdeplot(data, color='orange', shade='True')
plt.show()

#HEAT MAPS

import seaborn as snimport matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(500)
res = sn.kdeplot(data, color='orange', shade='True')
plt.show()


#BOX PLOTS

import matplotlib.pyplot as plt
import numpy as np
# Creating dataset
np.random.seed(10)
data = np.random.normal(100, 20, 200)
fig = plt.figure(figsize =(10, 7))
# Creating plot
plt.boxplot(data)
# show plot
plt.savefig('plt14.jpg')
plt.show()


# PIE CHART

from matplotlib import pyplot as plt
import numpy as np
# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
'TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]
# Creating plot
fig = plt.figure(figsize =(10, 7))plt.pie(data, labels = cars)
# show plot
plt.savefig('plt15.jpg')
plt.show()


# HISTOGRAM

from matplotlib import pyplot as plt
import numpy as np
# Creating dataset
a = np.array([22, 87, 5, 43, 56,73, 55, 54, 11,
20, 51, 5, 79, 31,
27])
# Creating histogram
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(a, bins = [0, 25, 50, 75, 100])
# show plot
plt.savefig('plt16.jpg')
plt.show()



