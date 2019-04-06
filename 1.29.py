import matplotlib.pyplot as plt
import numpy as np
import pathlib

font     = 'Serif'
title    = 'Where College Students Buy Textbooks' 
source   = ('Source: "Where College Students Buy Textbooks"'
            '(USA Today, October 14, 2010)')
filename = pathlib.Path(__file__)

data = [576, 48, 240, 168, 36, 12, 72]
categories = ['Campus', 'Campus Web Site', 'Online', 'Bookstore', 'Rented',
        'eBooks', 'No Purchase']
positions = np.arange(len(categories))

ax = plt.axes()
# set background color
ax.patch.set_facecolor('grey')
ax.figure.set_facecolor('black')
# set z-value for grid
ax.set_axisbelow(True)

plt.bar(positions, data, align='center', color='white', edgecolor='black', 
        linewidth='3')
plt.xticks(positions, categories, color='white', fontsize=10, fontname=font,
        rotation=10)
plt.ylabel('y out of 1152 Students', color='white', fontsize=10, fontname=font)
plt.yticks(color='grey')
plt.suptitle(title, color='white', fontsize=14, fontname=font)
plt.grid(color='black')
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontsize=8, 
            color='grey', fontname=font)

ax.tick_params(top=False, bottom=False, left=True, right=False,
        labelleft=True, labelbottom=True)

plt.gcf().set_size_inches(11, 6)

plt.savefig(filename.with_suffix('.jpg'), facecolor=ax.figure.get_facecolor())
plt.show()
