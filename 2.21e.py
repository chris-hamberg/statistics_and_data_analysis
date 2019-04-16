from plot_tools.dotplot import dotplot
import pandas as pd
import numpy as np
import pathlib


#NOTE Plot Info Configuration
font     = 'Serif'
title    = 'Word Count Simple Random Sample'
source   = 'Source: Proprietary'
filename = pathlib.Path(__file__)
xlabel   = 'Word Count'
ylabel   = 'Number of Pages'
skip     = 1
xmax     = 8

#NOTE Data Configuration
df = pd.read_csv(filename.with_suffix('.csv'))
x_col = 'count'
y_col = 'pages'
x_len = 8
y_len = 5


#NOTE Color Configuration
background = 'black'
spines     = 'black'
special    = spines # Bottom and left edges
# --- Text Colors
bold       = 'darkgrey'
trim       = 'grey'
# --- Grid Colors
grid       = 'black'
alpha      = 0.0
# --- Dotplot Colors
dcolor     = 'cyan'   # dot color
dsize      = 10      # dot size
ecolor     = 'cyan' # border color
ewidth     = 1       # border width


#NOTE Geometry Configuration
x_rotation = 0
x_size     = 7
y_size     = 6
y_ticks    = True
x_ticks    = True


################################################################## Make the plot
def xlabels(skip=0):
    '''
    Skip some x-axis labels
    '''
    labels = []
    for label in range(0, xmax):
        try:
            if not label%skip:
                labels.append(str(label))
            else:
                continue
                #labels.append(None)
        except ZeroDivisionError: 
            labels.append(str(label))
    return labels
        


plt = dotplot(df[x_col], df[y_col], dcolor, dsize, ecolor, ewidth)
locs, labels = plt.xticks()
plt.xticks(locs,
        [None, '100', '200', '300', '400', '500', '600', '700', '800'],
        fontname=font,
        color=trim, rotation=x_rotation)
plt.yticks(list(range(y_len)), list(range(1, y_len+1)), 
        fontname=font, color=trim)
plt.suptitle(title, fontsize=15, fontname=font, color=bold)
plt.title(source, fontsize=8, fontname=font, color=trim)
plt.ylabel(ylabel, fontsize=10, fontname=font, color=bold)
plt.xlabel(xlabel, fontsize=10, fontname=font, 
        color=bold)
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


#plt.savefig(filename.with_suffix('.jpg'), 
#        facecolor=plt.axes().figure.get_facecolor())
plt.show()
