import json
import string
import random
from pathlib import Path

class BankATM :
    database = 'data1.json'
    data = []
    Transaction_history = []

    try:
        if Path(database).exists() :
            with open (database) as fs :
                data = json.loads(fs.read())
        else :
            print("NO SUCH FILE EXISTS !")

    except Exception as err :
        print(f"AN ERROR OCCURED AS : {err} ")
    
    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs :
            fs.write(json.dumps(cls.data,indent = 4))


    @classmethod
    def __Account_genration(cls):
        number = random.choices(string.digits, k = 14)
        return ("".join (number))
    

    def Creating_new_acc(self):

        try:
            self.info = {
                "ACCOUNT NAME" : input ("ENTER YOUR NAME :- ").upper(),
                "AGE" : int(input("ENTER YOUR AGE :- ")),
                "EMAIL" : input("ENTER YOUR EMAIL ADDRESS :- "),
                "INITAIL AMOUNT" : float (input ("ENTER THE INITIAL AMOUNT :- ")),
                "BALANCE" : float(0), 
                "ACCOUNT NO." :BankATM.__Account_genration(),
                "PIN NUMBER": int(input("CREATE YOUR FOUR DIGIT ATM PIN NUMBER :-"))
            }
            self.info["BALANCE"] += self.info["INITAIL AMOUNT"]
            
            if len(str(self.info["PIN NUMBER"])) == 4:

                print("YOUR ACCOUNT IS CREATED SUCCESSFULLY !")
                for i in self.info:
                    print(f"{i} : {self.info[i]}")

            BankATM.data.append(self.info)
            BankATM.__update()

        except Exception as err:
            print(f"ACCOUNT CREATION IS INTERRUPTED : {err}")


    @classmethod
    def __Account_verification(cls):

        account_no= (input("ENTER THE ACCOUNT NUMBER :- "))
        pin_no = int (input ("ENTER THE FOUR DIGIT PIN NUMBER :- "))
        cls.user_data = [i for i in BankATM.data if i["ACCOUNT NO."] == account_no and i["PIN NUMBER"] == pin_no ]

        if cls.user_data == False :
            print("SORRY NO DATA FOUND")
        else :
            print("\n\nYOUR REQUEST UNDER PROCESS..... ")
            return


    
    def Get_balance(self):

        BankATM.__Account_verification()
        print(f"ACCOUNT '{BankATM.user_data[0]["ACCOUNT NO."]}' BALANCE = ${BankATM.user_data[0]["BALANCE"]}")
    


    def Deposite(self):

        try :
            BankATM.__Account_verification()
            self.damount = float(input("ENTER THE AMOUNT TO DEPOSITE = $"))
            BankATM.user_data[0]["BALANCE"] += self.damount
            print("DEPOSITE IS COMPLETED ✅")
            check = input('YOU WANT TO SEE THE BALNCE ENTER YOUR RESPONSE(YES/NO) =').strip().upper()

            data = [f"CREADITED AMOUNT : {self.damount}"]
            self.Transaction_history.append(data)

            if check == 'YES':
                print(f"ACCOUNT '{BankATM.user_data[0]["ACCOUNT NO."]}' BALANCE = ${BankATM.user_data[0]["BALANCE"]}")
            BankATM.__update()

        except Exception as err:
            print(f"DEPOSITE INTERRUPTED : {err}")


    
    def viableTransaction(self,amount):

        if BankATM.user_data[0]["BALANCE"] >= amount :
            return
        else :
            raise ValueError(
                f"\nSORRY, ACCOUNT '{BankATM.user_data[0]["ACCOUNT NAME"]}' ONLY HAS A BALANCE OF {BankATM.user_data[0]["BALANCE"]}"
            )
        

    
    def Withdraw(self):

        try:
            BankATM.__Account_verification()
            self.wamount = float(input("ENTER THE AMOUNT TO WITHDRAW = $"))
            self.viableTransaction(self.wamount)
            BankATM.user_data[0]["BALANCE"] -= self.wamount
            print("WITHDRAW IS COMPLETE ✅") 

            data =[ f"DEBITED AMOUNT : {self.wamount}"]
            self.Transaction_history.append(data)

            check = input('YOU WANT TO SEE THE BALNCE ENTER YOUR RESPONSE(YES/NO) =').strip().upper()

            if check == 'YES':
                print(f"ACCOUNT '{BankATM.user_data[0]["ACCOUNT NO."]}' BALANCE = ${BankATM.user_data[0]["BALANCE"]}")
            BankATM.__update()
                
        except Exception as err:
             print(f"\n WITHDRAW INTERRUPTED : {err}")


    
    def Transaction(self):
        
        try:
            self.tamount = float(input("ENTER THE AMOUNT TO TANSFER = $"))
            self.viableTransaction(self.tamount)
            person2 = input("ENTER THE RECEIVER ACCOUNT NUMBER = ")
        
            reciver_data = [i for i in BankATM.data if i["ACCOUNT NO."] == person2]

            print("VERIFY RECIVER ACCOUNT.....")
            if reciver_data == False :
                print("SORRY NO DATA FOUND")
                return
            else:
                print("\nYOUR TRANSACTION IS UNDER PROCESS.......(❁´◡`❁)")

                # Deduct from sender
                BankATM.user_data[0]["BALANCE"] -= self.tamount
                check = input('YOU WANT TO SEE THE BALNCE ENTER YOUR RESPONSE(YES/NO) =').strip().upper()
                if check == 'YES':
                    print(f"ACCOUNT '{BankATM.user_data[0]["ACCOUNT NO."]}' BALANCE = ${BankATM.user_data[0]["BALANCE"]}")

                # send money to another account
                reciver_data[0]["BALANCE"] += self.tamount

                print(f"${self.tamount} TRANSFERRED TO {reciver_data[0]["ACCOUNT NAME"]}")
                # Save in transaction history
                data = [f"TRANSFERRED ${self.tamount} TO {reciver_data[0]["ACCOUNT NAME"]}"]
                self.Transaction_history.append(data)

                print("TRANSACTION IS SUCCESSFUL ✅")
                BankATM.__update()

        except Exception as err:
            print(f"TRANSACTION FAILED DUE TO: {err}")


    def Transaction_hist(self):

        try:
            PIN_NO = int (input("ENTER YOUR FOUR DIGIT PIN NUMBER :-")) 
            if BankATM.user_data[0]["PIN NUMBER"] == PIN_NO:
                print( "TRANSACTION HISTORY :- \n")
                for i in person.Transaction_history:
                    print(i)
            else :
                print("PIN NUMBER IS INCORRECT ❌")
                return
            
        except Exception as err:

            print(f"REQUEST IS FAILED DUE TO: {err}")  
    

    def Account_detail(self):

        try:
            BankATM.__Account_verification()
            print("\n\n")
            for keys ,values in dict(BankATM.user_data[0]).items():
                print(f"{keys} : {values}")

        except Exception as err:
            print(f"REQUEST IS FAILED DUE TO: {err}")  


    def Reset_pin(self):
        try:
            BankATM.__Account_verification()
            current_pin = int(input("ENTER YOUR CURRENT FOUR DIGIT PIN NUMBER = "))
            if BankATM.user_data[0]["PIN NUMBER"] == current_pin :
                new_pin = int (input("ENTER NEW FOUR DIGIT PIN NUMBER :- "))
                BankATM.user_data[0]["PIN NUMBER"] = new_pin
                print('NEW PIN NUMBER IS CREATED SUCCESSFULLY ✅')
                BankATM.__update()
            else: 
                print("PIN NUMBER IS INCORRECT ❌")
                return
            
        except Exception as err:
            print(f"REQUEST IS FAILED DUE TO: {err}") 



    def Deactivate_acc(self):

        try:
            BankATM.__Account_verification()
            pin_no = int(input("ENTER YOUR CURRENT FOUR DIGIT PIN NUMBER = "))

            if BankATM.user_data[0]["PIN NUMBER"] == pin_no :
                index = BankATM.data.index(BankATM.user_data[0])
                BankATM.data.pop(index)
                print("ACCOUNT IS DEACTIVATED SUCCESSFULLY ✅")

                BankATM.__update()

            else:
                print("PIN NUMBER IS INCORRCET ❌")
        except Exception as err:
            print(f"REQUEST IS FAILED DUE TO: {err}") 

               
        


            

print("WELCOME TO SBI BANK ATM 🏦")

person = BankATM()

print("\n\n PLEASE INSERT THE ATM CARD ---- 💳")
while True:
    print("\n\n WELCOME TO SBI BANK ATM 🏦  SERVICES ")
    print("""
    -------------------------
    |        SBI ATM        |
    |                       |
    |     CHECK BALANCE     |
    |                       |
    |      DEPOSIT CASH     |
    |                       |
    |      WITHDRAW CASH    |
    |                       |
    |      TRANSFER MONEY   |
    |                       |
    |   TRANSACTION HISTORY |
    |                       |
    |     ACCOUNT DETAILS   |
    |                       |
    |     CHECK BALANCE     |
    |                       |
    |    RESET PIN NUMBER   |
    |                       |
    |  DEACTIVATING ACCOUNT |
    |                       |
    |     EXIT / CANCLE     |
    -------------------------
        
    """) 
    print("PRESS 1 FOR CREATING A NEW ACCOUNT ")
    print("PRESS 2 FOR DEPOSITE CASH ")
    print("PRESS 3 FOR WHITHDRAW CASH ")
    print("PRESS 4 FOR TRANSFER MONEY")
    print("PRESS 5 FOR CHECK TRANSACTION HISTORY ")
    print("PRESS 6 FOR ACCOUNT DETAILS ")
    print("PRESS 7 FOR CHECK BALANCE ")
    print("PRESS 8 FOR RESET PIN NUMBER ")
    print("PRESS 9 FOR DEACTIVATING ACCOUNT ")
    print("PRESS 10 FOR EXIT OR CANCLE ")

    Menu = {
        1 : person.Creating_new_acc,
        2 : person.Deposite,
        3 : person.Withdraw,
        4 : person.Transaction,
        5 : person.Transaction_hist,
        6 : person.Account_detail,
        7 : person.Get_balance,
        8 : person.Reset_pin,
        9 : person.Deactivate_acc       
    }
    choice = int (input("\nENTER YOUR RESPONSE FROM 1 TO 10 :- "))
    if choice in Menu:
        Menu[choice]()
    
    elif choice == 10:
        print("\n\nCANCLE OR EXIT THE PROCESS ......")
        break
    else :
        print("PLEASE PRESS VALID NUMBER ")
   
print("\nPLEASE GET YOUR CARD💳 BACK FROM ATM.. ")
print("\nTHANKYOU FOR USING SBI ATM")
print("(●'◡'●) PLEASE COME AGIAN (●'◡'●)")

    
