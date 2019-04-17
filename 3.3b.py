import matplotlib.pyplot as plt
import numpy as np
import pathlib


#NOTE Plot Info Configuration
font     = 'Serif'
title    = 'Cell Phone Usage at Work'
source   = 'Source: "Whistle - But Don\'t Tweet - While You Work," www.roberthalftechnology.com, October 6, 2009'
ylabel   = 'Cumulative Percentage'
filename = pathlib.Path(__file__).with_suffix('.jpg')


#NOTE Data Configuration
data       = [54, 19, 16, 10, 1]
legend     = ['Prohibited Completely', 'Permitted for Business Purposes Only', 
        'Permitted for Limited Personal Use', 'Permitted for Any Use', 'Don\'t Know/No response']


# NOTE Color Configuration
background = '#111111'
spines     = '#111111'
special    = spines # Bottom and left spines
# --- text colors
bold       = 'cyan'
trim       = 'cyan'
# --- bar colors
bars       = 'red'
edges      = 'black'
width      = 1
# --- grid colors
grid       = 'black'
alpha      = 0.1


#NOTE Geometry Configuration
x_rotation = 0
x_size     = 7
y_size     = 6
y_ticks    = True
x_ticks    = False


################################################################## Make the plot
plt.gcf().set_size_inches(x_size, y_size)


bottom = []
for datum, color in zip(data, ['#001122', '#113366', '#226688', '#3388AA', '#55BBDD']):
    plt.bar(0, np.array([datum]), bottom=sum(bottom), color=color, linewidth=width)
    bottom.append(np.array([datum]))


plt.xticks([], []) 
plt.ylabel(ylabel, fontsize=10, fontname=font, color=bold)
plt.yticks(color=trim)
plt.suptitle(title, fontsize=14, fontname=font, color=bold)
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
