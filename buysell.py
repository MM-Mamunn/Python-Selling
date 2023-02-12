
import os
os.system('cls')


class wallet: 
    
    def __init__(self,amount,name): 
        self.amount = amount 
        self.name = name 
        self.cart= [] 
    
    def add(self,item,price,quantity): 
        self.cart.append({'item' : item,'price' : price ,'quantity' : quantity}) 
        print(f'\t➡️   Added') 
        print(f'\t➡️ Enter any kew for exit:',end="")
        k = input()
        
     
    def checkout(self): 
        price = 0; 
        for i in range(0,len(self.cart)): 
            #print(self.cart['item']) 
            price = price +( self.cart[i]['quantity'] *  self.cart[i]['price'] )
        
        if(price > self.amount ):
            print(f'➡️ Not enough credit')
        else:
            print(f'\n\t➡️ Current Balance: {self.amount}\n\t➡️ Payed: {price}\n\t➡️ New balance: {self.amount - price}\n\n')
            self.amount-=price
            self.cart.clear()
        print(f'\t➡️ Enter any kew for exit:',end="")
        k = input()
print(f'➡️ Enter Your name : ',end = "") 
na= input() 
print(f'➡️ Enter the amount of wallet : ',end = "") 
am = int(input()) 
object = wallet(am,na) 
os.system('cls')
L = 1 
while 0<L: 
    #print("dd") 
    os.system('cls')
    print("\t➡️ Enter 1 for add item\n\t➡️ Enter 2 for checkout") 
    choice = int(input()) 
    os.system('cls')
 
    if(choice == 1): 
        
        print(f'➡️ Enter Item name : ',end="") 
        item = input() 
        print(f'➡️ Enter price : ',end="") 
        price = int(input()) 
        print(f'➡️ Enter Quantity : ',end="") 
        quantity = int(input()) 
        os.system('cls')
        object.add(item,price,quantity)
    else:
        os.system('cls')
        object.checkout()
