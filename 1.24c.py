import matplotlib.pyplot as plt
import numpy as np
import pathlib

font   = 'Serif'
title  = ('Water Quality Rating for Beaches '
          '\nSan Francisico County (dry weather)')
source = 'Source: Heal the Bay Beach Report Card, May 2009'
filename = pathlib.Path(__file__).with_suffix('.jpg')

data = [1/14, 9/14, 3/14, 0/14, 0/14, 1/14]
categories = ['A+', 'A', 'B', 'C', 'D', 'F']
positions = np.arange(len(categories))
#NOTE percentage conversion
data = list(map(lambda y: round(100 * y, 1), data))

ax = plt.axes()
# set background color
ax.patch.set_facecolor('black')
ax.figure.set_facecolor('black')
# set z-value for grid
ax.set_axisbelow(True)

plt.bar(positions, data, align='center', color='royalblue', 
        edgecolor='white', linewidth=0)
plt.xticks(positions, categories, fontsize=10, fontname=font, rotation=0, 
        color='cyan')
plt.ylabel('Percentage of Beaches', fontsize=10, fontname=font, 
        color='darkcyan')
plt.yticks(color='cyan')
plt.suptitle(title, fontsize=14, fontname=font, color='cyan')
plt.grid(color='grey', alpha=0.1)

ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['right'].set_color('black')
ax.tick_params(top=False, bottom=False, left=True, right=False, 
        labelleft=True, labelbottom=True)
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontname=font, fontsize=8,
        color='darkcyan')
plt.gcf().set_size_inches(7, 6)

plt.savefig(filename, facecolor=ax.figure.get_facecolor())
plt.show()
