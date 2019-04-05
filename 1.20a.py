from plot_tools.dotplot import dotplot

font     = 'Serif'
title    = '2008 Movie Ticket Sales (in dollars)'
source   = 'Source: Box Office Mojo (www.boxofficemojo.com)'
filename = '1.20a.jpg'

data = {'1'  :9, 
        '1.5':5, 
        '2'  :3, 
        '2.5':0, 
        '3'  :2, 
        '3.5':0, 
        '4'  :0,
        '4.5':0,
        '5'  :1}

plt = dotplot([1, 2, 3, 4, 5, 6, 7, 8, 9], list(data.values()))
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9], labels=list(data.keys()), fontname=font,
        color='green')
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8], labels=[1, 2, 3, 4, 5, 6, 7, 8, 9], 
        fontname=font, color='green')
plt.title(title, fontsize=14, fontname=font, color='lime')
plt.xlabel('Dollars (in millions)', fontsize=10, fontname=font, color='lime')
plt.ylabel('Number of Movies', fontsize=10, fontname=font, color='lime')
plt.figtext(0.5, 0.01, source, wrap=True, ha='center', fontsize=8, 
        fontname=font, color='green')
plt.gcf().set_size_inches(7, 6)
plt.axes().figure.set_facecolor('black')
plt.axes().set_facecolor('black')
plt.axes().spines['bottom'].set_color('lime')
plt.axes().spines['left'].set_color('lime')
#plt.grid(color='lightgrey', alpha=0.3)

plt.savefig(filename, facecolor=plt.axes().figure.get_facecolor())
plt.show()
