from cProfile import label
from cgitb import text
import random
from sre_parse import State
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m%y"))
        Ref = StringVar()
        Mobile_no = StringVar()
        ePincode = StringVar()
        
        Firstname = StringVar()
        eAddress = StringVar()
        Lastname = StringVar()
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()

        Membership = StringVar()
        Membership.set("0")

        def exitbtt():
            exitbtt = tkinter.messagebox.askyesno("Member Registration Form","Are You Sure")
            if exitbtt > 0:
                root.destroy()
                return
        
        def resetbtt():
            Firstname.set("")
            Ref.set("")
            Mobile_no.set("")
            ePincode.set("")
            eAddress.set("")
            Firstname.set("")
            Lastname.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            Membership.set("0")
            member_gendercmb.current(0)
            member_id_proofrcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt(state=DISABLED)
        def reesetbtt():
            reesetbtt = tkinter.messagebox.askyesno("member registration","sure?")
            if reesetbtt > 0:
                resetbtt()
            elif resetbtt <=0:
                resetbtt()
                detail_labeltxt.delete("1.0",END)
                return

        def Refrence_number():
            ranumber = random.randint(10000,999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def membership_fees():
            if (var5.get()==1):
                member_membershiptxt.configure(state=NORMAL)
                item = float(15000)
                Membership.set(str(item)+"Rs")
            elif(var5.get()==0):
                member_membershiptxt.configure(state=DISABLED)
                Membership.set("0")    
        
        def Receipt():
            Refrence_number()
            detail_labeltxt.insert(END,"\t"+Date_of_Registration.get()+ "  \t "+ 
            Ref.get()+"\t\t"+ Firstname.get() + "\t" + Lastname.get()+ "\t" 
            + Mobile_no.get()+ "\t\t" + eAddress.get() + "\t\t" 
            +  ePincode.get() + member_gendercmb.get() + "\t\t" + Membership.get() + "\t")
        ##################### TITLE ###########################
        title = Label(self.root, text = "Member Registration From", font=("monotype corsive",30,"bold"),bd=5,relief=GROOVE,bg="#E6005C",fg="#000000")
        title.pack(side=TOP,fill=X)

        Manage_frame = Frame(self.root, bd=4,relief=RIDGE,bg="#001a66")
        Manage_frame.place(x=20,y=100,width=450,height=580)

        Cus_title = Label(Manage_frame,text="Customer Detail",font=("arial",20,"bold"),bg="#001a66",fg="white")
        Cus_title.grid(row=0,columnspan=2,pady=5)

        member_detelb1 = Label(Manage_frame,text=" Data",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_detelb1.grid(row=1, column=0,padx=10,pady=5,sticky="w")

        member_datatxt = Entry(Manage_frame,font=("arail",15,"bold"),textvariable=Date_of_Registration)
        member_datatxt.grid(row=1,column=1,pady=5,padx=10,sticky="w")

        member_refib1 = Label(Manage_frame,text=" Refrence ID",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_refib1.grid(row=2, column=0, pady=5, padx=10, sticky="w")
        
        member_reftxt = Entry(Manage_frame,font=("arail",15,"bold"),state=DISABLED,text=Ref)
        member_reftxt.grid(row=2,column=1,pady=5,padx=10,sticky="w")

        member_fnamelb1 = Label(Manage_frame,text=" First Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_fnamelb1.grid(row=3, column=0,padx=10,pady=5,sticky="w")

        member_fnametxt = Entry(Manage_frame,font=("arail",15,"bold"),textvariable=Firstname)
        member_fnametxt.grid(row=3,column=1,pady=5,padx=10,sticky="w")

        member_lnamelb1 = Label(Manage_frame,text=" Last Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_lnamelb1.grid(row=4, column=0,padx=10,pady=5,sticky="w")

        member_lnametxt = Entry(Manage_frame,font=("arail",15,"bold"),textvariable=Lastname)
        member_lnametxt.grid(row=4,column=1,pady=5,padx=10,sticky="w")

        member_mobileb1 = Label(Manage_frame,text=" Mobile No",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_mobileb1.grid(row=5, column=0,padx=10,pady=5,sticky="w")

        member_mobiletxt = Entry(Manage_frame,font=("arail",15,"bold"),textvariable=Mobile_no)
        member_mobiletxt.grid(row=5,column=1,pady=5,padx=10,sticky="w")

        member_addressb1 = Label(Manage_frame,text=" Address",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_addressb1.grid(row=6, column=0,padx=10,pady=5,sticky="w")

        member_addresstxt = Entry(Manage_frame,font=("arail",15,"bold"),textvariable=eAddress)
        member_addresstxt.grid(row=6,column=1,pady=5,padx=10,sticky="w")

        member_pincodelb1 = Label(Manage_frame,text=" Pincode",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_pincodelb1.grid(row=7, column=0,padx=10,pady=5,sticky="w")

        member_pincodetxt = Entry(Manage_frame,font=("arail",15,"bold"),textvariable=ePincode)
        member_pincodetxt.grid(row=7,column=1,pady=5,padx=10,sticky="w")

        member_genderb1 = Label(Manage_frame,text=" Gender",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_genderb1.grid(row=8, column=0,padx=10,pady=5,sticky="w")

        # member_gendertxt = Entry(Manage_frame,font=("arail",15,"bold"),textvariable=ePincode)
        # member_gendertxt.grid(row=6,column=1,pady=5,padx=10,sticky="w")
        member_gendercmb = ttk.Combobox(Manage_frame,text= var4, state="readonly",font=("arial",15,"bold"),width=19)
        member_gendercmb['values'] = ("","Male","Female","Other")
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8, column=1,pady=5,padx=10,sticky="w")

        member_id_proofb1 = Label(Manage_frame,text=" ID Proof",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_id_proofb1.grid(row=9, column=0,padx=10,pady=5,sticky="w")

        member_id_proofrcmb = ttk.Combobox(Manage_frame,text= var3, state="readonly",font=("arial",15,"bold"),width=19)
        member_id_proofrcmb['values'] = ("","Adhaar","Passport","Driving License","Pan Card","Student ID")
        member_id_proofrcmb.current(0)
        member_id_proofrcmb.grid(row=9, column=1,pady=5,padx=10,sticky="w")

        member_memtypelb1 = Label(Manage_frame,text=" Member Type",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_memtypelb1.grid(row=10, column=0,padx=10,pady=5,sticky="w")

        member_memtypecmb = ttk.Combobox(Manage_frame,text= var2, state="readonly",font=("arial",15,"bold"),width=19)
        member_memtypecmb['values'] = ("","Ayushman Card","Insurence"," Pay Immediately","Pay When Leave")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row=10, column=1,pady=5,padx=10,sticky="w")

        member_paymentwithb1 = Label(Manage_frame,text=" PaymentWith",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_paymentwithb1.grid(row=11, column=0,padx=10,pady=5,sticky="w")

        member_paymentwithcmb = ttk.Combobox(Manage_frame,text= var1, state="readonly",font=("arial",15,"bold"),width=19)
        member_paymentwithcmb['values'] = ("","Cash","Debit Card","Credit Card","UPI","VISA","Master Card")
        member_paymentwithcmb.current(0)
        member_paymentwithcmb.grid(row=11, column=1,pady=5,padx=10,sticky="w")

        member_membership = Checkbutton(Manage_frame,text="Mebership Fees",variable=var5,onvalue=1,offvalue=0,font=("arial",15,"bold"),bg="#001a66",fg="white",command=membership_fees)
        member_membership.grid(row=12,column=0,sticky="w")
        member_membershiptxt = Entry(Manage_frame, font=("arial",15,"bold"),state=DISABLED,justify=RIGHT,textvariable=Membership)
        member_membershiptxt.grid(row=12,column=1,pady=5,padx=10,sticky="w")

        detail_frame = Frame(self.root, relief=RIDGE, bg="#001a66")
        detail_frame.place(x=500,y=100,width=850,height=580)
        detail_label = Label(detail_frame,font=("arial",11,"bold"),pady=10,padx=2,width=95,text="Date\t Ref ID\t Firstname   Lastname   Mobile No.   Address   Pincode   Gender   Membership")
        detail_label.grid(row=0,column=0,columnspan=25,sticky="w")
        detail_labeltxt = Text(detail_frame,width=123,height=34,font=("arial",12))
        detail_labeltxt.grid(row=1,column=0,columnspan=25)

        receiptionbtn = Button(detail_frame,padx=2,bd=5,font=("arial",12,"bold"),bg="#ff9966",width=15,text="Receipt",command=Receipt)
        receiptionbtn.grid(row=1,column=0)

        resetbtn = Button(detail_frame,padx=2,bd=5,font=("arial",12,"bold"),bg="#ff9966",width=15,command=reesetbtt,text="Reset")
        resetbtn.grid(row=1,column=1)

        exitbtn = Button(detail_frame,padx=2,bd=5,font=("arial",12,"bold"),bg="#ff9966",width=15,command=exitbtt,text="Exit")
        exitbtn.grid(row=1,column=2)

if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()
