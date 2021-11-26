import json ## json import
import pycountry ## pycountry import
from tkinter import Tk, Label, Button, Entry
from phone_iso3166.country import phone_country

### After adding above library you need to use following source code ###
class Location_Tracker:
    def __init__(self, App):
        self.window = App
        self.window.title("Phone number Info App")
        self.window.geometry("500x800")
        self.window.configure(bg="#3f5efb")
        self.window.resizable(False, False)

        #___________Application menu_____________
        Label(App, text="Enter a phone number",fg="white", font=("Times", 20), bg="#3f5efb").place(x=150,y= 30)
        self.phone_number = Entry(App, width=16, font=("Arial", 15), relief="flat")
        self.track_button = Button(App, text="Get Info", bg="#22c1c3", relief="sunken")
        self.country_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")

        #___________Place widgets on the window______
        self.phone_number.place(x=170, y=120)
        self.track_button.place(x=200, y=200)
        self.country_label.place(x=100, y=280)

        #__________Linking button with countries ________
        self.track_button.bind("<Button-1>", self.Track_location)
        #255757294146
    
    def Track_location(self,event):
        phoneNumber = self.phone_number.get()
        country = "Country is Unknown"
        if phoneNumber: 
            if hasattr(tracked, "official_name"):
                        country = tracked.official_name
            else:
		country = tracked.name
        self.country_label.configure(text=country)



PhoneTracker = Tk()
MyApp = Location_Tracker(PhoneTracker)
PhoneTracker.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------#
from tkinter import *

from tkinter import ttk

import phonenumbers

from phonenumbers import geocoder, carrier

from phonenumbers import timezone 

from bs4 import BeautifulSoup

import mechanize



rootentry = Tk()

rootentry.title('Mal-Or-Not')

rootentry.geometry("350x200+670+300")

bg= PhotoImage(file="matrixbg.png")

my_canvas = Canvas(rootentry, width=200, height=100, bd=0, highlightthickness=0, bg="green")

my_canvas.pack(fill="both", expand=True)



my_canvas.create_image(0,0, image=bg, anchor="nw")

my_canvas.create_text(180,45, text="Enter Domain name:", font=("Helvetica", 18,'bold'), fill="white")

entry = Entry(rootentry, font=("Helvitica",12),width=13, fg="black", bd=0)

entry_window = my_canvas.create_window(115,80,anchor='nw', window=entry)

typeid='Domain'

def store():

    global inp

    inp=entry.get()

    print(typeid+":"+inp)

    rootentry.destroy()



buttonentry=Button(rootentry, text="Done",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=store)

buttonentry_window = my_canvas.create_window(145,130, anchor='nw', window=buttonentry)



rootentry.mainloop()



w = whois.whois(inp)



rootentry = Tk()

rootentry.title('Domain info')

rootentry.geometry("410x600+670+300")



main_frame=Frame(rootentry)

main_frame.pack(fill=BOTH, expand=1)



my_canvas=Canvas(main_frame)

my_canvas.pack(side=LEFT, fill=BOTH, expand=1)



my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)

my_scrollbar.pack(side=RIGHT, fill=Y)



my_canvas.configure(yscrollcommand=my_scrollbar.set)

my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))



second_frame=Frame(my_canvas)



my_canvas.create_window((0,0), window=second_frame, anchor='nw')





my_canvas1 = Canvas(second_frame, width=400, height=2000, bd=0, highlightthickness=0, bg="black")

my_canvas1.pack(fill="both", expand=True)





number = input("Enter the phone number(+91..):")

phoneNumber = phonenumbers.parse(number)

  

Carrier = carrier.name_for_number(phoneNumber, 'en')

Region = geocoder.description_for_number(phoneNumber, 'en')

timeZone = timezone.time_zones_for_number(phoneNumber)

valid = phonenumbers.is_valid_number(phoneNumber)



mc = mechanize.Browser()

mc.set_handle_robots(False)



url = 'https://www.findandtrace.com/trace-mobile-number-location'

mc.open(url)



mc.select_form(name='trace')

mc['mobilenumber'] = number # Enter a mobile number

res = mc.submit().read()



soup = BeautifulSoup(res,'html.parser')

tbl = soup.find_all('table',class_='shop_table')

#print(tbl)





data = tbl[0].find('tfoot')

c=0

for i in data:

    c+=1

    if c in (1,4,6,8):

        continue

    th = i.find('th')

    td = i.find('td')

    print(th.text,td.text)





data = tbl[1].find('tfoot')

c=0

for i in data:

 c+=1

    if c in (2,20,22,26): 

        th = i.find('th')

        td = i.find('td')

        print(th.text,td.text)

  

print("Is the phone number valid: ",valid) 

print("Servide provider:          ",Carrier)

print("Country:                   ",Region)

print("Timezone:                  ",timeZone)





rootentry.mainloop()
