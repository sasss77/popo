from customtkinter import *
from PIL import Image,ImageTk
import tkinter as tk

root=CTk()

#making the root fit in the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

#title
root.title("Dashboard")
#icon
root.iconbitmap("pictures/32432hotbeverage_98916.ico")




def i_button1():
    #function to show message when i button is clicked 
    tk.messagebox.showinfo("User Login","Click here for Signing in to User Account .")

def i_button2():
    #function to show message when i button is clicked 
    tk.messagebox.showinfo("Admin Login","Click here for Signing in to Admin Account .")

def i_button3():
    #function to show message when i button is clicked 
    tk.messagebox.showinfo("User Signup","Click here for Creating a new User Account .")

def i_button4():
    #function to show message when i button is clicked 
    tk.messagebox.showinfo("Admin Signup","Click here for Creating a new Admin Account .")
   
def mealmate():
    pass


def user_login():
    #the main frame
    main_ulogin_frame2=CTkFrame(root)
    main_ulogin_frame2.place(relwidth=1,relheight=1,x=0,y=0)

    def reset_successful():
        #function to destroy top label window and show a message 
        win2.destroy()
        tk.messagebox.showinfo("Reset Successful","Password reset successful.")


    def back():
        #function to open dashboard when back button is clicked  
        main_ulogin_frame2.destroy()
        main()

    def click_here():
        #function to open user signup page when click here button is clicked 
        main_ulogin_frame2.place_forget()
        user_signup()



    def stretch(event):
        '''
        this function is made so that the pictures fits on the screen 
        even when the screen size changes . 
        '''
        global resized_tk

        #for the changing width and height of the window
        width=event.width
        height=event.height

        resized_image=ulogin_bg.resize((width,height))
        resized_tk=ImageTk.PhotoImage(resized_image)
    
        canvas.create_image(0,0,anchor=tk.NW,image=resized_tk)
        


    def onclick():
        '''
        it is made so that we can hide or show password clicking the eye button
        '''
        if ulogin_e2.cget("show") == "":
            ulogin_e2.configure(show="*")
        else:
            ulogin_e2.configure(show="")
        
    def reset_p1():
        if ulogin_etr1.cget("show") == "":
            ulogin_etr1.configure(show="*")
        else:
            ulogin_etr1.configure(show="")

    def reset_p2():
        if ulogin_etr2.cget("show") == "":
            ulogin_etr2.configure(show="*")
        else:
            ulogin_etr2.configure(show="")
            




    def login():
        """
        this function is made so that a messagebox is shown after clicking 
        the login button and the root window is destroyed . 
        """
        tk.messagebox.showinfo("Successful Message ","Login Successful !")
        main_ulogin_frame2.place_forget()
        main()
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
        ulogin_sec_image1=Image.open("pictures\\forgot-pass-pic.jpg")
        ulogin_sec_image1_resize=ulogin_sec_image1.resize((626,626))
        ulogin_sec_image1_tk=ImageTk.PhotoImage(ulogin_sec_image1_resize)
        ulogin_label1=tk.Label(win2,image=ulogin_sec_image1_tk)
        ulogin_label1.image = ulogin_sec_image1_tk  #reference to the picture
        ulogin_label1.place(relheight=1,relwidth=1,relx=0.2499)

    #the main frame of win1 
        ulogin_frame1=tk.Frame(win2,bg="#001129",width=626,height=626)
        ulogin_frame1.place(x=0,y=0)

    #frame which contains the questions 
        ulogin_frame2=tk.Frame(ulogin_frame1,bg="#001129",width=426,height=450,bd=3,relief="groove")
        ulogin_frame2.place(relx=0.16,rely=0.13)

    #label for security questions heading
        ulogin_label2=tk.Label(ulogin_frame1,text="Security Questions",font=("Inter",20,"bold"),fg="White",bg="#001129")
        ulogin_label2.place(relx=0.3,rely=0.1)

    #label for 1st question
        ulogin_label3=tk.Label(ulogin_frame2,text="Q1.  Which is your favourite number?",fg="White",bg="#001129",font=("Regular",15))
        ulogin_label3.place(relx=0.05,rely=0.1)

    #entry for 1st question
        ulogin_entry1=CTkEntry(ulogin_frame2,fg_color="#74A9D8",width=220)
        ulogin_entry1.place(relx=0.17,rely=0.17)

    #label for 2nd question
        ulogin_label4=tk.Label(ulogin_frame2,text="Q2.  Which is your favourite food?",fg="White",bg="#001129",font=("Regular",15))
        ulogin_label4.place(relx=0.05,rely=0.32)

    #entry for 2nd question
        ulogin_entry2=CTkEntry(ulogin_frame2,fg_color="#74A9D8",width=220)
        ulogin_entry2.place(relx=0.17,rely=0.39)

    #label for 3rd question
        ulogin_label5=tk.Label(ulogin_frame2,text="Q3.  Which is your favourite color?",fg="White",bg="#001129",font=("Regular",15))
        ulogin_label5.place(relx=0.05,rely=0.54)

    #entry for 3rd question
        ulogin_entry3=CTkEntry(ulogin_frame2,fg_color="#74A9D8",width=220)
        ulogin_entry3.place(relx=0.17,rely=0.61)

    #the submit button
        ulogin_button1=CTkButton(ulogin_frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=reset_pass)
        ulogin_button1.place(relx=0.3,rely=0.8)
        pass



    ulogin_eye_img=Image.open("pictures//Vectorblack_eye1.png")
    ulogin_eye_imgtk=ImageTk.PhotoImage(ulogin_eye_img)


    def reset_pass():
        global ulogin_etr1,ulogin_etr2
        
        win3=tk.Toplevel()
        win3.title("Reset password")
        win3.geometry("500x250")
        win3.resizable(0,0)
        #label
        ulogin_lbl1=tk.Label(win3,text="Enter New Password:",font=("Regular",13))
        ulogin_lbl1.place(relx=0.05,rely=0.08)
        #enter new pass entry box
        ulogin_etr1=CTkEntry(win3,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",show="*",text_color="Black")
        ulogin_etr1.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        #confirm pass label
        ulogin_lbl2=tk.Label(win3,text="Confirm new Password:",font=("Regular",13))
        ulogin_lbl2.place(relx=0.05,rely=0.33)
        #entrybox for confirm password
        ulogin_etr2=CTkEntry(win3,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",show="*",text_color="Black")
        ulogin_etr2.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        #the submit button
        ulogin_btn1=CTkButton(win3,text="SUBMIT",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",border_width=2,command=reset_successful)
        ulogin_btn1.place(relx=0.33,rely=0.75,relwidth=0.3,relheight=0.15)

        #eye button in entry box
        ulogin_btn2=tk.Button(win3,image=ulogin_eye_imgtk,bg="white",activebackground="white",bd=0,command=reset_p1)
        ulogin_btn2.place(relx=0.78,rely=0.2)
        #eye button in entry box
        ulogin_btn3=tk.Button(win3,image=ulogin_eye_imgtk,bg="white",activebackground="white",bd=0,command=reset_p2)
        ulogin_btn3.place(relx=0.78,rely=0.46)


#making pictures global so they dont get garbage collected 
    global ulogin_eyetk,ulogin_backtk,photo_ulogin_img1


    #eye button pic
    ulogin_eye=Image.open("pictures\\ion_eyeeye.png")
    ulogin_eyetk=ImageTk.PhotoImage(ulogin_eye)



    #bg image
    ulogin_bg = Image.open("pictures\\coffee.jpg")
    ulogin_bgtk=ImageTk.PhotoImage(ulogin_bg)


    ulogin_back=Image.open("pictures//Vectorarrow.png")
    ulogin_backtk=ImageTk.PhotoImage(ulogin_back)


    #canvas widget which covers the entire screen
    canvas=tk.Canvas(main_ulogin_frame2,bg="black",bd=0,highlightthicknes=0)
    canvas.place(relwidth=1,relheight=1)
    canvas.bind("<Configure>",stretch)

    #The main frame
    ulogin_f1=CTkFrame(main_ulogin_frame2,fg_color="#888888",bg_color="White",corner_radius=8)
    ulogin_f1.place(relx=0.08,rely=0.15,relheight=0.7,relwidth=0.3)

    #logo
    ulogin_img1=Image.open("pictures\\logo-no-1.png")#insert image
    ulogin_img1=ulogin_img1.resize((516,106))#resize
    photo_ulogin_img1=ImageTk.PhotoImage(ulogin_img1)#pil to photo image
    label = tk.Label(ulogin_f1, image=photo_ulogin_img1,bg="#888888")#label
    label.place(x=20, y=15, w=516, h=106)
    label=ulogin_img1


    #for spacing between logo and login frame
    ulogin_f2=tk.Frame(ulogin_f1,bg="#F8F9F7")
    ulogin_f2.place(relwidth=1,relheight=0.018,relx=0,rely=0.2)

    #login heading
    ulogin_l1=tk.Label(ulogin_f1,text="User Login",bg="#888888",font=("Inter",25,"bold"))
    ulogin_l1.place(relx=0.26,rely=0.25,relwidth=0.5,relheight=0.07)

    ulogin_l2=tk.Label(ulogin_f1,text="Email:",bg="#888888",font=("Regular",20))
    ulogin_l2.place(relx=0.08,rely=0.34)

    #email entrybox
    ulogin_e1=CTkEntry(ulogin_f1,fg_color="#FAF3DB",placeholder_text="example@gmail.com",placeholder_text_color="#DD2323",border_color="#888888",text_color="#DD2323",font=("Regular",15))
    ulogin_e1.place(relx=0.08,rely=0.40,relwidth=0.8,relheight=0.09)

    #password label
    ulogin_l3=tk.Label(ulogin_f1,text="Password:",bg="#888888",font=("Regular",20))
    ulogin_l3.place(relx=0.08,rely=0.51)



    #password entrybox
    ulogin_e2=CTkEntry(ulogin_f1,fg_color="#FAF3DB",border_color="#888888",text_color="#DD2323",font=("Regular",15),show="*")
    ulogin_e2.place(relx=0.08,rely=0.57,relwidth=0.8,relheight=0.09)


    #forgot pass label
    ulogin_l4=tk.Label(ulogin_f1,text="Forgot your password?",fg="White",bg="#888888",font=("Inter",15,"italic"))
    ulogin_l4.place(relx=0.35,rely=0.67)

    #click here
    ulogin_b1=tk.Button(ulogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=new)
    ulogin_b1.place(relx=0.713,rely=0.666)


    #login button
    ulogin_b2=CTkButton(ulogin_f1,text="LOGIN",text_color="Black",corner_radius=8,fg_color="#543627",hover_color="#543627",font=("Inter",20,"bold"), command = login)
    ulogin_b2.place(relx=0.35,rely=0.77,relwidth=0.3,relheight=0.1)


    #dont have account label
    ulogin_b5=tk.Label(ulogin_f1,text="Dont have an account?",fg="White",bg="#888888",font=("Inter",15,"italic"))
    ulogin_b5.place(relx=0.2,rely=0.9)

    #button for dont have an account
    ulogin_b3=tk.Button(ulogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=click_here)
    ulogin_b3.place(relx=0.56,rely=0.896)


    # eye button
    ulogin_b4=tk.Button(ulogin_f1,image=ulogin_eyetk,bg="#FAF3DB",activebackground="#FAF3DB",border=0,command=onclick)
    ulogin_b4.place(relx=0.8,rely=0.595)

    #the back button
    ulogin_b5=tk.Button(ulogin_f1,image=ulogin_backtk,text=" Back",compound=LEFT,bg="#888888",activebackground="#888888",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
    ulogin_b5.place(relx=0.048,rely=0.903)















def admin_login():
    #the main frame 
    main_frame4 = CTkFrame(root)
    main_frame4.place(relwidth = 1, relheight = 1,x = 0, y = 0)

    def back():
        #function to get to dashboard page when back button is clicked 
        main_frame4.place_forget()
        main()


    def no_account():
        #function to open admin_signup page when button in dont have an account is clicked
        main_frame4.place_forget()
        admin_signup()


    def stretch(event):
        '''
        this function is made so that the pictures fits on the screen 
        even when the screen size changes . 
        '''
        global resized_tk

        #for the changing width and height of the window
        width=event.width
        height=event.height

        resized_image=alogin_bg.resize((width,height))
        resized_tk=ImageTk.PhotoImage(resized_image)
    
        canvas.create_image(0,0,anchor=tk.NW,image=resized_tk)
        


    def onclick():
        '''
        it is made so that we can hide or show password clicking the eye button
        '''
        if alogin_e2.cget("show") == "":
            alogin_e2.configure(show="*")
        else:
            alogin_e2.configure(show="")

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
        main_frame4.place_forget()
        admin_dashboard()   
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
        win2.iconbitmap("pictures//32432hotbeverage_98916.ico")
        #the pic in the top label window
        sec_image=Image.open("pictures\\forgot-pass-pic.jpg")
        sec_image_resize=sec_image.resize((626,626))
        sec_image_tk=ImageTk.PhotoImage(sec_image_resize)
        sec_label1=tk.Label(win2,image=sec_image_tk)
        sec_label1.image = sec_image_tk  #reference to the picture
        sec_label1.place(relheight=1,relwidth=1,relx=0.2499)



    #the main frame of win1 
        sec_frame1=tk.Frame(win2,bg="#001129",width=626,height=626)
        sec_frame1.place(x=0,y=0)

    #frame which contains the questions 
        sec_frame2=tk.Frame(sec_frame1,bg="#001129",width=426,height=450,bd=3,relief="groove")
        sec_frame2.place(relx=0.16,rely=0.13)

    #label for security questions heading
        sec_lbl2=tk.Label(sec_frame1,text="Security Questions",font=("Inter",20,"bold"),fg="White",bg="#001129")
        sec_lbl2.place(relx=0.3,rely=0.1)

    #label for 1st question
        sec_lbl3=tk.Label(sec_frame2,text="Q1.  Which is your favourite number?",fg="White",bg="#001129",font=("Regular",15))
        sec_lbl3.place(relx=0.05,rely=0.1)

    #entry for 1st question
        sec_entry1=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
        sec_entry1.place(relx=0.17,rely=0.17)

    #label for 2nd question
        sec_lbl4=tk.Label(sec_frame2,text="Q2.  Which is your favourite food?",fg="White",bg="#001129",font=("Regular",15))
        sec_lbl4.place(relx=0.05,rely=0.32)

    #entry for 2nd question
        sec_entry2=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
        sec_entry2.place(relx=0.17,rely=0.39)

    #label for 3rd question
        sec_lbl5=tk.Label(sec_frame2,text="Q3.  Which is your favourite color?",fg="White",bg="#001129",font=("Regular",15))
        sec_lbl5.place(relx=0.05,rely=0.54)

    #entry for 3rd question
        sec_entry3=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
        sec_entry3.place(relx=0.17,rely=0.61)

    #the submit button
        sec_button1=CTkButton(sec_frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=security_update)
        sec_button1.place(relx=0.3,rely=0.8)
        pass


#making pictures global so they dont get garbage collected 
    global alogin_eyetk,alogin_backtk,photo_alogin_logo



    #eye button pic
    alogin_eye=Image.open("pictures\\ion_eyeeye.png")
    alogin_eyetk=ImageTk.PhotoImage(alogin_eye)


    #bg image
    alogin_bg = Image.open("pictures\\coffee.jpg")
    alogin_bgtk=ImageTk.PhotoImage(alogin_bg)

    alogin_back=Image.open("pictures//Vectorarrow.png")
    alogin_backtk=ImageTk.PhotoImage(alogin_back)


    #canvas widget which covers the entire screen
    canvas=tk.Canvas(main_frame4,bg="black",bd=0,highlightthicknes=0)
    canvas.place(relwidth=1,relheight=1)
    canvas.bind("<Configure>",stretch)

    #The main frame
    alogin_f1=CTkFrame(main_frame4,fg_color="#888888",bg_color="White",corner_radius=8)
    alogin_f1.place(relx=0.08,rely=0.15,relheight=0.7,relwidth=0.3)


    #logo
    alogin_logo=Image.open("pictures\\logo-no-1.png")#insert image
    alogin_logo=alogin_logo.resize((516,106))#resize
    photo_alogin_logo=ImageTk.PhotoImage(alogin_logo)#pil to photo image
    alogin_lbl = tk.Label(alogin_f1, image=photo_alogin_logo,bg="#888888")#label
    alogin_lbl.place(x=20, y=15, w=516, h=106)



    #for spacing between logo and login frame
    alogin_sep=tk.Frame(alogin_f1,bg="#F8F9F7")
    alogin_sep.place(relwidth=1,relheight=0.018,relx=0,rely=0.2)

    #login heading
    alogin_lbl1=tk.Label(alogin_f1,text="Admin Login",bg="#888888",font=("Inter",25,"bold"))
    alogin_lbl1.place(relx=0.26,rely=0.25,relwidth=0.5,relheight=0.1)

    alogin_lbl2=tk.Label(alogin_f1,text="Email:",bg="#888888",font=("Regular",20))
    alogin_lbl2.place(relx=0.08,rely=0.34)

    #email entrybox
    alogin_e1=CTkEntry(alogin_f1,fg_color="#FAF3DB",placeholder_text="example@gmail.com",placeholder_text_color="#DD2323",border_color="#888888",text_color="#DD2323",font=("Regular",15))
    alogin_e1.place(relx=0.08,rely=0.40,relwidth=0.8,relheight=0.09)

    #password label
    alogin_lbl3=tk.Label(alogin_f1,text="Password:",bg="#888888",font=("Regular",20))
    alogin_lbl3.place(relx=0.08,rely=0.51)



    #password entrybox
    alogin_e2=CTkEntry(alogin_f1,fg_color="#FAF3DB",border_color="#888888",text_color="#DD2323",font=("Regular",15),show="*")
    alogin_e2.place(relx=0.08,rely=0.57,relwidth=0.8,relheight=0.09)


    #forgot pass label
    alogin_lbl4=tk.Label(alogin_f1,text="Forgot your password?",fg="White",bg="#888888",font=("Inter",15,"italic"))
    alogin_lbl4.place(relx=0.35,rely=0.67)

    #click here
    alogin_btn1=tk.Button(alogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=new)
    alogin_btn1.place(relx=0.713,rely=0.666)


    #login button
    alogin_btn2=CTkButton(alogin_f1,text="LOGIN",text_color="Black",corner_radius=8,fg_color="#543627",hover_color="#543627",font=("Inter",20,"bold"), command = login)
    alogin_btn2.place(relx=0.35,rely=0.77,relwidth=0.3,relheight=0.1)


    #dont have account label
    alogin_lbl5=tk.Label(alogin_f1,text="Dont have an account?",fg="White",bg="#888888",font=("Inter",15,"italic"))
    alogin_lbl5.place(relx=0.28,rely=0.9)

    #button for dont have an account
    alogin_btn3=tk.Button(alogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=no_account)
    alogin_btn3.place(relx=0.64,rely=0.896)


    # eye button
    alogin_btn4=tk.Button(alogin_f1,image=alogin_eyetk,bg="#FAF3DB",activebackground="#FAF3DB",border=0,command=onclick)
    alogin_btn4.place(relx=0.8,rely=0.595)

    #the back button
    alogin_btn5=tk.Button(alogin_f1,image=alogin_backtk,text=" Back",compound=LEFT,bg="#888888",activebackground="#888888",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
    alogin_btn5.place(relx=0.048,rely=0.903)


    pass




def user_signup():


#the main frame
    main_frame3=CTkFrame(root)
    main_frame3.place(relwidth=1,relheight=1,x=0,y=0)


    def usignup_but():
        #function to open user login page after clicking signup button
        main_frame3.place_forget()
        user_login()


    def back():
       #function to open dashboard when back  utton is clicked 
       main_frame3.place_forget()
       main()




    def already_acc():
        #function to open user login page when click here button is clicked in already have an account
        main_frame3.place_forget()
        user_login()




    def password():
        '''
        it is made so that we can hide or show password clicking the eye button in password
        '''
        if usignup_e4.cget("show") == "":
            usignup_e4.configure(show="*")
        else:
            usignup_e4.configure(show="")

    def repassword():
        '''
        it is made so that we can hide or show password clicking the eye button in  repassword
        '''
        if usignup_e5.cget("show") == "":
            usignup_e5.configure(show="*")
        else:
            usignup_e5.configure(show="")


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
        win2.iconbitmap("pictures//32432hotbeverage_98916.ico")
        #the pic in the top label window
        sec_image=Image.open("pictures\\forgot-pass-pic.jpg")
        sec_image_resize=sec_image.resize((626,626))
        sec_image_tk=ImageTk.PhotoImage(sec_image_resize)
        sec_label1=tk.Label(win2,image=sec_image_tk)
        sec_label1.image = sec_image_tk  #reference to the picture
        sec_label1.place(relheight=1,relwidth=1,relx=0.2499)


    #the main frame of win1 
        sec_frame1=tk.Frame(win2,bg="#001129",width=626,height=626)
        sec_frame1.place(x=0,y=0)

    #frame which contains the questions 
        sec_frame2=tk.Frame(sec_frame1,bg="#001129",width=426,height=450,bd=3,relief="groove")
        sec_frame2.place(relx=0.16,rely=0.13)

    #label for security questions heading
        sec_lbl2=tk.Label(sec_frame1,text="Security Questions",font=("Inter",20,"bold"),fg="White",bg="#001129")
        sec_lbl2.place(relx=0.3,rely=0.1)

    #label for 1st question
        sec_lbl3=tk.Label(sec_frame2,text="Q1.  Which is your favourite number?",fg="White",bg="#001129",font=("Regular",15))
        sec_lbl3.place(relx=0.05,rely=0.1)

    #entry for 1st question
        sec_entry1=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
        sec_entry1.place(relx=0.17,rely=0.17)

    #label for 2nd question
        sec_lbl4=tk.Label(sec_frame2,text="Q2.  Which is your favourite food?",fg="White",bg="#001129",font=("Regular",15))
        sec_lbl4.place(relx=0.05,rely=0.32)

    #entry for 2nd question
        sec_entry2=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
        sec_entry2.place(relx=0.17,rely=0.39)

    #label for 3rd question
        sec_lbl5=tk.Label(sec_frame2,text="Q3.  Which is your favourite color?",fg="White",bg="#001129",font=("Regular",15))
        sec_lbl5.place(relx=0.05,rely=0.54)

    #entry for 3rd question
        sec_entry3=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
        sec_entry3.place(relx=0.17,rely=0.61)

    #the submit button
        sec_button1=CTkButton(sec_frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=security_info)
        sec_button1.place(relx=0.3,rely=0.8)
        pass

    def message():
        tk.messagebox.showinfo("Security question message","Security question must be answered. In case if you forgot your password, then this will help you reset your password .")


    global tksignup_eye,tkusignup_i,photo_usignup_logo,usignup_backtk,photosignup_image1
    

    #the bg frame
    usignup_frame=tk.Frame(main_frame3,bg="Black")
    usignup_frame.place(relwidth=1,relheight=1)

    #the main bg picture 
    usignup_image1=Image.open("pictures\\f327a69f-4c36-4c1e-8965-c5a71e3d9d99.png")
    usignup_image1=usignup_image1.resize((968,1080))
    photosignup_image1=ImageTk.PhotoImage(usignup_image1)
    usignup_label = tk.Label(main_frame3, image=photosignup_image1)
    usignup_label.place(x=952, y=0, w=968, h=1080)


    #image for eye button in password and repassword
    usignup_eye=Image.open("pictures\\ion_eyeeye.png")
    tksignup_eye=ImageTk.PhotoImage(usignup_eye)


    #image for i button 
    usignup_i=Image.open("pictures\\Vector.png")
    tkusignup_i=ImageTk.PhotoImage(usignup_i)


    #label for mealmate logo
    usignup_logo=Image.open("pictures\\logo-no-2.png")
    usignup_logo=usignup_logo.resize((641,141))
    photo_usignup_logo=ImageTk.PhotoImage(usignup_logo)
    usignup_logo_lbl = tk.Label(main_frame3, image=photo_usignup_logo,bg="#262731")
    usignup_logo_lbl.place(x=138, y=62, w=641, h=141)

    #image for back button
    usignup_back=Image.open("pictures//Vectorarrow.png")
    usignup_backtk=ImageTk.PhotoImage(usignup_back)




    #the main frame
    usignup_f1=CTkFrame(usignup_frame,bg_color="transparent",corner_radius=10,fg_color="#262731",width=681,height=900)
    usignup_f1.place(x=100,y=39,w=681,h=900)

    #sep frame
    sep_frame=tk.Frame(usignup_f1,bg="Black")
    sep_frame.place(relwidth=1,relheight=0.02,rely=0.2)

    #signup heading label
    usignup_lbl1=tk.Label(usignup_f1,text="User SignUp",font=("Inter",25,"bold"),bg="#262731",fg="white")
    usignup_lbl1.place(relx=0.32,rely=0.23)

    #firstname label
    usignup_lbl2=tk.Label(usignup_f1,text="First Name:",font=("Regular",15),bg="#262731",fg="White")
    usignup_lbl2.place(relx=0.05,rely=0.3)

    #firstname entry
    usignup_e1=CTkEntry(usignup_f1,placeholder_text="firstname",fg_color="#FAF3DB",width=180,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
    usignup_e1.place(relx=0.05,rely=0.33)

    #lastname label
    usignup_lbl3=tk.Label(usignup_f1,text="Last Name:",font=("Regular",15),bg="#262731",fg="White")
    usignup_lbl3.place(relx=0.53,rely=0.29)

    #lastname entry
    usignup_e2=CTkEntry(usignup_f1,placeholder_text="lastname",fg_color="#FAF3DB",width=190,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
    usignup_e2.place(relx=0.53,rely=0.33)

    #email label
    usignup_lbl4=tk.Label(usignup_f1,text="Email:",font=("Regular",15),bg="#262731",fg="White")
    usignup_lbl4.place(relx=0.05,rely=0.43)

    #email entry
    usignup_e3=CTkEntry(usignup_f1,placeholder_text="example@gmail.com",fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
    usignup_e3.place(relx=0.05,rely=0.46)

    #password label
    usignup_lbl5=tk.Label(usignup_f1,text="Password:",font=("Regular",15),bg="#262731",fg="White")
    usignup_lbl5.place(relx=0.05,rely=0.56)

    #password entry
    usignup_e4=CTkEntry(usignup_f1,fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",corner_radius=8,border_width=0,show="*")
    usignup_e4.place(relx=0.05,rely=0.59)

    #repassword label
    usignup_lbl6=tk.Label(usignup_f1,text="Re-Password:",font=("Regular",15),bg="#262731",fg="White")
    usignup_lbl6.place(relx=0.05,rely=0.69)

    #repassword entry
    usignup_e5=CTkEntry(usignup_f1,fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",corner_radius=8,border_width=0,show="*")
    usignup_e5.place(relx=0.05,rely=0.72)

    #security question label
    usignup_b1=CTkButton(usignup_f1,text="Security Questions",text_color="#CF7941",width=300,height=40,fg_color="#FAF3DB",hover=0,font=("Inter",15,"bold"),corner_radius=8,command=newwin)
    usignup_b1.place(relx=0.2,rely=0.81)

    #Signup button
    usignup_b2=CTkButton(usignup_f1,text="SIGN UP",fg_color="#FAF3DB",hover=0,height=45,font=("Inter",20,"bold"),text_color="#4D5053",corner_radius=8,command=usignup_but)
    usignup_b2.place(relx=0.35,rely=0.92)

    #eye button in password
    usignup_b3=tk.Button(usignup_f1,image=tksignup_eye,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = password)
    usignup_b3.place(relx=0.8,rely=0.61)

    #eye button in repassword
    usignup_b4=tk.Button(usignup_f1,image=tksignup_eye,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = repassword)
    usignup_b4.place(relx=0.8,rely=0.74)

    #i button in security question
    usignup_btn1=tk.Button(usignup_f1,image=tkusignup_i,bg="#FAF3DB",activebackground="#FAF3DB",bd=0,command=message)
    usignup_btn1.place(relx=0.68,rely=0.825)

    #already an account label
    usignup_lbl7=tk.Label(usignup_f1,text="Already have an account?",font=("Inter",12,"italic"),bg="#262731",fg="White")
    usignup_lbl7.place(relx=0.48,rely=0.87)

    # click here button 
    usignup_b5=tk.Button(usignup_f1,text="click here",font=("Inter",12,"bold italic"),bg="#262731",fg="#DD2323",activebackground="#262731",bd=0,command=already_acc)
    usignup_b5.place(relx=0.76,rely=0.869)

    #back button 
    usignup_btn1=tk.Button(usignup_f1,image=usignup_backtk,text=" Back",compound=LEFT,bg="#262731",activebackground="#262731",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
    usignup_btn1.place(relx=0.048,rely=0.94)
    pass
 


def admin_signup():
    #the main frame
    main_frame5=CTkFrame(root)
    main_frame5.place(relwidth=1,relheight=1,x=0,y=0)


    def asignup_but():
        #function to open admin login page after signup
        main_frame5.place_forget()
        admin_login()

    def back():
        #function to open dashboard when back button is clicked 
        main_frame5.place_forget()
        main()




    def already_acc():
        #function for click here ]button in already have an account
        main_frame5.place_forget()
        admin_login()




    def password():
        '''
        it is made so that we can hide or show password clicking the eye button in password
        '''
        if asignup_e4.cget("show") == "":
            asignup_e4.configure(show="*")
        else:
            asignup_e4.configure(show="")

    def repassword():
        '''
        it is made so that we can hide or show password clicking the eye button in  repassword
        '''
        if asignup_e5.cget("show") == "":
            asignup_e5.configure(show="*")
        else:
            asignup_e5.configure(show="")


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
        win2.iconbitmap("pictures//32432hotbeverage_98916.ico")
        #the pic in the top label window
        sec_image=Image.open("pictures\\forgot-pass-pic.jpg")
        sec_image_resize=sec_image.resize((626,626))
        sec_image_tk=ImageTk.PhotoImage(sec_image_resize)
        sec_label1=tk.Label(win2,image=sec_image_tk)
        sec_label1.image = sec_image_tk  #reference to the picture
        sec_label1.place(relheight=1,relwidth=1,relx=0.2499)



    #the main frame of win1 
        sec_frame1=tk.Frame(win2,bg="#001129",width=626,height=626)
        sec_frame1.place(x=0,y=0)

    #frame which contains the questions 
        sec_frame2=tk.Frame(sec_frame1,bg="#001129",width=426,height=450,bd=3,relief="groove")
        sec_frame2.place(relx=0.16,rely=0.13)

    #label for security questions heading
        sec_lbl2=tk.Label(sec_frame1,text="Security Questions",font=("Inter",20,"bold"),fg="White",bg="#001129")
        sec_lbl2.place(relx=0.3,rely=0.1)

    #label for 1st question
        sec_lbl3=tk.Label(sec_frame2,text="Q1.  Which is your favourite number?",fg="White",bg="#001129",font=("Regular",15))
        sec_lbl3.place(relx=0.05,rely=0.1)

    #entry for 1st question
        sec_entry1=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
        sec_entry1.place(relx=0.17,rely=0.17)

    #label for 2nd question
        sec_lbl4=tk.Label(sec_frame2,text="Q2.  Which is your favourite food?",fg="White",bg="#001129",font=("Regular",15))
        sec_lbl4.place(relx=0.05,rely=0.32)

    #entry for 2nd question
        sec_entry2=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
        sec_entry2.place(relx=0.17,rely=0.39)

    #label for 3rd question
        sec_lbl5=tk.Label(sec_frame2,text="Q3.  Which is your favourite color?",fg="White",bg="#001129",font=("Regular",15))
        sec_lbl5.place(relx=0.05,rely=0.54)

    #entry for 3rd question
        sec_entry3=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
        sec_entry3.place(relx=0.17,rely=0.61)

    #the submit button
        sec_button1=CTkButton(sec_frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=security_info)
        sec_button1.place(relx=0.3,rely=0.8)
        pass

    def message():
        tk.messagebox.showinfo("Security question message","Security question must be answered. In case if you forgot your password, then this will help you reset your password .")

    global tksignup_eye,tkasignup_i,photo_asignup_logo,asignup_backtk,photosignup_image1

    #the bg frame
    asignup_frame=tk.Frame(main_frame5,bg="Black")
    asignup_frame.place(relwidth=1,relheight=1)

    #the main bg picture 
    asignup_image1=Image.open("pictures\\f327a69f-4c36-4c1e-8965-c5a71e3d9d99.png")
    asignup_image1=asignup_image1.resize((968,1080))
    photosignup_image1=ImageTk.PhotoImage(asignup_image1)
    asignup_label = tk.Label(main_frame5, image=photosignup_image1)
    asignup_label.place(x=952, y=0, w=968, h=1080)


    #image for eye button in password and repassword
    asignup_eye=Image.open("pictures\\ion_eyeeye.png")
    tksignup_eye=ImageTk.PhotoImage(asignup_eye)


    #image for i button 
    asignup_i=Image.open("pictures\\Vector.png")
    tkasignup_i=ImageTk.PhotoImage(asignup_i)

    #label for mealmate logo
    asignup_logo=Image.open("pictures\\logo-no-2.png")
    asignup_logo=asignup_logo.resize((641,141))
    photo_asignup_logo=ImageTk.PhotoImage(asignup_logo)
    asignup_logo_lbl = tk.Label(main_frame5, image=photo_asignup_logo,bg="#262731")
    asignup_logo_lbl.place(x=138, y=62, w=641, h=141)

    asignup_back=Image.open("pictures//Vectorarrow.png")
    asignup_backtk=ImageTk.PhotoImage(asignup_back)



    #the main frame
    asignup_f1=CTkFrame(asignup_frame,corner_radius=10,fg_color="#262731",width=681,height=900)
    asignup_f1.place(x=100,y=39,w=681,h=900)

    #sep frame
    sep_frame=tk.Frame(asignup_f1,bg="Black")
    sep_frame.place(relwidth=1,relheight=0.02,rely=0.2)

    #signup heading label
    asignup_lbl1=tk.Label(asignup_f1,text="Admin SignUp",font=("Inter",25,"bold"),bg="#262731",fg="white")
    asignup_lbl1.place(relx=0.32,rely=0.23)

    #firstname label
    asignup_lbl2=tk.Label(asignup_f1,text="First Name:",font=("Regular",15),bg="#262731",fg="White")
    asignup_lbl2.place(relx=0.05,rely=0.3)

    #firstname entry
    asignup_e1=CTkEntry(asignup_f1,placeholder_text="firstname",fg_color="#FAF3DB",width=180,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
    asignup_e1.place(relx=0.05,rely=0.33)

    #lastname label
    asignup_lbl3=tk.Label(asignup_f1,text="Last Name:",font=("Regular",15),bg="#262731",fg="White")
    asignup_lbl3.place(relx=0.53,rely=0.29)

    #lastname entry
    asignup_e2=CTkEntry(asignup_f1,placeholder_text="lastname",fg_color="#FAF3DB",width=190,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
    asignup_e2.place(relx=0.53,rely=0.33)

    #email label
    asignup_lbl4=tk.Label(asignup_f1,text="Email:",font=("Regular",15),bg="#262731",fg="White")
    asignup_lbl4.place(relx=0.05,rely=0.43)

    #email entry
    asignup_e3=CTkEntry(asignup_f1,placeholder_text="example@admin.gmail.com ",fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
    asignup_e3.place(relx=0.05,rely=0.46)

    #password label
    asignup_lbl5=tk.Label(asignup_f1,text="Password:",font=("Regular",15),bg="#262731",fg="White")
    asignup_lbl5.place(relx=0.05,rely=0.56)

    #password entry
    asignup_e4=CTkEntry(asignup_f1,fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",corner_radius=8,border_width=0,show="*")
    asignup_e4.place(relx=0.05,rely=0.59)

    #repassword label
    asignup_lbl6=tk.Label(asignup_f1,text="Re-Password:",font=("Regular",15),bg="#262731",fg="White")
    asignup_lbl6.place(relx=0.05,rely=0.69)

    #repassword entry
    asignup_e5=CTkEntry(asignup_f1,fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",corner_radius=8,border_width=0,show="*")
    asignup_e5.place(relx=0.05,rely=0.72)

    #security question label
    asignup_b1=CTkButton(asignup_f1,text="Security Questions",text_color="#CF7941",width=300,height=40,fg_color="#FAF3DB",hover=0,font=("Inter",15,"bold"),corner_radius=8,command=newwin)
    asignup_b1.place(relx=0.2,rely=0.81)

    #Signup button
    asignup_b2=CTkButton(asignup_f1,text="SIGN UP",fg_color="#FAF3DB",hover=0,height=45,font=("Inter",20,"bold"),text_color="#4D5053",corner_radius=8,command=asignup_but)
    asignup_b2.place(relx=0.35,rely=0.92)

    #eye button in password
    asignup_b3=tk.Button(asignup_f1,image=tksignup_eye,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = password)
    asignup_b3.place(relx=0.8,rely=0.61)

    #eye button in repassword
    asignup_b4=tk.Button(asignup_f1,image=tksignup_eye,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = repassword)
    asignup_b4.place(relx=0.8,rely=0.74)

    #i button in security question
    asignup_btn1=tk.Button(asignup_f1,image=tkasignup_i,bg="#FAF3DB",activebackground="#FAF3DB",bd=0,command=message)
    asignup_btn1.place(relx=0.68,rely=0.825)

    #already an account label
    asignup_lbl7=tk.Label(asignup_f1,text="Already have an account?",font=("Inter",12,"italic"),bg="#262731",fg="White")
    asignup_lbl7.place(relx=0.48,rely=0.87)

    # click here button 
    asignup_b5=tk.Button(asignup_f1,text="click here",font=("Inter",12,"bold italic"),bg="#262731",fg="#DD2323",activebackground="#262731",bd=0,command=already_acc)
    asignup_b5.place(relx=0.76,rely=0.869)

    #the back button
    asignup_btn1=tk.Button(asignup_f1,image=asignup_backtk,text=" Back",compound=LEFT,bg="#262731",activebackground="#262731",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
    asignup_btn1.place(relx=0.048,rely=0.94)
    


    pass

def admin_dashboard():
    # the main frame
    main_frame6=CTkFrame(root,fg_color="Black")
    main_frame6.place(relheight=1,relwidth=1,relx=0,rely=0)

    global photo_a_db_logo, a_db_img1ctk, a_db_img5ctk, a_db_img2ctk, a_db_img6ctk, a_db_img3ctk, a_db_img7ctk, a_db_img4ctk, a_db_img8ctk, a_db_img9tk, photo_a_db_bg
    global admin_db_btn2,admin_db_btn3,admin_db_btn3_lbl,admin_db_btn4,admin_db_btn5


    def on_hover(enter):
        #to change the text colour and image of button on entering the widget
        admin_db_btn2.configure(image=a_db_img5ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

    def off_hover(leave):
        #to change the text colour and image of button on enxiting the widget
        admin_db_btn2.configure(image=a_db_img1ctk,text_color="#DD2323",fg_color="#D9D9D9")


    def on_hover2(enter):
        #to change the text colour and image of button on entering the widget
        admin_db_btn3.configure(text_color="#33303C",fg_color="#F38686",hover_color="#F38686")
        admin_db_btn3_lbl.configure(image=a_db_img6ctk,fg_color="#F38686",bg_color="#F38686")

    def off_hover2(leave):
        #to change the text colour and image of button on enxiting the widget
        admin_db_btn3.configure(text_color="#DD2323",fg_color="#D9D9D9")
        admin_db_btn3_lbl.configure(image=a_db_img2ctk,fg_color="#D9D9D9",bg_color="#D9D9D9")


    def on_hover3(enter):
        #to change the text colour and image of button on entering the widget
        admin_db_btn4.configure(image=a_db_img7ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

    def off_hover3(leave):
        #to change the text colour and image of button on enxiting the widget
        admin_db_btn4.configure(image=a_db_img3ctk,text_color="#DD2323",fg_color="#D9D9D9")


    def on_hover4(enter):
        #to change the text colour and image of button on entering the widget
        admin_db_btn5.configure(image=a_db_img8ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

    def off_hover4(leave):
        #to change the text colour and image of button on enxiting the widget
        admin_db_btn5.configure(image=a_db_img4ctk,text_color="#DD2323",fg_color="#D9D9D9")

    def go_to_dash():
        main_frame6.place_forget()
        tk.messagebox.showinfo("Success Message","LogOut Successful!!!")
        main()


    def dashboard_frame_ad():
        global admin_db_btn3,admin_db_btn3_lbl,admin_db_btn2,admin_db_btn4,admin_db_btn2_dash
        a_db_btn9.configure(text="             Dashboard")
        admin_db_btn2.place_forget()

    #dahboard button
        admin_db_btn2_dash=CTkButton(admin_db_frame2,image=a_db_img5ctk,fg_color="#F38686",text="Dashboard",text_color="#33303C",corner_radius=7,hover=0)
        admin_db_btn2_dash.place(relx=0.21,rely=0.25,relwidth=0.56,relheight=0.06)

    #Items button
        admin_db_btn3=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Items",text_color="#DD2323",corner_radius=7,command = items_frame_ad)
        admin_db_btn3.place(relx=0.21,rely=0.4,relwidth=0.56,relheight=0.06)
        admin_db_btn3_lbl=CTkLabel(admin_db_btn3,image=a_db_img2ctk,text="")
        admin_db_btn3_lbl.place(relx=0.3,rely=0.1)

    #Customers button
        admin_db_btn4=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Customers",text_color="#DD2323",image=a_db_img3ctk,corner_radius=7 , command = customers_frame_ad)
        admin_db_btn4.place(relx=0.21,rely=0.55,relwidth=0.56,relheight=0.06)

        #bindings so that that buttons act as intended
        admin_db_btn3.bind("<Enter>", on_hover2)
        admin_db_btn3.bind("<Leave>", off_hover2)
        admin_db_btn4.bind("<Enter>", on_hover3)
        admin_db_btn4.bind("<Leave>", off_hover3)



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
        #this function is made to make frame in dashboard swap with the frame in items page and make other buttons hover as usual

        #to configure dashboard label to item label
        a_db_btn9.configure(text="    Items")
        
        #making the buttons global 
        global admin_db_btn3,admin_db_btn3_lbl,admin_db_btn2,admin_db_btn4
        admin_db_btn3.place_forget()
        
        #Items button
        admin_db_btn3_items=CTkButton(admin_db_frame2,fg_color="#F38686",text="Items",text_color="#33303C",corner_radius=7,hover=0)
        admin_db_btn3_items.place(relx=0.21,rely=0.4,relwidth=0.56,relheight=0.06)
        #image in items button
        admin_db_btn3_items_lbl=CTkLabel(admin_db_btn3_items,image=a_db_img6ctk,text="")
        admin_db_btn3_items_lbl.place(relx=0.3,rely=0.1)

        #dashboard button
        admin_db_btn2=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Dashboard",image=a_db_img1ctk,text_color="#DD2323",corner_radius=7, command = dashboard_frame_ad)
        admin_db_btn2.place(relx=0.21,rely=0.25,relwidth=0.56,relheight=0.06)

        #customers button
        admin_db_btn4=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Customers",text_color="#DD2323",image=a_db_img3ctk,corner_radius=7 , command = customers_frame_ad)
        admin_db_btn4.place(relx=0.21,rely=0.55,relwidth=0.56,relheight=0.06)

        #bindings so that that buttons act as intended
        admin_db_btn2.bind("<Enter>", on_hover)
        admin_db_btn2.bind("<Leave>", off_hover)
        admin_db_btn4.bind("<Enter>", on_hover3)
        admin_db_btn4.bind("<Leave>", off_hover3)

        #Frame
        admin_db_iframe3=tk.Frame(main_frame6,bg="White")
        admin_db_iframe3.place(relx=0.302,rely=0.12,relwidth=0.7,relheight=0.9)
        pass


    def customers_frame_ad():
        #this function is made to make frame in dashboard swap with the frame in customers page and make other buttons hover as usual

        #this is to configure dashboard label to customers

        a_db_btn9.configure(text="             Customers")

    #making image global
        global admin_db_btn3,admin_db_btn3_lbl,admin_db_btn2,admin_db_btn4
        admin_db_btn4.place_forget()

    #customers button
        admin_db_btn4_customer=CTkButton(admin_db_frame2,fg_color="#F38686",text="Customers",text_color="#33303C",image=a_db_img7ctk,corner_radius=7 ,hover=0, command = customers_frame_ad)
        admin_db_btn4_customer.place(relx=0.21,rely=0.55,relwidth=0.56,relheight=0.06)

    #dashboard button
        admin_db_btn2=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Dashboard",image=a_db_img1ctk,text_color="#DD2323",corner_radius=7, command = dashboard_frame_ad)
        admin_db_btn2.place(relx=0.21,rely=0.25,relwidth=0.56,relheight=0.06)

    #Item button
        admin_db_btn3=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Items",text_color="#DD2323",corner_radius=7,command = items_frame_ad)
        admin_db_btn3.place(relx=0.21,rely=0.4,relwidth=0.56,relheight=0.06)
        admin_db_btn3_lbl=CTkLabel(admin_db_btn3,image=a_db_img2ctk,text="")
        admin_db_btn3_lbl.place(relx=0.3,rely=0.1)

        #Frame
        admin_db_cframe3=tk.Frame(main_frame6,bg="White")
        admin_db_cframe3.place(relx=0.302,rely=0.12,relwidth=0.7,relheight=0.9)

        #bindings so that that buttons act as intended
        admin_db_btn2.bind("<Enter>", on_hover)
        admin_db_btn2.bind("<Leave>", off_hover)

        admin_db_btn3.bind("<Enter>", on_hover2)
        admin_db_btn3.bind("<Leave>", off_hover2)
        
        pass







    #frame
    admin_db_frame1=tk.Frame(main_frame6,bg="#D9D9D9")
    admin_db_frame1.place(relwidth=1,relheight=0.11,x=0,y=0)


    # the logo
    a_db_logo=Image.open("pictures/Rectangle 41.png")
    a_db_logo=a_db_logo.resize((468,97))
    photo_a_db_logo=ImageTk.PhotoImage(a_db_logo)
    #label that contains image
    a_db_lbl = tk.Label(admin_db_frame1, image=photo_a_db_logo,bg="#D9D9D9")
    a_db_lbl.place(x=20, y=6, w=468, h=97)

    #frame
    admin_db_frame4=CTkFrame(admin_db_frame1,corner_radius=10,fg_color="#33303C")
    admin_db_frame4.place(relx=0.4,rely=0.3,relwidth=0.5,relheight=0.4)

    #Button used as a container to display label 
    a_db_btn7=CTkButton(admin_db_frame4,text="          Admin",text_color="#DD2323",fg_color="#D9D9D9",hover=0,font=("Regular",15),corner_radius=14)
    a_db_btn7.place(relx=0.1,rely=0.1,relwidth=0.17)
    a_db_lbl3=tk.Label(a_db_btn7,text="User:",fg="#33303C",font=("Regular",15),bg="#D9D9D9")
    a_db_lbl3.place(relx=0.15,rely=0.05)

    #Button used as a container to display label 
    a_db_btn8=CTkButton(admin_db_frame4,text="          Dristi",text_color="#DD2323",fg_color="#D9D9D9",hover=0,font=("Regular",15),corner_radius=14)
    a_db_btn8.place(relx=0.4,rely=0.1,relwidth=0.18)
    a_db_lbl4=tk.Label(a_db_btn8,text="Name:",fg="#33303C",font=("Regular",15),bg="#D9D9D9")
    a_db_lbl4.place(relx=0.15,rely=0.05)

    #Button used as a container to display label 
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


    #images in dashboard button
    a_db_img1=Image.open("pictures/Group 34group_home2.png")
    a_db_img1ctk=CTkImage(a_db_img1)
    a_db_img5=Image.open("pictures/Group 33grouped_home1.png")
    a_db_img5ctk=CTkImage(a_db_img5)

    #images in items button
    a_db_img2=Image.open("pictures/Vectoriconns-1.png")
    a_db_img2ctk=CTkImage(a_db_img2)
    a_db_img6=Image.open("pictures/Vectoriconns-5.png")
    a_db_img6ctk=CTkImage(a_db_img6)

    #images in customers button
    a_db_img3=Image.open("pictures/Vectoriconns.png")
    a_db_img3ctk=CTkImage(a_db_img3)
    a_db_img7=Image.open("pictures/Vectoriconns-4.png")
    a_db_img7ctk=CTkImage(a_db_img7)

    #images in exit button
    a_db_img4=Image.open("pictures/Groupiconns.png")
    a_db_img4ctk=CTkImage(a_db_img4)
    a_db_img8=Image.open("pictures/Groupiconns-1.png")
    a_db_img8ctk=CTkImage(a_db_img8)

    #the arrow pic in back button
    a_db_img9=Image.open("pictures//Vectorarrow.png")
    a_db_img9tk=ImageTk.PhotoImage(a_db_img9)


    #Dashboard Button
    admin_db_btn2=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Dashboard",image=a_db_img1ctk,text_color="#DD2323",corner_radius=7, command = dashboard_frame_ad)
    admin_db_btn2.place(relx=0.21,rely=0.25,relwidth=0.56,relheight=0.06)

    #Items Button
    admin_db_btn3=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Items",text_color="#DD2323",corner_radius=7,command = items_frame_ad)
    admin_db_btn3.place(relx=0.21,rely=0.4,relwidth=0.56,relheight=0.06)
    admin_db_btn3_lbl=CTkLabel(admin_db_btn3,image=a_db_img2ctk,text="")
    admin_db_btn3_lbl.place(relx=0.3,rely=0.1)

    #Customers Button
    admin_db_btn4=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Customers",text_color="#DD2323",image=a_db_img3ctk,corner_radius=7 , command = customers_frame_ad)
    admin_db_btn4.place(relx=0.21,rely=0.55,relwidth=0.56,relheight=0.06)

    #Exit Button Button
    admin_db_btn5=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Exit",text_color="#DD2323",image=a_db_img4ctk,corner_radius=7,command=lambda:root.destroy())
    admin_db_btn5.place(relx=0.21,rely=0.7,relwidth=0.56,relheight=0.06)

    admin_db_btn6=tk.Button(admin_db_frame2,text=" Log out",font=("Regular",15),image=a_db_img9tk,compound=LEFT,bg="#33303C",activebackground="#33303C",activeforeground="White",fg="White",bd=0,command=go_to_dash)
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



    





def main():
    global main_frame1
    #the mian frame
    main_frame1=tk.Frame(root)
    main_frame1.place(relheight=1,relwidth=1,x=0,y=0)
    #background image
    dashboard_image1=Image.open("pictures\\dashboard_bg.png")
    dashboard_image1=dashboard_image1.resize((1920,990))
    photodashboard_image1=ImageTk.PhotoImage(dashboard_image1)
    #label for image
    dash_label1 = tk.Label(main_frame1, image=photodashboard_image1)
    dash_label1.place(x=0, y=0, w=1920, h=990)


    #image in exit button
    exit_image=ImageTk.PhotoImage(file="pictures/dashicons_exit.png")

    
#image for i button 
    i_image=ImageTk.PhotoImage(file="pictures/Vectori_button(white).png")


#frame
    f=CTkFrame(main_frame1,width=450,height=600,border_width=3,fg_color="White",border_color="BLack")
    f.place(relx=0.35,rely=0.16)

#the image for logo
    image2=Image.open("pictures\\Rectangle 41.png")
    image2=image2.resize((508,105))
    photoimage2=ImageTk.PhotoImage(image2)
#button for logo
    Button1 = tk.Button(f, image=photoimage2,bg="White",activebackground="White",bd=0)
    Button1.place(relx=0.05,rely=0.025)


    f1=CTkFrame(f,bg_color="Black",width=550,height=10,border_color="Black",fg_color="Black")
    f1.place(rely=0.2)

#the frame containing all buttons
    f2=CTkFrame(f,width=433,height=457,fg_color="White",border_color="Black",border_width=3)
    f2.place(relx=0.0201,rely=0.226)


#user login button
    b1=CTkButton(f2,text="User Login",width=262,height=55,corner_radius=30,font=("Inter",33),text_color="#D1D1D1",fg_color="#3A3848",hover=0,command=user_login)
    b1.place(relx=0.204,rely=0.12)
#i button in user login
    ib1=tk.Button(b1,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button1)
    ib1.place(relx=0.87,rely=0.35)

#admin login button
    b2=CTkButton(f2,text="Admin Login",width=262,height=55,corner_radius=30,font=("Inter",33),text_color="#D1BC56",fg_color="#3A3848",hover=0,command=admin_login)
    b2.place(relx=0.204,rely=0.33)
#i button in admin login
    ib2=tk.Button(b2,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button2)
    ib2.place(relx=0.89,rely=0.35)

#user signup button
    b3=CTkButton(f2,text="User Signup",width=262,height=55,corner_radius=30,font=("Inter",33),text_color="#E25A00",fg_color="#3A3848",hover=0,command=user_signup)
    b3.place(relx=0.204,rely=0.54)
#i button in user signup
    ib3=tk.Button(b3,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button3)
    ib3.place(relx=0.89,rely=0.35)

#admin signup button
    b4=CTkButton(f2,text="Admin Signup",width=240,height=55,corner_radius=30,font=("Inter",33),text_color="#48A31E",fg_color="#3A3848",hover=0,command=admin_signup)
    b4.place(relx=0.204,rely=0.74)
#i button in admin signup
    ib4=tk.Button(b4,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button4)
    ib4.place(relx=0.9,rely=0.35)

    back_button=tk.Button(f2,text="Exit",image=exit_image,compound=LEFT,font=("Inter",20),bg="white",activebackground="white",activeforeground="black",bd=0,command=lambda :root.destroy())
    back_button.place(relx=0.05,rely=0.9)
    


    root.mainloop()

if __name__ == '__main__':
    main()