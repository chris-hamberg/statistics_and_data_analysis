import matplotlib.pyplot as plt
import numpy as np
import pathlib

font     = 'Serif'
title    = 'How Often People Get Sleepy at Work' 
source   = ('Source: "Americans Drowsy on the Job and the Road"'
            '(Associated Press, March 28, 2001)')
filename = pathlib.Path(__file__)

data = [31, 40, 22, 7]
categories = ['Never', 'Monthly', 'Weekly', 'Daily']
positions = np.arange(len(categories))

ax = plt.axes()
# set background color
ax.patch.set_facecolor('grey')
ax.figure.set_facecolor('grey')
# set z-value for grid
ax.set_axisbelow(True)

plt.bar(positions, data, align='center', color='lime', edgecolor='lime', 
        linewidth='3')
plt.xticks(positions, categories, color='yellow', fontsize=10, 
        fontname=font, rotation=0)
plt.ylabel('Percentage of Respondents', color='lime', fontsize=10, 
        fontname=font)
plt.yticks(color='yellow')
plt.suptitle(title, color='lime', fontsize=14, fontname=font)
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontsize=8, 
            color='black', fontname=font)

for position in ['bottom', 'top', 'left', 'right']:
    ax.spines[position].set_color('grey')
ax.tick_params(top=False, bottom=False, left=False, right=False,
        labelleft=True, labelbottom=True)

plt.gcf().set_size_inches(7, 6)

plt.savefig(filename.with_suffix('.jpg'), facecolor=ax.figure.get_facecolor())
plt.show()
