#plotting

import matplotlib.pyplot as py
list_1=[1,6,13,16,24]
list_2=[3,7,17,28,30]

plt.plot(list1,list2,c="blue",linewidth=1,label="A-line!",linestyle="dashed",marker='s',markerfacecolor="purple",markersize=2)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Plot a line")
plot.legend()
plot.show()
