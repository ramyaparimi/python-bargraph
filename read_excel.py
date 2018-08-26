import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd

data = pd.read_excel('/Users/adityaramya/Projects/ramya-projects/PythonForDataScience/BarGraphPython/for_graph.xlsx')


dict_data = data.to_dict('list')

num_of_private = []
num_of_public = []

for key,value in dict_data.items():
    num_of_private.append(value.count('Private'))
    num_of_public.append(value.count('Public'))

n_groups=len(data.columns)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8


bar_type1 = plt.bar(index, num_of_private, bar_width,
                 alpha=opacity,
                 color='b',
                 label='private')

bar_type2 = plt.bar(index + bar_width, num_of_private, bar_width,
                 alpha=opacity,
                 color='g',
                 label='public')

plt.xlabel('Type')
plt.ylabel('Total Number')
plt.title('Public vs Private')
plt.xticks(index + bar_width, (list(dict_data)))
plt.legend()

plt.tight_layout()
plt.savefig('testgraph.pdf')

plt.show()















