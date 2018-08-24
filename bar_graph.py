import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 12
private = (90, 55, 40, 65, 90, 55, 40, 65, 90, 55, 40, 65)
public = (85, 62, 54, 20, 85, 62, 54, 20, 85, 62, 54, 20)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, private, bar_width,
                 alpha=opacity,
                 color='b',
                 label='private')

rects2 = plt.bar(index + bar_width, public, bar_width,
                 alpha=opacity,
                 color='g',
                 label='public')

plt.xlabel('Type')
plt.ylabel('Total Number')
plt.title('Public vs Private')
plt.xticks(index + bar_width, ('Jan', 'Feb', 'Mar', 'Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec'))
plt.legend()

plt.tight_layout()
plt.show()

