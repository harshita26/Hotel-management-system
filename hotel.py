def intro(name,rest_total,laun_total,game_total,rent,address,checkin,checkout,room):
    print('''\n\n**********WELCOME TO HOTEL************ \n\n
1.Enter Customer Data
2.Calculate Room Rent
3.Calculate Restaurant Bill
4.Calculate Laundry Bill
5.Calculate Game Bill
6.Show Total Cost
7.EXIT
''')
    choice=input("Enter Your Choice: ")
    if choice=='1':
        count=1
        name=input("Enter Your Name: ")
        address=input("Enter Your Address: ")
        checkin=input('Enter Your Check In Date: ')
        checkout=input('Enter Your Check Out Date: ')
        print(f"\nYour Room Number is: 10{count}\n")
    elif choice=='2':
        print('''\nWe Have The Following Rooms For You:-
1.  Type A---->rs 6000 PN\-
2.  Type B---->rs 5000 PN\-
3.  Type C---->rs 4000 PN\-
4.  Type D---->rs 3000 PN\-\n''')
        type_room=input('Enter Your Choice Please: ')
        day=input("For How Many Days Did You Stay: ")
        if type_room=='1':            
            print('You Have Optend Room Type A')
            rent=6000*int(day)
        elif type_room=='2':
            rent=5000*int(day)
            print('You Have Optend Room Type B')
        elif type_room=='3':
            print('You Have Optend Room Type C')
            rent=4000*int(day)
        elif type_room=='4':
            print('You Have Optend Room Type D')
            rent=3000*int(day)            
        else:
            print('You Enter a Wrong Input')
        print(f'Your Room Rent is: {rent}')
    elif choice=='3':
        print('''*********RESTAURANT MENU************
1. Water           ---> Rs. 20
2. Tea             ---> Rs. 10
3. Lunch           ---> Rs. 110
4. Dinner          ---> Rs. 150
5. Breakfast Combo ---> Rs. 90
6. Exit
''')
        while True:
            menu=input('Enter Your Menu Choice: ')
            if menu=='1':
                quan=int(input("Enter the quantity:"))
                rest_total=rest_total+quan*20
            elif menu=='2':
                quan=int(input("Enter the quantity:"))
                rest_total=rest_total+quan*10
            elif menu=='3':
                quan=int(input("Enter the quantity:"))
                rest_total=rest_total+quan*110
            elif menu=='4':
                quan=int(input("Enter the quantity:"))
                rest_total=rest_total+quan*150
            elif menu=='5':
                quan=int(input("Enter the quantity:"))
                rest_total=rest_total+quan*90
            elif menu=='6':
                break
            else:
                print('Wrong Input')
        print(f"Total Food Cost=Rs {rest_total} \n")
        
    elif choice=='4':
        print('''*********LAUNDRY MENU***********
1.Shorts   --->Rs3
2.Trousers --->Rs4
3.Shirt    --->Rs5
4.Jeans    --->Rs6
5.Girlsuit --->Rs8
6.Exit
''')
        while True:
            laundry=input('Enter your choice: ')
            if laundry=='1':
                quant=int(input("Enter the quantity:"))
                laun_total=laun_total+quant*3
            elif laundry=='2':
                quant=int(input("Enter the quantity:"))
                laun_total=laun_total+quant*4
            elif laundry=='3':
                quant=int(input("Enter the quantity:"))
                laun_total=laun_total+quant*5
            elif laundry=='4':
                quant=int(input("Enter the quantity:"))
                laun_total=laun_total+quant*6
            elif laundry=='5':
                quant=int(input("Enter the quantity:"))
                laun_total=laun_total+quant*8
            elif laundry=='6':
                break
            else:
                print('Wrong Input')
        print(f"Total Food Cost=Rs {laun_total} \n")
        
    elif choice=='5':
        print('''**********GAME MENU***************
1.Table Tennis --->Rs60
2.Bowling      --->Rs80
3.Snooker      --->Rs70
4.Video Games  --->Rs90
5.Pool         --->Rs50
6.Exit
''')
        while True:
            game=input('Enter Your Game Choice:')
            if game=='1':
                quant=int(input("No. of hours: "))
                game_total=game_total+quant*60
            elif game=='2':
                quant=int(input("No. of hours: "))
                game_total=game_total+quant*80
            elif game=='3':
                quant=int(input("No. of hours: "))
                game_total=game_total+quant*70
            elif game=='4':
                quant=int(input("No. of hours: "))
                game_total=game_total+quant*90
            elif game=='5':
                quant=int(input("No. of hours: "))
                game_total=game_total+quant*50
            elif game=='6':
                break
            else:
                print('Wrong Input')
        print(f"Total Food Cost=Rs {game_total} \n")
        
        
    elif choice=='6':
        print('Customer details:')
        print(f'Customer Name: {name}')
        print(f'Customer Address: {address}')
        print(f'Check In Date: {checkin}')
        print(f'Check Out Date: {checkout}')
        print(f'Room Number: 101')
        print(f'Your Room Rent is: {rent}')
        print(f'Your Restaurant Bill is: {rest_total}')
        print(f'Your Laundary Bill is: {laun_total}')
        print(f'Your Game Bill is: {game_total}')
        print(f'Your Sub Total Bill is: {rent+rest_total+laun_total+game_total}')
        print(f'Additional Service Charges is: {1200}')
        print(f'Grand Total Cost is: {rent+rest_total+laun_total+game_total+1200}')
    elif choice=='7':
        exit('Thank You!')
    else:
        print('Invalid Input')
intro('',0,0,0,0,'','','','')
while True:#making a runable program
    yes_no=input("\nWant to you run again yes/ no?: ")
    if yes_no.lower()=='y':
##        if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
##            print(os.system('cls'))
##        else:
##            print(os.system('clear'))
        intro('',0,0,0,0,'','','','')
        
    else:
        exit("\nThank You!")
        
        
        
        
        
            
            















