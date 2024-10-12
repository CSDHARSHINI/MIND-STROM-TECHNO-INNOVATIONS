## GUI LIBRARY
import tkinter as tk
from tkinter import *

## IMAGE IMPORTING
from PIL import Image, ImageTk

## files and directory
import os
from tkinter import messagebox

import pymysql

class event():
    def __init__(self, root):
        self.root=root
        self.root.title("EVENT MANAGEMENT APP")

class firstpg():
    def __init__(self, root):
        self.root= root

## image  for gui app
        self.image = Image.open("i1.jpg")
        self.desired_width=1500
        self.desired_height=850
        self.image=self.image.resize((self.desired_width, self.desired_height))

        self.img = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(root, image= self.img)
        self.label.pack()

##label widget and it is display in main frame

        self.label = tk.Label(root, text= "MAKING YOUR SPECIAL DAY LOOK LIKE YOUR DREAM" , bg ="lightyellow" , font= " Publico", wraplength= "600" , padx=20, pady=20)
        self.label.place(x=750, y=50, anchor="center")

##entry-1 label
        self.label = tk.Label(root, text= "Every day of our life is NEW OCCASSION so, LIVE IN THE MOMENT. Make your day as LOVEABLE MEMORIES" , bg ="lightyellow" , font= " Publico", wraplength= "1600" , padx=20, pady=10)
        self.label.place(x=340, y=480)

### button
        self.btn = Button(root, text="REGISTER HERE",font= " Publico", wraplength= "600",command=self.reg_data,bg="lightblue")
        self.btn.place( x=650, y=600)

 ##################----------------------------------------------------------------------------------------------------------------------------------------------------   
    
    def reg_data(self):
        self.new_window=Toplevel(self.root)
        self.app = reg(self.new_window)
###########----------------------------------------------------------------------------------------event app-------------------------------------------------------------
class reg:
    def __init__(self,root):
         self.root=root  
         self.root.title("Registration form")
         self.image = Image.open("i3.jpg")
    
         self.desired_width=1500
         self.desired_height=850
         self.image=self.image.resize((self.desired_width, self.desired_height))

         self.img = ImageTk.PhotoImage(self.image)
         self.label = tk.Label(root, image= self.img)
         self.label.pack()

         
         self.label = tk.Label(root, text= "EVENT DETAILS" , bg ="lightyellow" , font= " Publico", wraplength= "300" , padx=20, pady=20)
         self.label.place(x=980, y=70, anchor="center",width=200)


         self.fr=Frame(root,bg="Lavender",bd=50)
         self.fr.place(x=150,y=140, width=500, height=500)


         self.label1 = tk.Label(root, 
                       text=" \n \n  Wishing you a year filled with love, laughter, and adventure.\n \n \n Feeling the rhythm of the music and dancing into the night.\n \n \n A celebration of culture, music, art and the joy of being alive \n \n \n A day filled with teamwork, dedication, and the pursuit of victory\n \n \n Spreading good vibes and positive energy through the power of music \n \n \n Creating memories that will warm your heart after the holiday season is over \n \n \n Bringing together the brightest culinary minds for an epic food extravaganza \n \n", 
                       fg="red", 
                       wraplength=410)
         self.label1.place(x=190, y=210)



         self.var_events= StringVar()
         self.var_Name= StringVar()
         self.var_date= StringVar()
         self.var_time= StringVar()
         self.var_people=StringVar()
         self.var_venue= StringVar()
         self.var_mailid= StringVar()
         self.var_mobile_no = StringVar()
         self.var_address = StringVar()

      
    
         self.event=Label(root,text=" EVENT NAME ",font="Arial", fg="white",bg="blue")
         self.event.place(x=730, y=140,width=160)
         self.event.entry=tk.Entry(root, font=("Arial"), bg="white",textvariable=self.var_events)
         self.event.entry.place(x=900, y=140,width=300)

         self.name=Label(root,text=" NAME ",font="Arial", fg="white",bg="blue")
         self.name.place(x=730, y=200,width=160)
         self.name.entry=tk.Entry(root, font=("Arial"), bg="white",textvariable=self.var_Name)
         self.name.entry.place(x=900, y=200,width=300)
 
         self.date=Label(root,text=" DATE ",font="Arial", fg="white",bg="blue")
         self.date.place(x=730, y=260,width=160)
         self.date.entry=tk.Entry(root, font=("Arial"), bg="white",textvariable=self.var_date)
         self.date.entry.place(x=900, y=260,width=300)

         self.time=Label(root,text=" TIMING",font="Arial", fg="white",bg="blue")
         self.time.place(x=730, y=320,width=160)
         self.time.entry=tk.Entry(root, font=("Arial"), bg="white",textvariable=self.var_time)
         self.time.entry.place(x=900, y=320,width=300)



         self.people=Label(root,text="VISITOR",font="Arial", fg="white",bg="blue")
         self.people.place(x=730, y=380,width=160)
         self.people.entry=tk.Entry(root, font=("Arial"), bg="white",textvariable=self.var_people)
         self.people.entry.place(x=900, y=380,width=300)

         
         self.venue=Label(root,text=" VENUE ",font="Arial", fg="white",bg="blue")
         self.venue.place(x=730, y=440,width=160)
         self.venue.entry=tk.Entry(root, font=("Arial"), bg="white",textvariable=self.var_venue)
         self.venue.entry.place(x=900, y=440,width=300)



         
         self.mail=Label(root,text=" E-MAIL ID ",font="Arial", fg="white",bg="blue")
         self.mail.place(x=730, y=500,width=160)
         self.mail.entry=tk.Entry(root, font=("Arial"), bg="white",textvariable=self.var_mailid)
         self.mail.entry.place(x=900, y=500,width=300)

     
         self.num=Label(root,text=" PHONE NUMBER",font="Arial", fg="white",bg="blue")
         self.num.place(x=730, y=560,width=160)
         self.num.entry=tk.Entry(root, font=("Arial"), bg="white",textvariable=self.var_mobile_no)
         self.num.entry.place(x=900, y=560,width=300)

         self.address=Label(root,text=" ADDRESS ",font="Arial", fg="white",bg="blue")
         self.address.place(x=730, y=620,width=160)
         self.address.entry=tk.Entry(root, font=("Arial"), bg="white",textvariable=self.var_address)
         self.address.entry.place(x=900, y=620,width=300)

         ####BUTTON----------------------------------------------------------------------
         self.button =Button(root ,text="SUBMIT",fg="black",bg="pink",command=self.er)
         self.button.place(x=930,y=700,width=150)

         #######----------------------------------------------------
    def events(self):
        if self.var_events.get()==" " or self.var_date.get()==" " or self.var_people.get()=="" or self.var_venue.get()==" " or self.var_mailid=="":
            messagebox.showerror("Error","all fields are required")
        
        try:
            conn= pymysql.connect(host='127.0.0.1',user='root',password='',database='event_management')
            cursor=conn.cursor()
            query=('SELECT * FROM eventslist WHERE mailid=%s;')
            value=(self.var_mailid.get(),)
            cursor.execute(query,value)
            givendata=cursor.fetchone()
            if givendata:
                messagebox.showerror("Error"," Your event will not be conformed")
            else:
                cursor.execute('INSERT INTO eventslist(events, Name, date, time, people, venue, mailid, mobile_no, address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_events.get(),
                    self.var_Name.get(),
                    self.var_date.get(),
                    self.var_time.get(),
                    self.var_people.get(),
                    self.var_venue.get(),
                    self.var_mailid.get(),
                    self.var_mobile_no.get(),
                    self.var_address.get()
                    ))
                conn.commit()
           
                messagebox.showinfo("Success","Register Sucessfully./n  YOUR EVENTS WILL HAVE MORE FUN ")
                    ####clear the data
                self.var_events.set("")
                self.var_Name.set("")
                self.var_date.set("")
                self.var_time.set("")
                self.var_people.set("")
                self.var_venue.set("")
                self.var_mailid.set("")
                self.var_mobile_no.set("")
                self.var_address.set("")

                
        except pymysql.MySQLError as e:
            print("Error connecting to MySQL:", e)
            messagebox.showerror("Error", f"An error occurred: {e}")
        
        finally:
             if conn:
                  conn.close()


##################----------------------------------------------------------------------------------------------------------------------------------------------------   
    
    def er(self):
        self.new_window2=Toplevel(self.root)
        self.app = er(self.new_window2)
#########------------------------------------------------------------------------------------------------
class er:
    def __init__(self,root):
        self.root=root
        self.root.title("Congratulations")
        self.root.geometry("620x400")
        

        self.bg=ImageTk.PhotoImage(file=r"C:\ML projects\gui\i2.jpg")
         
        self.label=tk.Label(self.root, image=self.bg)
        self.label.place(x=0, y=0) 

      
        self.label =tk.Label(root,text="\n Congratulations! your events will successfully registered \n \n for furthur information we contact you soon. \n  ", fg="red",bg="lightyellow",wraplength=300)
        self.label.place(x=150, y=150)












##################-------------------------------------------------------------------------------------------
if __name__ =="__main__":
    root = tk.Tk()
    app = firstpg(root)
 
    root.title("EVENT MANAGEMENT APP")
    ##run the mainloop
    root.mainloop()