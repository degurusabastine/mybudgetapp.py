import os

class Budget:
    
    def __init__(self, name):
        os.system('cls')
        self.name = name
        self.balance = 0
        self.main()
        
        
    def main(self):
         print("*" *50)
         print("HELLO, WELCOME TO MY BUDGET APP!")
         print("*" *50)
         self.budget = int(input("How much is your budget?\n"))
         print(f"Your total budget is ${self.budget}\n\n")
         main_option = int(input("What would you like to do? \n 1. Deposit \n 2. Withdraw \n 3. Check Balance \n 4. Transfer funds \n"))
        
         if main_option == 1:
             self.deposit()
         elif main_option == 2:
             self.withdraw()
         elif main_option == 3:
             self.balance()
         elif main_option == 4:
             self.transfer()
         else:
             print("Invalid Input")
           
    def deposit(self, amount):
         self.balance = amount
         
         return (f"Your new balance is {self.balance} in {self.name} budget")
        #  print("What budget category would you like to deposit into?")
        #  dep_cat_choice = int(input("\n 1. Food \n 2. Clothing \n Entertainment \n"))
        #  dep_amount = int(input("How much would you like to deposit into"))
        #  self.balance = dep_amount
         
         
    def withdraw(self, amount):
        # os.system('cls')
        if self.balance < amount:
            print("********** Transaction Failed **********")
            print("Insufficient funds")          
            
        else:
            self.balance = self.balance - amount
            result = ("********** Successful Transaction **********\n")
            result += (f"Your new balance is {self.balance} in {self.name} budget")
            
            return result
    #     print("What budget category would you like to withdraw from?")
    #     with_cat_choice = int(input("\n 1. Food \n 2. Clothing \n Entertainment \n"))
    #     with_amount = int(input("How much would you like to deposit into"))
    #     print("withdraw")
        
    def get_balance(self):
        balance = (f"The balance for {self.name} is {self.balance}")
        return balance
    #     os.system('cls')
    #     print('balance')
    
    def transfer(self, amount, category):
        if self.name == category.name:
            result = ("ERROR!\n")
            result += ("You cannot transfer funds within the same category\n")
            result += ("You can only transfer funds to another category")
            return result
        
        else:
            if self.balance < amount:
                print("********** Transaction Failed **********")
                print("Insufficient funds")
            else:
                self.balance -= amount
                category.balance += amount
            
                trans_result = ("********** Successful Transaction **********\n")
                trans_result += (f"The balance for the {self.name} budget is {self.balance}\n")
                trans_result += (f"The balance for the {category.name} budget is {category.balance}")
            
                return trans_result
    #     os.system('cls')
    #     print("What budget category would you like to transfer from?")
    #     cat_choice = int(input("\n 1. Food \n 2. Clothing \n Entertainment \n"))
    #     dep_amount = int(input("How much would you like to transfer to"))
    #     print("What budget category would you like to deposit into?")
    #     cat_choice = int(input("\n 1. Food \n 2. Clothing \n Entertainment \n"))
    #     dep_amount = int(input("How much would you like to deposit into"))
    #     print('transfer')
        

food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")

# Budget()
food.deposit (10000)
clothing.deposit(5000)
                 
                 
print(food.transfer(5000, food))
# print(f"{food.name} budget has ${food.balance}")
# print(food.deposit (10000))
# print("---------------------------------")
# print(clothing.deposit(5000))

# print("===================")
# print(food.withdraw (900))
# print("---------------------------------")
# print(clothing.withdraw (500))

# print("===================")
# print(food.get_balance())
# print("---------------------------------")
# print(clothing.get_balance())