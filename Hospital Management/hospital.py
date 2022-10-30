import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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
if __name__ == "__main__":
    root =Tk()
    app = Hospital(root)
    root.mainloop()
