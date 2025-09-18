#Sample Data 
Dict = {
    101 : { "name": "Ahad", "age": 20,"department": "DS", 'salary': 200000 },
    102 : { "name": "Imran", "age": 21,"department": "IT", 'salary': 300000 },
    103 : { "name": "Hannnan", "age": 22,"department": "HR", 'salary': 4000000 },
    104 : { "name": "Abdul", "age": 22,"department": "SALES", 'salary': 20000 },
    105 : { "name": "Juned", "age": 21,"department": "WEB", 'salary': 300000 },
    106 : { "name": "Asad", "age": 19,"department": "CS", 'salary': 90000 }
}

# Main menu

def menu():
    while True :
        print("MAIN MENU OF Employee Management System (EMS) >>>")
        print("""
    -------------------------
    |   ADD NEW ENMPLOYEE   |
    |                       |
    |     VIEW EMPLOYEES    |
    |                       |
    |  SEARCH FOR EMPLOYEE  |
    |                       |
    |         Exit          |
    ------------------------- """)
        
        print("PRESS 1 FOR ADD NEW EMPLOYEE >")
        print("PRESS 2 FOR VIEW EMPLOYEES >")
        print("PRESS 3 FOR SEARCH FOR EMPLOYEE >")
        print("PRESS 4 FOR EXIT >")


        menu = {
            1: add_Emp,
            2: view_Emp,
            3:search_emp
        }
        
        choice = int(input ("\n\nPLEASE ENTER YOUR RESPONSE (1-4) = "))
        if choice in menu :
            menu[choice]()
        elif choice == 4 :
            print("\n\nCANCLE AND EXIT THE PROCESS >>>")
            break
        else :
            print("\n\nPLEASE ENTER VALID RESPONSE (1-4) !")
    print('\n THANK YOU 😊 \n')



# View all Employees Details
def view_Emp():
    try:
        print("VIEW THE EMPLOYEE DETAILS >>>")

        if not Dict :
            print("NO EMPLOYYEES AVAILABLE !")
            return
        
        print("\n-------ALL EMPLOYEE--------\n")
        print("-"*60)

        print("{:<10} {:<15} {:<5} {:<15} {:<10}".format("ID","NAME","AGE","DEPARTMENT","SALARY"))
        print("-" * 60)

        for emp_id ,detail in Dict.items():
            print("{:<10} {:<15} {:<5} {:<15} {:<10}".format(emp_id ,detail['name'],detail["age"],detail['department'],detail["salary"]))
        print('-' * 60)
    except Exception as err:
        print(f"YOU CAN'T VIEW THE EMPLOYEE DETAIL : {err}")



# Search the Employee in Data
def search_emp():
    e_id = int (input("ENTER THE FOUR DIGIT EMP_ID :- "))
    if e_id in Dict :
        print("-"*20)
        print(f"EMP_ID = {e_id}")
        print("NAME = ",Dict[e_id]['name'])
        print("AGE = ",Dict[e_id]['age'])
        print("DEPARTMENT = ",Dict[e_id]['department'])
        print("SALARY = ",Dict[e_id]['salary'])
        print("-"*20)
            
    
    else :
        print("EMPLOYEE ID  IS NOT EXITS !")



# Adding new Employee Data
def add_Emp():
    try:
        attempt= 1
        check = False

        while True:
            id = int (input("CREATE FOUR DIGIT EMP_ID :- "))
            if id in Dict.keys():
                print("\nEMP_ID ALREADY EXITS PLEASE ENTER DIFFRENT ID ")
                attempt+=1
            else :
                check = True
                break
            if attempt == 4:
                return
        if check == True:
            Dict[id]= {
                "name": input("ENTER THE NAME :- "),
                "age": int (input('ENTER THE AGE :- ')),
                "department": input('ENTER THE DEPARTMENT :- '),
                "salary" : float(input("ENTER THE SALARY :- "))
            }
            print("\nEMPLOYEE DATA ADDED SUCCESSFULLY ! \n\n")

    except Exception as err :
        print(f"CAN'T ADD EMPLOYEE DETAIL : {err} ")

        
# to run the main mrnu
menu()






