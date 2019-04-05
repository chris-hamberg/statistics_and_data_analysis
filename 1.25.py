import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pathlib

font   = 'Serif'
title  = ('Percentage of Wireless Phone Only Households \n(with no landline)')
source = 'Source: Going Wireless (AARP Bulletin, June 2009)'
filename = pathlib.Path(__file__).with_suffix('.jpg')

ax = plt.axes()
ax.figure.set_facecolor('black')

def draw_subplot(n, frame, subtitle):
    
    percentage = frame['%']
    states = frame['state']
    positions = np.arange(len(states))
    
    ax = plt.subplot(3, 1, n+1)
    ax.patch.set_facecolor('black')
    ax.spines['bottom'].set_color(color_scheme[n][2])

    plt.bar(positions, percentage, align='center', color='black',
            edgecolor=color_scheme[n][1], linewidth=1)
    plt.xticks(positions, states, fontsize=10, fontname=font, 
            color=color_scheme[n][0])
    plt.ylabel('% Wireless', fontsize=10, fontname=font, 
            color=color_scheme[n][1])
    plt.yticks(color=color_scheme[n][0])
    plt.title(subtitle, fontsize=10, fontname=font, color=color_scheme[n][0], 
            loc='right')

df = pd.read_csv('1.25.csv', index_col=0)

frames = [
        df.loc[df['region'] == 'W'].sort_values(by=['%']),
        df.loc[df['region'] == 'M'].sort_values(by=['%']),
        df.loc[df['region'] == 'E'].sort_values(by=['%'])
          ]

color_scheme = {
        0: ['lightblue', 'lightblue', 'lightblue'],
        1: ['lightgreen', 'lightgreen', 'lightgreen'],
        2: ['magenta', 'magenta', 'magenta']
        }

# draw plots
for (n, frame), subtitle in zip(enumerate(frames), 
        ['Region: WEST', 'Region: MID', 'Region: EAST']):
    draw_subplot(n, frame, subtitle)

plt.subplots_adjust(hspace=0.75)
plt.suptitle(title, fontsize=15, fontname=font, color='grey')
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontname=font, fontsize=8,
        color='grey')
plt.gcf().set_size_inches(10, 7)

plt.savefig(filename, facecolor=ax.figure.get_facecolor())
plt.show()
