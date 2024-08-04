import tkinter as tk
from customtkinter import *
from PIL import ImageTk,Image

root=tk.Tk()

def user_login():
    # main_frame1.destroy()
    main_frame2=CTkFrame(root)
    main_frame2.place(relwidth=1,relheight=1,x=0,y=0)

    def reset_successful():
        win2.destroy()
        tk.messagebox.showinfo("Reset Successful","Password reset successful.")

    def no_account():
        root.destroy()
        import user_signup

    def back():
        main_frame2.destroy()
        # main()




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
        if login_e2.cget("show") == "":
            login_e2.configure(show="*")
        else:
            login_e2.configure(show="")
        
    def reset_p1():
        if etr1.cget("show") == "":
            etr1.configure(show="*")
        else:
            etr1.configure(show="")

    def reset_p2():
        if etr2.cget("show") == "":
            etr2.configure(show="*")
        else:
            etr2.configure(show="")
            




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
        win2.iconbitmap("pictures/32432hotbeverage_98916.ico")
        #the pic in the top label window
        
        security_qsn_resize=security_qsn.resize((626,626))
        security_qsn_tk=ImageTk.PhotoImage(security_qsn_resize)
        security_lbl=tk.Label(win2,image=security_qsn_tk)
        security_lbl.image = security_qsn_tk  #reference to the picture
        security_lbl.place(relheight=1,relwidth=1,relx=0.2499)

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
        button1=CTkButton(frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=reset_pass)
        button1.place(relx=0.3,rely=0.8)
        pass



 
    eye_imgtk=ImageTk.PhotoImage(eye_img)


    def reset_pass():
        global etr1
        global etr2

        win3=tk.Toplevel()
        win3.title("Reset password")
        win3.geometry("500x250")
        win3.resizable(0,0)

        lbl1=tk.Label(win3,text="Enter New Password:",font=("Regular",13))
        lbl1.place(relx=0.05,rely=0.08)
        etr1=CTkEntry(win3,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",show="*",text_color="Black")
        etr1.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        lbl2=tk.Label(win3,text="Confirm new Password:",font=("Regular",13))
        lbl2.place(relx=0.05,rely=0.33)
        etr2=CTkEntry(win3,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",show="*",text_color="Black")
        etr2.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        btn1=CTkButton(win3,text="SUBMIT",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",border_width=2,command=reset_successful)
        btn1.place(relx=0.33,rely=0.75,relwidth=0.3,relheight=0.15)

        btn2=tk.Button(win3,image=eye_imgtk,bg="white",activebackground="white",bd=0,command=reset_p1)
        btn2.place(relx=0.78,rely=0.2)

        btn3=tk.Button(win3,image=eye_imgtk,bg="white",activebackground="white",bd=0,command=reset_p2)
        btn3.place(relx=0.78,rely=0.46)


        



    #eye button pic
    eye_var=ImageTk.PhotoImage(eye_open_login)





    #bg image
    a = Image.open("pictures\\coffee.jpg")
    f=ImageTk.PhotoImage(a)

    
    arrow =Image.open("pictures//Vectorarrow.png")
    arrow_var=ImageTk.PhotoImage(arrow)


    #canvas widget which covers the entire screen
    canvas=tk.Canvas(main_frame2,bg="black",bd=0,highlightthicknes=0)
    canvas.place(relwidth=1,relheight=1)
    canvas.bind("<Configure>",stretch)

    #The main frame
    login_f1=CTkFrame(main_frame2,fg_color="#888888",bg_color="White",corner_radius=8)
    login_f1.place(relx=0.08,rely=0.15,relheight=0.7,relwidth=0.3)

    #logo
    login_logo=Image.open("pictures/logo-no-1.png")
    login_logo=login_logo.resize((516,106))
    login_call=ImageTk.PhotoImage(login_logo)
    login_lbl=tk.Label(login_f1,image=login_call,bg="#888888")
    login_lbl.place(x=20,y=15,w=516,h=106)
    

    


    #for spacing between logo and login frame
    login_f2=tk.Frame(login_f1,bg="#F8F9F7")
    login_f2.place(relwidth=1,relheight=0.018,relx=0,rely=0.2)

    #login heading
    login_l1=tk.Label(login_f1,text="User Login",bg="#888888",font=("Inter",25,"bold"))
    login_l1.place(relx=0.26,rely=0.25,relwidth=0.5,relheight=0.07)

    login_l2=tk.Label(login_f1,text="Email:",bg="#888888",font=("Regular",20))
    login_l2.place(relx=0.08,rely=0.34)

    #email entrybox
    login_e2=CTkEntry(login_f1,fg_color="#FAF3DB",placeholder_text="example@gmail.com",placeholder_text_color="#DD2323",border_color="#888888",text_color="#DD2323",font=("Regular",15))
    login_e2.place(relx=0.08,rely=0.40,relwidth=0.8,relheight=0.09)

    #password label
    login_l3=tk.Label(login_f1,text="Password:",bg="#888888",font=("Regular",20))
    login_l3.place(relx=0.08,rely=0.51)



    #password entrybox
    login_e2=CTkEntry(login_f1,fg_color="#FAF3DB",border_color="#888888",text_color="#DD2323",font=("Regular",15),show="*")
    login_e2.place(relx=0.08,rely=0.57,relwidth=0.8,relheight=0.09)


    #forgot pass label
    login_l4=tk.Label(login_f1,text="Forgot your password?",fg="White",bg="#888888",font=("Inter",15,"italic"))
    login_l4.place(relx=0.35,rely=0.67)

    #click here
    login_bl=tk.Button(login_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=new)
    login_bl.place(relx=0.713,rely=0.666)


    #login button
    login_b2=CTkButton(login_f1,text="LOGIN",text_color="Black",corner_radius=8,fg_color="#543627",hover_color="#543627",font=("Inter",20,"bold"), command = login)
    login_b2.place(relx=0.35,rely=0.77,relwidth=0.3,relheight=0.1)


    #dont have account label
    login_l5=tk.Label(login_f1,text="Dont have an account?",fg="White",bg="#888888",font=("Inter",15,"italic"))
    login_l5.place(relx=0.2,rely=0.9)

    #button for dont have an account
    login_b3=tk.Button(login_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"))
    login_b3.place(relx=0.56,rely=0.896)


    # eye button
    login_b4=tk.Button(login_f1,image=eye_var,bg="#FAF3DB",activebackground="#FAF3DB",border=0,command=onclick)
    login_b4.place(relx=0.8,rely=0.595)

    login_b5=tk.Button(login_f1,text=" Back",bg="#888888",activebackground="#888888",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
    login_b5.place(relx=0.048,rely=0.903)


root.mainloop()