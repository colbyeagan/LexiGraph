import matplotlib.pyplot as plt

dyslexia_friendly_settings = {
    'font.family': 'Arial',
    'font.size': 14,
    'font.style': 'normal',  
    'axes.labelsize': 12,    
    'axes.titlesize': 16,    
    'axes.titleweight': 'bold',
    'axes.titlepad': 20,     
    'axes.labelweight': 'bold',
    'xtick.labelsize': 12,   
    'ytick.labelsize': 12,   
    'legend.fontsize': 12,   
    'lines.linewidth': 2,    
    'lines.markersize': 8,   
    'legend.title_fontsize': 12,
    'axes.labelcolor': 'black',  
    'text.color': 'black',  
    'axes.edgecolor': 'black',  
    'axes.facecolor': 'white',  
    'axes.grid': True,      
    'axes.grid.axis': 'both',  
    'grid.color': 'gray',   
    'grid.linestyle': '--',  
    'grid.linewidth': 0.5   
}

plt.rcParams.update(dyslexia_friendly_settings)

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]

plt.plot(x, y)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Dyslexia-Friendly Line Plot')

plt.legend(['Line 1'])
plt.show()
