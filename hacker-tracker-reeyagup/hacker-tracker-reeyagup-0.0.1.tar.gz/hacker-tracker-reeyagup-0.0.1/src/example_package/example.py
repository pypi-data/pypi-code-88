from tkinter import *
import tkinter as tk
from tkcalendar import Calendar
import nltk
import spacy
from nltk.corpus import wordnet
from spacytextblob.spacytextblob import SpacyTextBlob

'''def homeScreen():
    window = Tk()
    window.title("HackerTracker")
    window.geometry('1000x400')
    lbl = Label(window, text="Welcome to HackerTracker!", font=("Arial Bold", 50))
    lbl.grid(column=0, row=0)
    lbl.place(relx=.5, rely=.5, anchor="c")
    btn = Button(window, text="Click here to start!", bg="blue")
    btn.grid(column=0, row=1)
    btn.place(relx=.5, rely=.65, anchor="c")
    window.mainloop()'''

def nlp():
    print("test")
    nltk.download('wordnet')

    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe("spacytextblob")
    print("Input one or two sentences")
    text = input()

  
    # Input single text?
    doc = nlp(text)

    # print(doc._.assessments)

    # list comphresion to get the emotional words
    words = list(zip(*doc._.assessments))
    # for index in range(0, len(words)):
    word = list(zip(*words[0]))
    word3 = list(zip(*word))
    for index in range(0, len(word3)):
        print(index, "-", *word3[index])

        # Word Cloud
        synonyms = []
        for syn in wordnet.synsets(*word3[index]):
            for lm in syn.lemmas():
                synonyms.append(lm.name())  # adding into synonyms

        print(set(synonyms))

    # Input multiple lines of text?
    docs = list(nlp.pipe([text]))



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

#home page
class HomePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        lbl = Label(self, text="Welcome to HackerTracker!", font=("Comic Sans MS", 50, 'bold'), bg="black", fg="SpringGreen2")
        lbl.place(relx=0.5, rely=0.5, anchor ="c")

#Second page asking for date
class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        lbl = Label(self, text="Please select today's date:  ",font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        lbl.place(relx=.5, rely=.05, anchor="c")

        #cal = Calendar(self, selectmode="day", year=2021, month=6, day=21, selectforeground='pink', foreground='yellow', highlightcolor='pink', normalforeground='orange', font=("Comic Sans MS", 20))
        cal = Calendar(self, background="black", disabledbackground="black", bordercolor="black",
                 headersbackground="black", normalbackground="black", foreground='white',
                 normalforeground='white', headersforeground='white', font=("Comic Sans MS", 20))
        cal.place(relx=.5, rely=.5, anchor="c")

        #create spins to add date
        #month = Label(self, text="Month")
        #month.grid(column=0, row=1, sticky="")
        #spin = Spinbox(self, from_=1, to=12, width=5, format="%02.0f")
        #spin.grid(column=0, row=2, sticky="")

        #day = Label(self, text="Day")
        #day.grid(column=1, row=1, sticky="")
        #spin2 = Spinbox(self, from_=1, to=30, width=5, format="%02.0f")
        #spin2.grid(column=1, row=2, sticky="")

        #year = Label(self, text="Year")
        #year.grid(column=2, row=1, sticky="")
        #spin3 = Spinbox(self, from_=0000, to=9999, width=5, format="%04.0f")
        #spin3.grid(column=2, row=2, sticky="")        # spin3.grid(column=2, row=2, sticky="")

#Third page asking to select options
class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")                            #copy these 3 lines to make a new class
        #make checkbutton for multiselect
        lbl = Label(self, text="Select desired categories", font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        lbl.place(relx=.5, rely=.05, anchor="c")
        sleep_state = BooleanVar()
        sleep = Checkbutton(self, text="Sleep", var=sleep_state, font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        sleep.place(relx=.28, rely=.2, anchor="c")
        exercise = Checkbutton(self, text="Exercise", font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        exercise.place(relx=.28, rely=.3, anchor="c")
        caffeine = Checkbutton(self, text="Caffeine", font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        caffeine.place(relx=.28, rely=.4, anchor="c")
        mood = Checkbutton(self, text="Mood", font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        mood.place(relx=.28, rely=.5, anchor="c")
        confidence = Checkbutton(self, text="Confidence", font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        confidence.place(relx=.48, rely=.2, anchor="c")
        screenTime = Checkbutton(self, text="Screen Time", font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        screenTime.place(relx=.48, rely=.3, anchor="c")
        socializing = Checkbutton(self, text="Socializing", font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        socializing.place(relx=.48, rely=.4, anchor="c")
        productivity = Checkbutton(self, text="Productivity", font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        productivity.place(relx=.48, rely=.5, anchor="c")
        hygiene = Checkbutton(self, text="Hygiene", font=("Comic Sans MS", 20), bg="black", fg='white', highlightbackground ="SpringGreen2")
        hygiene.place(relx=.68, rely=.2, anchor="c")
        #https://likegeeks.com/python-gui-examples-tkinter-tutorial/

#Fourth Page prompting journaling input
class Page4(Page):
     def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        choice_lbl = Label(self, text="Select Best Option", font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        choice_lbl.place(relx=.5, rely=.05, anchor="c")

        sleep_label = Label(self, text="How many hours did you sleep last night?", font=("Comic Sans MS", 30, 'bold'), bg="black", fg='white')
        sleep_label.place(relx=.5, rely=.25, anchor="c")

        redbutton = Button(self, text="0-3 hours", fg="white", padx=10, pady=20, font=("Comic Sans MS", 20), bg='red')
        #redbutton.pack(side=LEFT)
        redbutton.place(relx=.25, rely=.5, anchor="c")

        orangeredbutton = Button(self, text="3-5 hours", fg="white", padx=10, pady=20, font=("Comic Sans MS", 20), bg='orange red')
        #greenbutton.pack(side=LEFT)
        orangeredbutton.place(relx=.37, rely=.5, anchor="c")

        orangebutton = Button(self, text="6-8 hours", fg="white", padx=10, pady=20, font=("Comic Sans MS", 20), bg='orange')
        #bluebutton.pack(side=LEFT)
        orangebutton.place(relx=.49, rely=.5, anchor="c")

        yellowbutton = Button(self, text="9-11 hours", fg="white", padx=10, pady=20, font=("Comic Sans MS", 20), bg='yellow')
        #purpbutton.pack(side=LEFT)
        yellowbutton.place(relx=.618, rely=.5, anchor="c")

        greenbutton = Button(self, text="11+ hours", fg="white", padx=10, pady=20, font=("Comic Sans MS", 20), bg='green')
        #blackbutton.pack(side=LEFT)
        greenbutton.place(relx=.749, rely=.5, anchor="c")

#Page 5 with plots
class Page5(Page):
     def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        graph_lab = Label(self, text="Plots",  font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        graph_lab.place(relx=.5, rely=.05, anchor="c")

#NLP prompting user for input
class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        graph_lab = Label(self, text="How are you feeling today:", font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        graph_lab.place(relx=.5, rely=.05, anchor="c")
        E1 = Entry(self)
        E1.place(relx=.5, rely=.25, anchor="c")
        blueButton = Button(self, text="Submit", bg="black", fg="white")
        blueButton.place(relx=.5, rely=.35, anchor="c")

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        #objects for each of the screens
        home = HomePage(self)
        date = Page2(self)
        options = Page3(self)
        choices = Page4(self)
        plots = Page5(self)
        nlp = Page6(self)

        #global variables
        global screens
        screens = [home, date, options, choices, plots, nlp]
        global num
        num = 0

        #create menu
        menu = Menu(window)
        new_item = Menu(menu)
        new_item.add_command(label='Next', command=lambda: self.goNext(num))
        new_item.add_command(label='Back', command=lambda: self.goBack(num))
        new_item.add_command(label='Exit', command=lambda: self.close())
        menu.add_cascade(label='File', menu=new_item)
        window.config(menu=menu)

        #make frames
        button_frame = tk.Frame(self, bg="gray")
        container = tk.Frame(self, bg="black")
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        #create next button
        next_btn = Button(button_frame, text="Next", bg="blue", command=lambda: self.goNext(num))
        next_btn.pack(side="right")
        #create back button
        back_btn = Button(button_frame, text="Back", bg="blue", command=lambda: self.goBack(num))
        back_btn.pack(side="left")
        #place screens into a container
        home.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        date.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        options.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        choices.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        plots.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        nlp.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        screens[0].show()

    #moves to next screen
    def goNext(self, index):
        if index < len(screens)-1:
            global num
            num += 1
            screens[index+1].show()

    #move to prev screen
    def goBack(self, index):
        if index > 0:
            global num
            num -= 1
            screens[index-1].show()

    #exits GUI
    def close(self):
        window.destroy()
        exit()


if __name__ == "__main__":
    nlp()
    window = Tk()
    main = MainView(window)
    main.pack(side="top", fill="both", expand=True)
    window.title("HackerTracker")
    window.geometry('1200x600')
    window.mainloop()
