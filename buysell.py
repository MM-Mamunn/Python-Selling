import os
os.system('cls')
class wallet: 
    
    def __init__(self,amount,name): 
        self.amount = amount 
        self.name = name 
        self.cart= [] 
    
    def add(self,item,price,quantity): 
        self.cart.append({'item' : item,'price' : price ,'quantity' : quantity}) 
        print(f'\n\t\tâ¬   Added   â¬') 
        print("\nð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹")
        print(f'\n\t\tð Enter any kew for exit:',end="")
        k = input()
    
    
    def show(self):
        print(f'\t  ð¹ Name : {self.name}\n\t  ð¹ Current amount : {self.amount}\n ====================================================================')
        
        for i in range (0,len(self.cart)):
            #print(f'\tâ¡ï¸Item name : {self.cart[i]['item']}\n\tâ¡ï¸Price(per pcs) : {self.cart[i]['price']}\n\tâ¡ï¸Quantity : {self.cart[i]['quantity']}\n')
            #print("hi")
            print("\n\tð¸ Item name : ",end="")
            print(self.cart[i]['item'])
            print("\tð¸ Price(per pcs) : ",end="")
            print(self.cart[i]['price'])
            print("\tð¸ Quantity : ",end="")
            print(self.cart[i]['quantity'])
            #print("\t.......................")
            print("\tð¸ Totall : ",end="")
            print(self.cart[i]['quantity'] * self.cart[i]['price']  )
            print("\n\tð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹")
        
        if(len(self.cart) == 0):
            print("\n\t\t\tâ ï¸â ï¸ Nothing in Cart\n")
        
     
    def checkout(self): 
        price = 0; 
        
        for i in range(0,len(self.cart)): 
            #print(self.cart[i]['item']) 
            price = price +( self.cart[i]['quantity'] *  self.cart[i]['price'] )
        
        if(price > self.amount ):
            print(f'\n\n\t\tâ ï¸ Not enough credit')
        elif(self.amount == 0):
            print("\n\t\tâ ï¸  You don't have enough amount\n")
        else:
            self.show()
            print(f'\n\t|â¡ï¸ Current Balance: {self.amount}\n\t|â¡ï¸ Payed: {price}\n\t|------------------------------------------------\n\t|â¡ï¸ New balance: {self.amount - price}\n\n')
            self.amount-=price
            self.cart.clear()
        print(f'\tð Enter any kew for exit:',end="")
        k = input()
     
    def clear_cart(self):
        os.system('cls')
        self.cart.clear()
        print(f'\n\n\t\tâ ï¸â ï¸ Clear cart\n\n\t\tð Enter any kew for exit:',end="")
        k = input()

print("\n\t\tð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹ ð¹")
print(f'\n\t\t\tâ¡ï¸ Enter Your name : ',end = "") 
na= input() 
print(f'\t\t\tâ¡ï¸ Enter the amount of wallet : ',end = "") 
am = int(input()) 
object = wallet(am,na) 
os.system('cls')
L = 1 
while 0<L: 
    #print("dd") 
    os.system('cls')
    print("\n\t\t1ï¸â£ â»ï¸  Enter  1  for add item\n\t\t2ï¸â£ â»ï¸  Enter  2  for checkout\n\t\t3ï¸â£ â»ï¸  Enter  3  to view cart\n\n\t\tð ",end="") 
    choice = input()
    os.system('cls')
 
    if(choice == "1"): 
        
        print(f'\n\t\tâ»ï¸ Enter Item name : ',end="") 
        item = input() 
        print(f'\t\tâ»ï¸ Enter price : ',end="") 
        price = int(input()) 
        print(f'\t\tâ»ï¸ Enter Quantity : ',end="") 
        quantity = int(input()) 
        os.system('cls')
        object.add(item,price,quantity)
    elif(choice == "2"):
        os.system('cls')
        object.checkout()
    
    elif(choice == "3"):
        os.system('cls')
        object.show()
        print(f'\n\n\tâ»ï¸ Enter 1 for clear cart\n\tâ¡ï¸ Enter any other kew for exit\n\n\tð ',end="")
        k = input()
        if(k == "1"):
            object.clear_cart();

