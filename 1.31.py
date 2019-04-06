import matplotlib.pyplot as plt
import numpy as np
import pathlib

font     = 'Serif'
title    = 'House Hold Composition' 
source   = ('Source: "Ozzie and Harriet Don\'t Live Here Anymore"'
            ' (San Luis Obispo Tribune, February 26, 2002)')
filename = pathlib.Path(__file__)

data = [29, 29, 27, 15]
categories = ['Non-family', 'Family', 'Married (No Kids)', 'Single Parent']
positions = np.arange(len(categories))

ax = plt.axes()
# set background color
ax.patch.set_facecolor('white')
ax.figure.set_facecolor('white')
# set z-value for grid
ax.set_axisbelow(True)

plt.bar(positions, data, align='center', color='red', edgecolor='red', 
        linewidth='0')
plt.xticks(positions, categories, color='black', fontsize=10, 
        fontname=font, rotation=5)
plt.ylabel('Percentage of Respondents', color='black', fontsize=10, 
        fontname=font)
plt.yticks(color='darkgrey')
plt.suptitle(title, color='black', fontsize=14, fontname=font)
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontsize=8, 
            color='black', fontname=font)

for position in ['top', 'right']:
    ax.spines[position].set_color('white')
ax.tick_params(top=False, bottom=False, left=False, right=False,
        labelleft=True, labelbottom=True)

plt.gcf().set_size_inches(7, 6)

plt.savefig(filename.with_suffix('.jpg'), facecolor=ax.figure.get_facecolor())
plt.show()
