from customtkinter import *
from PIL import Image,ImageTk
import tkinter as tk

root=CTk()
# root.geometry("1500x750")
root.minsize(width=1550,height=750)
root.title("Dashboard")
root.iconbitmap("pictures//32432hotbeverage_98916.ico")

main_frame1=tk.Frame(root)
main_frame1.place(relheight=1,relwidth=1,x=0,y=0)

def i_button1():
    tk.messagebox.showinfo("User Login","Click here for Signing in to User Account .")

def i_button2():
    tk.messagebox.showinfo("Admin Login","Click here for Signing in to Admin Account .")

def i_button3():
    tk.messagebox.showinfo("User Signup","Click here for Creating a new User Account .")

def i_button4():
    tk.messagebox.showinfo("Admin Signup","Click here for Creating a new Admin Account .")
   
def mealmate():
    pass

def user_login():
    root.destroy()
    import user_login
    


def admin_login():
    root.destroy()

    import admin_login


def user_signup():
    root.destroy()
    import user_signup


def admin_signup():
    root.destroy()
    import admin_signup




image1=Image.open("pictures\\dashboard_bg.png")
image1=image1.resize((1920,990))
photoimage1=ImageTk.PhotoImage(image1)
label1 = tk.Label(main_frame1, image=photoimage1)
label1.place(x=0, y=0, w=1920, h=990)
label1=image1 

i_image=ImageTk.PhotoImage(file="pictures/Vectori_button(white).png")



f=CTkFrame(main_frame1,width=450,height=600,border_width=3,fg_color="White",border_color="BLack")
f.place(relx=0.35,rely=0.16)

image2=Image.open("pictures\\Rectangle 41.png")#insert image
image2=image2.resize((508,105))#resize
photoimage2=ImageTk.PhotoImage(image2)#pil to photo image
Button1 = tk.Button(f, image=photoimage2,bg="White",activebackground="White",bd=0)#label
Button1.place(relx=0.05,rely=0.025)


f1=CTkFrame(f,bg_color="Black",width=550,height=10,border_color="Black",fg_color="Black")
f1.place(rely=0.2)

f2=CTkFrame(f,width=433,height=457,fg_color="White",border_color="Black",border_width=3)
f2.place(relx=0.0201,rely=0.226)


b1=CTkButton(f2,text="User Login",width=262,height=55,corner_radius=30,font=("Inter",33),text_color="#D1D1D1",fg_color="#3A3848",hover=0,command=user_login)
b1.place(relx=0.204,rely=0.12)
ib1=tk.Button(b1,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button1)
ib1.place(relx=0.87,rely=0.35)

b2=CTkButton(f2,text="Admin Login",width=262,height=55,corner_radius=30,font=("Inter",33),text_color="#D1BC56",fg_color="#3A3848",hover=0,command=admin_login)
b2.place(relx=0.204,rely=0.33)
ib2=tk.Button(b2,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button2)
ib2.place(relx=0.89,rely=0.35)

b3=CTkButton(f2,text="User Signup",width=262,height=55,corner_radius=30,font=("Inter",33),text_color="#E25A00",fg_color="#3A3848",hover=0,command=user_signup)
b3.place(relx=0.204,rely=0.54)
ib3=tk.Button(b3,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button3)
ib3.place(relx=0.89,rely=0.35)

b4=CTkButton(f2,text="Admin Signup",width=240,height=55,corner_radius=30,font=("Inter",33),text_color="#48A31E",fg_color="#3A3848",hover=0,command=admin_signup)
b4.place(relx=0.204,rely=0.74)

ib4=tk.Button(b4,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button4)
ib4.place(relx=0.9,rely=0.35)


root.mainloop()