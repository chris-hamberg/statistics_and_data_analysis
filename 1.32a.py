from plot_tools.dotplot import dotplot
import pandas as pd
import pathlib

font     = 'Serif'
title    = 'Beach Water Quality'
source   = 'Source: Testing the Waters 2009 (www.nrdc.org)'
filename = pathlib.Path(__file__)
color    = 'lightgreen'

def xlabels():
    labels = []
    for label in range(0, 46):
        if label is 0:
            labels.append(None)
        elif not label%5:
            labels.append(label)
        else:
            labels.append(None)
    return labels

df = pd.read_csv(filename.with_suffix('.csv'))

plt = dotplot(df['%'], df['freq'])
plt.xticks(list(range(46)), labels=xlabels(), fontname=font,
        color='green', rotation=0)
plt.yticks(list(range(4)), labels=list(range(1, 5)), 
        fontname=font, color='green')
plt.suptitle(title, fontsize=15, fontname=font, color='lightgreen')
plt.title(source, fontsize=8, fontname=font, color='green')
plt.ylabel('Number of Beaches', fontsize=10, fontname=font, color='lightgreen')
plt.xlabel('Percentage of Failed Tests', fontsize=10, fontname=font, 
        color='lightgreen')

plt.gcf().set_size_inches(10, 4.5)

ax = plt.axes()
ax.figure.set_facecolor('#111111')
ax.set_facecolor('#111111')
for position in ['bottom', 'left']:
    ax.spines[position].set_color(color)
for position in ['top', 'right']:
    ax.spines[position].set_color('#111111')

plt.savefig(filename.with_suffix('.jpg'), facecolor=plt.axes().figure.get_facecolor())
plt.show()
