import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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







if __name__ == "__main__":
    root =Tk()
    app = Doctor(root)
    root.mainloop()
