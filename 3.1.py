import matplotlib.pyplot as plt
from math import floor
import pathlib

data = [.18, .55, .27]
labels = ['Toned & Fit', 'A Little Bit\nFlabby', 'Seriously Out\nof Shape']
colors = ['cyan', 'lightcyan', 'skyblue']
title  = 'Financial Physique (opinion poll)'
source = ('Source: "2009 Young Adults & Money, '
          'Survey Findings," Charles Schwab, 2009')
filename = pathlib.Path(__file__)

font       = 'Serif'
rotation   = True
background = '#111111'
title_txt  = 'cyan'
sub_text   = 'royalblue'
minor_txt  = 'darkcyan'

###############################################################################

plt.pie(data, labels=labels, colors=colors, 
        textprops={'fontname': font, 'fontsize': 9, 'color': sub_text},
        autopct=lambda n: str(floor(n))+'%', rotatelabels=rotation)

plt.suptitle(title, fontname=font, fontsize=14, color=title_txt)
plt.title(source, fontname=font, fontsize=8, color=minor_txt)

plt.gcf().set_size_inches(6, 6)
plt.axes().figure.set_facecolor(background)

plt.savefig(filename.with_suffix('.jpg'), 
        facecolor=plt.axes().figure.get_facecolor())

plt.show()
