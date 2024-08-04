from customtkinter import *
import tkinter as tk
from PIL import Image,ImageTk

root=CTk()
root.geometry("1500x750")
root.iconbitmap("pictures//32432hotbeverage_98916.ico")
root.title("Admin_Dashboard")



def on_hover(enter):
    admin_db_btn2.configure(image=a_db_img5ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

def off_hover(leave):
    admin_db_btn2.configure(image=a_db_img1ctk,text_color="#DD2323",fg_color="#D9D9D9")


def on_hover2(enter):
    admin_db_btn3.configure(text_color="#33303C",fg_color="#F38686",hover_color="#F38686")
    admin_db_btn3_lbl.configure(image=a_db_img6ctk,fg_color="#F38686",bg_color="#F38686")

def off_hover2(leave):
    admin_db_btn3.configure(text_color="#DD2323",fg_color="#D9D9D9")
    admin_db_btn3_lbl.configure(image=a_db_img2ctk,fg_color="#D9D9D9",bg_color="#D9D9D9")


def on_hover3(enter):
    admin_db_btn4.configure(image=a_db_img7ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

def off_hover3(leave):
    admin_db_btn4.configure(image=a_db_img3ctk,text_color="#DD2323",fg_color="#D9D9D9")


def on_hover4(enter):
    admin_db_btn5.configure(image=a_db_img8ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

def off_hover4(leave):
    admin_db_btn5.configure(image=a_db_img4ctk,text_color="#DD2323",fg_color="#D9D9D9")


def dashboard_frame_ad():
    #Frame
    admin_db_frame3=tk.Frame(main_frame6,bg="White")
    admin_db_frame3.place(relx=0.302,rely=0.12,relwidth=0.7,relheight=0.9)

    
    #the bg image
    global photo_a_db_bg
    a_db_bg=Image.open("pictures/5883 1bg_adb.png")
    a_db_bg=a_db_bg.resize((1250,683))
    photo_a_db_bg=ImageTk.PhotoImage(a_db_bg)
    a_db_lbl2 = tk.Label(admin_db_frame3, image=photo_a_db_bg)
    a_db_lbl2.place(x=0, y=0, w=1250, h=683)

    #labels
    a_db_lbl6=tk.Label(admin_db_frame3,text="Welcome,",font=("Inter",60,"bold"),bg="White")
    a_db_lbl6.place(relx=0.26,rely=0.78)

    a_db_lbl7=tk.Label(admin_db_frame3,text="Dristi",font=("Inter",60,"bold"),bg="White",fg="#DD2323")
    a_db_lbl7.place(relx=0.55,rely=0.78)


    pass


def items_frame_ad():
    #Frame
    admin_db_frame3=tk.Frame(main_frame6,bg="White")
    admin_db_frame3.place(relx=0.302,rely=0.12,relwidth=0.7,relheight=0.9)
    pass


def customers_frame_ad():
    #Frame
    admin_db_frame3=tk.Frame(main_frame6,bg="White")
    admin_db_frame3.place(relx=0.302,rely=0.12,relwidth=0.7,relheight=0.9)
    pass






# global photo_a_db_logo, a_db_img1ctk, a_db_img5ctk, a_db_img2ctk, a_db_img6ctk, a_db_img3ctk, a_db_img7ctk, a_db_img4ctk, a_db_img8ctk, a_db_img9tk, photo_a_db_bg


# the main frame
main_frame6=CTkFrame(root,fg_color="Black")
main_frame6.place(relheight=1,relwidth=1,relx=0,rely=0)

admin_db_frame1=tk.Frame(main_frame6,bg="#D9D9D9")
admin_db_frame1.place(relwidth=1,relheight=0.11,x=0,y=0)


# the logo
a_db_logo=Image.open("pictures/Rectangle 41.png")
a_db_logo=a_db_logo.resize((468,97))
photo_a_db_logo=ImageTk.PhotoImage(a_db_logo)
a_db_lbl = tk.Label(admin_db_frame1, image=photo_a_db_logo,bg="#D9D9D9")
a_db_lbl.place(x=20, y=6, w=468, h=97)

admin_db_frame4=CTkFrame(admin_db_frame1,corner_radius=10,fg_color="#33303C")
admin_db_frame4.place(relx=0.4,rely=0.3,relwidth=0.5,relheight=0.4)

#buttons and levels inside buttons
a_db_btn7=CTkButton(admin_db_frame4,text="          Admin",text_color="#DD2323",fg_color="#D9D9D9",hover=0,font=("Regular",15),corner_radius=14)
a_db_btn7.place(relx=0.1,rely=0.1,relwidth=0.17)
a_db_lbl3=tk.Label(a_db_btn7,text="User:",fg="#33303C",font=("Regular",15),bg="#D9D9D9")
a_db_lbl3.place(relx=0.15,rely=0.05)

a_db_btn8=CTkButton(admin_db_frame4,text="          Dristi",text_color="#DD2323",fg_color="#D9D9D9",hover=0,font=("Regular",15),corner_radius=14)
a_db_btn8.place(relx=0.4,rely=0.1,relwidth=0.18)
a_db_lbl4=tk.Label(a_db_btn8,text="Name:",fg="#33303C",font=("Regular",15),bg="#D9D9D9")
a_db_lbl4.place(relx=0.15,rely=0.05)

a_db_btn9=CTkButton(admin_db_frame4,text="             Dashboard",text_color="#DD2323",fg_color="#D9D9D9",hover=0,font=("Regular",15),corner_radius=14)
a_db_btn9.place(relx=0.7,rely=0.1,relwidth=0.2)
a_db_lbl5=tk.Label(a_db_btn9,text="Page:",fg="#33303C",font=("Regular",15),bg="#D9D9D9")
a_db_lbl5.place(relx=0.12,rely=0.05)

admin_db_frame2=CTkFrame(main_frame6,corner_radius=10,fg_color="#33303C")
admin_db_frame2.place(relheight=0.879,relwidth=0.3,relx=0,rely=0.12)


#separator frame
adb_sep_frame=tk.Frame(admin_db_frame2,bg="Black")
adb_sep_frame.place(relwidth=1,relheight=0.01,relx=0,rely=0.1)

#managenment system heading
admin_db_btn=CTkButton(admin_db_frame2,fg_color="#33303C",text="Management System",font=("Regular",23),height=45,hover=0,border_color="#D9D9D9",corner_radius=0,border_width=1)
admin_db_btn.place(relx=0.21,rely=0.017,relwidth=0.56)


#images in buttons
a_db_img1=Image.open("pictures/Group 34group_home2.png")
a_db_img1ctk=CTkImage(a_db_img1)
a_db_img5=Image.open("pictures/Group 33grouped_home1.png")
a_db_img5ctk=CTkImage(a_db_img5)

a_db_img2=Image.open("pictures/Vectoriconns-1.png")
a_db_img2ctk=CTkImage(a_db_img2)
a_db_img6=Image.open("pictures/Vectoriconns-5.png")
a_db_img6ctk=CTkImage(a_db_img6)

a_db_img3=Image.open("pictures/Vectoriconns.png")
a_db_img3ctk=CTkImage(a_db_img3)
a_db_img7=Image.open("pictures/Vectoriconns-4.png")
a_db_img7ctk=CTkImage(a_db_img7)

a_db_img4=Image.open("pictures/Groupiconns.png")
a_db_img4ctk=CTkImage(a_db_img4)
a_db_img8=Image.open("pictures/Groupiconns-1.png")
a_db_img8ctk=CTkImage(a_db_img8)

a_db_img9=Image.open("pictures//Vectorarrow.png")
a_db_img9tk=ImageTk.PhotoImage(a_db_img9)


#Buttons
admin_db_btn2=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Dashboard",image=a_db_img1ctk,text_color="#DD2323",corner_radius=7, command = dashboard_frame_ad)
admin_db_btn2.place(relx=0.21,rely=0.25,relwidth=0.56,relheight=0.06)

admin_db_btn3=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Items",text_color="#DD2323",corner_radius=7,command = items_frame_ad)
admin_db_btn3.place(relx=0.21,rely=0.4,relwidth=0.56,relheight=0.06)
admin_db_btn3_lbl=CTkLabel(admin_db_btn3,image=a_db_img2ctk,text="")
admin_db_btn3_lbl.place(relx=0.3,rely=0.1)

admin_db_btn4=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Customers",text_color="#DD2323",image=a_db_img3ctk,corner_radius=7 , command = customers_frame_ad)
admin_db_btn4.place(relx=0.21,rely=0.55,relwidth=0.56,relheight=0.06)

admin_db_btn5=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Exit",text_color="#DD2323",image=a_db_img4ctk,corner_radius=7,command=lambda:root.destroy())
admin_db_btn5.place(relx=0.21,rely=0.7,relwidth=0.56,relheight=0.06)

admin_db_btn6=tk.Button(admin_db_frame2,text=" Log out",font=("Regular",15),image=a_db_img9tk,compound=LEFT,bg="#33303C",activebackground="#33303C",activeforeground="White",fg="White",bd=0)
admin_db_btn6.place(relx=0.39,rely=0.85)


#binding events in buttons
admin_db_btn2.bind("<Enter>", on_hover)
admin_db_btn2.bind("<Leave>", off_hover)

admin_db_btn3.bind("<Enter>", on_hover2)
admin_db_btn3.bind("<Leave>", off_hover2)

admin_db_btn4.bind("<Enter>", on_hover3)
admin_db_btn4.bind("<Leave>", off_hover3)

admin_db_btn5.bind("<Enter>", on_hover4)
admin_db_btn5.bind("<Leave>", off_hover4)




dashboard_frame_ad()






root.mainloop()