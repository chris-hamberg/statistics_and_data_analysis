from plot_tools.dotplot import dotplot
import pandas as pd
import numpy as np
import pathlib


#NOTE Plot Info Configuration
font     = 'Serif'
title    = 'Food Safety Analysis for School Cafeterias'
source   = ('Source: "Making the Grade: An Analysis of Food Safety in School Cafeterias"'
           '\n(cspi.us/new/pdf/makingthegrade.pdf, 2007)')
filename = pathlib.Path(__file__)
xlabel   = 'Score'
ylabel   = 'Number of Cafeterias (out of 20)'
skip     = 0

#NOTE Data Configuration
df = pd.read_csv(filename.with_suffix('.csv'))
x_col = 'score'
y_col = 'count'
x_len = 7
y_len = 8


#NOTE Color Configuration
background = 'white'
spines     = 'white'
special    = spines # Bottom and left edges
# --- Text Colors
bold       = 'black'
trim       = '#888888'
t_txt      = trim
src_txt    = 'black'
labels     = 'black'
# --- Grid Colors
grid       = 'white'
alpha      = 0.0
# --- Dotplot Colors
dcolor     = 'lightskyblue'   # dot color
dsize      = 10      # dot size
ecolor     = dcolor  # border color
ewidth     = 1       # border width


#NOTE Geometry Configuration
x_rotation = 0
x_size     = 7
y_size     = 6
y_ticks    = False
x_ticks    = False


################################################################## Make the plot
def xlabels(skip=0):
    '''
    Skip some x-axis labels
    '''
    labels = []
    for label in range(0, 46):
        try:
            if not label%skip:
                labels.append(label)
            else:
                labels.append(None)
        except ZeroDivisionError: 
            labels.append(label)
    return labels
        


plt = dotplot(df[x_col], df[y_col], dcolor, dsize, ecolor, ewidth)
plt.xticks(list(range(x_len)), 
        ['30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100'], 
        fontname=font, color=trim, rotation=x_rotation)
plt.yticks(list(range(y_len)), list(range(1, y_len+1)), 
        fontname=font, color=trim)
plt.suptitle(title, wrap=True, fontsize=15, fontname=font, color=t_txt)
plt.title(source, wrap=True, fontsize=8, fontname=font, color=src_txt)
plt.ylabel(ylabel, fontsize=10, fontname=font, color=labels)
plt.xlabel(xlabel, fontsize=10, fontname=font, 
        color=labels)
plt.gcf().set_size_inches(x_size, y_size)
plt.grid(color=grid, alpha=alpha)


ax = plt.axes()
ax.figure.set_facecolor(background)
ax.set_facecolor(background)
for position in ['bottom', 'left']:
    ax.spines[position].set_color(spines)
for position in ['top', 'right']:
    ax.spines[position].set_color(special)
ax.tick_params(top=False, bottom=x_ticks, left=y_ticks, right=False,
        labelleft=True, labelbottom=True)


plt.savefig(filename.with_suffix('.jpg'), 
        facecolor=plt.axes().figure.get_facecolor())
plt.show()
