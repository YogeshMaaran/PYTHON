import mysql.connector as connector
import datetime
import random

#------------------------------------------------------------------------------------------------------
#-------------------------------------Local_Database-----------------------------------------------------------------

States=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
        "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka",
        "Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya",
        "Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim",
        "Tamilnadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]        

Districts=[ "Ariyalur","Chennai","Coimbatore","Cuddalore",
            "Dharmapuri","Dindigul","Erode","Kanchipuram","Kanyakumari","Karur",
            "Krishnagiri","Madurai","Nagapattinam","Namakkal","Nilgiris",
            "Perambalur","Pudukkottai","Ramanathapuram","Salem","Sivaganga",
            "Thanjavur","Theni","Thoothukudi (Tuticorin)","Tiruchirappalli",
            "Tirunelveli","Tiruppur","Tiruvallur","Tiruvannamalai","Tiruvarur",
            "Vellore","Viluppuram","Virudhunagar"]

storage=[]

date_time=datetime.datetime.now().strftime("%d %b %Y |")
date_time_today=datetime.date.today().strftime("| %d %b %Y |")
date_time_tmw=datetime.date.today()+datetime.timedelta(days=1)
tod=datetime.date.today().strftime("%Y")

informate= ("\n! Slots are updated by state vaccination"
         "centers and private hospitals everyday at 8AM, 12PM, 4PM, & 8PM.\n"
         "Walk-in availableat all vaccination centers for age 12 years and above" 
         "\n(For timings for walk-in vaccinations, please contact the vaccine center.")

#----------------------------****** Database_Connection ******------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
print("\n***P*Y*T*H*O*N*V*A*C*C*I*N*E**P*Y*T*H*O*N*V*A*C*C*I*N*E**P*Y*T*H*O*N*V*A*C*C*I*N*E*****")
print("\t\t\t\t\033[1mPYvaccine++\033[m")
print("***P*Y*T*H*O*N*V*A*C*C*I*N*E**P*Y*T*H*O*N*V*A*C*C*I*N*E***P*Y*T*H*O*N*V*A*C*C*I*N*E****")

class Connector():
   
    def __init__ (self):

        self.mydb=connector.connect(
        host="localhost",
        user="root",
        password="000000",
        database="db001")

        mycursor=self.mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS db001")      
        mycursor.execute("CREATE TABLE IF NOT EXISTS COVID_REG(ID INT AUTO_INCREMENT,USER_ID VARCHAR(50) UNIQUE,NAME VARCHAR(100),EMAIL_ID VARCHAR(100),MOBILE_NO VARCHAR(13) UNIQUE,PRIMARY KEY(ID,USER_ID))")
             
db_connection=Connector()

#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------




     
#----------------------------------------------------------------------------------------------------------------------
#-----------------------------***** Searching_Vaccination_Center *****--------------------------------------------------    

class Slots_searching(Connector):
    
     
    try:
        
        def state(self): #-------------------->>>>> State_selection
            self.user=input("\nEnter Code '01' See Your State : ")
            
            if self.user=="01":
                for i in States:
                    print(i)   
            elif self.user=="2":
                exit()
            else:
                print("\nInvaild Code! Please Enter Valid Code...")
                slots.state()          
    
        def state_selection(self):
            print("\n")
            user=input("Enter sel state : ")
            if user in States:
                if user=="Tamilnadu":
                    storage.append(user)
                    print(storage)
                elif user=="2":
                    exit()
                else:
                    print("\n!SORRY Now Temproary Tamilnadu Only Avilable...\n")
                    slots.state_selection()
                 #---------------------------------------------------------------------------        
                    # user=input("Enter To continue : ")          
                    # tryagain=input("Try Again! Enter : ")
                    # if tryagain=="1":
                    #     sel.state_selection()
                    # elif tryagain=="2":
                    #     exit()
                    # else:
                    #     print("Enter Choice Correctly")  
                 #-------------------------------------------------------------------------------
            
            elif user=="2":
                exit()      
           
            else:
                print("Not In Lists!... Please Enter Correctly\n")
                slots.state_selection()
           
            #----------------------------------------------------------------------------------   
                # tryagain=input("To Continue Enter : ")
                # if tryagain=="1":
                #     sel.state_selection()
                # elif tryagain=="2":
                #     exit()
            #--------------------------------------------------------------------------------------    

#-------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------****** District Selection ******--------------------------------------------------------------------------------------------



        def district(self): #----------------------------------->>>>> District_selection
            input("\n|Click Enter|")
            print("\n")
            for i in  Districts:
                
                print(i)
            user=input("Enter Your District : ")    
            if user in Districts: 
                if user=="Chennai":
                    storage.append(user)
                    input("\n|Click Enter|")
                    print(storage)
                    print(informate)
                    print("\t\tAPOLLO CLINIC VALASARAVAKKAM\n"
                          "1 Prakasam Salai Near McDonald Valasaravakkam,Chennai,Tamil Nadu,600087\n"
                          "COVISHIELD: ₹386.25 PAID\n"
                          "Age: 18 & Above Dose: 1 \n"
                          f"{date_time} - 9 Slots\n"
                          f"{date_time_tmw} - 10 Slots\n"
                          "10 Slots\n"
                          "N/A")
                        

                elif user=="Coimbatore":
                    storage.append(user)
                    input("\n|Click Enter|")
                    print(storage)
                    print(informate)
                    print("\t\tALIYAR NAGAR APHC\n"
                          "Vaparai Road Aliyar Nagar,Coimbatore,Tamil Nadu,642114\n"
                          "COVISHIELD: FREE"
                          "Age: 18 & Above Dose: 1\n"
                         f"{date_time} - 1 Slots\n"
                         f"{date_time_tmw} - N/A\n"
                          "N/A\n"
                          "N/A")
                    print("\t\tKMCH MAIN"
                          "99 Avanashi Road Coimbatore, Coimbatore, Tamil Nadu, 641014.\n"
                          "COVISHIELD: ₹386.25PAID\n"
                          "Age: 18 & Above Dose: 1 & 2\n"
                          f"{date_time} - 50 Slots\n"
                          f"{date_time_tmw} - 50 Slots")
                        
                
                elif user=="Madurai":
                    storage.append(user)
                    input("\n|Click Enter|")
                    print(storage)
                    print(informate)
                    print("\t\tAPOLLO SPECIALITY HOSPITAL\n"
                           "Lake View Road K K NagarMadurai, Madurai, Tamil Nadu, 625020\n"
                           "COVAXIN: ₹386.25PAID\n"
                           "Age: 15 & Above Dose: Precaution\n"
                           f"{date_time} - 49 Slots")       
                
                elif user=="Thanjavur":
                    storage.append(user)
                    input("|Click Enter|")
                    print(storage)
                    print(informate)
                    print("\tGovernment Hospitals\n"
                          "COVISHIELD: FREE\n"
                          "Age: 18 & Above Dose: 1\n"
                         f"{date_time} - 1 Slots\n"
                         f"{date_time_tmw} - N/A\n"
                          "N/A\n"
                          "N/A")
                
                elif user=="Theni":
                    storage.append(user)
                    input("\n|Click Enter|")
                    print(storage)
                    print(informate)
                    print("\tGovernment Hospitals\n"
                          "COVISHIELD: FREE\n"
                          "Age: 18 & Above Dose: 1\n"
                         f"{date_time} - 1 Slots\n"
                         f"{date_time_tmw} - N/A\n"
                          "N/A\n"
                          "N/A")
                
                elif user in Districts:
                    storage.append(user)
                    input("\n|Click Enter|")
                    print(storage)
                    print(informate)
                    
                else:
                    print(f"\nInvaild {user} District")

    except:
        print("\nNumbers Not Supported!...")


slots=Slots_searching()

#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------


    

    
#--------------------------------****** Registration ******---------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------



class Register(Slots_searching,Connector): 

    

    def signup(self):
        print("\033[1m\n\n\t\tSIGN UP\033[m\n")
        try:
            name       =   input("Enter Your Name        : ")
            user_id    =   input("Choose Your User Id*   : ")
            email_id   =   input("Enter Your EMail Id    : ")
            mobile_no  =   input("Enter Your Mobile No*  : ")
           
            sql="insert into covid_reg(USER_ID,NAME,EMAIL_ID,MOBILE_NO) values(%s,%s,%s,%s)"
            val=(user_id,name,email_id,mobile_no)
            mycursor=self.mydb.cursor()
            mycursor.execute(sql,val)
            self.mydb.commit()
            print(f"\n'{name}' Submitted Successfully.......\n")
            
              
        except:
            print("\033[1m\n !The User Id Alredy Exists...\n"'\033[m')
            
#----------------------------------------------------------------------------------------------------------------------------------------------            
#-----------------------------------****** Signin ******----------------------------------------------------------------------------------------------------

    def signin(self):
        print("\n\t\tLOGIN\n")
        mycursor=self.mydb.cursor()
        mycursor.execute("select USER_ID from covid_reg")
        dat=mycursor.fetchall()
        
        user=input("Enter Your User Id : ")
        if (user,) in dat:
            print("\n\033[1m Login Successfully....."'\033[m')
                    
        else:
            print("\n\033[1m User Id Wrong!!! Enter User Id Correctly\n"'\033[m')
            print("---------------------------------------")
            print("To Continue Enter  -  1\n"
                "\nTo Exit            -  2")
            print("---------------------------------------")
            while True:
                try0=(input("!Try Again Enter : "))
                if try0=="1":
                    reg.signin()
                    break
                elif try0=="2":
                    break     
                else:
                    print("Enter Key Correctly!.....\n")
                    break
                
                  
#----------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------****** Rename ******----------------------------------------------------------------------------------------------------------------    

    def rename(self):

        mycursor=self.mydb.cursor()
        mycursor.execute("select USER_ID from covid_reg")
        dat=mycursor.fetchall()
        "\n"
        id=input("Enter Your Old User Id : \n")
        if (id,) in dat:
            user_id   = input("Choose Your User Id*  : ")
            name      = input("Enter Your Name       : ") 
            email_id  = input("Enter Your E-mail Id  : ")
            mobile_no = input("Enter Your Mobile No* : ")
            sql2=("update covid_reg set USER_ID=%s,NAME=%s,EMAIL_ID=%s,MOBILE_NO=%s where USER_ID=%s")
            val2=(user_id,name,email_id,mobile_no,id)
            mycursor.execute(sql2,val2)
            self.mydb.commit()
            print(f"\n'{name}' Changed Successfully...... Your User Id is '{user_id}'\n") 
            
        else:
            print("\n\033[1m!INVAILD SELECTION! Please Try Again...\n"'\033[m')
            print("---------------------------------------")
            print("To Continue Enter  -  1\n"
                  "To Exit            -  2")
            print("---------------------------------------")
            while True:
                try0=(input("!Try Again Enter : "))
                if try0=="1":
                    reg.signin()
                    break
                elif try0=="2":
                    break     
                else:
                    print("Enter Key Correctly!.....\n")
                    break
#----------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------****** Forgot Password ******----------------------------------------------------------------------------------------------------------
    
    def forgot(self):
        print("\t\t\t\033[1mForgot Password\033[m\n")
        try:
            mycursor=self.mydb.cursor()
            mycursor.execute("select MOBILE_NO from covid_reg")
            dat=mycursor.fetchall()
            find=input("Enter your Mobile Number : ")  
        
            if (find,) in dat:
                otp=random.randrange(100000,500000)
                print(f"\nYour One Time Password to forgot \nPYvacci+ is \033[4m{otp}\033[m it will be vaild \nfor 1 time\n")
                too=int(input("Enter Your OTP : "))
                if too==otp:
                    mycursor=self.mydb.cursor()
                    mycursor.execute("select USER_ID from covid_reg")
                    dat=mycursor.fetchone()
                    for i in dat:
                        print(f"Your User Id \033[1m{i}\033[m\n")
                        break
                else:
                    print("\n!Invaild Wrong OTP...\n")
                    print("---------------------------------------")
                    print("     To Continue Enter  -  1\n"
                          "     To Exit            -  2")
                    print("---------------------------------------")
                    while True:
                        try0=(input("!Try Again Enter : "))
                        if try0=="1":
                            reg.forgot()
                            break
                        elif try0=="2":
                            break    
                        else:
                            print("Enter Key Correctly!.....\n")
                            break        
            else:
                print("\n!Mobile Number Incorrect Please Check The number\n")
                print("---------------------------------------")
                print("     To Continue Enter  -  1\n"
                      "     To Exit            -  2")
                print("---------------------------------------")
                while True:
                    try0=(input("!Try Again Enter : "))
                    if try0=="1":
                        reg.forgot()
                        break
                    elif try0=="2":
                        break
                        exit()    
                    else:
                        print("Enter Key Correctly!.....\n")
                        break
    
        
        except:
            print("\n!OTP Invaild,Albhebatic NOt Supported,Enter NUmbers Only...\n")
            reg.forgot() 


reg=Register()

#------------------------------------------------------------------------------------------------------------------------------



#-----------------------------****** Vacination *******-------------------------------------------------------------------

class Vaccination(Register,Slots_searching,Connector):
    
    vaccinated=0
    ref_id=10040080
    cer_id=255578880

    def __init__(self):
        
        Vaccination.vaccinated+=1
        Vaccination.ref_id+=1
        Vaccination.cer_id+=1

    def vax_reg(self):
        try:
            
            reg=input("\nEnter Code '1' : ")
            if reg=="1":
                name   =input("\nName                 : ")       
                aadhar = input("Your Aadhar Number    : ")
                sex    = input("Enter Sex             : ")
                age    = int(input("Enter Year Of Birth   : "))
                vaccine= input("Enter Vaccine Name    : ")  
                dose   = input("Enter Dose 1st or 2nd : ")
                vac_by = input("Vacciination By       : ")
                vac_at = input("Vaccination Center    : ")
                print("Thanku You For Vaccinating....\n")
                down=input("Enter Code '001' To Download : ")
                if down=="001":
                    cert=("\t\t\nCertiﬁcate for (COVID-19) Vaccination\n"
                          "\nIssued in India by Ministry of Health & Family Welfare,Govt.of Python\n"
                         f"\t\t\t\nCertiﬁcate ID {Vaccination.cer_id}\n"
                          "\n\t\t____Benificiary Details____"
                         f"\n\t\tName                 {name.capitalize()}"
                         f"\n\t\tAge                  {int(tod)-age}"
                         f"\n\t\tGender               {sex.capitalize()}"
                         f"\n\t\tID Verified          Aadhaar {aadhar.capitalize()}"
                         f"\n\t\tRefrence ID          {Vaccination.ref_id}"
                         f"\n\t\tVaccine Name         {vaccine.upper()}"
                         f"\n\t\tDate of  Dose        {dose + date_time_today}\n"
                          "\n\t\t____Vaccination Details____"
                         f"\n\t\tVccinated by         {vac_by.capitalize()}"                                 
                         f"\n\t\tVaccination at       {vac_at.capitalize()}")
                    print(cert) 
    
                else:
                    print("SORRY! TRY Again Code Invaild..\n")
                    print("---------------------------------------")                   
                    print("     To Continue Enter  -  1\n"
                          "     To Exit            -  2")
                    print("---------------------------------------\n")
                    down=input("Warning! Last Chance Enter Code Correctly : ")
                    if down=="001":
                        cert=("\t\\ntCertiﬁcate for (COVID-19) Vaccination\n"
                          "Issued in India by Ministry of Health & Family Welfare,Govt.of Python\n"
                         f"\t\t\t\nCertiﬁcate ID {Vaccination.cer_id}\n"
                          "\n\t\t____Benificiary Details____"
                         f"\n\t\tName                 {name.capitalize()}"
                         f"\n\t\tAge                  {int(tod)-age}"
                         f"\n\t\tGender               {sex.capitalize()}"
                         f"\n\t\tID Verified          Aadhaar {aadhar.capitalize()}"
                         f"\n\t\tRefrence ID          {Vaccination.ref_id}"
                         f"\n\t\tVaccine Name         {vaccine.upper()}"
                         f"\n\t\tDate of 1st Dose     {dose+date_time_today}"
                         f"\n\t\tDate of 2nd Dose     {dose+date_time_today}\n"
                          "\n\t\t____Vaccination Details____"
                         f"\n\t\tVccinated by         {vac_by.capitalize()}"                                 
                         f"\n\t\tVaccination at       {vac_at.capitalize()}")
                    print(cert) 

            elif reg=="2":
                exit()         
            
            else:
                print("\033[1mInvaild Code! Enter Vaild Code.....\n"'\033[m')
                print("---------------------------------------")                   
                print("     To Continue Enter  -  1\n"
                      "     To Exit            -  2")
                print("---------------------------------------\n")
                vax.vax_reg()

        except ValueError:
            print("\nWarning Missing Field or Unsupporte Format please Enter Numbers Only..\n")
            print("---------------------------------------")                   
            print("     To Continue Enter  -  1\n"
                  "     To Exit            -  2")
            print("---------------------------------------\n")
            vax.vax_reg()


vax=Vaccination()

#-------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------****** if __name__=="__main__" ******----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------


if __name__=="__main__":
    
    
    while True:
        def come():
            print("\n")
            print("To Exit Enter - '02' ")
            enter=input("GO HOME Enter Code '01' : ")
            if enter=="01":
                print("\n\033[1m\t 1 - To Signup\t 2 - To Login\t 3 - Forgot UserId\n")
                user=input("Sign  : ")
                
                if user=="1":
                    reg=Register()
                    reg.signup()
                
                elif user=="3":
                    reg=Register()
                    reg.forgot()
        
                elif user=="2":
                    reg=Register()
                    reg.signin()
                    print("\n\033[1m 1 - Searching Vaccine Center \t 2 - Vaccination" 
                          "\n\n 3 - Changing User Id \t\t 0 - Lagout\n\n 00 - Home\033[m\n")  
                    hom=input("Enter Your Choice : ") 
                    if hom=="1":
                        slots=Slots_searching() 
                        slots.state()
                        slots.state_selection() 
                        slots.district()
                    
                    elif hom=="2":
                        vax=Vaccination()
                        vax.vax_reg()
                    elif hom=="3":
                        reg.rename()
                    elif hom=="0":
                        exit()    
                    elif hom=="00":
                        come()

                    else:
                        print("\nInvaild Code Enter Corect Key")         
                
                else:
                    print("\n! You Must Signup or Login......\n"
                          "--Enter Code Correctly--")
                    come()
            elif enter=="02":
                exit()       
            else:
                print("!Enter Code The Correctly\n")
                come()    


        come()           


#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
































































