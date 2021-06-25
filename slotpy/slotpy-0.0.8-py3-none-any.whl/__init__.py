from .buildgui import Ourcoolapp
from .dataframe import DataFrame
from .plotter import Plotter
import tkinter as tk
import requests
import os

if not os.path.exists('slotpy/pictures/histogram.png'):
    print('Downloading files...')
    response = requests.get('https://raw.githubusercontent.com/Chia-vie/slotpy/main/slotpy/pictures/histogram.png')
    histogram=open('slotpy/pictures/histogram.png','wb')
    histogram.write(response.content)
    response = requests.get('https://raw.githubusercontent.com/Chia-vie/slotpy/main/slotpy/pictures/laurasplot.png')
    laurasplot=open('slotpy/pictures/laurasplot.png','wb')
    laurasplot.write(response.content)
    response = requests.get('https://raw.githubusercontent.com/Chia-vie/slotpy/main/slotpy/pictures/surprise.png')
    surprise=open('slotpy/pictures/surprise.png','wb')
    surprise.write(response.content)
    response = requests.get('https://raw.githubusercontent.com/Chia-vie/slotpy/main/slotpy_logo.png')
    logo=open('slotpy/pictures/slotpy_logo.png','wb')
    logo.write(response.content)
    print('Finished download')

print('Welcome, to slotpy!\n'
      'I am starting the GUI for you.\n'
      'Enjoy your slotpy session!')

# Create tkinter window
window = tk.Tk()
# Call Ourcoolapp
Ourcoolapp(window)
# Let the window loop
window.mainloop()
