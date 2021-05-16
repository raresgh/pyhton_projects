from tkinter import *
from PIL import ImageTk, Image  

texti = 0
imgi = 0
textboxi = 0
font = 10

class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)

		self.master = master

		self.init_window()

	def init_window(self):
		self.theme = "white"
		global textboxi, font
		self.textbox = Text(self.master, undo = True, font = ("Helvetica", font))
		self.textbox.pack(fill = BOTH, expand = 1)
		textboxi = 1

		self.master.title("GUI")
		self.pack()

		global menu
		menu = Menu(self.master)
		self.master.config(menu = menu)

	#File
		file = Menu(menu)
		file.add_command(label = "New File", command = self.new_file)
		file.add_command(label = "Open File")
		file.add_command(label = "Open Folder")
		file.add_command(label = "Save")
		file.add_command(label = "Save As...")
		file.add_command(label = "Close File", command = self.close_file)
		file.add_command(label = "Exit", command = self.clientexit)
		
		menu.add_cascade(label = "File", menu = file)

	#Edit
		edit = Menu(menu)	

		edit.add_command(label = "Delete", command = self.delete_element)
		edit.add_command(label = "Undo", command = self.textbox.edit_undo)
		edit.add_command(label = "Redo", command = self.textbox.edit_redo)

		menu.add_cascade(label = "Edit", menu = edit)

	#Insert
		insert = Menu(menu)

		insert.add_command(label = "Insert Img", command = self.showImg)
		insert.add_command(label = "Insert Text", command = self.showText)

		menu.add_cascade(label = "Insert", menu = insert)
	#View	
		view = Menu(menu)

		view.add_command(label = "Enter Full Screen", command = self.fullscreen)
		view.add_command(label = "Word Wrap")
		view.add_command(label = "Hide Menu", command = self.hide_menu)

		menu.add_cascade(label = "View", menu = view)

	#Preferences
		preferences = Menu(menu)

		preferences.add_command(label = "Theme", command = self.change_theme)
		preferences.add_command(label = "Font +", command = self.font_up)
		preferences.add_command(label = "Font -", command = self.font_down)

		menu.add_cascade(label = "Preferences", menu = preferences)

	def showImg(self):
		global my_image, imgi
		my_image = PhotoImage(file = "C:/Users/rares/OneDrive/Desktop/python_curs/lectia 14(modul 2)/background.png")
		self.textbox.image_create(END, image = my_image)
		imgi = 1
		
	def showText(self):
		self.textbox.insert('insert','Hello there!')
		
	def new_file(self):
		root2 = Toplevel()
		root2.geometry("400x300")
		app2 = Window(root2)

	def delete_element(self):
		if imgi:
			self.textbox.delete('1.0', END)
		

	def close_file(self):
		self.master.destroy()

	def clientexit(self):
		exit()

	def fullscreen(self):
		self.master.state("zoomed")

	def hide_menu(self):
		nomenu = Menu(self.master)
		self.master.config(menu = nomenu)
		revert = Menu(nomenu)
		revert.add_command(label = "Show Menu", command = self.init_window)
		revert.add_cascade(label = "Show Menu", menu = revert)

	def font_up(self):
		global font
		font = font + 1
		if textboxi:
			self.textbox.config(font = ("Helvetica", font))

	def font_down(self):
		global font
		font = font - 1
		if textboxi:
			self.textbox.config(font = ("Helvetica", font))

	def change_theme(self):
		if self.theme == "white":
			self.configure(bg = "black")
			self.textbox.config(fg = "white", bg = "black")
			self.theme = "black"
		elif self.theme == "black":
			self.configure(bg = "white")
			self.textbox.config(fg = "black", bg = "white")
			self.theme = "white"

root = Tk()
root.geometry("400x300")

app = Window(root)
app.mainloop()
