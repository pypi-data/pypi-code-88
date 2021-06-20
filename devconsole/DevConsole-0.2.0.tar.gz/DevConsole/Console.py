import os, sys
import tkinter as tk


class Command:
	def __init__(self, CommandName, Command):
		self.command = CommandName
		self.commandFunc = Command

	def execute(self):
		try:
			self.commandFunc()
		except TypeError:
			print("Please Check That The Command Is A Function.")

class Console:
	def __init__(self, Title=None, IconPath=None, BackGroundColor="#d9d9d9"):
		# Setup The GUI

		self.window = tk.Tk()

		exitcmd = Command("exit", self.exit)

		self.window.geometry("450x300")
		self.window.minsize(120, 1)
		self.window.maxsize(1604, 881)
		self.window.resizable(1, 1)
		self.window.title("Developer Console")

		if Title:
			self.window.title(Title)
		

		if IconPath:
			if os.exist(IconPath):
				self.window.iconbitmap(IconPath)

		self.window.configure(background=BackGroundColor)

		self.SubmitButton = tk.Button(self.window)
		self.SubmitButton.place(relx=0.822, rely=0.833, height=44, width=70)
		self.SubmitButton.configure(activebackground="#ececec")
		self.SubmitButton.configure(activeforeground="#000000")
		self.SubmitButton.configure(background="#d9d9d9")
		self.SubmitButton.configure(disabledforeground="#a3a3a3")
		self.SubmitButton.configure(foreground="#000000")
		self.SubmitButton.configure(highlightbackground="#d9d9d9")
		self.SubmitButton.configure(highlightcolor="black")
		self.SubmitButton.configure(pady="0")
		self.SubmitButton.configure(text='''Execute''')
		self.SubmitButton.configure(command=self.exec)

		self.CommandEntry = tk.Entry(self.window)
		self.CommandEntry.place(relx=0.044, rely=0.867, height=30
			  , relwidth=0.764)
		self.CommandEntry.configure(background="white")
		self.CommandEntry.configure(disabledforeground="#a3a3a3")
		self.CommandEntry.configure(font="TkFixedFont")
		self.CommandEntry.configure(foreground="#000000")
		self.CommandEntry.configure(insertbackground="black")

		self.CommandList = tk.Listbox(self.window)
		self.CommandList.place(relx=0.022, rely=0.033, relheight=0.773
				, relwidth=0.964)
		self.CommandList.configure(background="white")
		self.CommandList.configure(disabledforeground="#a3a3a3")
		self.CommandList.configure(font="TkFixedFont")
		self.CommandList.configure(foreground="#000000")

		self.Commands = [exitcmd]

		self.window.bind('<Return>', self.exec)

	def ChangeGUI(self, _window):
		"""
		The Required Components For This Is The SubmitButton CommandEntry CommandList
		"""
		self.window = _window

		self.window.bind('<Return>', self.exec)

		try:
			self.window.SubmitButton.configure(command=self.exec)
		except:
			pass

	def WriteLine(self, Message):
		self.CommandList.insert(tk.END, Message)

	def Clear(self):
		self.CommandList.delete(0, tk.END)

	def RegisterCommand(self, CommandObj):
		for i in self.Commands:
			if i.command == CommandObj.command:
				raise ConsoleError("The Command Already Exists.")
		self.Commands.append(CommandObj)

	def exec(self, event=None, command=None):
		commandExecuting = self.CommandEntry.get().lower()
		commandInputed = self.CommandEntry.get()
		if command:
			commandExecuting = command.lower()
			commandInputed = command
		self.CommandEntry.delete(0, 'end')
		if commandExecuting == "" or commandExecuting.isspace() == True:
			return
		for i in self.Commands:
			if i.command.lower() == commandExecuting:
				i.execute()
				return
		self.WriteLine(f"Command {commandExecuting} Doesn't Exist!")

	def exit(self):
		sys.exit()

	def mainloop(self):
		tk.mainloop()


class ConsoleError(Exception):
	pass


if __name__ == '__main__':	
	# Demo
	cons = Console()

	def func():
		cons.WriteLine("Wrote Something")

	def cl():
		cons.Clear()

	cmd = Command("write", func)
	clear = Command("Clear", cl)
	cons.RegisterCommand(cmd)
	cons.RegisterCommand(clear)
	tk.mainloop()