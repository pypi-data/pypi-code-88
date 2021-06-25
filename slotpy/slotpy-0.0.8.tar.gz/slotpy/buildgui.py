# Color schemes
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

import tkinter as tk, numpy as np, os
from tkinter import StringVar, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from .plotter import Plotter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from .dataframe import DataFrame, dummydata, dummydata2

class Ourcoolapp():
    def __init__(self, window):
        self.window = window
        # background color
        self.window.config(bg='pale turquoise')
        # title
        self.window.title('Group-34: Our fabulous App')
        # Variables for the output, currently just a string
        self.out = tk.StringVar()
        self.out.set('')
        self.logmsg = tk.StringVar()
        self.logmsg.set('Please select a dataframe and click on the type of plot you would you like to make')
        # Read in preview images
        self.preview_img_1 = tk.PhotoImage(file='slotpy/pictures/histogram.png')
        self.preview_img_2 = tk.PhotoImage(file='slotpy/pictures/laurasplot.png')
        self.preview_img_3 = tk.PhotoImage(file='slotpy/pictures/surprise.png')
        self.logoimage = tk.PhotoImage(file='slotpy/pictures/slotpy_logo.png')
        self.buttonsandlabels()

        self.file = StringVar

    def pressbutton(self,choice):
        '''This function is called when one
        clicks on one of the image buttons'''
        # check if dataframe was read in
        if hasattr(self, 'df'):
            if choice == "2":
                gui_input = {"title": "plot_type2", "xlim": (0.3, 120), "ylim": (0.5, 18),
                "xyz_cols": ("period", "radius", "core_mass"),
                "fig_size": (600,700)
                 }
                gui_input["slider_cols"] = self.slider_cols
                plot = Plotter(choice, self.df, gui_input=gui_input)
                # the idea is to have this plot object, which through the GUI
                # we can change parameters of, like the axis ranges, the 
                # columns to plot etc... and after such update, one calls 
                # the create_plot() method on the plot object to show the
                # updated plot

                plot.create_plot()
                # set out variable accordingly
                self.logmsg.set(plot.plottype())
            else:
                # call plotter function
                plot = Plotter(choice, self.df)
                # set out variable accordingly
                self.logmsg.set(plot.plottype())
        else:
            self.logmsg.set('Please select a dataframe before plotting')
        # display the updated out string in window
        self.window.update_idletasks()

    def linktopage(self):
        '''We could use the logo as a button to link to our github or so.'''
        pass

    def decrease(self):
        x, y = self.line.get_data()
        self.line.set_ydata(y - 0.2 * x)
        self.canvas.draw()

    def increase(self):
        x, y = self.line.get_data()
        self.line.set_ydata(y + 0.2 * x)
        self.canvas.draw()

    def select_file(self):
        '''This function is called by the open_button'''
        # Which kind of files are accepted?
        filetypes = (
            ('CSV files', '*.csv'),
            ('HDF5 files', '*.hdf5'),
            ('Fits files', '*.fits'),
            ('All files', '*.*'))

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=filename)

        self.file = filename

        self.df = DataFrame(self.file)
        if not self.file.endswith('.csv'):
            updated_path = self.df.to_csv()
        else:
            updated_path = self.file
        data = self.df.read_data(updated_path)
        self.df = data[0]
        self.slider_cols = data[1]
        self.logmsg.set("You chose to load Laura's data the general way.")

    # just for testing
    def select_dummy_file(self):
        self.df = dummydata()
        self.logmsg.set('You chose to load the dummy data.')

    def select_dummy_file2(self):
        self.df, self.slider_cols = dummydata2()
        self.logmsg.set("You chose to load Laura's data")

    def makefig(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot(range(10))

    def buttonsandlabels(self):

        # Header in the window
        self.header = tk.Label(self.window,
                          text='*******    Welcome to slotpy!   ********',
                          font=('Helvetica',16, 'bold'), bg='light blue', fg='blue4',
                          width = 40, height=2)

        self.logo = tk.Button(self.window, image=self.logoimage,
                                     text='Enter', bg='red', fg='orange',
                                     command=self.linktopage,
                                     width=100, height=100)
        # Show log messages
        self.description = tk.Label(self.window,
                               textvariable=self.logmsg,
                               font=('Helvetica', 16), bg='light blue', fg='black')

        # Buttons to choose which plot you want
        self.plotbutton1 = tk.Button(self.window, image=self.preview_img_1,
                                     text='Enter', bg='red', fg='orange',
                                     command=lambda: self.pressbutton('1'),
                                     width = 400, height=400)
        self.plotbutton2 = tk.Button(self.window, image=self.preview_img_2,
                                     text='Enter', bg='red', fg='orange',
                                     command=lambda: self.pressbutton('2'),
                                     width = 400, height=400)
        self.plotbutton3 = tk.Button(self.window, image=self.preview_img_3,
                                     text='Enter', bg='red', fg='orange',
                                     command=lambda: self.pressbutton('3'),
                                     width = 400, height=400)

        self.open_button = ttk.Button(self.window, text='Open a file', command=self.select_file)
        self.dummy_button = ttk.Button(self.window, text='Open dummy data', command=self.select_dummy_file)
        self.dummy_button2 = ttk.Button(self.window, text="Open Laura's dummy data", command=self.select_dummy_file2)

        self.makefig()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.draw()
        self.widgets = self.canvas.get_tk_widget()
        # Call function to place everything on the window
        self.place()

    def place(self):
        '''
        # place everything on the window
        # row,column
        #  __ __ __
        # |00 01 02|
        # |10 11 12|
        # |20 21 22|
        '''
        self.header.grid(row=0, column=0, columnspan=3, rowspan=2)
        self.description.grid(row=2,column=0, columnspan=3, rowspan=1)
        self.open_button.grid(row=0, column=0)
        self.dummy_button.grid(row=1,column=0)
        self.dummy_button2.grid(row=1,column=2)
        self.plotbutton1.grid(row=3, column=0)
        self.plotbutton2.grid(row=3,column=1)
        self.plotbutton3.grid(row=3, column=2)
        self.logo.grid(row=0,column=2)
        self.widgets.grid(row=7,column=1, columnspan=1)