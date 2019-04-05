from plot_tools.dotplot import dotplot

font     = 'Serif'
title    = '2007 Movie Ticket Sales (in dollars)'
source   = 'Source: Box Office Mojo (www.boxofficemojo.com)'
filename = '1.21.jpg'

data = {'1'  :7, 
        '1.5':2, 
        '2'  :5, 
        '2.5':2, 
        '3'  :4}

plt = dotplot([1, 2, 3, 4, 5, 6, 7], list(data.values()))
plt.xticks([1, 2, 3, 4, 5], labels=list(data.keys()), fontname=font,
        color='cyan')
plt.yticks([0, 1, 2, 3, 4, 5, 6], labels=[1, 2, 3, 4, 5, 6, 7], 
        fontname=font, color='cyan')
plt.title(title, fontsize=14, fontname=font, color='lightcyan')
plt.xlabel('Dollars (in millions)', fontsize=10, fontname=font, color='lightcyan')
plt.ylabel('Number of Movies', fontsize=10, fontname=font, color='lightcyan')
plt.figtext(0.5, 0.01, source, wrap=True, ha='center', fontsize=8, 
        fontname=font, color='cyan')
plt.gcf().set_size_inches(7, 6)
plt.axes().figure.set_facecolor('purple')
plt.axes().set_facecolor('purple')
plt.axes().spines['bottom'].set_color('cyan')
plt.axes().spines['left'].set_color('cyan')
plt.axes().spines['top'].set_color('cyan')
plt.axes().spines['right'].set_color('cyan')
plt.axes().tick_params(colors='cyan')
#plt.grid(color='purple', alpha=0.3)

plt.savefig(filename, facecolor=plt.axes().figure.get_facecolor())
plt.show()
