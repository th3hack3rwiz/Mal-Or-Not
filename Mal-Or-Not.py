from tkinter import *
import os
from tkinter import ttk
from tkinter import filedialog
import whois
import subprocess
root = Tk()
root.title('Mal-Or-Not')
root.geometry("430x200+630+350")
bg= PhotoImage(file="matrixbg.png")  

my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg, anchor="nw")
my_canvas.create_text(220,80, text="Welcome to", font=("Helvetica", 24,'bold'), fill="white")
my_canvas.create_text(220,120, text="Mal-O-Not", font=("Helvetica", 24,'bold'), fill="white")

def destroy():
	root.destroy()
root.after(2000, destroy)
root.mainloop()

root = Tk()
root.title('Mal-Or-Not')
root.geometry("430x370+630+250")
bg= PhotoImage(file="matrixbg.png")  

my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg, anchor="nw")
my_canvas.create_text(220,30, text="Mal-Or-Not", font=("Helvetica", 24,'bold'), fill="white")

def IP():
	global typeid
	typeid='IP'
	rootentry = Tk()
	rootentry.title('IP Intel')
	rootentry.geometry("350x200+670+300")
	#bg= PhotoImage(file="matrixbg.png")
	ip_canvas = Canvas(rootentry, width=200, height=100, bd=0, highlightthickness=0, bg="green")
	ip_canvas.pack(fill="both", expand=True)

	#my_canvas.create_image(0,0, image=bg, anchor="nw")
	ip_canvas.create_text(180,45, text="Enter IP Address:", font=("Helvetica", 18,'bold'), fill="white")
	entry = Entry(rootentry, font=("Helvitica",12),width=13, fg="black", bd=0)
	entry_window = ip_canvas.create_window(115,80,anchor='nw', window=entry)
	def store():
	    global inp
	    inp=entry.get()
	    print(typeid+":"+inp)
	    rootentry.destroy()

	buttonentry=Button(rootentry, text="Done",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=store)
	buttonentry_window = ip_canvas.create_window(145,130, anchor='nw', window=buttonentry)

	rootentry.mainloop()
	subprocess.check_output(["./mal-o-not.sh", "-i", inp])

	rootentry = Tk()

	rootentry.title('IP Information')
	rootentry.geometry("410x600+670+370")

	main_frame=Frame(rootentry)
	main_frame.pack(fill=BOTH, expand=1)

	ip_canvas=Canvas(main_frame)
	ip_canvas.pack(side=LEFT, fill=BOTH, expand=1)

	my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL, command=ip_canvas.yview)
	my_scrollbar.pack(side=RIGHT, fill=Y)

	ip_canvas.configure(yscrollcommand=my_scrollbar.set)
	ip_canvas.bind('<Configure>', lambda e:ip_canvas.configure(scrollregion=ip_canvas.bbox("all")))

	second_frame=Frame(ip_canvas)

	ip_canvas.create_window((0,0), window=second_frame, anchor='nw')


	my_canvas1 = Canvas(second_frame, width=900, height=2000, bd=0, highlightthickness=0, bg="black")
	my_canvas1.pack(fill="both", expand=True)
	
	with open("output","r") as f:
	    data=f.read()

	my_canvas1.create_text(400,150, text=data, font=("Helvetica", 12,'bold'), fill="lime", anchor='n')

	rootentry.mainloop()

def Domain():
	subprocess.call(['python3','WhoIsInfo.py'])

def Email():
	global typeid
	typeid='Email'
	clickentry()

def phno():
	global typeid
	typeid='phno'
	clickentry()

def link():
	global typeid
	typeid='link'
	clickentry()

def files():
	global typeid
	typeid='path'
	clickbrowse()

def clickentry():
	pass
	
def clickbrowse():
	rootbrowse = Tk()
	rootbrowse.title('Mal-Or-Not')
	rootbrowse.geometry("350x200+670+300")
	my_canvas1 = Canvas(rootbrowse, width=200, height=100, bd=0, highlightthickness=0, bg="green")
	my_canvas1.pack(fill="both", expand=True)
	my_canvas1.create_text(180,30, text="Mal-O-Not", font=("Helvetica", 24,'bold'), fill="white")
	
	def browseFiles():
		global path
		path = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
		print(typeid+":"+path)
		rootbrowse.destroy()
	
	button_explore=Button(rootbrowse, text="Browse Files",font=("times",15),width=5,padx=40, pady=10, fg='white', bg='black', bd=0, command=browseFiles)
	button_explore_window = my_canvas1.create_window(112,90,anchor='nw', window=button_explore)

	rootbrowse.mainloop()

def clickquit():
	root.destroy()

button1=Button(root, text="IP",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=IP)
button1_window = my_canvas.create_window(100,70,anchor='nw', window=button1)

button2=Button(root, text="Email",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=Email)
button2_window = my_canvas.create_window(100,140,anchor='nw', window=button2)

button3=Button(root, text="Link",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=link)
button3_window = my_canvas.create_window(100,210,anchor='nw', window=button3)

button4=Button(root, text="Domain",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=Domain)
button4_window = my_canvas.create_window(260,70,anchor='nw', window=button4)

button5=Button(root, text="Phone no.",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=phno)
button5_window = my_canvas.create_window(260,140,anchor='nw', window=button5)

button6=Button(root, text="Files",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=files)
button6_window = my_canvas.create_window(260,210,anchor='nw', window=button6)

button7=Button(root, text="Quit",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=clickquit)
button7_window = my_canvas.create_window(180,280,anchor='nw', window=button7)

root.mainloop()
