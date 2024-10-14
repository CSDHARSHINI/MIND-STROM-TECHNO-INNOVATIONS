import tkinter as tk
from tkinter import ttk 

from tkinter import *
from tkinter import messagebox, StringVar, BooleanVar
import cv2
from datetime import datetime
from PIL import Image, ImageTk
import pymysql


def main():
    root = tk.Tk()
    root.geometry("1600x800") 
    root.title("EMPLOYEES MANAGEMENT SYSTEM")
    video_path = "v1.mp4"  # replace with your video file path
    app=VideoPlayer(root, video_path)
   
    root.mainloop()




class LOGIN:
    def __init__(self, root) :
        self.root=root
        self.root.title("Login")

class VideoPlayer:
    def __init__(self, root, video_path):
        self.root = root
        self.root.title("Login")
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)

        ## video label
        self.video_label = Label(root)
        self.video_label.place(x=0, y=0, relwidth=1, relheight=1)  

        ## login frame  entry
        self.login_frame = Frame(root,bg="lightblue",bd=5)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        ## login details
        self.user_var = StringVar()
        self.var_mail = StringVar()
        self.password_var = StringVar()

 ##login label
             ## username entry
        Label(self.login_frame, text="Usermail", bg="white").grid(row=0, column=0, pady=5)
        self.user_entry = Entry(self.login_frame, textvariable=self.user_var)
        self.user_entry.grid(row=0, column=1, pady=5)

             ## password entry
        Label(self.login_frame, text="Password:", bg="white").grid(row=1, column=0, pady=5)
        self.password_entry = Entry(self.login_frame, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)

         # Login button
        self.login_button = Button(self.login_frame, text="Login", command=self.login_checking)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

## register labels

         # register button
        self.register_button = Button(self.login_frame, text="Create account",command=self.register,bg="white")
        self.register_button.grid(row=5, column=1, columnspan=1, pady=8)

         # forgot_password button
        self.forgot_password_button = Button(self.login_frame, text="forgotpassword",bg="white", command=self.register)
        self.forgot_password_button.grid(row=5, column=0, columnspan=1, pady=8)





        self.update_video()

    def update_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        self.root.after(30, self.update_video)



#### ----------------------------------register frame 2------------------------------------------------------------------------------------------------------------------------------------------------
    def register(self):
        self.new_window1=Toplevel(self.root)
        self.app=register(self.new_window1)


    def login_checking(self):
          username = self.user_var.get()
          password = self.password_var.get()

          if username == "" and password == "":
            print("Login successful")
            self.on_button_click()
            self.login_success()
           
          else:
              conn= pymysql.connect(host='localhost',user='DHARSH',password='DN',database='employees_management')
              cursor=conn.cursor()
              cursor.execute('SELECT * FROM registration WHERE mail=%s and pass_word=%s', (
                        self.user_var.get(),
                        self.password_var.get()
                        
              ))
              self.user_var.set("")
              self.password_var.set("")
              data=cursor.fetchone()
              print(data)
              if data!=None:
                  open_main=messagebox.askyesno("YesNo","your access accepted")
                  if open_main>0:
                      self.new_window2=Toplevel(self.root)
                      self.app=Mainframe(self.new_window2)
                  else:
                      if not open_main:
                          return
               
              else:
                  messagebox.showerror("Error"," Invalid User")
           
              conn.commit()
              conn.close()
                  
##----------------------------------------------------------------------------------------

    def login_success(self):
        self.login_frame.destroy()

    def on_button_click(self):
         messagebox.showinfo("Information", "Login successfully")
        
    def __del__(self):
        self.cap.release()

##----------------------------------#### registration window 1-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class register:
    def __init__(self, root) : 
        self.root=root  
        self.root.title("Registration form")
        self.root.geometry("1200x600")     

## registration  variablesdetails
        self.var_reg_fname = StringVar()
        self.var_reg_lname= StringVar()
        self.var_dob = StringVar()
        self.var_mail = StringVar()
        self.var_gender = StringVar()
        self.var_mobile = StringVar()
        self.var_pass_word = StringVar()
        self.var_conf_pass_word = StringVar()
        self.var_chk=BooleanVar()

         ##background image
        self.bg=ImageTk.PhotoImage(file=r"C:\ML projects\employ\r1.jpg")
        self.lbel=tk.Label(self.root, image=self.bg)
        self.lbel.place(x=0, y=0)  

        ## register frame
        self.fr=Frame(root,bg="lightyellow",bd=50)
        self.fr.place(x=520,y=100, width=500, height=500)

##register label
        self.register_label=Label(root, text="REGISTRATION FORM", font="Arial",fg="lightgreen")
        self.register_label.place(x=700,y=60, anchor="center")
       
        ## reg name
        self.reg_fname=Label(root, text="First Name:", bg="lightblue")
        self.reg_fname.place(x=650,y=150,anchor="center")
        self.reg_fname.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_reg_fname)
        self.reg_fname.entry.place(x=600,y=160,width=150)

        ## register last name
        self.reg_lname=Label(root, text="Last Name:", bg="lightblue")
        self.reg_lname.place(x=850,y=150,anchor="center")## Y=HORIZONTAL, X=VERTICAL
        self.reg_lname.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_reg_lname)
        self.reg_lname.entry.place(x=800,y=160,width=150)

        ## register dob
        self.dob=Label(root, text="Date Of Birth:", bg="lightblue")
        self.dob.place(x=650,y=250,anchor="center")
        self.dob.entry=tk.Entry(root,text="yy-mm-DD",font=("Arial"),bg="White",textvariable=self.var_dob)
        self.dob.entry.place(x=600,y=260,width=150)

        ## mail
        self.mail=Label(root,text="Email Id:", bg="lightblue")
        self.mail.place(x=850,y=250,anchor="center")
        self.mail.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_mail)
        self.mail.entry.place(x=800,y=260,width=150)

        ## gender
        self.gender=Label(root, text="Gender:", bg="lightblue")
        self.gender.place(x=650,y=350,anchor="center")
        self.gender.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_gender)
        self.gender.entry.place(x=600,y=360,width=150)

        self.combo=ttk.Combobox(root)
        self.combo["values"]=("select","Male","Female")
        self.combo.place(x=600,y=360,width=150)

       
        ## mobile number
        self.mobile=Label(root, text="Mobile Number:", bg="lightblue")
        self.mobile.place(x=850,y=350,anchor="center")
        self.mobile.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_mobile)
        self.mobile.entry.place(x=800,y=360,width=150)

        ##password
        self.pass_word=Label(root, text=" Set Password:", bg="lightblue")
        self.pass_word.place(x=650,y=450,anchor="center")
        self.pass_word.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_pass_word)
        self.pass_word.entry.place(x=600,y=460,width=150)

        ## conform password
        self.conf_password=Label(root, text=" Confirm  Password:", bg="lightblue")
        self.conf_password.place(x=850,y=450,anchor="center")
        self.conf_password.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_conf_pass_word)
        self.conf_password.entry.place(x=800,y=460,width=150)


        ##checkbutton

        self.checkbtn=Checkbutton(root,text="Agree to use your data for our company purpose.",font="Black",bg="lightyellow")
        self.checkbtn.place(x=600,y=500)

        ### registration button
        reg_button=Button(root ,text="Submit",command= self.register_Data)
        reg_button.place(x=600,y=550,width=100)
         
        ## back to login
        reg_button=Button(root ,text="Back to Login",command="VideoPlayer")
        reg_button.place(x=800,y=550,width=100)
         

        ##function
    def register_Data(self):
        if self.var_reg_fname.get()==" " or self.var_mail.get()==" " or self.var_mail.get()=="" or self.var_mobile.get()==" " or self.checkbtn=="":
            messagebox.showerror("Error","all fields are required")
        elif self.var_pass_word.get()!=self.var_conf_pass_word.get():
            messagebox.showerror("Error","password and conform password must be same")
        elif self.var_chk.get():
            messagebox.showerror("Error","please check the information")
        else:
            try:
                conn= pymysql.connect(host='localhost',user='DHARSH',password='DN',database='employees_management')
                cursor=conn.cursor()
                query=('SELECT * FROM registration WHERE mail=%s;')
                value=(self.var_mail.get(),)
                cursor.execute(query,value)
                data=cursor.fetchone()
                print(data)
                if data:
                    messagebox.showerror("Error","User already exists,please try with another email")
                else:
                    cursor.execute('INSERT INTO registration(reg_fname, reg_lname, dob, mail, gender, mobile, pass_word, conf_pass_word) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (
                        self.var_reg_fname.get(),
                        self.var_reg_lname.get(),
                        self.var_dob.get(),
                        self.var_mail.get(),
                        self.var_gender.get(),
                        self.var_mobile.get(),
                        self.var_pass_word.get(),
                        self.var_conf_pass_word.get()
                        ))
                    conn.commit()
           
                    messagebox.showinfo("Success","Register Sucessfully")
                
            except pymysql.MySQLError as e:
                print("Error connecting to MySQL:", e)
                messagebox.showerror("Error", f"An error occurred: {e}")
        
            finally:
             if conn:
                conn.close()



###--------------------------------------------------------------------------------------------------------------------------------------
###############-----------------------------mainframe------------------------------------------------------------------------------------




class Mainframe:
    def __init__(self, root):
        self.root=root
        self.root.title("EMPLOYEES MANAGEMENT")
        
 ##----------------------------------DETAILS---------------------------------------------------------------------------------------------
        self.var_Id = StringVar()
        self.var_Name= StringVar()
        self.var_department = StringVar()
        self.var_Role= StringVar()
        self.var_mail = StringVar()
        self.var_mobile = StringVar()
        self.var_address = StringVar()
        self.var_login_time= StringVar()
        self.var_logout_time= StringVar()
     
#-----------------------------------------------------------------------------------------------------------------------------------------
     ##background image
        self.image = Image.open("r2.jpg")
        self.desired_width=1500
        self.desired_height=850
        self.image=self.image.resize((self.desired_width, self.desired_height))


        self.img = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(root, image= self.img)
        self.label.pack()

 ##----------------------------- main frame------------------------------------------------------------------------------------------------
       ### employees main frame
        self.empls=Label(root, text="EMPLOYERS WORLD", font="Arial, 28",fg="Blue",bg="black")
        self.empls.place(x=800,y=60, anchor="center")

        ###  empls id---------------------------------------------------------------------------------------------------------------------
        self.Id=Label(root, text="Employer Id:",font="Arial", fg="red",bg="black")
        self.Id.place(x=150,y=150,anchor="center",width=150)
        self.Id.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_Id)
        self.Id.entry.place(x=150,y=160,width=150)
         
 ## empls name
        self.Name=Label(root, text="Employer Name:",font="Arial", fg="red",bg="black")
        self.Name.place(x=150,y=200,anchor="center",width=150)
        self.Name.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_Name)
        self.Name.entry.place(x=150,y=210,width=150)

        # empls department
        self.department=Label(root, text="Emp.Department:",font="Arial", fg="red",bg="black")
        self.department.place(x=150,y=250,anchor="center",width=150)
        self.department.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_department)
        self.department.entry.place(x=150,y=260,width=150)

         ## empls ROLE
        self.Role=Label(root, text="Emp.Role:",font="Arial", fg="red",bg="black")
        self.Role.place(x=150,y=300,anchor="center",width=150)
        self.Role.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_Role)
        self.Role.entry.place(x=150,y=310,width=150)

         ## empls mail
        self.mail=Label(root, text="Emp.mailId:",font="Arial", fg="red",bg="black")
        self.mail.place(x=150,y=350,anchor="center",width=150)
        self.mail.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_mail)
        self.mail.entry.place(x=150,y=360,width=150)

         ## empls mobile
        self.mobile=Label(root, text="Emp.Number:",font="Arial", fg="red",bg="black")
        self.mobile.place(x=150,y=400,anchor="center",width=150)
        self.mobile.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_mobile)
        self.mobile.entry.place(x=150,y=410,width=150)

         ## empls Address
        self.address=Label(root, text="Emp.Address:",font="Arial", fg="red",bg="black")
        self.address.place(x=150,y=450,anchor="center",width=150)
        self.address.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_address)
        self.address.entry.place(x=150,y=460,width=150)

         ## empls salary
        self.login_time=Label(root, text="Emp.logintime:",font="Arial", fg="red",bg="black")
        self.login_time.place(x=150,y=500,anchor="center",width=150)
        self.login_time=Label(root, text="(YYYY-MM-DD-HH-MM-SS)",font="Arial", fg="red",bg="black")
        self.login_time.place(x=170,y=530,anchor="center",width=250)
        self.login_time.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_login_time)
        self.login_time.entry.place(x=150,y=540,width=150)


           ## empls logout
        self.logout_time=Label(root, text="Emp.logouttime:",font="Arial", fg="red",bg="black")
        self.logout_time.place(x=150,y=580,anchor="center",width=150)
        self.logout_time=Label(root, text="(YYYY-MM-DD-HH-MM-SS)",font="Arial", fg="red",bg="black")
        self.logout_time.place(x=170,y=610,anchor="center",width=250)
        self.logout_time.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_logout_time)
        self.logout_time.entry.place(x=150,y=620,width=150)

        ### submit button
        emp_button=Button(root ,text="SUBMIT", fg="black",font="Arial", bg="red",command=self.empdata)
        emp_button.place(x=150,y=700,width=100)

#-----------------------------------------------addd details button-----------------------------------------------------------------------
     ### ADD button
        add_button=Button(root ,text="Add Details", fg="white",font="Arial", bg="black", command="self.fetch_data")
        add_button.place(x=500,y=200,width=150)

         ### update button
        update_button=Button(root ,text="Update Details", fg="white",font="Arial", bg="black",command=self.adddet)
        update_button.place(x=750,y=200,width=150)

        ## view button
        view_button=Button(root ,text="Edit Details", fg="white",font="Arial", bg="black", command=self.adddet)
        view_button.place(x=1000,y=200,width=150)
     
           ## delete button
        del_button=Button(root ,text="Delete Details", fg="white",font="Arial", bg="black", command=self.delete_item)
        del_button.place(x=1250,y=200,width=150)

## frame

        fr_detail=tk.Frame(self.root,bg="lightyellow",bd=5)
        fr_detail.place(x=500,y=350,width=900,height=300)

        treeview=ttk.Treeview(fr_detail)
        treeview['columns']=("Id", "Name","department", "Role", "Login_Time")
        
        treeview.column("#0", width=10,minwidth=10)
        treeview.column("Id", anchor=tk.W, width=30)
        treeview.column("Name", anchor=tk.W, width=30)
        treeview.column("department", anchor=tk.CENTER, width=30)
        treeview.column("Role", anchor=tk.W, width=30)
        treeview.column("Login_Time", anchor=tk.W, width=30)

        treeview.heading("#0", text="  EMP.NO  ",anchor=tk.W)
        treeview.heading("Id",text="  ID  " ,anchor=tk.W)
        treeview.heading("Name", text="  NAME  ", anchor=tk.W)
        treeview.heading("department", text="  DEPARTMENT  ", anchor=tk.CENTER)
        treeview.heading("Role", text="  ROLE  ", anchor=tk.W)
        treeview.heading("Login_Time", text=" MAIL ID ", anchor=tk.W)
        
        treeview.pack(fill='both')

        self.fetch_data(treeview)
#===================================================================================================================================================
    def on_button_click(self):
      self.fetch_data(self.treeview)
    
#------------------------------------#---------------------------------------------------------------------------------------------------------------
    ###-------------------------------------------------------------------------------------------------------------------------------------------------------------
    def fetch_data(self, treeview):
          try:
              conn= pymysql.connect(host='localhost',user='DHARSH',password='DN',database='employees_management')
              cursor=conn.cursor()


              cursor.execute("SELECT * FROM empdetails")
              data=cursor.fetchall()
              if len(data)!=0:
                  for row in data:
                      treeview.insert('', tk.END, values=row)
          except Exception as e:
              print(f"Error fetching data: {e}")
          finally:
            if conn:
                conn.close()

 #===================================================================================================================================================================
    def delete_item(Self):
        messagebox.showinfo("Success","your Data will be Delete in database")
        

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def delete_item(self, treeview):
        selected_item = treeview.selection()
        if selected_item:
            self.treeview.delete(selected_item)

#----------------------------------------------------def calling function----------------------------------------------------------------------------------------------
    def empdata(self):
        conn= pymysql.connect(host='localhost',user='DHARSH',password='DN',database='employees_management')
        try:
            cursor=conn.cursor()
            query=('SELECT * FROM empdetails  WHERE mail=%s;')
            value=(self.var_mail.get(),)
            cursor.execute(query,value)
            data=cursor.fetchone()
        
            if not data:
                cursor.execute('INSERT INTO empdetails(Id, Name, department, Role, mail, mobile, address, login_time, logout_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,0)', (
                self.var_Id.get(),
                self.var_Name.get(),
                self.var_department.get(),
                self.var_Role.get(),
                self.var_mail.get(), 
                self.var_mobile.get(), 
                self.var_address.get(),
                self.var_login_time.get(),
       
            
                )
                )
                conn.commit()
                messagebox.showinfo("Success","your Data will be submitted")
               ## clear the data
                self.var_Id.set("")
                self.var_Name.set("")
                self.var_department.set("")
                self.var_Role.set("")
                self.var_mail.set("")
                self.var_mobile.set("")
                self.var_address.set("")
                self.var_login_time.set("")
                self.var_logout_time.set("")
            
            else:
                 if data[8] == 0 or self.var_logout_time.get():
                  query = "UPDATE empdetails SET logout_time=%s WHERE mail=%s"
                  values = (self.var_logout_time.get(), self.var_mail.get())
                  cursor.execute(query, values)
                  conn.commit()
                  messagebox.showinfo("Success", "Thanks! Have a nice day.see you tomorrow")
                    ## clear the data
                 self.var_Id.set("")
                 self.var_Name.set("")
                 self.var_department.set("")
                 self.var_Role.set("")
                 self.var_mail.set("")
                 self.var_mobile.set("")
                 self.var_address.set("")
                 self.var_login_time.set("")
                 self.var_logout_time.set("")
            


        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
        finally:
            conn.close()
###----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def adddet(self):
        self.new_window3=Toplevel(self.root)
        self.app=inn(self.new_window3)


class inn:
    def __init__(self, root) :
        self.root=root
        self.root.title("Details form")

        self.var_Id = StringVar()
        self.var_Name= StringVar()
        self.var_dob= StringVar()
        self.var_department = StringVar()
        self.var_mail = StringVar()
        self.var_mobile = StringVar()
        self.var_address = StringVar()
        self.var_salary= StringVar()
        self.var_bloodgrp= StringVar()
        self.var_Aadhaar= StringVar()
        self.var_pan_number= StringVar()
        self.var_Native= StringVar()
        self.var_Nationality = StringVar()
        self.var_Identity = StringVar()





         ##background image
        self.image = Image.open("r3.jpg")
        self.desired_width=1500
        self.desired_height=850
        self.image=self.image.resize((self.desired_width, self.desired_height))

        self.img = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(root, image= self.img)
        self.label.pack()

###----------------------------------------------------------------------------
         ### employees main frame
        self.empls=Label(root, text="PERSONAL DETAILS", font="Arial, 28",fg="black",bg="pink")
        self.empls.place(x=750,y=60, anchor="center")


        
        ##details
        self.Id=Label(root, text="Employer Id:",font="Arial", fg="grey",bg="pink")
        self.Id.place(x=350,y=150,anchor="center",width=150)
        self.Id.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_Id)
        self.Id.entry.place(x=380,y=160,width=200)
         

        ## empls name
        self.Name=Label(root, text="Employer Name:",font="Arial", fg="grey",bg="pink")
        self.Name.place(x=350,y=230,anchor="center",width=150)
        self.Name.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_Name)
        self.Name.entry.place(x=380,y=240,width=200)

        ## register dob
        self.dob=Label(root, text="Date Of Birth:",font="Arial", fg="grey",bg="pink")
        self.dob.place(x=350,y=310,anchor="center",width=150)
        self.dob=Label(root, text="(YYYY-MM-DD)",font="Arial", fg="grey",bg="pink")
        self.dob.place(x=380,y=340,anchor="center",width=150)
        self.dob.entry=tk.Entry(root,text="yy-mm-DD",font=("Arial"),bg="White",textvariable=self.var_dob)
        self.dob.entry.place(x=380,y=350,width=200)

        # empls department
        self.department=Label(root, text="Emp.Department:",font="Arial", fg="grey",bg="pink")
        self.department.place(x=350,y=420,anchor="center",width=150)
        self.department.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_department)
        self.department.entry.place(x=380,y=430,width=200)

          ## empls mail
        self.mail=Label(root, text="Emp.mailId:",font="Arial", fg="grey",bg="pink")
        self.mail.place(x=350,y=500,anchor="center",width=150)
        self.mail.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_mail)
        self.mail.entry.place(x=380,y=510,width=200)

         ## empls mobile
        self.mobile=Label(root, text="Emp.Number:",font="Arial", fg="grey",bg="pink")
        self.mobile.place(x=350,y=580,anchor="center",width=150)
        self.mobile.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_mobile)
        self.mobile.entry.place(x=380,y=590,width=200)

         ## empls Address
        self.address=Label(root, text="Emp.Address:",font="Arial", fg="grey",bg="pink")
        self.address.place(x=350,y=660,anchor="center",width=150)
        self.address.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_address)
        self.address.entry.place(x=380,y=670,width=200)


         # empls salary
        self.salary=Label(root, text="Emp.Salary:",font="Arial", fg="grey",bg="pink")
        self.salary.place(x=950,y=150,anchor="center",width=150)
        self.salary.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_salary)
        self.salary.entry.place(x=980,y=160,width=200)

          ## empls bloodgrp
        self.bloodgrp=Label(root, text="Emp.bloodGrp:",font="Arial", fg="grey",bg="pink")
        self.bloodgrp.place(x=950,y=230,anchor="center",width=150)
        self.bloodgrp.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_bloodgrp)
        self.bloodgrp.entry.place(x=980,y=240,width=200)

         ## empls aadhaar number
        self.mobile=Label(root, text="Aadhaar Number",font="Arial", fg="grey",bg="pink")
        self.mobile.place(x=950,y=310,anchor="center",width=150)
        self.mobile=Label(root, text="(1234-5678-9000)",font="Arial", fg="grey",bg="pink")
        self.mobile.place(x=980,y=340,anchor="center",width=150)
        self.mobile.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_Aadhaar)
        self.mobile.entry.place(x=980,y=350,width=200)


        ## empls pan_no
        self.pan_no=Label(root, text="pan number:",font="Arial", fg="grey",bg="pink")
        self.pan_no.place(x=950,y=420,anchor="center",width=150)
        self.pan_no.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_pan_number)
        self.pan_no.entry.place(x=980,y=430,width=200)

         ## empls Native
        self.Native=Label(root, text="Emp.Native:",font="Arial", fg="grey",bg="pink")
        self.Native.place(x=950,y=500,anchor="center",width=150)
        self.Native.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_Native)
        self.Native.entry.place(x=980,y=510,width=200)

        ## empls Nationality
        self.Nationality=Label(root, text="Emp.Nationality:",font="Arial", fg="grey",bg="pink")
        self.Nationality.place(x=950,y=580,anchor="center",width=150)
        self.Nationality.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_Nationality)
        self.Nationality.entry.place(x=980,y=590,width=200)

        ## empls Identity
        self.identity=Label(root, text="Emp.Identity:",font="Arial", fg="grey",bg="pink")
        self.identity.place(x=950,y=660,anchor="center",width=150)
        self.identity.entry=tk.Entry(root,font=("Arial"),bg="White",textvariable=self.var_Identity)
        self.identity.entry.place(x=980,y=670,width=200)


  ### submit button-------------------------------------------------------------------------------------------------------------------------------------------
        emp1_button=Button(root ,text="SUBMIT", fg="black",font="Arial", bg="pink", command=self.adddata)
        emp1_button.place(x=700,y=700,width=100)

#############----------------------------------------------------------------------------------------
   


##----------------------------------------------------def calling function--------------------------------------------------------------
    def adddata(self):
        conn= pymysql.connect(host='localhost',user='DHARSH',password='DN',database='employees_management')
        try:
            cursor=conn.cursor()
            query=('SELECT * FROM personal_detail  WHERE mail=%s;')
            value=(self.var_mail.get(),)
            cursor.execute(query,value)
            data=cursor.fetchone()
            if not data:
                cursor.execute('INSERT INTO personal_detail(Id, Name, dob, department, mail, mobile, address, salary, bloodgrp, Aadhaar, pan_number, Native, Nationality, Identity) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                self.var_Id.get(),
                self.var_Name.get(),
                self.var_dob.get(),
                self.var_department.get(),
                self.var_mail.get(), 
                self.var_mobile.get(), 
                self.var_address.get(),
                self.var_salary.get(),
                self.var_bloodgrp.get(),
                self.var_Aadhaar.get(),
                self.var_pan_number.get(),
                self.var_Native.get(),
                self.var_Nationality.get(),
                self.var_Identity.get()
                )
                )
                conn.commit()
                messagebox.showinfo("Success","your Data will be submitted")
               ## clear the data
                self.var_Id.set("")
                self.var_Name.set("")
                self.var_dob.set("")
                self.var_department.set("")
                self.var_mail.set("")
                self.var_mobile.set("")
                self.var_address.set("")
                self.var_salary.set("")
                self.var_bloodgrp.set("")
                self.var_Aadhaar.set("")
                self.var_pan_number.set("")
                self.var_Native.set("")
                self.var_Nationality.set("")
                self.var_Identity.set("")
            
            else:
                 if data[8] == 0 :
                  query = "UPDATE empdetails SET logout_time=%s WHERE mail=%s"
                  values = (self.var_salary.get(), self.var_mail.get())
                  cursor.execute(query, values)
                  conn.commit()

                  messagebox.showinfo("Success", "Thanks! once again your data will be sumitted.")
                    ## clear the data
                 self.var_Id.set("")
                 self.var_Name.set("")
                 self.var_department.set("")
                 self.var_mail.set("")
                 self.var_mobile.set("")
                 self.var_address.set("")
                 self.var_dob.set("")
                 self.var_salary.set("")
                 self.var_bloodgrp.set("")
                 self.var_Aadhaar.set("")
                 self.var_pan_number.set("")
                 self.var_Native.set("")
                 self.var_Nationality.set("")
                 self.var_Identity.set("")
                


        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
        finally:
            conn.close()
###-------------------------------------------------------------------------------------------------------------------

####################-----------------------------------------------------------------------------------------------------------------------------------------------------------
  


#####################---------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
