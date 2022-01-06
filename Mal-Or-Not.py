from tkinter import *
import os
from tkinter import ttk
from tkinter import filedialog
import whois
import subprocess
from time import strftime
from bs4 import BeautifulSoup
import requests
root = Tk()
root.title('Mal-Or-Not')
root.geometry("430x200+630+350")
bg= PhotoImage(file="matrixbg.png")  

my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0,bg='black')
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0,0, image=bg, anchor="nw")

text_key= Label(my_canvas, text="Welcome To", anchor="w", justify=LEFT, font='"Helvetica" 20', bg='black', fg='white').place(relx = 0.5, rely = 0.25, anchor = 'center')
text_key= Label(my_canvas, text="Mal", anchor="w", justify=LEFT, font='"Helvetica" 20', bg='black', fg='#ff8000').place(relx = 0.367, rely = 0.55, anchor = 'center')
text_key= Label(my_canvas, text="-OR-", anchor="w", justify=LEFT, font='"Helvetica" 20', bg='black', fg='white').place(relx = 0.5, rely = 0.55, anchor = 'center')
text_key= Label(my_canvas, text="Not", anchor="w", justify=LEFT, font='"Helvetica" 20', bg='black', fg='lime').place(relx = 0.627, rely = 0.55, anchor = 'center')
text_key= Label(my_canvas, text="Loading...", anchor="w", justify=LEFT, font='"Helvetica" 12', bg='black', fg='white').place(relx = 0.92, rely = 0.95, anchor = 'center')

def destroy():
	global data
	subprocess.check_output(["sh","./speedtest.sh"])
	with open ("/tmp/speed_report.txt","r") as f:
		data=f.readline()
	root.destroy()
root.after(2000, destroy)

root.mainloop()

root = Tk()
root.title('Mal-Or-Not')
root.geometry("430x200+630+350")
bg= PhotoImage(file="matrixbg.png")  

my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0,bg='black')
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0,0, image=bg, anchor="nw")

text_key= Label(my_canvas, text="Enter Username:", anchor="w", justify=LEFT, font='"Helvetica" 15', bg='black', fg='white').place(relx = 0.25, rely = 0.3, anchor = 'center')
entry1 = Entry(root, font=("Helvitica",12),width=13, fg="black", bd=0)
entry_window1 = my_canvas.create_window(200,46,anchor='nw', window=entry1)
text_key= Label(my_canvas, text="Enter City:", anchor="w", justify=LEFT, font='"Helvetica" 15', bg='black', fg='white').place(relx = 0.25, rely = 0.5, anchor = 'center')
entry2 = Entry(root, font=("Helvitica",12),width=13, fg="black", bd=0)
entry_window2 = my_canvas.create_window(200,86,anchor='nw', window=entry2)

def storeiden():
	global city, username
	username=entry1.get()
	cityinp=entry2.get()
	city = cityinp+" weather"
	root.destroy()

buttoniden=Button(root, text="Done",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=storeiden)
buttoniden_window = my_canvas.create_window(180,130, anchor='nw', window=buttoniden)
root.mainloop()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
 
def weather(city):
	global location, weatherf
	city = city.replace(" ", "+")
	res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
	soup = BeautifulSoup(res.text, 'html.parser')
	location = soup.select('#wob_loc')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	weather = soup.select('#wob_tm')[0].getText().strip()
	weatherf=weather+"°C, "+info
weather(city)

root = Tk()
root.title('Mal-Or-Not')
root.geometry("995x510+630+250")
bg= PhotoImage(file="matrixbg.png")  

my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0,bg='black')
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg, anchor="nw")
my_canvas.create_text(430,40, text="Mal-O", font=("Helvetica", 40,'bold'), fill="white")
my_canvas.create_text(580,40, text="R-Not", font=("Helvetica", 40,'bold'), fill="black")

def my_time():
    time_string = strftime('%H:%M:%S %p \n %A \n %x') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds
my_font=('times',15,'bold') # display size and style
l1=Label(my_canvas,font=my_font,fg='black',bg='white')
l1.grid(row=1,column=1,padx=880,pady=5)

my_time()

my_canvas.create_text(100,20, text=location, font=("times", 15,'bold'), fill="white")
my_canvas.create_text(100,40, text=weatherf, font=("times", 15,'bold'), fill="white")

speed=float(data.split()[1])
if speed < 100:
	my_canvas.create_text(920,500, text=data, font=("times", 15,'bold'), fill="green")
elif speed > 100 and speed <250:
	my_canvas.create_text(920,500, text=data, font=("times", 15,'bold'), fill="orange")
else:
    my_canvas.create_text(920,500, text=data, font=("times", 15,'bold'), fill="red")


def IP():
	global typeid
	typeid='IP'
	rootentry = Tk()
	rootentry.title('IP Intel')
	rootentry.geometry("350x200+670+300")
	#bg= PhotoImage(file="matrixbg.png")
	ip_canvas = Canvas(rootentry, width=200, height=100, bd=0, highlightthickness=0, bg="black")
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
	    
	    subprocess.check_output(["./ipintel.sh", "-i", inp])
	    
	    rootip = Tk()
	    rootip.title('IP Information')
	    rootip.geometry("800x300+670+300")
	    
	    my_canvas=Canvas(rootip, bg='black', bd=0, highlightthickness=0, relief='ridge')
	    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
	    
	    with open(inp+".ip.report","r") as f:
	    	data=f.read()
	    text_key= Label(my_canvas, text=data, anchor="w", justify=LEFT, font='"Helvetica" 12', bg='black', fg='lime').grid(row=0, column=0)

	    rootip.mainloop()

	buttonentry=Button(rootentry, text="Done",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=store)
	buttonentry_window = ip_canvas.create_window(145,130, anchor='nw', window=buttonentry)

	rootentry.mainloop()
	

def Domain():
	subprocess.call(['python3','WhoIsInfo.py'])

def Email():
	global typeid
	typeid='email'
	rootentry = Tk()
	rootentry.title('Email Intel')
	rootentry.geometry("350x200+670+300")
	#bg= PhotoImage(file="matrixbg.png")
	email_canvas = Canvas(rootentry, width=200, height=100, bd=0, highlightthickness=0, bg="black")
	email_canvas.pack(fill="both", expand=True)

	#my_canvas.create_image(0,0, image=bg, anchor="nw")
	email_canvas.create_text(180,45, text="Enter Email Address:", font=("Helvetica", 18,'bold'), fill="white")
	entry = Entry(rootentry, font=("Helvitica",12),width=13, fg="black", bd=0)
	entry_window = email_canvas.create_window(115,80,anchor='nw', window=entry)
	def store():
	    global inp
	    inp=entry.get()
	    print(typeid+":"+inp)
	    rootentry.destroy()
	    
	    subprocess.check_output(["./email.sh",inp])
	    
	    rootemail = Tk()
	    rootemail.title('Email Information')
	    rootemail.geometry("250x200+670+300")
	    
	    my_canvas=Canvas(rootemail, bg='black', bd=0, highlightthickness=0, relief='ridge')
	    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
	    
	    with open("output/email/"+inp.split("@")[0]+".email.report","r") as f:		# I changed
	    	data=f.read()
	    text_key= Label(my_canvas, text=data, anchor="w", justify=LEFT, font='"Helvetica" 12', bg='black', fg='lime').grid(row=0, column=0)

	    rootemail.mainloop()

	buttonentry=Button(rootentry, text="Done",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=store)
	buttonentry_window = email_canvas.create_window(145,130, anchor='nw', window=buttonentry)

	rootentry.mainloop()

def phno():
	global typeid
	typeid='phno'
	rootentry = Tk()
	rootentry.title('Phone Number Intel')
	rootentry.geometry("350x200+670+300")
	phno_canvas = Canvas(rootentry, width=200, height=100, bd=0, highlightthickness=0, bg="black")
	phno_canvas.pack(fill="both", expand=True)

	phno_canvas.create_text(180,45, text="Enter Phone Number:", font=("Helvetica", 18,'bold'), fill="white")
	entry = Entry(rootentry, font=("Helvitica",12),width=13, fg="black", bd=0)
	entry_window = phno_canvas.create_window(115,80,anchor='nw', window=entry)
	def store():
	    global inp
	    inp=entry.get()
	    print(typeid+":"+inp)
	    rootentry.destroy()
	    
	    subprocess.check_output(["sh","./number.sh", inp])
	    
	    rootphno = Tk()
	    rootphno.title('Phone Number Information')
	    rootphno.geometry("320x170+670+300")
	    
	    my_canvas=Canvas(rootphno, bg='black', bd=0, highlightthickness=0, relief='ridge')
	    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
	    
	    with open(inp+".number.report","r") as f:
	    	data=f.read()
	    text_key= Label(my_canvas, text=data, anchor="w", justify=LEFT, font='"Helvetica" 12', bg='black', fg='lime').grid(row=0, column=0)

	    rootphno.mainloop()

	buttonentry=Button(rootentry, text="Done",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=store)
	buttonentry_window = phno_canvas.create_window(145,130, anchor='nw', window=buttonentry)

	rootentry.mainloop()


def link():
	global typeid
	typeid='url'
	rootentry = Tk()
	rootentry.title('URL Intel')
	rootentry.geometry("350x200+670+300")
	url_canvas = Canvas(rootentry, width=200, height=100, bd=0, highlightthickness=0, bg="black")
	url_canvas.pack(fill="both", expand=True)

	url_canvas.create_text(180,45, text="Enter URL:", font=("Helvetica", 18,'bold'), fill="white")
	entry = Entry(rootentry, font=("Helvitica",12),width=13, fg="black", bd=0)
	entry_window = url_canvas.create_window(115,80,anchor='nw', window=entry)
	def store():
	    global inp
	    inp=entry.get()
	    print(typeid+":"+inp)
	    rootentry.destroy()
	    
	    subprocess.check_output(["./urlreport.sh", inp])
	    
	    rooturl = Tk()
	    rooturl.title('URL Information')
	    rooturl.geometry("280x300+670+300")
	    
	    my_canvas=Canvas(rooturl, bg='black', bd=0, highlightthickness=0, relief='ridge')
	    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
	    
	    with open(inp.split("/")[2]+".url.report","r") as f:
	    	data=f.read()
	    text_key= Label(my_canvas, text=data, anchor="w", justify=LEFT, font='"Helvetica" 12', bg='black', fg='lime').grid(row=0, column=0)

	    rooturl.mainloop()

	buttonentry=Button(rootentry, text="Done",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=store)
	buttonentry_window = url_canvas.create_window(145,130, anchor='nw', window=buttonentry)

	rootentry.mainloop()

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
	my_canvas1 = Canvas(rootbrowse, width=200, height=100, bd=0, highlightthickness=0, bg="black")
	my_canvas1.pack(fill="both", expand=True)
	my_canvas1.create_text(180,30, text="Mal-O-Not", font=("Helvetica", 24,'bold'), fill="white")
	
	def browseFiles():
		global inp
		inp = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
		subprocess.check_output(["./file.sh", inp])
		rootbrowse.destroy()		
		# text_key= Label(my_canvas, text=data, anchor="w", justify=LEFT, font='"Helvetica" 12', bg='black', fg='lime').grid(row=0, column=0)

		rootentry = Tk()
		rootentry.title('File info')
		rootentry.geometry("410x600+670+300")

		main_frame=Frame(rootentry)
		main_frame.pack(fill=BOTH, expand=1)

		my_canvas1=Canvas(main_frame, bg='black', bd=0, highlightthickness=0, relief='ridge')
		my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

		my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas1.yview)
		my_scrollbar.pack(side=RIGHT, fill=Y)

		my_canvas1.configure(yscrollcommand=my_scrollbar.set)
		my_canvas1.bind('<Configure>', lambda e:my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))
		second_frame=Frame(my_canvas1, bg='black')
		my_canvas1.create_window((0,0), window=second_frame, anchor='nw')

		with open(inp.split("/")[-1].split(".")[0]+".file.report","r") as f:
			data=f.read()
		text_key= Label(my_canvas1, text=data, anchor="w", justify=LEFT, font='"Helvetica" 12', bg='black', fg='lime').grid(row=0, column=0)

		rootentry.mainloop()
	
	button_explore=Button(rootbrowse, text="Browse Files",font=("times",15),width=5,padx=40, pady=10, fg='white', bg='black', bd=0, command=browseFiles)
	button_explore_window = my_canvas1.create_window(112,90,anchor='nw', window=button_explore)

	rootbrowse.mainloop()

def clickquit():
	root.destroy()

button1=Button(my_canvas, text="IP",font=("times",17,'bold'),width=5,padx=15, pady=7, fg='black', bg='white', bd=0, command=IP, activebackground="black", activeforeground="white")
button1_window = my_canvas.create_window(300,100,anchor='nw', window=button1)

button2=Button(my_canvas, text="Email",font=("times",17,'bold'),width=5,padx=15, pady=7, fg='black', bg='white', bd=0, command=Email, activebackground="black", activeforeground="white")
button2_window = my_canvas.create_window(200,240,anchor='nw', window=button2)

button3=Button(my_canvas, text="Url",font=("times",17,'bold'),width=5,padx=15, pady=7, fg='black', bg='white', bd=0, command=link, activebackground="black", activeforeground="white")
button3_window = my_canvas.create_window(300,380,anchor='nw', window=button3)

button4=Button(my_canvas, text="Domain",font=("times",17,'bold'),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=Domain, activebackground="white", activeforeground="black")
button4_window = my_canvas.create_window(600,100,anchor='nw', window=button4)

button5=Button(my_canvas, text="Phone no.",font=("times",17,'bold'),width=7,padx=15, pady=10, fg='white', bg='black', bd=0, command=link, activebackground="white", activeforeground="black")
button5_window = my_canvas.create_window(700,240,anchor='nw', window=button5)

button6=Button(my_canvas, text="Files",font=("times",17,'bold'),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=files, activebackground="white", activeforeground="black")
button6_window = my_canvas.create_window(600,380,anchor='nw', window=button6)

button7=Button(my_canvas, text="Quit",font=("times",17,'bold'),width=5,padx=15, pady=7, fg='red', bg='black', bd=0, command=clickquit, activebackground="red", activeforeground="black")
button7_window = my_canvas.create_window(20,450,anchor='nw', window=button7)

root.mainloop()
