# using class oop
import os, platform
class Hotel:
    def __init__(self,name,rest_total,laun_total,game_total,rent,address,checkin,checkout,room):
        print('''\n\n**********WELCOME TO HOTEL************ \n\n''')
        self.name=name
        self.rest_total=rest_total
        self.laun_total=laun_total
        self.game_total=game_total
        self.rent=rent
        self.address=address
        self.checkin=checkin
        self.checkout=checkout
        self.room=room
    def intro(self):
        count=1
        self.name=input("Enter Your Name: ")
        self.address=input("Enter Your Address: ")
        self.checkin=input('Enter Your Check In Date: ')
        self.checkout=input('Enter Your Check Out Date: ')
        print(f"\nYour Room Number is: 10{count}\n")
    def rooms(self):
        print('''\nWe Have The Following Rooms For You:-
1.  Type A---->rs 6000 PN\-
2.  Type B---->rs 5000 PN\-
3.  Type C---->rs 4000 PN\-
4.  Type D---->rs 3000 PN\-\n''')
        type_room=input('Enter Your Choice Please: ')
        try:
            day=int(input("For How Many Days Did You Stay: "))
        except:
            print('You Enter a Wrong Input')
        else:
            if type_room=='1':                
                print('You Have Optend Room Type A')
                self.rent=6000*int(day)
            elif type_room=='2':
                self.rent=5000*int(day)
                print('You Have Optend Room Type B')
            elif type_room=='3':
                print('You Have Optend Room Type C')
                self.rent=4000*int(day)
            elif type_room=='4':
                print('You Have Optend Room Type D')
                self.rent=3000*int(day)            
            else:
                print('You Enter a Wrong Input')
            print(f'Your Room Rent is: {self.rent}\n')
    def food(self):
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
                try:
                    quan=int(input("Enter the quantity: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.rest_total=self.rest_total+quan*20
            elif menu=='2':
                try:
                    quan=int(input("Enter the quantity: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.rest_total=self.rest_total+quan*10
            elif menu=='3':
                try:
                    quan=int(input("Enter the quantity: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.rest_total=self.rest_total+quan*110
            elif menu=='4':
                try:
                    quan=int(input("Enter the quantity: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.rest_total=self.rest_total+quan*150
            elif menu=='5':
                try:
                    quan=int(input("Enter the quantity: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.rest_total=self.rest_total+quan*90
            elif menu=='6':
                break
            else:
                print('Wrong Input')
        print(f"Total Food Cost=Rs {self.rest_total} \n")
    def laundry_menu(self):
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
                try:
                    quan=int(input("Enter the quantity: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.laun_total=self.laun_total+quan*3
            elif laundry=='2':
                try:
                    quant=int(input("Enter the quantity: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.laun_total=self.laun_total+quant*4
            elif laundry=='3':
                try:
                    quant=int(input("Enter the quantity: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.laun_total=self.laun_total+quant*5
            elif laundry=='4':
                try:
                    quant=int(input("Enter the quantity: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.laun_total=self.laun_total+quant*6
            elif laundry=='5':
                try:
                    quant=int(input("Enter the quantity: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.laun_total=self.laun_total+quant*8
            elif laundry=='6':
                break
            else:
                print('Wrong Input')
        print(f"Total Food Cost=Rs {self.laun_total} \n")
    def game_menu(self):
        print('''**********GAME MENU***************
1.Table Tennis --->Rs60
2.Bowling      --->Rs80
3.Snooker      --->Rs70
4.Video Games  --->Rs90
5.Pool         --->Rs50
6.Exit
''')
        while True:
            game=input('Enter Your Game Choice: ')
            if game=='1':
                try:
                    quant=int(input("No. of hours: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.game_total=self.game_total+quant*60
            elif game=='2':
                try:
                    quant=int(input("No. of hours: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.game_total=self.game_total+quant*80
            elif game=='3':
                try:
                    quant=int(input("No. of hours: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.game_total=self.game_total+quant*70
            elif game=='4':
                try:
                    quant=int(input("No. of hours: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.game_total=self.game_total+quant*90
            elif game=='5':
                try:
                    quant=int(input("No. of hours: "))
                except:
                    print('Enter Only Quantity')
                else:
                    self.game_total=self.game_total+quant*50
            elif game=='6':
                break
            else:
                print('Wrong Input')
        print(f"Total Food Cost=Rs {self.game_total} \n")
    def show(self):
        print('Customer details:')
        print(f'Customer Name: {self.name}')
        print(f'Customer Address: {self.address}')
        print(f'Check In Date: {self.checkin}')
        print(f'Check Out Date: {self.checkout}')
        print(f'Room Number: {101}')
        print(f'Your Room Rent is: {self.rent}')
        print(f'Your Restaurant Bill is: {self.rest_total}')
        print(f'Your Laundary Bill is: {self.laun_total}')
        print(f'Your Game Bill is: {self.game_total}')
        print(f'Your Sub Total Bill is: {self.rent+self.rest_total+self.laun_total+self.game_total}')
        print(f'Additional Service Charges is: {1200}')
        print(f'Grand Total Cost is: {self.rent+self.rest_total+self.laun_total+self.game_total+1200}\n')
    
def main():
    a=Hotel('',0,0,0,0,'','','','')
    while True:
        print('''\n1.Enter Customer Data
2.Calculate Room Rent
3.Calculate Restaurant Bill
4.Calculate Laundry Bill
5.Calculate Game Bill
6.Show Total Cost
7.EXIT
''')
        choice=input("Enter Your Choice: ")
        if choice=='1':
            a.intro()
        elif choice=='2':
            a.rooms()
        elif choice=='3':
            a.food()
        elif choice=='4':
            a.laundry_menu()
        elif choice=='5':
            a.game_menu()
        elif choice=='6':
            a.show()
        elif choice=='7':
            exit('THANK YOU!')
        else:
            print('Invalid Input')
        input('Enter the key to clear the screen: ')
        if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
            print(os.system('cls'))
        else:
            print(os.system('clear'))
    
main() 
        


        
