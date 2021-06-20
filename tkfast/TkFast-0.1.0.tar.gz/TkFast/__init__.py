from tkinter import *
import tkinter.ttk as tsk
from tkinter.messagebox import *
def get_input(lst,text,label,canclose=False,toshow=""):
    class A():
        result = ""
    tk = Tk()
    tk.geometry("300x180")
    tk.resizable(0,0)
    tk.title(label)

    def close():
        if canclose :
           if askyesno("退出","是否退出？"):
               tk.destroy()
               return None
        else:
            pass
    def change():
        A.result = txt.get()
        lst.append(A.result)
        tk.destroy()
    tk.protocol("WM_DELETE_WINDOW",close)
    Label(tk,text=text).pack(pady=10)
    txt = tsk.Entry(tk,show=toshow)
    txt.pack()

    tsk.Button(tk,text="完成",command=change).pack(pady=5)
    mainloop()
def get_yesno(lst,text,question,label,canclose=False):
    class A():
        result = ""
    tk = Tk()
    tk.geometry("300x180")
    tk.resizable(0,0)
    tk.title(label)

    def close():
        if canclose :
           if askyesno("退出","是否退出？"):
               tk.destroy()
               return None
        else:
            pass
    def change():
        if i.get():
            lst.append(True)
        else:
            lst.append(False)
        tk.destroy()
    i = IntVar()
    Label(tk,text=text).pack(pady=10)
    c = tsk.Checkbutton(tk,text=question,variable=i,onvalue=1,offvalue=0)
    c.pack()
    tsk.Button(tk,text="完成",command=change).pack(pady=10)
    mainloop()
def get_choose(lst,question,label,chooses,canclose=False):
    class A():
        result = ""
    tk = Tk()
    tk.geometry("400x200")
    tk.title(label)

    def close():
        if canclose :
           if askyesno("退出","是否退出？"):
               tk.destroy()
               return None
        else:
            pass
    Label(tk,text=question).pack(pady=10)
    int_ = IntVar()
    index_value = 0
    for i in chooses:
        tsk.Radiobutton(tk,text=i,variable=int_,value=index_value).pack()
        index_value = index_value + 1
    def change():
        lst.append(int_.get())
        tk.destroy()
    tsk.Button(tk,text="完成",command=change).pack(pady=5)
    tk.protocol("WM_DELETE_WINDOW",close)
    tk.resizable(0, 0)
    mainloop()
def show_alert(text,label):
    tk = Tk()
    tk.geometry("300x200")
    tk.title(label)
    Label(tk,text=text).pack(pady=20)
    tsk.Button(tk,text="完成",command=lambda:tk.destroy()).pack()
    mainloop()
if __name__ == "__main__":
    lists = []
    yesno = []
    get_input(lists,"请输入用户","用户")
    get_input(lists,"请输入密码","用户",toshow="●")
    print("你好，"+lists[0]+"\n密码是"+lists[1])
    get_yesno(yesno,"请回答问题，同意打勾，不同意不打。","直线长20m","问题",False)
    if not yesno[0]:
        print("答对了！")
    else:
        print("答错了！")
    ch = []
    get_choose(ch,question="请问哪项是正确的？",label="选择",canclose=True
               ,chooses=["作者是郭燕铭","作者是lcz","作者是lby"])
    if ch[0] == 0:
        print("没错，就是郭燕铭做的！")
    else:
        print("你搞错了吧...")