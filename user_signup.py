from customtkinter import *
from PIL import Image,ImageTk
import tkinter as tk


root=CTk()
root.geometry("1500x750")
root.title("user_signup")


def already_acc():
    root.destroy()
    import user_login




def password():
    '''
    it is made so that we can hide or show password clicking the eye button in password
    '''
    if e4.cget("show") == "":
        e4.configure(show="*")
    else:
        e4.configure(show="")

def repassword():
    '''
    it is made so that we can hide or show password clicking the eye button in  repassword
    '''
    if e5.cget("show") == "":
        e5.configure(show="*")
    else:
        e5.configure(show="")


def security_info():
    '''
    this function is made to show a message when user clicks submit on win1 window
    '''
    win2.destroy()         
    tk.messagebox.showinfo("Successful Message ","Security questions Entry Successful !")
    pass



def newwin():
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
    image=Image.open("pictures\\forgot-pass-pic.jpg")
    image_resize=image.resize((626,626))
    image_tk=ImageTk.PhotoImage(image_resize)
    label1st=tk.Label(win2,image=image_tk)
    label1st.image = image_tk  #reference to the picture
    label1st.place(relheight=1,relwidth=1,relx=0.2499)


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
    button1=CTkButton(frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=security_info)
    button1.place(relx=0.3,rely=0.8)
    pass





#the bg frame
frame=tk.Frame(root,bg="Black")
frame.place(relwidth=1,relheight=1)

#the main bg picture 
image1=Image.open("pictures\\f327a69f-4c36-4c1e-8965-c5a71e3d9d99.png")
image1=image1.resize((968,1080))
photoimage1=ImageTk.PhotoImage(image1)
label1 = tk.Label(root, image=photoimage1)
label1.place(x=952, y=0, w=968, h=1080)
label1=image1

#image for eye button in password and repassword
image2=Image.open("pictures\\ion_eyeeye.png")
tkimage2=ImageTk.PhotoImage(image2)


#image for i button 
image3=Image.open("pictures\\Vector.png")
tkimage3=ImageTk.PhotoImage(image3)


#label for mealmate logo
image4=Image.open("pictures\\logo-no-2.png")
image4=image4.resize((641,141))
photoimage4=ImageTk.PhotoImage(image4)
label4 = tk.Label(root, image=photoimage4,bg="#262731")
label4.place(x=138, y=62, w=641, h=141)




#the main frame
f1=CTkFrame(frame,bg_color="transparent",corner_radius=10,fg_color="#262731",width=681,height=900)
f1.place(x=100,y=39,w=681,h=900)

#sep frame
sep_frame=tk.Frame(f1,bg="Black")
sep_frame.place(relwidth=1,relheight=0.02,rely=0.2)

#signup heading label
l1=tk.Label(f1,text="Sign Up",font=("Inter",25,"bold"),bg="#262731",fg="white")
l1.place(relx=0.38,rely=0.23)

#firstname label
l2=tk.Label(f1,text="First Name:",font=("Regular",15),bg="#262731",fg="White")
l2.place(relx=0.05,rely=0.3)

#firstname entry
e1=CTkEntry(f1,placeholder_text="firstname",fg_color="#FAF3DB",width=180,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
e1.place(relx=0.05,rely=0.33)

#lastname label
l3=tk.Label(f1,text="Last Name:",font=("Regular",15),bg="#262731",fg="White")
l3.place(relx=0.53,rely=0.3)

#lastname entry
e2=CTkEntry(f1,placeholder_text="lastname",fg_color="#FAF3DB",width=190,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
e2.place(relx=0.53,rely=0.33)

#email label
l4=tk.Label(f1,text="Email:",font=("Regular",15),bg="#262731",fg="White")
l4.place(relx=0.05,rely=0.43)

#email entry
e3=CTkEntry(f1,placeholder_text="Your Email Here",fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
e3.place(relx=0.05,rely=0.46)

#password label
l5=tk.Label(f1,text="Password:",font=("Regular",15),bg="#262731",fg="White")
l5.place(relx=0.05,rely=0.56)

#password entry
e4=CTkEntry(f1,fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",corner_radius=8,border_width=0,show="*")
e4.place(relx=0.05,rely=0.59)

#repassword label
l6=tk.Label(f1,text="Re-Password:",font=("Regular",15),bg="#262731",fg="White")
l6.place(relx=0.05,rely=0.69)

#repassword entry
e5=CTkEntry(f1,fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",corner_radius=8,border_width=0,show="*")
e5.place(relx=0.05,rely=0.72)

#security question label
b1=CTkButton(f1,text="Security Questions",text_color="#CF7941",width=300,height=40,fg_color="#FAF3DB",hover=0,font=("Inter",15,"bold"),corner_radius=8,command=newwin)
b1.place(relx=0.2,rely=0.81)

#Signup button
b2=CTkButton(f1,text="SIGN UP",fg_color="#FAF3DB",hover=0,height=45,font=("Inter",20,"bold"),text_color="#4D5053",corner_radius=8)
b2.place(relx=0.35,rely=0.92)

#eye button in password
b3=tk.Button(f1,image=tkimage2,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = password)
b3.place(relx=0.8,rely=0.61)

#eye button in repassword
b4=tk.Button(f1,image=tkimage2,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = repassword)
b4.place(relx=0.8,rely=0.74)

#i button in security question
b4=tk.Button(f1,image=tkimage3,bg="#FAF3DB",activebackground="#FAF3DB",bd=0)
b4.place(relx=0.68,rely=0.825)

#already an account label
l7=tk.Label(f1,text="Already have an account?",font=("Inter",12,"italic"),bg="#262731",fg="White")
l7.place(relx=0.48,rely=0.87)

# click here button 
b5=tk.Button(f1,text="click here",font=("Inter",12,"bold italic"),bg="#262731",fg="#DD2323",activebackground="#262731",bd=0,command=already_acc)
b5.place(relx=0.76,rely=0.869)

root.mainloop()
