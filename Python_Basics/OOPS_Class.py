# Class are blue print of object. If bank is class than its attribues are A/c no, name, IFsc code, Balance
# And deposite, withdraw loan are function
#1st and 2nd July 2024
'''
class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f"Name is {self.name} and Last name is {self.last_name}"

person1 = Person("Dhiraj", "Chaware")
print(person1)

#Write a programe for bank account

class bank_acct:
    def __init__(self,acct_num,acct_name,acct_bala):
        self.acct_num = acct_num
        self.acct_name = acct_name
        self.acct_bala = acct_bala

    def deposit(self,amount):
        self.acct_bala += amount
        print(f"Deposited {amount}. New balance: {self.acct_bala}")


    def withdraw(self,amount):
        if amount > self.acct_bala:
            print("Insufficent balance in account")
        else:
            self.acct_bala -= amount
            print(f"Withdrawn {amount}. Balance after withdrawal: {self.acct_bala}") 
        

    def show_details(self):
        print(f"Account holder name is {self.acct_name}")
        print(f"Account number is {self.acct_num}")
        print(f"Account balance is {self.acct_bala}")
        
        


customer1 = bank_acct(50100236485,"Dhiraj Chaware", 35000)
#customer1.show_details()
customer1.deposit(4000)
customer1.withdraw(5000060)
customer1.show_details()


# TODO task list

class todo():
    #constructor
    def __init__(self,owner):       
        self.owner  =owner
        self.tasks = []            # initilize blank list

    def add_task(self,task):
        self.tasks.append(task)
        print(f"Task {task} added to TODO list ")
    
    def complete_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Tasks {self.task}removed from list")
        else:
            print(f"No such task found {task}")

    def display_task(self):
        print(f"Task in list are {self.tasks}")
         


list1 = todo("Dhiraj Chaware")

list1.add_task("Jumping")
list1.display_task()
list1.complete_task("cycle")



class cars():
    def __init__(self,owner,brand,model,colour,):
        self.owner = owner
        self.brand = brand
        self.model  = model
        self.colour = colour
    
    def display_details(self):
        print(f"Car details are Owner name is {self.owner} Brand name is {self.brand} Model name is {self.model} Colour of car is {self.colour}")

peron1 = cars("Dhiraj Chaware","Toyota","Corolla","White")    #object created by class functions and attributes are called in main function
peron1.display_details()        

class Mobile():
    def __init__(self,owner,brand,model,Processor,price):
        self.owner = owner       #attributes of object created by class functions and attributes are called in main function
        self.brand = brand
        self.model = model
        self.Processor = Processor
        self.price = price

    def display_details(self):
        print(f"""Mobile details  are: 
              Owner name is {self.owner} 
              Brand name is {self.brand} 
              Model name is {self.model} 
              Processor of mobile is {self.Processor} 
              Price of mobile is {self.price}""" )


mobile1 = Mobile("Dhiraj Chaware","Apple","iPhone X","A12 Bionic Chipset", "Rs. 10,000")
mobile1.display_details() 

'''
        
