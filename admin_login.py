from customtkinter import *
from PIL import Image,ImageTk
import tkinter as tk

root=CTk()
root.geometry("1500x750")
root.title("Admin_Login")



def stretch(event):
    '''
    this function is made so that the pictures fits on the screen 
    even when the screen size changes . 
    '''
    global resized_tk

    #for the changing width and height of the window
    width=event.width
    height=event.height

    resized_image=a.resize((width,height))
    resized_tk=ImageTk.PhotoImage(resized_image)
   
    canvas.create_image(0,0,anchor=tk.NW,image=resized_tk)
    


def onclick():
    '''
    it is made so that we can hide or show password clicking the eye button
    '''
    if e2.cget("show") == "":
        e2.configure(show="*")
    else:
        e2.configure(show="")

def security_update():
    '''
    this function is made to show a message when user clicks submit on win1 window
    '''
    win2.destroy()         
    tk.messagebox.showinfo("Successful Message ","Security questions Entry Successful !")
    pass

def login():
    """
    this function is made so that a messagebox is shown after clicking 
    the login button and the root window is destroyed . 
    """
    tk.messagebox.showinfo("Successful Message ","Login Successful !")
    root.destroy()   
    pass      
    



def new():
    """this function contains a toplevel window which opens when click here button is clicked 
    which is by the side of forgot password .
    """
    global win2

    #the forgot password window
    win2=tk.Toplevel()
    win2.geometry("1252x626")
    win2.resizable(0,0)
    win2.title("Forgot password")
    #the pic in the top label window
    image1=Image.open("pictures\\forgot-pass-pic.jpg")
    image1_resize=image1.resize((626,626))
    image1_tk=ImageTk.PhotoImage(image1_resize)
    label1=tk.Label(win2,image=image1_tk)
    label1.image = image1_tk  #reference to the picture
    label1.place(relheight=1,relwidth=1,relx=0.2499)

#the main frame of win1 
    frame1=tk.Frame(win2,bg="#001129",width=626,height=626)
    frame1.place(x=0,y=0)

#frame which contains the questions 
    frame2=tk.Frame(frame1,bg="#001129",width=426,height=450,bd=3,relief="groove")
    frame2.place(relx=0.16,rely=0.13)

#label for security questions heading
    label2=tk.Label(frame1,text="Security Questions",font=("Inter",20,"bold"),fg="White",bg="#001129")
    label2.place(relx=0.3,rely=0.1)

#label for 1st question
    label3=tk.Label(frame2,text="Q1.  Which is your favourite number?",fg="White",bg="#001129",font=("Regular",15))
    label3.place(relx=0.05,rely=0.1)

#entry for 1st question
    entry1=CTkEntry(frame2,fg_color="#74A9D8",width=220)
    entry1.place(relx=0.17,rely=0.17)

#label for 2nd question
    label4=tk.Label(frame2,text="Q2.  Which is your favourite food?",fg="White",bg="#001129",font=("Regular",15))
    label4.place(relx=0.05,rely=0.32)

#entry for 2nd question
    entry2=CTkEntry(frame2,fg_color="#74A9D8",width=220)
    entry2.place(relx=0.17,rely=0.39)

#label for 3rd question
    label5=tk.Label(frame2,text="Q3.  Which is your favourite color?",fg="White",bg="#001129",font=("Regular",15))
    label5.place(relx=0.05,rely=0.54)

#entry for 3rd question
    entry3=CTkEntry(frame2,fg_color="#74A9D8",width=220)
    entry3.place(relx=0.17,rely=0.61)

#the submit button
    button1=CTkButton(frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=security_update)
    button1.place(relx=0.3,rely=0.8)
    pass


    



#eye button pic
d=Image.open("pictures\\ion_eyeeye.png")
e=ImageTk.PhotoImage(d)



#bg image
a = Image.open("pictures\\coffee.jpg")
f=ImageTk.PhotoImage(a)


#canvas widget which covers the entire screen
canvas=tk.Canvas(root,bg="black",bd=0,highlightthicknes=0)
canvas.place(relwidth=1,relheight=1)
canvas.bind("<Configure>",stretch)

#The main frame
f1=CTkFrame(root,fg_color="#888888",bg_color="White",corner_radius=8)
f1.place(relx=0.08,rely=0.15,relheight=0.7,relwidth=0.3)

#logo
image1=Image.open("pictures\\logo-no-1.png")#insert image
image1=image1.resize((516,106))#resize
photoimage1=ImageTk.PhotoImage(image1)#pil to photo image
label = tk.Label(f1, image=photoimage1,bg="#888888")#label
label.place(x=20, y=15, w=516, h=106)
label=image1


#for spacing between logo and login frame
f2=tk.Frame(f1,bg="#F8F9F7")
f2.place(relwidth=1,relheight=0.018,relx=0,rely=0.2)

#login heading
l1=tk.Label(f1,text="LOGIN",bg="#888888",font=("Inter",25,"bold"))
l1.place(relx=0.4,rely=0.25,relwidth=0.2,relheight=0.05)

l2=tk.Label(f1,text="Email:",bg="#888888",font=("Regular",20))
l2.place(relx=0.08,rely=0.34)

#email entrybox
e1=CTkEntry(f1,fg_color="#FAF3DB",placeholder_text="example@gmail.com",placeholder_text_color="#DD2323",border_color="#888888",text_color="#DD2323",font=("Regular",15))
e1.place(relx=0.08,rely=0.40,relwidth=0.8,relheight=0.09)

#password label
l3=tk.Label(f1,text="Password:",bg="#888888",font=("Regular",20))
l3.place(relx=0.08,rely=0.51)



#password entrybox
e2=CTkEntry(f1,fg_color="#FAF3DB",border_color="#888888",text_color="#DD2323",font=("Regular",15),show="*")
e2.place(relx=0.08,rely=0.57,relwidth=0.8,relheight=0.09)


#forgot pass label
l4=tk.Label(f1,text="Forgot your password?",fg="White",bg="#888888",font=("Inter",15,"italic"))
l4.place(relx=0.35,rely=0.67)

#click here
b1=tk.Button(f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=new)
b1.place(relx=0.713,rely=0.666)


#login button
b2=CTkButton(f1,text="LOGIN",text_color="Black",corner_radius=8,fg_color="#543627",hover_color="#543627",font=("Inter",20,"bold"), command = login)
b2.place(relx=0.35,rely=0.77,relwidth=0.3,relheight=0.1)


#dont have account label
l5=tk.Label(f1,text="Dont have an account?",fg="White",bg="#888888",font=("Inter",15,"italic"))
l5.place(relx=0.2,rely=0.9)

#button for dont have an account
b3=tk.Button(f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"))
b3.place(relx=0.56,rely=0.896)


# eye button
b4=tk.Button(f1,image=e,bg="#FAF3DB",activebackground="#FAF3DB",border=0,command=onclick)
b4.place(relx=0.8,rely=0.595)


root.mainloop()
