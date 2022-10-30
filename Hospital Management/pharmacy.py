import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def main():
    root = Tk()
    app = windows1(root)
    root.mainloop()

class windows1:
    def __init__(self,master):
        self.master = master
        self.master.title('        Pharmacy Management System            ')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.username = StringVar()
        self.password = StringVar()

        self.LabelTitle = Label(self.frame,text="Pharmacy Management System", font=('arial',40,'bold'),
        bd=10,relief='sunken')
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        self.LoginFrame1 = Frame(self.frame, width=1000,height=300,bd=10,relief='groove')
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2 = Frame(self.frame, width=1000,height=200,bd=10,relief='groove')
        self.LoginFrame2.grid(row=2,column=0,pady=15)

        self.LoginFrame3 = Frame(self.frame, width=1000,height=200,bd=10,relief='groove')
        self.LoginFrame3.grid(row=6,column=0,pady=5)

        self.button_reg = Button(self.LoginFrame3,text="Patient Registration Window",state=DISABLED,font=('arial',15,'bold'),command=self.Registration_window)
        self.button_reg.grid(row=0,column=0,padx=10,pady=10)

        self.button_Hosp = Button(self.LoginFrame3,text="Hospital Management Window",state=DISABLED,font=('arial',15,'bold'),command=self.Hospital_window)
        self.button_Hosp.grid(row=0,column=1,padx=10,pady=10)

        self.button_Dr_appt = Button(self.LoginFrame3,text="Dr Appointment Window",state=DISABLED,font=('arial',15,'bold'),command=self.Dr_Appoint_window)
        self.button_Dr_appt.grid(row=1,column=0,padx=10,pady=10)

        self.button_med_stock = Button(self.LoginFrame3,text="Medicine Management Window",state=DISABLED,font=('arial',15,'bold'),command=self.Medicine_stock)
        self.button_med_stock.grid(row=1,column=1,padx=10,pady=10)

        self.LabelUsername = Label(self.LoginFrame1,text='User Name',font=('arial',20,'bold'),bd=3)
        self.LabelUsername.grid(row=0,column=0)
        
        self.textUsername = Entry(self.LoginFrame1,font=('arial',20,'bold'),bd=3,textvariable = self.username)
        self.textUsername.grid(row=0,column=1,padx=40,pady=15)

        self.LabelPassword = Label(self.LoginFrame1,text='Password',font=('arial',20,'bold'),bd=3)
        self.LabelPassword.grid(row=1,column=0)

        self.textPassword = Entry(self.LoginFrame1,font=('arial',20,'bold'),show="*",bd=3,textvariable = self.password)
        self.textPassword.grid(row=1,column=1,padx=40,pady=15)

        self.button_login = Button(self.LoginFrame2,text = 'login', width=20,font=('arial',18,'bold'),command=self.login_system)
        self.button_login.grid(row=0,column=0,padx=10,pady=10)

        self.button_Reset = Button(self.LoginFrame2,text = 'Reset', width=20,font=('arial',18,'bold'),command=self.reset_btn)
        self.button_Reset.grid(row=0,column=3,padx=10,pady=10)

        self.button_Exit = Button(self.LoginFrame2,text = 'Exit', width=20,font=('arial',18,'bold'),command=self.Exit_btn)
        self.button_Exit.grid(row=0,column=6,padx=10,pady=10)
    
    def login_system(self):
        user = self.username.get()
        pswd = self.password.get()

        if(user == str("admin") and pswd == str("admin")):
            self.button_reg.config(state=NORMAL)
            self.button_Hosp.config(state=NORMAL)
            self.button_Dr_appt.config(state=NORMAL)
            self.button_med_stock.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System","You have invalid user and password")
            self.button_reg.config(state=DISABLED)
            self.button_Hosp.config(state=DISABLED)
            self.button_Dr_appt.config(state=DISABLED)
            self.button_med_stock.config(state=DISABLED)

            self.username.set("")
            self.password.set("")
            self.textUsername.focus()
      
    def reset_btn(self):
        self.button_reg.config(state=DISABLED)
        self.button_Hosp.config(state=DISABLED)
        self.button_Dr_appt.config(state=DISABLED)
        self.button_med_stock.config(state=DISABLED)

        self.username.set("")
        self.password.set("")
        self.textUsername.focus()

    def Exit_btn(self):
        self.Exit_btn = tkinter.messagebox.askyesno("Pharmacy Management System","Are You Sure to exit")
        if self.Exit_btn > 0:
            self.master.destroy()
            return
    
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Hospital(self.newWindow)

    def Dr_Appoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Doctor(self.newWindow)

    def Medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)

# class windows2:
#     def __init__(self,master):
#         self.master = master
#         self.master.title('        Patient Management System            ')
#         self.master.geometry('1350x750+0+0')
#         self.frame = Frame(self.master)
#         self.frame.pack()
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
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Registration(self.newWindow)
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
            Ref.get()+"\t"+ Firstname.get()+"  "  + Lastname.get()+ "\t" 
            + Mobile_no.get()+ "\t" + eAddress.get() + "\t" 
            +  ePincode.get() +"  "+ member_gendercmb.get() + "\t" + Membership.get() + "\n")
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

# class windows3:
#     def __init__(self,master):
#         self.master = master
#         self.master.title('        Hospital Management System            ')
#         self.master.geometry('1350x750+0+0')
#         self.frame = Frame(self.master)
#         self.frame.pack()
class Hospital():
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1200x850+0+0")
        self.root.configure(background="black")

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        cmbTableNames = StringVar()
        HospitalCode = StringVar()
        Number_of_Tablets = StringVar()
        Lot = StringVar()
        IssueDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInformation =StringVar()
        StorageAdvice = StringVar()
        Medication = StringVar()
        PatientId = StringVar()
        PatientNHnumber = StringVar()
        Patientname = StringVar()
        DateofBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        NHSnumber = StringVar()
        Hospital_code = StringVar()

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Hospital Management System","Are you Sure To Exits ??")
            if exitbtn >0:
                root.destroy()
                return
        def deletebtn():
            Ref.set("")
            cmbTableNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumber.set("")
            Patientname.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            Hospital_code.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return
        def resetbtn():
            Ref.set("")
            cmbTableNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumber.set("")
            Patientname.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            Hospital_code.set("")
            TextPrescription.delete("1.0",END)
            return
        def Refrence_btn():
            ranumber = random.randint(100000,999999)
            randnumber = str(ranumber)
            Ref.set(randnumber)

        def PrescriptionDatabtn():
            Refrence_btn()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+Ref.get()+"\t"+PatientId.get()+"\t"+Patientname.get()+"\t"+DateofBirth.get()+"\t"+NHSnumber.get()+"\t"+cmbTableNames.get()+"\t"+Number_of_Tablets.get()+"\t"+IssueDate.get()+"\t"+ExpiryDate.get()+"\t"+ExpiryDate.get()+"\t"+DailyDose.get()+"\t"+StorageAdvice.get()+"\t"+PatientId.get()+"\n")
            return
        
        def Pescriptionfunc():
            Refrence_btn()
            TextPrescription.insert(END,"Patient ID:\t"+PatientId.get()+"\n")
            TextPrescription.insert(END,"Patient Name:\t"+Patientname.get()+"\n")
            TextPrescription.insert(END,"Tablet:\t"+cmbTableNames.get()+"\n")
            TextPrescription.insert(END,"Number of Tablet:\t"+Number_of_Tablets.get()+"\n")
            TextPrescription.insert(END,"Daily Dose:\t"+DailyDose.get()+"\n")
            TextPrescription.insert(END,"Issue Ddate:\t"+IssueDate.get()+"\n")
            TextPrescription.insert(END,"Expiry Date:\t"+ExpiryDate.get()+"\n")
            TextPrescription.insert(END,"Storage:\t"+StorageAdvice.get()+"\n")
            TextPrescription.insert(END,"More Information:\t"+MoreInformation.get()+"\n")
            return

        title = Label(self.root, text = "Hospital Management System", font=("monotype corsive",42,"bold"),
        bd=5,relief=GROOVE,bg="#2eb8b8",fg="black")
        title.pack(side=TOP,fill=X)

        Manage_frame = Frame(self.root, width=1250,height=400,bd=5,relief=RIDGE,bg='#0099cc')
        Manage_frame.place(x=10,y=80)

        Button_frame = Frame(self.root, width=1355,height=55,bd=4,relief=RIDGE,bg='#32B695')
        Button_frame.place(x=10,y=460)

        Data_frame = LabelFrame(self.root, width=1355,height=190,bd=4,relief=RIDGE,bg='#266e73')
        Data_frame.place(x=10,y=510)

        Data_frameLeft = LabelFrame(Manage_frame, width=900,text="General Information",font=("arial",20,"italic bold"),
        height=390,bd=7,relief=RIDGE,bg='#0099cc')
        Data_frameLeft.pack(side=LEFT)

        Data_frameRifgt = LabelFrame(Manage_frame, width=450,text="Prescription",font=("arial",20,"italic bold"),
        height=390,bd=7,relief=RIDGE,bg='#0099cc')
        Data_frameRifgt.pack(side=RIGHT)

        Data_frameData = LabelFrame(Data_frame, width=900,text="Prescription Data",font=("arial",20,"italic bold"),
        height=390,bd=7,relief=RIDGE,bg='#3eb7bb')
        Data_frameData.pack(side=LEFT)

        Datalb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Data",padx=2,bg='#0099cc')
        Datalb1.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        Datatxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Date_of_Registration)
        Datatxt.grid(row=0,column=1,padx=10,pady=5,sticky=E)

        Reflb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Refrence Number",padx=2,bg='#0099cc')
        Reflb1.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        Reftxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,state=DISABLED,textvariable=Ref)
        Reftxt.grid(row=1,column=1,padx=10,pady=5,sticky=E)

        Patientlb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Patient ID",padx=2,bg='#0099cc')
        Patientlb1.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        Patienttxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=PatientId)
        Patienttxt.grid(row=2,column=1,padx=10,pady=5,sticky=E)

        PatientNamelb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Patient Name",padx=2,bg='#0099cc')
        PatientNamelb1.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        PatientNametxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Patientname)
        PatientNametxt.grid(row=3,column=1,padx=10,pady=5,sticky=E)

        Doblb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Date of Birth",padx=2,bg='#0099cc')
        Doblb1.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        Dobtxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=DateofBirth)
        Dobtxt.grid(row=4,column=1,padx=10,pady=5,sticky=E)

        Addresslb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Address",padx=2,bg='#0099cc')
        Addresslb1.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        Addresstxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=PatientAddress)
        Addresstxt.grid(row=5,column=1,padx=10,pady=5,sticky=E)

        NHSnumberlb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="NHS No.",padx=2,bg='#0099cc')
        NHSnumberlb1.grid(row=6,column=0,padx=10,pady=5,sticky=W)
        NHSnumbertxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=NHSnumber)
        NHSnumbertxt.grid(row=6,column=1,padx=10,pady=5,sticky=E)

        Tabletlb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Tablets.",padx=2,bg='#0099cc')
        Tabletlb1.grid(row=7,column=0,padx=10,pady=5,sticky=W)
        Tabletcmb = ttk.Combobox(Data_frameLeft,textvariable=cmbTableNames,width=25,state="readonly",font=('arial',12,'bold'))
        Tabletcmb['values'] = ("","Paracetamol","Dan-p","Dio-1","Calpol","nexium")
        Tabletcmb.grid(row=7,column=1,padx=10,pady=5)

        No_of_Tabletlb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text=" No of Tablets",padx=2,bg='#0099cc')
        No_of_Tabletlb1.grid(row=8,column=0,padx=10,pady=5,sticky=W)
        No_of_Tablettxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Number_of_Tablets)
        No_of_Tablettxt.grid(row=8,column=1,padx=10,pady=5,sticky=E)
       
        HospitalCodelb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text=" Hospital Code",padx=2,bg='#0099cc')
        HospitalCodelb1.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        HospitalCodetxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Hospital_code)
        HospitalCodetxt.grid(row=0,column=3,padx=10,pady=5,sticky=E)

        StorageAdvicelb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text=" Storage Advice",padx=2,bg='#0099cc')
        StorageAdvicelb1.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        StorageAdvicecmb = ttk.Combobox(Data_frameLeft,textvariable=StorageAdvice,width=25,state="readonly",font=('arial',12,'bold'))
        StorageAdvicecmb['values'] = ("","Under Room Temp","below 5 degree","below 0 *c","Refrigenetor")
        StorageAdvicecmb.grid(row=1,column=3,padx=10,pady=5,sticky=E)

        Lotnolb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text=" Lot Number",padx=2,bg='#0099cc')
        Lotnolb1.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        Lotnotxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Lot)
        Lotnotxt.grid(row=2,column=3,padx=10,pady=5,sticky=E)

        Issuelb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text=" Issue Date",padx=2,bg='#0099cc')
        Issuelb1.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        Issuetxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=IssueDate)
        Issuetxt.grid(row=3,column=3,padx=10,pady=5,sticky=E)

        Expirylb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text=" Expiry Date",padx=2,bg='#0099cc')
        Expirylb1.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        Expirytxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=ExpiryDate)
        Expirytxt.grid(row=4,column=3,padx=10,pady=5,sticky=E)

        Doselb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text=" Dose",padx=2,bg='#0099cc')
        Doselb1.grid(row=5,column=2,padx=10,pady=5,sticky=W)
        Dosetxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=DailyDose)
        Dosetxt.grid(row=5,column=3,padx=10,pady=5,sticky=E)

        SideEffectb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text=" Side Effects",padx=2,bg='#0099cc')
        SideEffectb1.grid(row=6,column=2,padx=10,pady=5,sticky=W)
        SideEffecttxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=SideEffects)
        SideEffecttxt.grid(row=6,column=3,padx=10,pady=5,sticky=E)

        Moreinfotb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="  More Informatio",padx=2,bg='#0099cc')
        Moreinfotb1.grid(row=7,column=2,padx=10,pady=5,sticky=W)
        Moreinfotxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=MoreInformation)
        Moreinfotxt.grid(row=7,column=3,padx=10,pady=5,sticky=E)

        Medicationtb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="  Medication",padx=2,bg='#0099cc')
        Medicationtb1.grid(row=8,column=2,padx=10,pady=5,sticky=W)
        Medicationtxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Medication)
        Medicationtxt.grid(row=8,column=3,padx=10,pady=5,sticky=E)

        TextPrescription = Text(Data_frameRifgt,font=("arial",12,'bold'),width=55,height=17,padx=3,pady=5)
        TextPrescription.grid(row=0,column=0)

        TextPrescriptionData = Text(Data_frameData,font=("arial",12,'bold'),width=203,height=12)
        TextPrescriptionData.grid(row=1,column=0)

        Prescriptionbtn = Button(Button_frame,text="Prescription",bg="#ffaab0",activebackground="#fcceb2",
        font=("arial",12,"bold"),width=22,command=Pescriptionfunc)
        Prescriptionbtn.grid(row=0,column=0,padx=15)

        Receiptbtn = Button(Button_frame,text="Prescription Data",bg="#ffaab0",activebackground="#fcceb2",
        font=("arial",12,"bold"),width=25,command=PrescriptionDatabtn)
        Receiptbtn.grid(row=0,column=1,padx=15)

        Resetbtn = Button(Button_frame,text="Reset",bg="#ffaab0",activebackground="#fcceb2",font=("arial",12,"bold"),width=25,command=resetbtn)
        Resetbtn.grid(row=0,column=2,padx=15)

        Deletebtn = Button(Button_frame,text="Delete",bg="#ffaab0",activebackground="#fcceb2",font=("arial",12,"bold"),width=22,command=deletebtn)
        Deletebtn.grid(row=0,column=3,padx=15)

        Exitbtn = Button(Button_frame,text="Exit",bg="#ffaab0",activebackground="#fcceb2",font=("arial",12,"bold"),width=22,command=exitbtn)
        Exitbtn.grid(row=0,column=4,padx=15)

        Pescriptiondatarow = Label(Data_frameData, bg="white",font=('arial',12,"bold"),
        text="Data\tRefrence Id\tPatient Name\tDate of Birth\tNHS Number\tTablet\tNo of Tablets\tIssued Date\tExpiry Date\tDaily Dose\tStorage Advice\tPatien ID")
        Pescriptiondatarow.grid(row=0,column=0,sticky=W)

# class windows4:
#     def __init__(self,master):
#         self.master = master
#         self.master.title('        Doctor Management System            ')
#         self.master.geometry('1350x750+0+0')
#         self.frame = Frame(self.master)
#         self.frame.pack()

class Doctor():
    def __init__(self,root):
        self.root = root
        self.root.title("Doctor Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Doctorname = StringVar()
        Dateofbirth = StringVar()
        Spes = StringVar()
        Govpri = StringVar()
        Surgeries = StringVar()
        Experience = StringVar()
        Nurses = StringVar()
        DrMobile = StringVar()
        PtName = StringVar()
        Apptime = StringVar()
        PtAge = StringVar()
        PatientAddress = StringVar()
        PtMobile = StringVar()
        Disease = StringVar()
        Case = StringVar()
        BenefitCard = StringVar()
        DrID =StringVar()

        def Exitfunc():
            Exitfunc = tkinter.messagebox.askyesno("Doctor Management System","Sure To Exit")
            if Exitfunc>0:
                root.destroy()
                return

        def Resetfunc():
            Doctorname.set("")
            Dateofbirth.set("")
            Spes.set("")
            Govpri.set("")
            Surgeries.set("")
            Experience.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            DrID.set("")
            TextPrescription.delete("1.0",END)
            return
        
        def Deletefunc():
            Doctorname.set("")
            Dateofbirth.set("")
            Spes.set("")
            Govpri.set("")
            Surgeries.set("")
            Experience.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            DrID.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return
        def Patient_idfunc():
            ranumber = random.randint(100000,999999)
            randonumber = str(ranumber)
            DrID.set(randonumber)
        def prescriptiondatafunc():
            Patient_idfunc()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+DrID.get()+"\t"+Doctorname.get()+"\t"+
            Dateofbirth.get()+"\t"+Spes.get()+"\t"+Govpri.get()+"\t"+Surgeries.get()+"\t"+Experience.get()+"\t"+Nurses.get()+"\t"+
            DrMobile.get()+"\t"+PtName.get()+"\t"+Case.get()+"\t"+PtAge.get()+"\n")
            return

        def DrDetailfunc():
            return

        def Pescriptionfunc():
            Patient_idfunc()
            TextPrescription.insert(END,"Date : \t\t"+Date_of_Registration.get()+"\n")
            TextPrescription.insert(END,"Patient Name : \t\t"+PtName.get()+"\n")
            TextPrescription.insert(END,"Appoinment Time : \t\t"+Apptime.get()+"\n")
            TextPrescription.insert(END,"Age : \t\t"+PtAge.get()+"\n")
            TextPrescription.insert(END,"Address : \t\t"+PatientAddress.get()+"\n")
            TextPrescription.insert(END,"Disease : \t\t"+Disease.get()+"\n")
            TextPrescription.insert(END,"Case : \t\t"+Case.get()+"\n")            
            TextPrescription.insert(END,"Benefit of Card : \t\t"+BenefitCard.get()+"\n")
            TextPrescription.insert(END,"Meet To Dr : \t\t"+Doctorname.get()+"\n")
            TextPrescription.insert(END,"Dr. Mobile No : \t\t"+DrMobile.get()+"\n")
            
            return
        title = Label(self.root, text = "Doctor Management System", font=("monotype corsive",42,"bold"),
        bd=5,relief=GROOVE,bg="#b7d8d6",fg="black")
        title.pack(side=TOP,fill=X)

        Manage_frame = Frame(self.root, width=1510,height=400,bd=5,relief=RIDGE,bg='#789e9e')
        Manage_frame.place(x=10,y=80)

        Button_frame = Frame(self.root, width=1510,height=55,bd=4,relief=RIDGE,bg='#eef3db')
        Button_frame.place(x=10,y=460)

        Data_frame = LabelFrame(self.root, width=1510,height=270,bd=4,relief=RIDGE,bg='#eef3db')
        Data_frame.place(x=10,y=510)

        Data_frameLeft = LabelFrame(Manage_frame, width=900,text="General Information",font=("arial",20,"italic bold"),
        height=390,bd=7,relief=RIDGE,bg='#0099cc')
        Data_frameLeft.pack(side=LEFT)

        Data_frameData = LabelFrame(Data_frame, width=900,text="Doctor Details",font=("arial",20,"italic bold"),
        height=390,bd=7,relief=RIDGE,bg='#3eb7bb')
        Data_frameData.pack(side=LEFT)

        Data_frameRifgt = LabelFrame(Manage_frame, width=450,text="Patient Information",font=("arial",20,"italic bold"),
        height=390,bd=7,relief=RIDGE,bg='#0099cc')
        Data_frameRifgt.pack(side=RIGHT)

        Doctorlb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Doctor ID",padx=2,bg='#0099cc')
        Doctorlb1.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        Doctortxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=DrID,state=DISABLED)
        Doctortxt.grid(row=0,column=1,padx=10,pady=5,sticky=E)

        DoctorNamelb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Doctor Name",padx=2,bg='#0099cc')
        DoctorNamelb1.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        DoctorNametxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Doctorname)
        DoctorNametxt.grid(row=1,column=1,padx=10,pady=5,sticky=E)

        Doblb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Date Of Birth",padx=2,bg='#0099cc')
        Doblb1.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        Dobtxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Dateofbirth)
        Dobtxt.grid(row=2,column=1,padx=10,pady=5,sticky=E)

        Speslb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Specialization",padx=2,bg='#0099cc')
        Speslb1.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        Spestxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Spes)
        Spestxt.grid(row=3,column=1,padx=10,pady=5,sticky=E)

        GovPrilb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Gov\Pri",padx=2,bg='#0099cc')
        GovPrilb1.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        GovPricmb = ttk.Combobox(Data_frameLeft,textvariable=Govpri,width=25,state="readonly",font=('arial',12,'bold'))
        GovPricmb['values'] = ("","Government","Private")
        GovPricmb.current(0)
        GovPricmb.grid(row=4,column=1,padx=10,pady=5,sticky=E)

        Sergurieslb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Surgeries",padx=2,bg='#0099cc')
        Sergurieslb1.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        Serguriestxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Surgeries)
        Serguriestxt.grid(row=5,column=1,padx=10,pady=5,sticky=E)

        Experiencelb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Experience",padx=2,bg='#0099cc')
        Experiencelb1.grid(row=6,column=0,padx=10,pady=5,sticky=W)
        Experiencetxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Experience)
        Experiencetxt.grid(row=6,column=1,padx=10,pady=5,sticky=E)

        Nurselb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Nurses Unser Dr",padx=2,bg='#0099cc')
        Nurselb1.grid(row=7,column=0,padx=10,pady=5,sticky=W)
        Nursestxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Nurses)
        Nursestxt.grid(row=7,column=1,padx=10,pady=5,sticky=E)

        DrMobilelb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Dr Mobile",padx=2,bg='#0099cc')
        DrMobilelb1.grid(row=8,column=0,padx=10,pady=5,sticky=W)
        DrMobiletxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=DrMobile)
        DrMobiletxt.grid(row=8,column=1,padx=10,pady=5,sticky=E)

        Datelb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Date",padx=2,bg='#0099cc')
        Datelb1.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        Datetxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Date_of_Registration)
        Datetxt.grid(row=0,column=3,padx=10,pady=5,sticky=E)

        PtNamelb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Patient Name",padx=2,bg='#0099cc')
        PtNamelb1.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        PtNametxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=PtName)
        PtNametxt.grid(row=1,column=3,padx=10,pady=5,sticky=E)

        Apptlb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Appointment Time",padx=2,bg='#0099cc')
        Apptlb1.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        Appttxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Apptime)
        Appttxt.grid(row=2,column=3,padx=10,pady=5,sticky=E)

        PtAgelb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Patient Age",padx=2,bg='#0099cc')
        PtAgelb1.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        PtAgetxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=PtAge)
        PtAgetxt.grid(row=3,column=3,padx=10,pady=5,sticky=E)

        PtAddlb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Patient Address",padx=2,bg='#0099cc')
        PtAddlb1.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        PtAddtxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=PatientAddress)
        PtAddtxt.grid(row=4,column=3,padx=10,pady=5,sticky=E)

        PtMobilelb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Patient Mobile",padx=2,bg='#0099cc')
        PtMobilelb1.grid(row=5,column=2,padx=10,pady=5,sticky=W)
        PtMobiletxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=PtMobile)
        PtMobiletxt.grid(row=5,column=3,padx=10,pady=5,sticky=E)

        Diseaselb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Patient Disease",padx=2,bg='#0099cc')
        Diseaselb1.grid(row=6,column=2,padx=10,pady=5,sticky=W)
        Diseasetxt = Entry(Data_frameLeft,font=('arial',12,'bold'),width=27,textvariable=Disease)
        Diseasetxt.grid(row=6,column=3,padx=10,pady=5,sticky=E)

        caselb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Case",padx=2,bg='#0099cc')
        caselb1.grid(row=7,column=2,padx=10,pady=5,sticky=W)
        casecmb = ttk.Combobox(Data_frameLeft,textvariable=Case,width=25,state="readonly",font=('arial',12,'bold'))
        casecmb['values'] = ("","New Case","Old Case")
        casecmb.current(0)
        casecmb.grid(row=7,column=3,padx=10,pady=5,sticky=E)

        BenifitCardlb1 = Label(Data_frameLeft, font=("arial",12,"bold"),width=20,text="Benefit Card",padx=2,bg='#0099cc')
        BenifitCardlb1.grid(row=8,column=2,padx=10,pady=5,sticky=W)
        BenefitCardcmb = ttk.Combobox(Data_frameLeft,textvariable=BenefitCard,width=25,state="readonly",font=('arial',12,'bold'))
        BenefitCardcmb['values'] = ("","Ayushman Card","Health Insurence","Senior Citizen","Army Card")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row=8,column=3,padx=10,pady=5,sticky=E)

        TextPrescription = Text(Data_frameRifgt,font=("arial",12,'bold'),width=55,height=17,padx=3,pady=5)
        TextPrescription.grid(row=0,column=0)

        TextPrescriptionData = Text(Data_frameData,font=("arial",12,'bold'),width=203,height=12)
        TextPrescriptionData.grid(row=1,column=0)

        Prescriptionbtn = Button(Button_frame,text="Patient Information",bg="#ffaab0",activebackground="#fcceb2",
        font=("arial",12,"bold"),width=22,command=Pescriptionfunc)
        Prescriptionbtn.grid(row=0,column=0,padx=15)

        DrDetailbtn = Button(Button_frame,text="Doctor Details",bg="#ffaab0",activebackground="#fcceb2",
        font=("arial",12,"bold"),width=22,command=prescriptiondatafunc)
        DrDetailbtn.grid(row=0,column=1,padx=15)

        Resetlbtn = Button(Button_frame,text="Reset",bg="#ffaab0",activebackground="#fcceb2",
        font=("arial",12,"bold"),width=22,command=Resetfunc)
        Resetlbtn.grid(row=0,column=2,padx=15)

        Deletbtn = Button(Button_frame,text="Delete",bg="#ffaab0",activebackground="#fcceb2",
        font=("arial",12,"bold"),width=22,command=Deletefunc)
        Deletbtn.grid(row=0,column=3,padx=15)

        Exitbtn = Button(Button_frame,text="Exit",bg="#ffaab0",activebackground="#fcceb2",
        font=("arial",12,"bold"),width=22,command=Exitfunc)
        Exitbtn.grid(row=0,column=4,padx=15)

        Pescriptiondatarow = Label(Data_frameData, bg="white",font=('arial',12,"bold"),
        text="Data\tDoctor Id\tDoctor Name\tDate of Birth\tSpecialization\tGov/Priv\tSurgeries\tExperience\tNurses\tDr Mobile No\tPatient Name\tCase\tPt Age\n")
        Pescriptiondatarow.grid(row=0,column=0,sticky=W)



class windows5:
    def __init__(self,master):
        self.master = master
        self.master.title('        Medicine System            ')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

if __name__=='__main__':
    main()