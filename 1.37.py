import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pathlib


#NOTE Plot Info Configuration
font     = 'Serif'
title    = 'Reasons Adolescents Want to be Professional Athletes'
source   = ('Source: "Why Adolescent Boys Dream of Becoming Professional'
            'Athletes" \n(Psychological Reports [1999]: 1075-1085)')
ylabel   = 'Number of Boys'
filename = pathlib.Path(__file__).with_suffix('.jpg')


#NOTE Data Configuration
data       = [94, 56, 29, 27, 24, 19, 19]
categories = ['Fame', 'Money', 'Women', 'Like Sports', 'Easy Life', 
        'No Education', 'Other']
positions  = np.arange(len(categories))


# NOTE Color Configuration
background = 'white'
spines     = 'white'
special    = spines # Bottom and left spines
# --- text colors
bold       = '#333355'
trim       = 'royalblue'
# --- bar colors
bars       = 'lightblue'
edges      = 'lightblue'
width      = 1
# --- grid colors
grid       = 'blue'
alpha      = 0.1


#NOTE Geometry Configuration
x_rotation = 10
x_size     = 9
y_size     = 6
y_ticks    = False
x_ticks    = False


################################################################## Make the plot
plt.gcf().set_size_inches(x_size, y_size)
plt.bar(positions, data, align='center', color=bars, 
        edgecolor=edges, linewidth=width)
plt.xticks(positions, categories, fontsize=10, fontname=font, 
        rotation=x_rotation, color=bold)
plt.ylabel(ylabel, fontsize=10, fontname=font, 
        color=bold)
plt.yticks(color=trim)
plt.suptitle(title, fontsize=14, fontname=font, color=bold)
#plt.title(source, fontsize=8, fontname=font, color=trim)
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontname=font, fontsize=8,
        color=trim)
plt.grid(color=grid, alpha=alpha)

 
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
