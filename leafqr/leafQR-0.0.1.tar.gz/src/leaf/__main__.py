import pyqrcode
from tkinter import *
from tkinter.messagebox import showinfo, showerror
import os
from pathlib import Path
from tkinter import filedialog
import webbrowser

def main():
    gui = Tk()
    gui.title("Leaf-A Simple Qr-Code generator")
    gui.geometry("500x500")
    gui.configure(background="black")

    def generate():
        try:
            change_dir_to = os.chdir(Path.home())
            try:
                os.mkdir("Leaf-Qr-Codes")
            except:
                pass
            changed_dir_to = os.chdir("Leaf-Qr-Codes")
        except:
            pass
        if name.get():
            global qr_name
            qr = pyqrcode.create(data.get())
            qr_name = str(name.get()) + ".png"
            qr.png((qr_name), scale=10)
            label_show.config(text="Qr-Code Generated")
            showinfo("QR-Code Generated", "QR-Code generated. To open it, click the open button, or check the in directory you saved Leaf")
        else:
            qr = pyqrcode.create(data.get())
            qr_name = "Leaf QrCode.png"
            qr.png((qr_name), scale=10)
            label_show.config(text="Qr-Code Generated")
            showinfo("QR-Code Generated", "QR-Code with deflaut name generated. To open it, click the open button, or check the in 'HOME/Leaf-Qr-Codes' Directory")

    def open():
        change_dir_to = os.chdir(f'{Path.home()}/Leaf-Qr-Codes')
        try:
            file = qr_name
            os.system('"%s"' %file)
            label_text = str(file) + "Opened"
            label_show.config(text=label_text)
        except:
            showerror("No file found", "No Qr-Code saved to open found")

    def open_any():
        change_dir_to = os.chdir(f'{Path.home()}/Leaf-Qr-Codes')
        try:
            file = filedialog.askopenfilenames(initialdir=change_dir_to, title="Choose a Qr-Code", filetypes=(("Image Files", "*.png"), ("Image Files", "*.jpg")))
            os.system('"%s"' %file)
            label_text = str(file) + "Opened"
            label_show.config(text=label_text)
        except:
            showerror("No file found", "No Qr-Code selected")

    def delqr():
        change_dir_to = os.chdir(f'{Path.home()}/Leaf-Qr-Codes')
        try:
            file = qr_name
            os.remove(file)
            label_text = str(file) + "Deleted"
            label_show.config(text=label_text)
        except:
            showerror("No file found", "No Qr-Code saved to delete")

    def del_any():
        change_dir_to = os.chdir(f'{Path.home()}/Leaf-Qr-Codes')
        try:
            file = filedialog.askopenfilenames(initialdir=change_dir_to, title="Choose a Qr-Code", filetypes=(("Image Files", "*.png"), ("Image Files", "*.jpg")))
            os.remove(file)
            label_text = str(file) + "Deleted"
            label_show.config(text=label_text)
        except:
            showerror("No file found", "No Qr-Code saved to delete")

    def del_all():
        try:
            change_dir_to = os.chdir(f'{Path.home()}/Leaf-Qr-Codes')
            for file in os.listdir(): 
                if file.endswith('.png'):
                    os.remove(file) 
                    showinfo("Deleted", "All Qr-Code Generated with Leaf in the ~/Leaf-Qr-Codes Deleted.")
        except:
            showerror("No files found", "No Qr-Codes saved to delete")
        
    Author = "I wrote Leaf because I needed a simple QR-Generator which is light-weight, safe and private. It is also very easy to use. It is also free and open source. You can check the code at https://github.com/newtoallofthis123/leaf. Leaf is written purely in python. It is a beginner friendly project. Hope you enjoy using it."    
    About = "Leaf Qr-Code is a small project I made to learn tkinter. This is purely written in python. It is free and open source. It has no telementry and is completely safe and private. Check out some of my other projects at https://newtoallofthis123.github.io/About"
        
    def openNoobweb():
        webbrowser.open("https://newtoallofthis123.github.io/About")
        
    def showInfo():
        showinfo("About NoobNote", About)

    def aboutAuthor():
        showinfo("NoobScience", Author)
        
    def projects():
        webbrowser.open("https://github.com/newtoallofthis123")
        
    def openleafweb():
        webbrowser.open("https://newtoallofthis123.github.io/leaf")

    def source():
        webbrowser.open("https://github.com/newtoallofthis123/leaf")

    def issue():
        webbrowser.open("https://github.com/newtoallofthis123/leaf/issues")
        
    def quit1(e):
        gui.quit()

    def doc(e):
        webbrowser.open("https://newtoallofthis123.github.io/leaf")

    def show_all():
        change_dir_to = os.chdir(f'{Path.home()}/Leaf-Qr-Codes')
        file = filedialog.askopenfilenames(initialdir=change_dir_to, title="Choose a Qr-Code", filetypes=(("Image Files", "*.png"), ("Image Files", "*.jpg")))


    label = Label(gui, text="Leaf", fg="black", bg="#71FFDD", font=("Cascadia Code", 24))
    label.pack(padx=10, pady=20)

    root = Frame(gui, bg="black")
    root.pack()

    data_label = Label(root, text="Enter Data", font=("Cascadia Code", 18), fg="black", bg="#F13C51")
    data_label.grid(row=0, column=1)

    data = Entry(root, fg="black", bg="#93F0CC", font=("Cascadia Code", 18))
    data.grid(row=0, column=0, padx=10, pady=5)

    name_label = Label(root, bg="#F13C51", fg="black", text="Enter Name",font=("Cascadia Code", 18))
    name_label.grid(row=1, column=1, pady=5, padx=10)

    name = Entry(root, fg="black", bg="#99F4D1", font=("Cascadia Code", 18))
    name.grid(row=1, column=0)

    generate_btn = Button(gui, text="Generate", fg="Black", bg="#EFCEB0", font=("Cascadia Code", 18), borderwidth=0, command=generate)
    generate_btn.pack(padx=10, pady=20)

    open_title = Label(gui, text="Press open to open the saved Qr-Code ", fg="#E8EDDD", bg="black", borderwidth=0, font=("Cascadia", 8))
    open_title.pack(padx=10,)

    open_btn = Button(gui, text="Open", command=open, font=("Cascadia", 14), fg="black", bg="#EFCEB0")
    open_btn.pack(padx=10, pady=10, ipady=3)

    about = Label(gui,text = "Made by NoobScience",font = ("Cascadia", 16),bg = "black",fg = "#D8EFB0",)
    about.pack(fill=X, pady=10)

    label_show = Label(gui, text="Enter data, name and click generate", font=("Cascadia", 8), fg="white", bg="black")
    label_show.pack()

    _menu = Menu(gui)
    gui.config(menu=_menu)
    file = Menu(_menu, tearoff=False)
    _menu.add_cascade(label="File", menu=file)
    file.add_command(label="Open current Qr-code", command=open)
    file.add_command(label="Open any Qr-code", command=open_any)
    file.add_separator()
    file.add_command(label="Generate Qr-Code", command=generate)
    file.add_command(label="Show All Qr", command=show_all)
    file.add_separator()
    file.add_command(label="Exit", command=gui.quit())

    edit = Menu(_menu, tearoff=False)
    _menu.add_cascade(label="Edit", menu=edit)
    edit.add_command(label="Delete Generated QR-Code", command=delqr)
    edit.add_command(label="Delete any QR-Code", command=del_any)
    edit.add_command(label="Delete all QR-Codes", command=del_all)

    about = Menu(_menu, tearoff=False)
    _menu.add_cascade(label="Help", menu=about)
    about.add_command(label="Read the Docs", command=lambda: doc(False))
    about.add_command(label="About Author", command=aboutAuthor)
    about.add_command(label="About Leaf", command=showInfo)
    about.add_command(label="NoobScience Website", command=openNoobweb)
    about.add_command(label="Leaf Website", command=openleafweb)
    about.add_command(label="View Source Code", command=source)
    about.add_command(label="Report a Issue", command=issue)    
    about.add_command(label="Some of my other projects", command=projects)


    gui.bind('<Control-q>', quit1)

    gui.mainloop()

if __name__ == '__main__':
    main()