#restaurant menu
menu = {
    "Piza" : 80,
    "piza" : 80,
    "Coffee": 30,
    "coffee": 30,
    "Veg Biryani":100,
    "veg Biryani":100,
    "Kabab":80,
    "kabab":80,
    "Shorma":80 ,
    "shorma":80 
}
#Greet  To The Customer And Ask For Order
print("Welcome To Choudhary Restaurant '__'")
print("Menu of Choudhary Restaurant !")
print('''
 --------------------
|     MENU CARD      |
|                    |
|  Piza : 80         |
|  Coffee : 30       |
|  Veg Biryani : 100 |
|  Kabab : 80        |
|  Shorma : 80       |
|                    |
 --------------------''')

Ordered_item = 0

item1 = input("PLEASE ENTER THE NAME OF ITEM = ")
if item1 in menu:
    print(f"YOUR ORDER OF {item1} IS PLACED")
    Ordered_item += menu[item1]
else :
    print(f"{item1} IS NOT AVAILABLE !")

another_order = input("DO YOU WANT TO ADD MORE ITEM? (YES / NO)= ")
if another_order == "YES":
    print('''
 --------------------
|     MENU CARD      |
|                    |
|  Piza : 80         |
|  Coffee : 30       |
|  Veg Biryani : 100 |
|  Kabab : 80        |
|  Shorma : 80       |
|                    |
 --------------------''')
    item2 = input("PLEASE ENTER THE NAME OF ITEM = ")
    if item2 in menu:
        print(f"YOUR ORDER {item1} AND {item2}  IS PLACED")
        Ordered_item += menu[item2]
    else :
        print(f"{item2} IS NOT AVIALABLE !")

another_order = input("DO YOU WANT TO ADD MORE ITEM? (YES / NO)= ")
if another_order == "YES":
    print('''
 --------------------
|     MENU CARD      |
|                    |
|  Piza : 80         |
|  Coffee : 30       |
|  Veg Biryani : 100 |
|  Kabab : 80        |
|  Shorma : 80       |
|                    |
 --------------------''')
    item3 = input("PLEASE ENTER THE NAME OF ITEM = ")
    if item3 in menu:
        print(f"YOUR ORDER {item1} , {item2} AND {item3}  IS PLACED")
        Ordered_item += menu[item3]
    else :
        print(f"{item3} IS NOT AVIALABLE !")

print ("ENJOY YOUR MEAL....")
print(f"\nTOTAL AMOUNT OF ITEMS TO PAY IS {Ordered_item}")
print("\nTHANKS FOR DINING WITH US !\n PLEASE COME AGAIN")









