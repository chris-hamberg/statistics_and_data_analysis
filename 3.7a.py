import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np
import pathlib


#NOTE Plot Info Configuration
font     = 'Serif'
title    = 'The Percentage of Women (per country)\nWho Say Their Spouses Never Help with House Work'
source   = 'Source: "Housework Around the World" (USA Today, September 15, 2009)'
ylabel   = ''
filename = pathlib.Path(__file__).with_suffix('.jpg')


#NOTE Data Configuration
data       = [74, 44, 40, 34, 31] # percentages
categories = ['Japan', 'France', 'UK', 'US', 'Canada']
positions  = np.arange(len(categories))


# NOTE Color Configuration
background = '#EEDDCC'
spines     = background
special    = spines # Bottom and left spines
# --- text colors
bold       = 'black'
t_txt      = 'black'
src_txt    = 'black'
trim       = '#777777'
labels     = bold
# --- bar colors
bars       = 'white'
edges      = bars
width      = 1
# --- grid colors
grid       = background
alpha      = 0.1


#NOTE Geometry Configuration
x_rotation = 0
x_size     = 7
y_size     = 6
y_ticks    = False
x_ticks    = False


################################################################## Make the plot
plt.gcf().set_size_inches(x_size, y_size)
plt.bar(positions, data, align='center', color=bars, 
        edgecolor=edges, linewidth=width)
plt.xticks(positions, categories, fontsize=10, fontname=font, 
        rotation=x_rotation, color=labels)
plt.ylabel(ylabel, fontsize=10, fontname=font, 
        color=labels)
plt.yticks(color=trim)
plt.suptitle(title, fontsize=14, fontname=font, color=t_txt)
#plt.title(source, fontsize=8, fontname=font, color=trim)
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontname=font, fontsize=8,
        color=src_txt)
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
