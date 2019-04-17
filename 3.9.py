import matplotlib.pyplot as plt
import numpy as np
import pathlib


#NOTE Plot Info Configuration
font     = 'Serif'
title    = 'How Often Adults Swear in Conversations'
source   = 'Source: "Rinse Out Your Mouth" (Associated Press, March 29, 2006)'
ylabel   = 'Cumulative Percentage'
filename = pathlib.Path(__file__).with_suffix('.jpg')


#NOTE Data Configuration
data       = [46, 32, 21]
legend     = ['Weekly', 'Monthly', 'Never']


# NOTE Color Configuration
background = '#CCDCDD'
spines     = background
special    = spines # Bottom and left spines
# --- text colors
bold       = '#112122'
trim       = '#778788'
# --- bar colors
bars       = 'red'
edges      = 'black'
width      = 1
# --- grid colors
grid       = 'white'
alpha      = 0.1


#NOTE Geometry Configuration
x_rotation = 0
x_size     = 7
y_size     = 6
y_ticks    = False
x_ticks    = False


################################################################## Make the plot
plt.gcf().set_size_inches(x_size, y_size)


bottom = []
for datum, color in zip(data, ['skyblue', 'royalblue', 'cyan']):
    plt.bar(0, np.array([datum]), bottom=sum(bottom), color=color, 
            linewidth=width, alpha=0.66)
    bottom.append(np.array([datum]))


plt.xticks([], []) 
plt.ylabel(ylabel, fontsize=10, fontname=font, color=bold)
plt.yticks(color=trim)
plt.suptitle(title, wrap=True, fontsize=14, fontname=font, color=bold)
plt.title(source, wrap=True, fontname=font, fontsize=8, color=bold)
plt.grid(color=grid, alpha=alpha)
plt.legend(legend)

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
