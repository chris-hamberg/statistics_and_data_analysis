import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pathlib


#NOTE Plot Info Configuration
font     = 'Serif'
title    = 'Self Perception of Physical Health (College Senior Opinion Poll)\nComparative Analysis'
source   = ('Source: "Findings from the 2009 Administration of the College Senior Survey"\n'
           '(Higher Education Research Institute, 2010)')
ylabel   = 'Percentages'
filename = pathlib.Path(__file__).with_suffix('.jpg')


#NOTE Data Configuration
data_men   = [35.9, 47.1, 16.0, 0.9, 0.1]
data_wom   = [22.7, 53.6, 22.6, 0.7, 0.4]
categories = ['Top 10%', 'Above Average', 'Average', 'Below Average', 
        'Bottom 10%']
positions  = np.arange(len(categories))


# NOTE Color Configuration
background = '#222222'
spines     = background
special    = spines # Bottom and left spines
# --- text colors
bold       = 'lightcyan'
t_txt      = bold
src_txt    = 'cyan'
trim       = 'cyan'
labels     = bold
# --- bar colors
mbars      = 'cyan'
wbars      = 'lightcyan'
edges      = background
medges     = mbars
wedges     = wbars
width      = 0
# --- grid colors
grid       = background
alpha      = 0.1


#NOTE Geometry Configuration
x_rotation = 0
x_size     = 10
y_size     = 8
y_ticks    = False
x_ticks    = False


################################################################## Make the plot
plt.gcf().set_size_inches(x_size, y_size)
plt.bar(positions, data_men, width=-0.3, align='edge', color=mbars, 
        edgecolor=medges, linewidth=width, alpha=0.15)
plt.bar(positions, data_wom, width=0.3, align='edge', color=wbars,
        edgecolor=wedges, linewidth=width, alpha=0.15)
plt.xticks(positions, categories, fontsize=10, fontname=font, 
        rotation=x_rotation, color=bold)
plt.ylabel(ylabel, fontsize=10, fontname=font, 
        color=labels, alpha=0.66)
plt.xlabel('Self Rating of Physical Health', fontsize=10, fontname=font,
        color=trim, alpha=0.3)
plt.yticks(color=trim)
plt.suptitle(title, fontsize=14, fontname=font, color=t_txt)
plt.title(source, fontsize=8, fontname=font, color=src_txt, alpha=0.8)
#plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontname=font, fontsize=8,
#        color=src_txt)
plt.grid(color=grid, alpha=alpha)
legend = plt.legend(['men', 'women'])
legend.get_frame().set_color('black')
for text in legend.get_texts():
    text.set_color('lightcyan')

 
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
