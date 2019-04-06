from plot_tools.dotplot import dotplot
import pandas as pd
import pathlib

font     = 'Serif'
title    = 'Beach Water Quality (Other)'
source   = 'Source: Testing the Waters 2009 (www.nrdc.org)'
filename = pathlib.Path(__file__)
color    = 'royalblue'

def xlabels():
    labels = []
    for label in range(0, 46):
        if not label%5:
            labels.append(label)
        else:
            labels.append(None)
    return labels

df = pd.read_csv(filename.with_suffix('.csv'))

plt = dotplot(df['%'], df['freq'])
plt.xticks(list(range(46)), labels=xlabels(), fontname=font,
        color='black', rotation=0)
plt.yticks(list(range(10)), labels=list(range(1, 11)), 
        fontname=font, color='black')
plt.suptitle(title, fontsize=15, fontname=font, color='darkblue')
plt.title(source, fontsize=8, fontname=font, color='black')
plt.ylabel('Number of Beaches', fontsize=10, fontname=font, color='darkblue')
plt.xlabel('Percentage of Failed Tests', fontsize=10, fontname=font, 
        color='darkblue')

plt.gcf().set_size_inches(10, 4.5)
plt.grid(color='black', alpha=0.1)

ax = plt.axes()
ax.figure.set_facecolor('royalblue')
ax.set_facecolor('royalblue')
for position in ['bottom', 'left']:
    ax.spines[position].set_color(color)
for position in ['top', 'right']:
    ax.spines[position].set_color(color)
ax.tick_params(top=False, bottom=False, left=False, right=False,
        labelleft=True, labelbottom=True)

plt.savefig(filename.with_suffix('.jpg'), facecolor=plt.axes().figure.get_facecolor())
plt.show()
