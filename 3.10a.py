import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pathlib


#NOTE Plot Info Configuration
font     = 'Serif'
title    = ('College Students Who Would Like to Get All Textbooks '
            'in Digital Form\n(2011/2012 Comparative Analysis)')
source   = 'Source: The Chronicle of Higher Education, August 23, 2013'
ylabel   = 'Percentage'
filename = pathlib.Path(__file__).with_suffix('.jpg')


#NOTE Data Configuration
data_2011   = [21.3, 29.2, 25.0, 13.2, 11.3]
data_2012   = [19.1, 27.5, 26.3, 16.0, 11.1]
categories = ['Strongly Disgree', 'Disgree', 'Agree', 'Strongly Agree', 
        'Don\'t Know/No response']
positions  = np.arange(len(categories))


# NOTE Color Configuration
background = '#222222'
spines     = 'darkcyan'
special    = spines # Bottom and left spines
# --- text colors
bold       = 'lightcyan'
t_txt      = bold
src_txt    = 'lightcyan'
trim       = 'cyan'
labels     = bold
# --- bar colors
mbars      = 'purple'
wbars      = 'seagreen'
edges      = 'cyan'
medges     = 'purple'
wedges     = 'seagreen'
width      = 0
# --- grid colors
grid       = 'black'
alpha      = 0


#NOTE Geometry Configuration
x_rotation = 15
x_size     = 10
y_size     = 8
y_ticks    = False
x_ticks    = False


################################################################## Make the plot
plt.gcf().set_size_inches(x_size, y_size)
plt.bar(positions, data_2011, width=-0.3, align='edge', color=mbars, 
        edgecolor=medges, linewidth=width, alpha=0.66)
plt.bar(positions, data_2012, width=0.3, align='edge', color=wbars,
        edgecolor=wedges, linewidth=width, alpha=0.66)
plt.xticks(positions, categories, fontsize=10, fontname=font, 
        rotation=x_rotation, color=bold)
plt.ylabel(ylabel, fontsize=10, fontname=font, 
        color=labels, alpha=1)
plt.yticks(color=trim, alpha=0.66)
plt.suptitle(title, fontsize=14, fontname=font, color=t_txt)
plt.title(source, fontsize=8, fontname=font, color=src_txt, alpha=0.8)
#plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontname=font, fontsize=8,
#        color=src_txt)
plt.grid(color=grid, alpha=alpha)
legend = plt.legend(['2011', '2012'])
legend.get_frame().set_color('black')
for text in legend.get_texts():
    text.set_color('lightcyan')

 
ax = plt.axes()
ax.patch.set_facecolor('#CCCCCC')
ax.figure.set_facecolor(background)
ax.set_axisbelow(True)
for position in ['top', 'right']:
    ax.spines[position].set_color(spines)
    ax.spines[position].set_linewidth(3)
for position in ['bottom', 'left']:
    ax.spines[position].set_color(special)
    ax.spines[position].set_linewidth(3)
ax.tick_params(top=False, bottom=False, left=y_ticks, right=x_ticks, 
        labelleft=True, labelbottom=True)


plt.savefig(filename, facecolor=ax.figure.get_facecolor())
plt.show()
