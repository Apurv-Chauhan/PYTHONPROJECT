import sqlite3
import os
import getpass
import matplotlib.pyplot as plt

con= sqlite3.connect("Hospital.db")
tc=0

def illnessAnalysis():
    print("Illness Analysis and Summary ")
    print("--------------------------------------------------------")
    q="select Illness,count(*) from Patient group by Illness "
    cursor=con.execute(q)
    x=[]
    y=[]
    head="%20s   %15s"%("Illness","Total")
    print(head)
    print("--------------------------------------------------------")
    for rec in cursor:
        x.append(rec[0])
        y.append(rec[1])
        r="%20s   %15d"%(rec[0],rec[1])
        print(r)
    print()
    plt.bar(x,y)
    plt.xlabel("Illness")
    plt.ylabel("Patient Count")
    plt.show()
    input("Press ENTER to return to Summary and Analysis Menu ")
    
def genderAnalysis():
    print("Gender Wise Patient Analysis ")
    print("------------------------------------------------------")
    q="select Gender,count(*) from Patient group by Gender "
    cursor=con.execute(q)
    x=[]
    y=[]
    head="%20s   %15s"%("Gender","Total")
    print(head)
    print("------------------------------------------------------")
    for rec in cursor:
        x.append(rec[0])
        y.append(rec[1])
        r="%20s   %15d"%(rec[0],rec[1])
        print(r)
    print()
    plt.bar(x,y)
    plt.xlabel("Gender")
    plt.ylabel("Patient Count")
    plt.show()
    input("Press ENTER to return to Summary and Analysis Menu ")

def ageAnalysis():
    print("Age Wise Patient Analysis ")
    print("--------------------------------------------------------")
    q="select Age,count(*) from Patient group by Age "
    cursor=con.execute(q)
    x=[]
    y=[]
    head="%10s   %15s"%("Age","Total")
    print(head)
    print("--------------------------------------------------------")
    for rec in cursor:
        x.append(rec[0])
        y.append(rec[1])         
        r="%10d   %15d"%(rec[0],rec[1])
        print(r)
    print()
    plt.bar(x,y)
    plt.xlabel("Age")
    plt.ylabel("Patient Count")
    plt.show()
    input("Press ENTER to return to Summary and Analysis Menu ")
    
def isPresent(pname):
    q="select * from Patient where Name='%s'"%(pname)
    cursor=con.execute(q)
    s=cursor.fetchall()
    if len(s)==0:
        return False
    else:
        return True

    
while True:
    os.system("cls")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("WELCOME TO STAR HEALTH HOSPITAL ")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("There's nothing more important than your good health-- That's our capital asset :)")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("1. Press '1' if you want to book an appointment ")
    print("2. Press '2' to see the list of all patients ")
    print("3. Press '3' to see the list of all doctors/nurse staff ")
    print("4. Press '4' for summary and analysis ")
    print("5. Press '5' to update details of any patient ")
    print("6. Exit ")
    print("--------------------------------------------------------------")
    ch=int(input("Please enter your choice "))

    if ch==1:
        os.system("cls")
        print("BOOK AN APPOINTMENT")
        print("-------------------")

        pname=input("Enter Patient's Name   : ")
        if isPresent(pname):
            print("Entered Patient already has an appointment ")
            
            input("Press ENTER to return to MAIN MENU ")
            continue
            
        age=int(input("Enter Patient's Age    :"))
        gen=input("Enter Patient's Gender  :")
        cno=input("Enter Contact Number   :")
        add=input("Enter Address          :")
        ill=input("Kindly enter the illness/disease or the reason to see the doctor :")
        q="insert into Patient values('%s', %d, '%s', '%s', '%s', '%s')"%(pname,age,gen,cno,add,ill)
        con.execute(q)
        con.commit()
        nc=con.total_changes        
        n=nc-tc
        print("Appointment Booked ")
        input=("Press Enter to return to MAIN MENU ")
        tc=nc
        
    elif ch==2:
        os.system("cls")
        uid=input("Admin ID: ")
        pwd=getpass.getpass()
        if uid=="admin" and pwd=="admin123":
            print("List of Patients ")
            print("-----------------------------------------------------------------------------------------------------------------------")
            cursor=con.execute("Select * from Patient ")
            head="%20s      %3s     %6s     %10s      %20s        %25s"%("Patient's Name","Age","Gender","Contact No.","Address","Illness")
            print(head)
            print("-----------------------------------------------------------------------------------------------------------------------")
            for rec in cursor:
                r="%20s     %3d   %6s        %10s          %20s      %25s"%(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5])
                print(r)
                print("------------------------------------------------------------------------------------------------------------------------")
            
            input("Press ENTER to return to MAIN MENU ")
        else:
            print("Incorrect Admin ID/Password ")
            print("----------------------------")
        input("Press ENTER to return to MAIN MENU ")
    elif ch==3:
        os.system("cls")
        print("Enter 'D' to see the list of Doctors ")
        print("Enter 'N' to see the list of Nurses ")
        ch1=input("Enter your choice ")
        if ch1=='D':
            print("List of Doctors ")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            cursor=con.execute("select * from Doctor ")
            head="%20s      %20s                      %10s                          %20s                            %6s"%("Doctor's Name","Speciality","Contact No.","Appointment Hours","Fees(in Rupees)")
            print(head)
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for rec in cursor:
                r="%20s      %20s                 %10s                               %20s                            %6s"%(rec[0],rec[1],rec[2],rec[3],rec[4])
                print(r)
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
               
            input("Press ENTER to return MAIN MENU ")    
        elif ch1=='N':
            print("List of Nurses ")
            print("-------------------------------------------------------------------------------------------------------------")
            cursor=con.execute("select * from Nurse ")
            head="%20s         %20s         %15s"%("Name","Joined Since","Working hours")
            print(head)
            print("-------------------------------------------------------------------------------------------------------------")
            for rec in cursor:
                r="%20s         %20s         %15s"%(rec[0],rec[1],rec[2])
                print(r)
                print("-------------------------------------------------------------------------------------------------------------")
            input("Press ENTER to return to MAIN MENU ")
        else:
            print("Invalid choice ")
            print("Kindly enter a valid choice ")
   
    elif ch==4:
        os.system("cls")
        print("Summary and Analysis ")
        print("----------------------------------------")
        uid=input("Admin ID: ")
        pwd=getpass.getpass()
        if uid=="admin" and pwd=="admin123":
            while True:
                os.system("cls")
                print("1. Illness Analysis ")
                print("2. Gender Analysis ")
                print("3. Age Analysis ")
                print("4. Return to MAIN MENU ")
                print("----------------------------------------")
                ch2=int(input("Enter your choice "))
                if ch2==1:
                    illnessAnalysis()
                elif ch2==2:
                    genderAnalysis()
                elif ch2==3:
                    ageAnalysis()
                elif ch2==4:
                    break
                else:
                    print("Invalid choice ")
                input("Press ENTER ")
        else:
            print("Incorrect Admin ID/Password ")
            print("----------------------------")
        input("Press ENTER to return to MAIN MENU ") 
        
    elif ch==5:
        os.system("cls")
        uid=input("Admin ID: ")
        pwd=getpass.getpass()
        if uid=="admin" and pwd=="admin123":
            print("Update Patient Details")
            print("--------------------------------------------------------------------------------------------------------------------------")
            pname=input("Enter patient's name you want to update details of: ")
            if isPresent(pname):    
                age=int(input("Enter Patient's Age    :"))
                gen=input("Enter Patient's Gender  :")
                cno=input("Enter Contact Number   :")
                add=input("Enter Address          :")
                ill=input("Kindly enter the illness/disease or the reason to see the doctor :")
                q="update Patient set Age=%d,Gender='%s',ContactNo='%s'Address='%s',Illness='%s' where Name='%s' "%(age,gen,cno,add,ill,pname)
                con.execute(q)
                con.commit()
                nc=con.total_changes
                n=nc-tc
                print(n,"Details Updated ")
                print("--------------------------------------------------------------------------------------------------------------------------")
                input("Press ENTER to return to MAIN MENU ")
                nc=tc
            else:
                print("Entered Patient is not present ")
                print("--------------------------------------------------------------------------------------------------------------------------")
            input("Press ENTER to return to MAIN MENU ")
        else:
            print("Incorrect Admin ID/Password ")
            print("----------------------------")
        input("Press ENTER to return to MAIN MENU ")    

    elif ch==6:
        print("HAVE A GREAT DAY :)")
        break
con.close()  
           
         
           

           
        
          
