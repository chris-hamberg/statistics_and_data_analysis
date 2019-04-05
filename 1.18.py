import matplotlib.pyplot as plt
import numpy as np

font = 'Serif'
caption = ('Findings from the 2008 Administration of the College Senior Survey\n'
          '(Higher Education Research Institute, UCLA, June 2009)')

data = [0.447, 0.373, 0.134, 0.046]
categories = ['Definitely Yes', 'Probably Yes', 'Probably No', 'Definitely No']
positions = np.arange(len(categories))
data = list(map(lambda y: round(100 * y, 1), data))

ax = plt.axes()
# set background color
ax.patch.set_facecolor('grey')
# set z-value for grid
ax.set_axisbelow(True)

plt.bar(positions, data, align='center', color='black', edgecolor='white')
plt.xticks(positions, categories, fontsize=10, fontname=font)
plt.ylabel('Percentage of Students', fontsize=10, fontname=font)
plt.title('Students Who Would Choose to Re-enroll \nat Their Current College', 
           fontsize=14, fontname=font)
plt.grid(color='lightgrey')
plt.figtext(.5, 0.01, caption, wrap=True, ha='center', fontsize=8, 
            fontname=font)
plt.gcf().set_size_inches(7, 6)

plt.savefig('1.18.jpg')
plt.show()
