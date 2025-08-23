class BankATM :

    def __init__(self, InitialAmount, AccName,PinNumber):
        self.pin = PinNumber
        self.balance = InitialAmount
        self.accname = AccName
        self.Transaction_history = []
        print(f"\n ACCOUNT {self.accname} IS CREATED. \n BALANCE = ${self.balance}")
    
    def get_balance(self):
        print(f"ACCOUNT '{self.accname}' BALANCE = ${self.balance}")

    def deposite(self,amount):
        self.balance = self.balance + amount 
        print("DEPOSITE IS COMPLETED")
        check = input('YOU WANT TO SEE THE BALNCE ENTER YOUR RESPONSE(YES/NO) =')
        data = [f"CREADITED AMOUNT : {amount}"]
        self.Transaction_history.append(data)
        if check == 'YES':
            self.get_balance()
    
    def viableTransaction(self,amount):
        if self.balance >= amount :
            return
        else :
            raise ValueError(
                f"\nSORRY, ACCOUNT '{self.accname}' ONLY HAS A BALANCE OF {self.balance}"
            )
    
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("WITHDRAW IS COMPLETE !") 
            data =[ f"DEBITED AMOUNT : {amount}"]
            self.Transaction_history.append(data)
            check = input('YOU WANT TO SEE THE BALNCE ENTER YOUR RESPONSE(YES/NO) =')
            if check == 'YES':
                self.get_balance()
        except Exception as err:
             print(f"\n WITHDRAW INTERRUPTED : {err}")
    
    def transaction(self, amount):
        self.P2_balance = 1000  # Assume receiver starts with 1000
        try:
            self.viableTransaction(amount)
            person2 = input("ENTER THE RECEIVER ACCOUNT NAME = ")

            print("YOUR TRANSACTION IS UNDER PROCESS.......(❁´◡`❁)")

            # Deduct from sender
            self.balance -= amount
            check = input('YOU WANT TO SEE THE BALNCE ENTER YOUR RESPONSE(YES/NO) =')
            if check == 'YES':
                self.get_balance()

            # Credit to receiver (dummy account)
            self.P2_balance += amount
            print(f"RECEIVER ACCOUNT: {person2}, BALANCE: ${self.P2_balance}")
            print(f"${amount} TRANSFERRED TO {person2}")

            # Save in transaction history
            data = [f"TRANSFERRED ${amount} TO {person2}"]
            self.Transaction_history.append(data)

            print("TRANSACTION IS SUCCESSFUL ✅")

        except Exception as err:
            print(f"TRANSACTION FAILED DUE TO: {err}")

        
            

print("WELCOME TO SBI BANK ATM 🏦")
AccName = input("ENTER THE ACCOUNT NAME = ")
InitialAmount = float(input("ENTER THE INITIAL AMOUNT = $"))
PinNumber = int(input("CREATE THE FOUR DIGITFOUR DIGIT  PIN NUMBER = "))
person = BankATM(InitialAmount,AccName,PinNumber)

print("PLEASE INSERT THE ATM CARD ---- 💳")
while True:
    print("WELCOME TO SBI BANK ATM 🏦  SERVICES ")
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
    |     EXIT / CANCLE     |
    -------------------------
        
    """) 
    print("PRESS 1 FOR CHECK BALANCE ")
    print("PRESS 2 FOR DEPOSITE CASH ")
    print("PRESS 3 FOR WHITHDRAW CASH ")
    print("PRESS 4 FOR TRANSFER MONEY")
    print("PRESS 5 FOR CHECK TRANSACTION HISTORY ")
    print("PRESS 6 FOR EXIT OR CANCLE ")
    result = int (input("ENTER YOUR RESPONSE = "))
    if result == 1 :
        pin = int(input("ENTER THE FOUR DIGIT PIN = "))
        if person.pin == pin:
            person.get_balance()
        else :
            print ("PIN NUMBER IS INCORRECT ❌")

    elif result == 2 :
        pin = int(input("ENTER THE FOUR DIGIT PIN = "))
        if person.pin == pin:
            damount = float(input("ENTER THE AMOUNT TO DEPOSITE = $"))
            person.deposite(damount)
        else :
            print ("PIN NUMBER IS INCORRECT ❌")

    elif result == 3 :
        pin = int(input("ENTER THE FOUR DIGIT PIN = "))
        if person.pin == pin:
            wamount = float(input("ENTER THE AMOUNT TO WITHDRAW = $"))
            person.withdraw(wamount)
        else :
            print ("PIN NUMBER IS INCORRECT ❌")
        
    elif result == 4 :
        pin = int(input("ENTER THE FOUR DIGIT PIN = "))
        if person.pin == pin:
            tamount = float(input("ENTER THE AMOUNT TO TANSFER = $"))
            obj = person.transaction(tamount)
        else :
            print ("PIN NUMBER IS INCORRECT ❌")
        
    elif result == 5 :
        pin = int(input("ENTER THE FOUR DIGIT PIN = "))
        if person.pin == pin:
            print( "TRANSACTION HISTORY :- \n")
            for i in person.Transaction_history:
                print(i)
        else :
            print ("PIN NUMBER IS INCORRECT ❌")
        
    
    elif result == 6 :
        print("CANCLE OR EXIT THE PROCESS ......")
        break

        
    else :
        print("PLEASE PRESS VALID NUMBER")

print("PLEASE GET YOUR CARD💳 BACK FROM ATM.. ")
print("\nTHANKYOU FOR USING SBI ATM")
print("(●'◡'●) PLEASE COME AGIAN (●'◡'●)")

    
