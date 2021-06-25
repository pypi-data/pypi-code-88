from .buildgui import Ourcoolapp
from .dataframe import DataFrame
from .plotter import Plotter
import tkinter as tk

print('Welcome, to slotpy!\n'
      'I am starting the GUI for you.\n'
      'Enjoy your slotpy session!')

# Create tkinter window
window = tk.Tk()
# Call Ourcoolapp
Ourcoolapp(window)
# Let the window loop
window.mainloop()