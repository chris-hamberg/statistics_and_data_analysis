from plot_tools.dotplot import dotplot

font = 'Serif'
caption = 'Festing on Protien (AARP Bulletin, Sept. 2009)'

data = {'1 - 1.9':3, 
        '2 - 2.9':5, 
        '3 - 3.9':4, 
        '4 - 4.9':0, 
        '5 - 5.9':6, 
        '6 - 6.9':1}

plt = dotplot([1, 2, 3, 4, 5, 6], list(data.values()))
plt.xticks([1, 2, 3, 4, 5, 6], labels=list(data.keys()), fontname=font)
plt.yticks([0, 1, 2, 3, 4, 5], labels=[1, 2, 3, 4, 5, 6], fontname=font)
plt.title('The Cost of Protien (per gram)', fontsize=14, fontname=font)
plt.xlabel('Cents', fontsize=10, fontname=font)
plt.ylabel('Number of Food Sources', fontsize=10, fontname=font)
plt.figtext(0.5, 0.01, caption, wrap=True, ha='center', fontsize=8, 
        fontname=font)
plt.gcf().set_size_inches(7, 6)
plt.axes().figure.set_facecolor('lightgrey')
plt.grid(color='lightgrey', alpha=0.3)

plt.savefig('1.19.jpg', facecolor=plt.axes().figure.get_facecolor())
plt.show()
