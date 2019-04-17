import matplotlib.pyplot as plt
import numpy as np
import pathlib


#NOTE Plot Info Configuration
font     = 'Serif'
title    = 'College Students Who Would Like to Get All Textbooks\nin Digital Form'
source   = 'Source: The Chronicle of Higher Education, August 23, 2013'
ylabel   = 'Percentage'
filename = pathlib.Path(__file__).with_suffix('.jpg')


#NOTE Data Configuration
data       = [21.3, 29.2, 25.0, 13.2, 11.3]
legend     = ['Strongly Disagree', 'Disagree', 'Agree', 'Strongly Agree', 
        'Don\'t Know/No response']


# NOTE Color Configuration
background = '#EEEEEE'
spines     = '#EEEEEE'
special    = spines # Bottom and left spines
# --- text colors
bold       = 'black'
trim       = '#444444'
# --- bar colors
bars       = 'red'
edges      = 'black'
width      = 1
# --- grid colors
grid       = 'white'
alpha      = 0.1


#NOTE Geometry Configuration
x_rotation = 0
x_size     = 7
y_size     = 6
y_ticks    = False
x_ticks    = False


################################################################## Make the plot
plt.gcf().set_size_inches(x_size, y_size)


bottom = []
for datum, color in zip(data, ['#003322', '#117766', '#228888', '#33BBCC', '#55EEFF']):
    plt.bar(0, np.array([datum]), bottom=sum(bottom), color=color, linewidth=width)
    bottom.append(np.array([datum]))


plt.xticks([], []) 
plt.ylabel(ylabel, fontsize=10, fontname=font, color=bold)
plt.yticks(color=trim)
plt.suptitle(title, wrap=True, fontsize=14, fontname=font, color=bold)
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontname=font, fontsize=8,
        color=trim)
plt.grid(color=grid, alpha=alpha)
plt.legend(legend)

ax = plt.axes()
ax.patch.set_facecolor(background)
ax.figure.set_facecolor(background)
ax.set_axisbelow(True)
for position in ['top', 'right']:
    ax.spines[position].set_color(spines)
for position in ['bottom', 'left']:
    ax.spines[position].set_color(special)
ax.tick_params(top=False, bottom=False, left=y_ticks, right=x_ticks, 
        labelleft=True, labelbottom=True)


plt.savefig(filename, facecolor=ax.figure.get_facecolor())
plt.show()
