import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image 

data = {}

def win():
	global window, question_frame, question_lbl, answer_frame, submit_bt, message_lbl, answer_entry
	window = tk.Tk()
	window.geometry("500x370+520+200")
	#window.resizable(False, False)
	window.title("Robot Assistant")
	window.configure(bg = "#00074a")

	question_frame = tk.Frame(
		master = window,
		height = 200,
		bg = "#00074a")
	question_frame.pack(fill = "x")

	answer_frame = tk.Frame(
		master = window,
		height = 100,
		bg = "#00074a")
	answer_frame.pack(fill = "x")

	message_frame = tk.Frame(
		master = window,
		bg = '#00074a')
	message_frame.pack()

	question_lbl = tk.Label(
		master = question_frame,
		text = "Enter your name to continue:",
		font = ("Helvetica", 12),
		bg = "#00074a",
		fg = "white")
	question_lbl.pack(pady = 20)

	message_lbl = tk.Label(
		master = message_frame,
		text = "",
		font = ("Helvetica", 12),
		bg = "#00074a",
		fg = "white")
	message_lbl.pack()

	global ANSWER
	ANSWER = StringVar()

	answer_entry = tk.Entry(
		master = answer_frame,
		textvariable = ANSWER,
		bg = "#323052",
		fg = "white",
		relief = FLAT,
		font = 10)
	answer_entry.pack(pady = 20, ipady = 2)
	answer_entry.focus_force()
	submit_bt = Button(
		master = answer_frame,
		text = "Submit",
		command = name_func,
		bg = "black",
		fg = "white",
		relief = FLAT)
	submit_bt.pack(pady = 20)

	submit_bt.bind('<Return>',name_func)

	window.mainloop()

def name_func(event = None):
	answer_entry.focus_force()
	global name
	name = ANSWER.get()
	ANSWER.set("")
	subdict = {name:{"age": 0, "grade":"unknown", "school":"unknown", "hobbies":"unknown", "favourite sport": "unknown", "favourite class":"unknown", "dream job":"unknown"}}
	data.update(subdict)
	question_lbl.config(text = "Enter your age:")
	submit_bt.config(command = age_func)
	submit_bt.bind('<Return>',age_func)

def age_func(event = None):
	answer_entry.focus_force()
	global age
	age = ANSWER.get()
	ANSWER.set("")
	data[name]["age"] = age
	question_lbl.config(text = "What grade are you in?")
	submit_bt.config(command = grade_func)
	submit_bt.bind('<Return>',grade_func)


def grade_func(event = None):
	answer_entry.focus_force()
	global grade
	grade = ANSWER.get()
	ANSWER.set("")
	data[name]["grade"] = grade
	question_lbl.config(text = "What school are you in?")
	submit_bt.config(command = school_func)	
	submit_bt.bind('<Return>',school_func)


def school_func(event = None):
	answer_entry.focus_force()
	global school
	school = ANSWER.get()
	ANSWER.set("")
	data[name]["school"] = school
	question_lbl.config(text = "What are your hobbies?")
	submit_bt.config(command = hobbies_func)
	submit_bt.bind('<Return>',hobbies_func)


def hobbies_func(event = None):
	answer_entry.focus_force()
	global hobbies
	hobbies = ANSWER.get()
	ANSWER.set("")
	data[name]["hobbies"] = hobbies
	question_lbl.config(text = "What is your favourite sport?")
	submit_bt.config(command = sport_func)
	submit_bt.bind('<Return>',sport_func)


def sport_func(event = None):
	answer_entry.focus_force()
	global sport
	sport = ANSWER.get()
	ANSWER.set("")
	data[name]["favourite sport"] = sport
	question_lbl.config(text = "What is your favourite class in school?")
	submit_bt.config(command = class_func)
	submit_bt.bind('<Return>',class_func)


def class_func(event = None):
	answer_entry.focus_force()
	global classd
	classd = ANSWER.get()
	ANSWER.set("")
	data[name]["favourite class"] = classd
	question_lbl.config(text = "And last but not least, what is your dream job?")
	submit_bt.config(command = job_func)
	submit_bt.bind('<Return>',job_func)


def job_func(event = None):
	answer_entry.focus_force()
	global job
	job = ANSWER.get()
	ANSWER.set("")
	data[name]["dream job"] = job
	question_lbl.config(text = "OK, that would be it...Thanks!")
	submit_bt.config(command = restart, text = "Restart")
	message_lbl.config(text = "Here are the informations that are in the data base now:\nName: " + name + "\nAge: " + age + "\nGrade: " + grade + "\nSchool: " + school  + "\nHobbies: " + hobbies + "\nFavourite Sport: " + sport + "\nFavourite Class: " + classd + "\nDream Job: " + job )
	print(data)

def restart(event = None):
	window.destroy()
	win()

win()