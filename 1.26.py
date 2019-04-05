from plot_tools.dotplot import dotplot
import pandas as pd
import pathlib

font     = 'Serif'
title    = 'Violent Crime on College Campuses in Florida, 2012'
source   = 'Source: The FBI web site'
filename = pathlib.Path(__file__)

df = pd.read_csv(filename.with_suffix('.csv'), index_col=0)
data = df['crimes']

plt = dotplot(list(range(16)), df['crimes'])
plt.xticks(list(range(16)), labels=df['school'], fontname=font,
        color='cyan', rotation=33)
plt.yticks(list(range(31)), labels=list(range(1, 32)), 
        fontname=font, color='darkcyan')
plt.suptitle(title, fontsize=15, fontname=font, color='cyan')
plt.title(source, fontsize=8, fontname=font, color='darkcyan')
plt.ylabel('Number of Crimes', fontsize=10, fontname=font, color='purple')

plt.gcf().set_size_inches(13, 7)

ax = plt.axes()
ax.figure.set_facecolor('black')
ax.set_facecolor('black')
plt.grid(color='purple', alpha=0.4)

plt.savefig(filename.with_suffix('.jpg'), facecolor=plt.axes().figure.get_facecolor())
plt.show()
