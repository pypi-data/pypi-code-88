from tkinter import *
import tkinter as tk
import Genskew_univiecube as gs
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# noch  zu tun: größe des grund fensters umändern(wirklich notwendig?) und output folder funktionabel machen (done)
window = Tk()
global filename
filename = None
global output_folder
output_folder = None

# functions that controll what the Buttons do
def save():
    global filename
    global output_folder
    output_folder = filedialog.askdirectory()
    nuc_1 = nuc_1_box.get()
    nuc_2 = nuc_2_box.get()
    sequence = gs.gen_sequence(filename, 'fasta')
    try:
        stepsize = int(stepsize_input.get())
    except:
        stepsize = None

    try:
        windowsize = int(windowsize_input.get())
    except:
        windowsize = None
    skew_calculation = gs.Object(sequence, nuc_1, nuc_2, stepsize, windowsize)
    results = gs.Object.gen_results(skew_calculation)
    gs.plot_sequence(results, filename, output_folder, file_type_box.get())

def browse():
    global filename
    filename = askopenfilename()
    lbl = Label(window, text=filename)

    lbl.grid(column=0, row=1, columnspan=5)



def plot_sequence(results, filelocation, outputfolder=None, out_file_type=None, dpi=None):
    if not outputfolder:
        outputfolder = filelocation.replace(filelocation.split('/')[-1], "")
        not_spec = 'vuusjv7i93'
    if not out_file_type:
        out_file_type = 'png'
    fig, ax = plt.subplots()
    # plotting the graph
    ax.plot(results.x, results.skew, color="blue", linewidth=0.3)
    ax.plot(results.x, results.cumulative, color="red", linewidth=0.3)
    ax.axvline(x=int(results.max_cm_position), color="green", linewidth=0.3,
               label="maximum, at " + str(results.max_cm_position))
    ax.axvline(x=int(results.min_cm_position), color="green", linewidth=0.3,
               label="minimum, at " + str(results.min_cm_position))
    ax.set_title("Gen-skew plot for sequence: " + filelocation.split('/')[-1] + ", with stepsize: " + str(  # + q_variables[b].description
        results.stepsize) + " and windowsize: " + str(results.windowsize))
    ax.set_xlabel("position in sequence")
    ax.set_ylabel(results.nuc_1 + " " + results.nuc_2 + " skew")
    ax.grid(b=None, which='major', axis='both')
    ax.ticklabel_format(axis='x', style='plain')
    ax.legend()


def calculate():
    global filename
    global output_folder
    nuc_1 = nuc_1_box.get()
    nuc_2 = nuc_2_box.get()
    sequence = gs.gen_sequence(filename, 'fasta')
    # defining the stepsize
    try:
        stepsize = int(stepsize_input.get())
    except:
        stepsize = None

    try:
        windowsize = int(windowsize_input.get())
    except:
        windowsize = None
    # calculating and displaying the figure
    skew_calculation = gs.Object(sequence, nuc_1, nuc_2, stepsize, windowsize)
    results = gs.Object.gen_results(skew_calculation)
    fig = Figure(figsize=(9, 6), facecolor="white")
    axis = fig.add_subplot(111)
    axis.plot(results.x, results.skew, color="blue", linewidth=0.3)
    axis.plot(results.x, results.cumulative, color="red", linewidth=0.3)
    axis.axvline(x=int(results.max_cm_position), color="green", linewidth=0.3,
               label="maximum, at " + str(results.max_cm_position))
    axis.axvline(x=int(results.min_cm_position), color="green", linewidth=0.3,
               label="minimum, at " + str(results.min_cm_position))
    axis.set_title("Gen-skew plot for sequence: " + filename.split('/')[-1] + ", with stepsize: " + str(  # + q_variables[b].description
        results.stepsize) + " and windowsize: " + str(results.windowsize))
    axis.set_xlabel("position in sequence")
    axis.set_ylabel(results.nuc_1 + " " + results.nuc_2 + " skew")
    axis.grid(b=None, which='major', axis='both')
    axis.ticklabel_format(axis='x', style='plain')
    axis.legend()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas._tkcanvas.grid(column=0,row=2, columnspan=5)

# Widgets in the tk window
window.title("GUIskew")

Browse_btn = Button(window, text="Browse", command=browse)
Browse_btn.grid(column=0, row=0)

nuc_1_box = Combobox(window)
nuc_1_box['values']= ("A", "C", "G", "T")
nuc_1_box.current(2)
nuc_1_box.grid(column=1, row=0)

nuc_2_box = Combobox(window)
nuc_2_box['values'] = ("A", "C", "G", "T")
nuc_2_box.current(1)
nuc_2_box.grid(column=2, row=0)

lbl = Label(window, text=" Stepsize, Windowsize:")
lbl.grid(column=3, row=0)

stepsize_input = Entry(window, width=10)
stepsize_input.grid(column=4, row=0)

windowsize_input = Entry(window, width=10)
windowsize_input.grid(column=5, row=0)

file_type_box = Combobox(window)
file_type_box['values'] = ("jpg", "png", )
file_type_box.current(0)
file_type_box.grid(column=6, row=0)

calculate_btn = Button(window, text="Calculate", command=calculate)
calculate_btn.grid(column=6, row=1)

save_btn = Button(window, text="Save", bg="green", command=save)
save_btn.grid(column=6, row=3)


window.mainloop()
