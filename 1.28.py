import matplotlib.pyplot as plt
import numpy as np
import pathlib

font   = 'Serif'
title  = ('Student Debt for an AA Degree \nPublic Community Colleges, 2008')
source = ('Source: "Trends in Education 2010: Community Colleges"'
          ' (www.collegeboard.com/trends)')
filename = pathlib.Path(__file__).with_suffix('.jpg')

data = [0.62, 0.23, 0.10, 0.05]
categories = ['None', '< $10,000', '$10,000 to 20,000', '> $20,000']
positions = np.arange(len(categories))
#NOTE percentage conversion
data = list(map(lambda y: round(100 * y, 1), data))

ax = plt.axes()

plt.bar(positions, data, align='center', color='white', 
        edgecolor='blue', linewidth=.33)
plt.xticks(positions, categories, fontsize=10, fontname=font, rotation=5, 
        color='darkcyan')
plt.ylabel('Percentage of Students', fontsize=10, fontname=font, 
        color='darkcyan')
plt.yticks(color='cyan')
plt.suptitle(title, fontsize=14, fontname=font, color='darkcyan')

ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.tick_params(top=False, bottom=False, left=False, right=False, 
        labelleft=True, labelbottom=True)
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontname=font, fontsize=8,
        color='black')
plt.gcf().set_size_inches(9, 6)

plt.savefig(filename, facecolor=ax.figure.get_facecolor())
plt.show()
