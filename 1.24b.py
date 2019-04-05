import matplotlib.pyplot as plt
import numpy as np
import pathlib

font   = 'Serif'
title  = ('Water Quality Rating for Beaches '
          '\nSan Francisico County (wet weather)')
source = 'Source: Heal the Bay Beach Report Card, May 2009'
filename = pathlib.Path(__file__).with_suffix('.jpg')

data = [4/14, 2/14, 2/14, 2/14, 1/14, 2/14]
categories = ['A+', 'A', 'B', 'C', 'D', 'F']
positions = np.arange(len(categories))
#NOTE percentage conversion
data = list(map(lambda y: round(100 * y, 1), data))

ax = plt.axes()
# set background color
ax.patch.set_facecolor('lightblue')
ax.figure.set_facecolor('lightblue')
# set z-value for grid
ax.set_axisbelow(True)

plt.bar(positions, data, align='center', color='lightblue', 
        edgecolor='black', linewidth=0.33)
plt.xticks(positions, categories, fontsize=10, fontname=font, rotation=0, 
        color='darkcyan')
plt.ylabel('Percentage of Beaches', fontsize=10, fontname=font, 
        color='black')
plt.yticks(color='darkcyan')
plt.suptitle(title, fontsize=14, fontname=font, color='black')

ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('lightblue')
ax.spines['left'].set_color('lightblue')
ax.spines['right'].set_color('lightblue')
ax.tick_params(top=False, bottom=False, left=True, right=False, 
        labelleft=True, labelbottom=True)
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontname=font, fontsize=8,
        color='black')
plt.gcf().set_size_inches(7, 6)

plt.savefig(filename, facecolor=ax.figure.get_facecolor())
plt.show()
