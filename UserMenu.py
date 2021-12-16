from Stock import Stock
import random
from calculator import calc
ans3=True
while ans3:
    login=input('Select [user] for stock system\nSelect [customer] for basket system\n \nChoice: ')
    menu = 0
    if login == 'user':
        menu = 1
    if login == 'customer':
        menu = 2
    if menu == 1:    
        ans=True
        while ans:
            print ("""
            1. Add a product
            2. View all products
            3. Calculate Change
            4. Calculate Packaging
            5. Exit
            """)

            ans = input('What would you like to do?\n \nEnter the number corresponding to your choice: ')

            if ans == '1':
                name = input('Enter product name: ')
                temp = input('Select a product category\n \n1.Luxury\n2.Essential\n3.Gift\n \nEnter the number corresponding to your choice: ')
                if temp == '1':
                    good=('Luxury')
                    price=50
                    vat=price*0.2
                    ans2 = False
                    id = random.randrange(1000000)
                    quantity = input('Enter product quantity: ')
                    expiration_date = input("Enter product expiration date: ")
                    height = input("Enter product height: ")
                    width = input("Enter product width: ")
                    depth = input("Enter product depth: ")
                    weight = input("Enter product weight: ")
                if temp == '2':
                    good=('Essential')
                    price=30
                    vat=price*0.1
                    ans2 = False
                    id = random.randrange(1000000)
                    quantity = input('Enter product quantity: ')
                    expiration_date = input("Enter product expiration date: ")
                    height = input("Enter product height: ")
                    width = input("Enter product width: ")
                    depth = input("Enter product depth: ")
                    weight = input("Enter product weight: ")
                if temp == '3':
                    good=('Gift')
                    price=20
                    vat=price*0.05
                    ans2 = False
                    id = random.randrange(1000000)
                    quantity = input('Enter product quantity: ')
                    expiration_date = input("Enter product expiration date: ")
                    height = input("Enter product height: ")
                    width = input("Enter product width: ")
                    depth = input("Enter product depth: ")
                    weight = input("Enter product weight: ")
                Stock.add_item(name, good, vat, expiration_date, weight, height, width, depth, id, price, quantity)
                Stock.view_all_items() 

            if ans == '2':
                all = Stock.view_all_items()

                print('Do you want to delete an item from the list?: ')
                delete= input('Select 1 or 2\n1. Yes\n2. No which will return you to the home screen: ')
                if delete== '1':
                    deleted= input('enter the name of item you want to be deleted: ')
                    Stock.delete(deleted)

            if ans == '3':
                item_cost = float(input("Enter the total basket cost: € ")) 
                moneygiven = float(input("Enter how much money given: € ")) 
                calc(item_cost, moneygiven)
            
            if ans == '4':
                box_wt= float(input("Enter box weight: "))
                Stock.packaging(box_wt)

            if ans=='5':
                print('exit')
                ans=False
    if menu==2:
        ans=True
        while ans:
            print ("""
            1. View products by type
            2. select item
            3. Exit
            """)
            ans=input('Choose an option: ')
            if ans=='1':
                temp = input('Select [Luxury], [Essential] or [Gift]\nLuxury\nEssential\nGift\nChoice: ')
                if temp == 'Luxury':
                    Stock.viewType('Luxury')
                if temp == 'Essential':
                    Stock.viewType('essential')
                if temp == 'Gift':
                    Stock.viewType('gift')
            if ans=='2':
                selec=input('Enter product name: ')
                quant=int(input('How many would you like?: '))
                Stock.addbasket(selec, quant)
                Stock.adjustquant(selec, quant)
                Stock.getTotal(quant)
                Stock.viewbasket()
            if ans=='3':
                print('exit')
                ans=False