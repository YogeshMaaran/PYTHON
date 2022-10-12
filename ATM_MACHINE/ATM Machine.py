
import mysql.connector
import random


print("\n\t\033[1m$-$-$-$-$ WELCOME PEOPLE BANK OF INDIA $-$-$-$-$\033[m")

#---------------------****** DATABASE CONNECTOR ******--------------------------------------------------------------------------------------------------------------------------------------------       

class Machine:
 
    def __init__(self):
 
        self.pyatm=mysql.connector.connect(
            host      =  "localhost",
            user      =  "root",
            password  =  "000000",
            database  =  "pyatm")

        mycursor=self.pyatm.cursor()
        mycursor.execute("create database if not exists pyatm")
        mycursor.execute("create table if not exists atm(ID int primary key auto_increment,CARD_NO int unique,ACCOUNT_NO int unique,MOBILE_NO varchar(10) unique,PIN_NO varchar(4) unique)")
    
    #------------------------------------------------------------------------------------       







#------------------------------****** NEW USER ****** ----------------------------------------------------------------------
    def new(self):
        
        try:
      #------------------------------------------------------------------------------------                   
            print("\n\t\t\t\033[1m NEW USER\033[m\n")        
      #------------------------------------------------------------------------------------                  
            name  = input("Enter Your Name                       : ")
            card  = input("Enter Your Six Digit Card No*         : ") 
            accno = input("Enter Your Six Digit Account Number*  : ")
            mob   = input("Enter Your Ten Digit Mobile Number    : ") 
            pin   = input("Create Your 4 Digit Pin               : ")
            
            udep = int(input("\nEnter Your Deposit Amount             : "))
        #----------------------------------------------------------------------------------
            mycursor=self.pyatm.cursor()
            sql=("insert into atm(CARD_NO,ACCOUNT_NO,MOBILE_NO,PIN_NO,NAME,DEPOSIT,BALANCE) values(%s,%s,%s,%s,%s,%s,%s)")
            val=(card,accno,mob,pin,name,udep,udep)
            if udep >= 2000:
                mycursor.execute(sql,val)
        #----------------------------------------------------------------------------------
                otp=random.randrange(100000,500000)
                print(f"\nYour One Time Password \nis \033[4m{otp}\033[m it will be vaild \nfor 1 time.So Enter Correctly!...\n")
                too=int(input("Enter Your OTP : "))
                if too==otp:        
                    self.pyatm.commit()
                    print("\n\t\tCreated Successfully......\n")
                    print("____________________________________________________")
                    print(f"\n            {name} Welcome To POBI BANK".upper())
                    print("_____________________________________________________\n")
                else:
                    print("\n!OTP NOT Vaild Sorry Try Again...\n")
                    mne.new()
            else:
                print("You Must Intial Deposit Rs: 2000.00")
        #--------------------------------------------------------------------      
        except ValueError:
            print("\n!Alphebatic Not Supported Enter Numberrs Only\n")
        except mysql.connector.errors.DataError:
            print("\n!Your OTP or Mobile Number Tooo Long...\n")
            mne.new()
        except mysql.connector.errors.IntegrityError:
            print("\n!User ACC-NO,CARD-NO or PIN Number Alredy Exists...\n")
        #--------------------------------------------------------------------


  





#---------------------------****** DEPOSIT ****** ----------------------------------------------------------------------------  
  
    def deposit(self):
        
        try:
    #------------------------------------------------------------------------
            print("\n\t\t\t\033[1mDEPOSIT\033[m\n")
    #------------------------------------------------------------------------
            mycursor=self.pyatm.cursor()
            mycursor.execute("select ACCOUNT_NO from atm")
            data=mycursor.fetchall()
    #------------------------------------------------------------------------
            accno=input("\nEnter Account number : ")
            if (accno,) in data:
                userdep=int(input("Enter Amount          : "))
                sql=("update atm set BALANCE = %s + BALANCE,DEPOSIT=%s where ACCOUNT_NO=%s;")
                val=((userdep,userdep,accno))
                mycursor.execute(sql,val)
                self.pyatm.commit()
                print("\n____________________________________________________")
                print("\n\t\t   Please Wait...")
                print("\n\t\tTransaction Successfull")
                print("____________________________________________________\n")
            else:
                print("!Try Again Later...")
        except ValueError:
            print("!Try Again Missing Field...")
        except mysql.connector.errors.DataError:
            print("\n!Your OTP or Mobile Number Tooo Long...\n")
            mne.new()
        except mysql.connector.errors.IntegrityError:
            print("\n!User ACC-NO,CARD-NO or PIN Number Alredy Exists...\n")        
    #-----------------------------------------------------------------------

    def in_deposit(self):

        print("\n\t\t\033[1m0 BALANCE INTIAL DEPOSIT\033[m\n")
     #----------------------------------------------------------------------
        pin = input("\nEnter Your 4 Digit Pin : ")    
        mycursor=self.pyatm.cursor()
        mycursor.execute("select ACCOUNT_NO from atm")
        data=mycursor.fetchall()
    #------------------------------------------------------------------------
        accno=input("Enter Account number : ")
        if (accno,) in data:
            userdep=int(input("\nEnter Amount\t     : "))
            sql=("update atm set  DEPOSIT=%s,BALANCE =%s where ACCOUNT_NO=%s;")
            val=((userdep,userdep,accno))
            mycursor.execute(sql,val)
            self.pyatm.commit()
            print("\nPlease Wait...")
            print("\n\tTransaction Successfull")
            print("\n______________________________________________________________")
            print(f"\n\tYOUR INITIAL AMOUNT DEPOSITED SUCCESSFULLY \n\t\t\tRs:{userdep}.00")
            print("______________________________________________________________\n")

        else:
            print("erorrrrr...")
    #------------------------------------------------------------------------






#-------------------------****** BALANCE ENQUIRY ****** ----------------------------------------------------------------------

    def balance(self):
       
        try:
        #------------------------------------------------------------------------
            print("\n\t\t\t\033[1mBALANCE ENQUIRY\033[m")
        #----------------------------------------------------------------------
            pin = input("\nEnter Your 4 Digit Pin : ")
            mycursor=self.pyatm.cursor()
            mycursor.execute("select PIN_NO from atm")
            pinno=mycursor.fetchall()
        #----------------------------------------------------------------------
            pin = input("\nEnter Your 4 Digit Pin : ")
            if (pin,) in pinno:
                mycursor=self.pyatm.cursor()
                sql=("select BALANCE from atm where PIN_NO=%s")
                val=(pin)
                mycursor.execute(sql,(val,))
                bal=mycursor.fetchone()
              #-------------------------------------------------------------------------------
                for i in bal:
                    print("\n\t    Please Wait....")
                    print("\n\tTransaction Successfull")
                    print("_________________________________________________")
                    print(f"\n\t     Available Main Balance\n\t\t  Rs:{i}.00")
                    print("_________________________________________________\n")
            else:
                print("\n!Invaild Pin.....\nTry Again Later...\n")        
           #------------------------------------------------------------------------------------
        
        except ValueError:
            print("!Try Again Missing Field...")
        except mysql.connector.errors.DataError:
            print("\n!Your OTP or Mobile Number Tooo Long...\n")
            mne.new()
        except mysql.connector.errors.IntegrityError:
            print("\n!User ACC-NO,CARD-NO or PIN Number Alredy Exists...\n")   
        except:
            print("Try Again Correctly...\n")    

        #------------------------------------------------------------------------------------






#-------------------------****** WITHDRAW ****** ----------------------------------------------------------------------
       
    def withdraw(self):
      #------------------------------------------------------------------------
        print("\n\t\t\t\033[1mwithdraw\033[m".upper())
      #-------------------------------------------------------------------------
        try:
            mycursor=self.pyatm.cursor()
            mycursor.execute("select PIN_NO from atm")
            pinno=mycursor.fetchall()
        #-------------------------------------------------------------------------    
            pin =(input("\nEnter Your  Pin : "))
            if (pin,) in pinno:
                draw=int(input("\nEnter Amount    : "))
                if draw > 99:  
                    mycursor=self.pyatm.cursor()
                    sql=("update atm set BALANCE = BALANCE - %s,WITHDRAWW=%s where PIN_NO=%s;\n")
                    val=(draw,draw,pin)
                    mycursor.execute(sql,val)
                    self.pyatm.commit()
                    print("\n____________________________________________________")   
                    print( f"\n\tPlease Wait...\n\n\tPlease Collect Your Cash Rs: {draw}.00")
                    print("____________________________________________________\n")   
                else:
                    print("\nInsufficient Balance...\nYou Will Withdraw Above Rs:100.00\n")
                    exit()
            else:
                print("\nInncorrect Pin Try Again...\n")
                exit()
        #----------------------------------------------------------------------
            print("\n\n\n\033[1mBALANCE\033[m\nDo You See Your Balance - 1\nTo Exit Enter           - 2")
            user=input("\nSEE YOUR BALANCE  : ")
            if user=="1":
                mycursor=self.pyatm.cursor()
                sql=("select BALANCE from atm where PIN_NO=%s")
                val=(pin)
                mycursor.execute(sql,(val,))
                bal=mycursor.fetchone()
                for i in bal:
                    print("\n_________________________________________________")
                    print(f"\n     Current Balance Rs: {i}.00               ")
                    print("_________________________________________________\n")    
            elif user=="2":
                print("\n\tThanking You.....\n")
            else:
                print("!Invaild Option Try Again Later...")
        #----------------------------------------------------------------------
        except ValueError:
            print("!Try Again Missing Field...")
        except mysql.connector.errors.DataError:
            print("\n!Your OTP or Mobile Number Tooo Long...\n")
            mne.new()
        except mysql.connector.errors.IntegrityError:
            print("\n!User ACC-NO,CARD-NO or PIN Number Alredy Exists...\n")   
        except:
            print("Try Again Correctly...\n")            
       #----------------------------------------------------------------------






#------------------------****** PIN GENERATION ****** ----------------------------------------------------------------------


    def generate(self):
       #------------------------------------------------------------------------- 
        print("\n\t\t\t\033[1mPIN GENERATION\033[m\n")
       #------------------------------------------------------------------------- 
        try:
            mycursor=self.pyatm.cursor()
            mycursor.execute("select CARD_NO from atm")
            cardno=mycursor.fetchall()
            print(cardno)
        #----------------------------------------------------------------------
            user=input("(Insert)Enter Card Number : ")
            if (user,) in cardno:
                pin = input("CREATE YOUR NEW PIN : ")
                pin2= input("RE-ENTER PIN        : ")
                if pin in pin2:
                    mycursor=self.pyatm.cursor()
                    sql=("update atm SET PIN_NO=%s where CARD_NO=%s;")
                    val=((pin2,user))
                    mycursor.execute(sql,val)
            #----------------------------------------------------------------------
                    otp=random.randrange(100000,500000)
                    print(f"\nYour One Time Password \nis \033[4m{otp}\033[m it will be vaild \nfor 1 time.So Enter Correctly!...\nDont Share Your OTP\n")
                    too=int(input("Enter Your OTP : "))
                    if too==otp:
                        mycursor.execute(sql,val)        
                        self.pyatm.commit()
                        print("\n____________________________________________________")
                        print("\n\tPIN Number Created Successfully....")
                        print("\n____________________________________________________\n")
                    #----------------------------------------------------------------------
                    else:
                        print("\n!Invaild OTP Try Again...\n")
                else:
                    print("\nDo Not Match Input???\n")
            else:
                print("\n!Invaild Account Number Please Check The NO\n")                      
        #----------------------------------------------------------------------       
        except ValueError:
            print("!Try Again Missing Field...")
        except mysql.connector.errors.DataError:
            print("\n!Your OTP or Mobile Number Tooo Long...\n")
            mne.new()
        except mysql.connector.errors.IntegrityError:
            print("\n!User ACC-NO,CARD-NO or PIN Number Alredy Exists...\n")  
        except:
            print("\n!Try Again...\n")     

        #----------------------------------------------------------------------






#------------------****** MINI STATEMENT ****** ------------------------------------------------------------------------------------------    
    
    def minist(self):
        try:
        #-------------------------------------------------------------------------    
            print("\n\t\t\t\033[1mMINI STATEMENT\033[m\n")
        #------------------------------------------------------------------------- 
            minst=input("\nEnter Your 4 Digit Pin : ")
            mycursor=self.pyatm.cursor()
            sql=("SELECT DEPOSIT,WITHDRAWW,BALANCE FROM ATM WHERE PIN_NO=%s")
            val=(minst)
            mycursor.execute(sql,(val,))
            minist=mycursor.fetchone()
            for i in minist:
                print(i)
                # print(f"\nLast deposit Amount  : ",i)
                # print(f"Last Withdraw Amount : ",i)
                # print("\n______________________________________")        
                # print(f"\n    Main Balance Amount Rs: ",i,i,i)
                # print("\n______________________________________")   
                # print("\n")           
                # break
        #----------------------------------------------------------------------------------------- 
        except ValueError:
            print("!Try Again Missing Field...")
        except mysql.connector.errors.DataError:
            print("\n!Your OTP or Mobile Number Tooo Long...\n")
            mne.new()
        except mysql.connector.errors.IntegrityError:
            print("\n!User ACC-NO,CARD-NO or PIN Number Alredy Exists...\n")  
        except:
            print("\n!Try Again...\n")     

        #----------------------------------------------------------------------------------------- 

    
    
    
    
    
    
    def banking(self):
        try:
        #-------------------------------------------------------------------------     
            print("\n\t\t\t\t\033[1mBANKING\033[m")
        #------------------------------------------------------------------------- 
            user = input ("\n\t\t\tEnter Your Card Number  \n\t\t\t\t")
            pin  = input ("\n\t\t\tEnter Your 4 Digit PIN   \n\t\t\t\t ")
            mycursor=self.pyatm.cursor()
            sql=("select CARD_NO,PIN_NO from atm where CARD_NO=%s")
            val=(user)
            mycursor.execute(sql,(val,))
            data=mycursor.fetchone()
    #---------------------------------------------------------------------------------------     
            if user in data:
                if pin in data:
                    print("\n\t\t\tLogin Successfully.....\n")
                else:
                    print("\nInvaild Pin Please Enter Correctly\nTry Again Later...\n")
                    exit()
            else:
                print("\nInvaild Card Number Please Enter Correctly...\n")
                exit()
    #----------------------------------------------------------------------------------------- 
        except ValueError:
            print("!Try Again Missing Field...")
        except mysql.connector.errors.DataError:
            print("\n!Your OTP or Mobile Number Tooo Long...\n")
            mne.new()
        except mysql.connector.errors.IntegrityError:
            print("\n!User ACC-NO,CARD-NO or PIN Number Alredy Exists...\n")  
        except TypeError:
            print("\n!Try Again Card Number Too Long...\n")
            exit()
    #----------------------------------------------------------------------------------------- 



mne=Machine()






#----------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------****** if __name__=="__main__" ******------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------



if __name__ == "__main__":
     
    
    while True:
        
        def engine():
            
            mne=Machine()
            print("\n\n\n\t\033[1m   1 - NEW USER\t\t   2 - ATM\n\n\t   3 - PIN \t\t   0 - EXIT\033[m\n") 
            user1=input("\nSelect Code : ")
            if user1=="1":
                mne.new()
            elif user1=="2":
                mne.banking()
                print("\n\n\033[1m 1 - WITHDRAW \t\t\t 2 - DEPOSIT \n\n 3 - BALANCE ENQUIRY \t\t 4 - MINI STATEMENT \n\n 0 - EXIT \033[m\n")
                user2=input("\nSelect Banking : ")
                if user2=="1":
                    mne.withdraw()
                elif user2=="2":
                    mne.deposit()
                elif user2=="4":
                    mne.minist() 
                elif user2=="3":
                    mne.balance()
                elif user2=="0":
                    exit() 
                else:
                    print("!Invaild Code Please Select Correctly...")       
            elif user1=="3":
                 mne.generate()                
            elif user1=="0":
                exit()
            else:
                print("!Invaild Code Please Select Correctly...") 

        engine()                                












# mne.new()   
# mne.deposit()
# mne.withdraw()
# mne.balance()
# mne.generate()
# mne.minist()
# mne.banking()
# mne.in_deposit()xxxxx










