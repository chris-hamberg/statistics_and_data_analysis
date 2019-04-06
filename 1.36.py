from plot_tools.dotplot import dotplot
import pandas as pd
import numpy as np
import pathlib


#NOTE Plot Info Configuration
font     = 'Serif'
title    = 'Top 25 Business Schools\n(percentage of applicants admitted)'
source   = 'Source: U.S News and World Report'
filename = pathlib.Path(__file__)
xlabel   = 'Acceptance Rates'
ylabel   = 'Number of Schools'
skip     = 0

#NOTE Data Configuration
df = pd.read_csv(filename.with_suffix('.csv'))
x_col = '%'
y_col = 'freq'
x_len = 8
y_len = 5


#NOTE Color Configuration
background = '#CCCCCC'
spines     = '#CCCCCC'
special    = spines # Bottom and left edges
# --- Text Colors
bold       = 'black'
trim       = '#555555'
# --- Grid Colors
grid       = 'white'
alpha      = 0.5
# --- Dotplot Colors
dcolor     = '#777777'   # dot color
dsize      = 10      # dot size
ecolor     = '#111111' # border color
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
plt.xticks(list(range(x_len)), labels=df[x_col], fontname=font,
        color=bold, rotation=x_rotation)
plt.yticks(list(range(y_len)), labels=list(range(1, y_len+1)), 
        fontname=font, color=trim)
plt.suptitle(title, fontsize=15, fontname=font, color=bold)
plt.title(source, fontsize=8, fontname=font, color=trim)
plt.ylabel(ylabel, fontsize=10, fontname=font, color=bold)
plt.xlabel(xlabel, fontsize=10, fontname=font, 
        color=trim)
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
