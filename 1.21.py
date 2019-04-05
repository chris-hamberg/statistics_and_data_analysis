import matplotlib.pyplot as plt
import numpy as np

font   = 'Serif'
source = 'Source: Grant MacEwan College Early Leaver Survey Report, 2004'
filename = '1.21.jpg'

data = [19, 12, 8, 6, 4, 2, 2, 10]
categories = [
        'Financial', 
        'Health', 
        'Employment', 
        'Family', 
        'Break',
        'Moving',
        'Travel',
        'Other'
        ]
positions = np.arange(len(categories))
#data = list(map(lambda y: round(100 * y, 1), data))

ax = plt.axes()
# set background color
ax.patch.set_facecolor('black')
ax.figure.set_facecolor('black')
# set z-value for grid
ax.set_axisbelow(True)

plt.bar(positions, data, align='center', color='black', edgecolor='cyan',
        linewidth=3)
plt.xticks(positions, categories, fontsize=10, fontname=font, rotation=25, 
        color='lightcyan')
plt.ylabel('Frequency of Students', fontsize=10, fontname=font, color='darkcyan')
plt.yticks(color='darkcyan')
plt.suptitle('Reasons for Leaving College Prior to Graduation', 
           fontsize=14, fontname=font, color='lightcyan')
plt.title(source, fontsize=8, fontname=font, color='darkcyan')
#plt.axes().spines['bottom'].set_color('grey')
plt.gcf().set_size_inches(7, 6)

plt.savefig(filename, facecolor=plt.axes().figure.get_facecolor())
plt.show()
