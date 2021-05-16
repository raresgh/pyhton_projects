import tkinter as tk
from tkinter import *
class Supermarket:
	def __init__(self, nume, inaltime, arie):
		self.nume = nume
		self.inaltime = inaltime
		self.arie = arie

def win():
	global window, nume_entry, inaltime_entry, arie_entry, nume_label, inaltime_label, arie_label, bottom_frame
	window = tk.Tk()
	window.geometry("800x600+600+180")
	window.resizable(False, False)
	window.title("Supermarket GUI")
	window.configure(bg = "#00074a")

	global nume, inaltime, arie
	nume = StringVar()
	inaltime = StringVar()
	arie = StringVar()


	#empty frame
	empty_frame = tk.Frame(
		master = window,
		bg = "#00074a",
		height = 80)
	empty_frame.pack()

	#entry frame
	entry_frame = tk.Frame(
		master = window,
		bg = "#00074a"
		)
	entry_frame.pack(fill = "x")

	bottom_frame = tk.Frame(
		master = window,
		bg = "#00074a"
		)
	bottom_frame.pack()

	nume_label = tk.Label(
		master = entry_frame,
		text = "Numele Supermarket-ului:",
		bg = "#00074a",
		fg = "white",
		font = ("Arial", 14)
		)
	nume_label.pack(pady = 15)

	nume_entry = tk.Entry(
		master = entry_frame,
		textvariable = nume
		)
	nume_entry.pack()

	inaltime_label = tk.Label(
		master = entry_frame,
		text = "Inaltimea Supermarket-ului:",
		bg = "#00074a",
		fg = "white",
		font = ("Arial", 14)
		)
	inaltime_label.pack(pady = 15)

	inaltime_entry = tk.Entry(
		master = entry_frame,
		textvariable = inaltime
		)
	inaltime_entry.pack()

	arie_label = tk.Label(
		master = entry_frame,
		text = "Aria Supermarket-ului:",
		bg = "#00074a",
		fg = "white",
		font = ("Arial", 14)
		)
	arie_label.pack(pady = 15)

	arie_entry = tk.Entry(
		master = entry_frame,
		textvariable = arie
		)
	arie_entry.pack()

	button_ok = tk.Button(
		master = entry_frame,
		text = "OK",
		command = ok,
		width = 10,
		bg = "green")
	button_ok.pack(pady = 40)

	window.mainloop()

def ok():
	supermarket = Supermarket(nume.get(), inaltime.get(), arie.get())
	supermarket_label = tk.Label(
		master = bottom_frame,
		text = supermarket.nume + ": " + supermarket.inaltime + "(inaltime), " + supermarket.arie + "(arie)",
		bg = "#00074a",
		fg = "white",
		font = ("Arial", 15)
		)
	supermarket_label.pack(pady = 30)

win()