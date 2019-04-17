import matplotlib.pyplot as plt
from math import floor
import pathlib

data = [198, 147.6, 14.4]
labels = ['No', 'Yes', 'No Response']
colors = ['lightskyblue', 'yellow', 'lightcyan']
title  = 'Number of Adults Whom Set Aside a Personal Stash of Halloween Candy'
source = 'Source: USA Today, October 22, 2009'
filename = pathlib.Path(__file__)

font       = 'Serif'
rotation   = False
background = 'white'
title_txt  = 'black'
sub_text   = 'black'
minor_txt  = 'black'

###############################################################################

plt.pie(data, labels=['', '', ''], colors=colors, 
        textprops={'fontname': font, 'fontsize': 9, 'color': sub_text},
        autopct=lambda n: str(floor(n))+'%', rotatelabels=rotation)

plt.title(title, wrap=True, fontname=font, fontsize=14, color=title_txt)
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontname=font, 
        fontsize=8, color=minor_txt)

plt.gcf().set_size_inches(6, 6)
plt.axes().figure.set_facecolor(background)

plt.legend(labels)

plt.savefig(filename.with_suffix('.jpg'), 
        facecolor=plt.axes().figure.get_facecolor())

plt.show()
