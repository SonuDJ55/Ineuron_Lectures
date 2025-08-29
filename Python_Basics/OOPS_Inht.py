#Inheritance in python
'''
class person():
    def __init__(self,name):
        self.name=name
    
    def display_info(self):
        print(f"Name of the Person is: {self.name}" )

class student(person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def display_info(self):
        print(f"Grade of the Student is: {self.grade}")

student1 = student("John", "12th")
student2 = student("Kalem", "10th")

student1.display_info()
student2.display_info()

class teacher(person):
    def __init__ (self,name,subject):
        super().__init__(name)
        self.subject = subject
    
    def display_info(self):
        print(f"Subject of teacher is {self.subject}")
    

teacher1 = teacher("Sharuman","History")
teacher2 = teacher("Saloni","Design of cloths")

teacher1.display_info()
teacher2.display_info()
 

 # Create class vehical and method start than create diff class like car, bicycle, truck class and inherit attribute of vehical in them

class Vehicle():
    def __init__(self,model,brand,price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def start(self,method):
        self.method = method
        print(f"Vehical starts by {self.method}")

    
    def display_info(self):
        print(f""" The brande of vehical is{self.brand}
                   The model of vehical is {self.model}
                   The price of vehical is {self.price}""")
        
        
        
class Vehicle_Type(Vehicle):
    def __init__(self,model,brand,price,car,bicycle,cart):
        self.car = car
        self.cart = cart
        self.bicycel = bicycle
        super().__init__(model,brand,price)
        

    def display_info(self):
           print(f"Car : {self.car}, Bicycle:{self.bicycel}, Cart: {self.cart}")

    Vehicle1 = Vehicle("BMW","X5","1 Cr")
    Vehicle1.start("Electric")
    Vehicle1.display_info()
    
# Animal class and method eat than create diff class like cat, dog, bird class and inherit attribute of animal in them

class Animal():
    def __init__(self,name,food):
        self.name = name
        self.food= food

    def eat(self):
        
        print(f"{self.name} eats {self.food}")

class cat(Animal):
    def __init__(self,name,food):
        super().__init__(name,food)

class dog (Animal):
    def __init__(self, name, food):
        super().__init__(name, food)
        
   

cat1 = cat("TOM","Jerry")
cat1.eat()
    
dog1 = dog("Bruno","Tom")
dog1.eat()

#Public variable are accessible by all the class and method in them
#Protected variable are accessible by all the child class of parent class but not accessible by any other classes or methods in them.
#For protected "__" is used to make it protected attributes in a class."
#Private variable are accessible only by that particular class and method in which they are declared.
#For private "___" is used to make it private attribute in a class.

class Student():
    def __init__(self,name,roll_no):  #Public Variable of Class "Person" is Declared Here.
        self.__name  = name                #Privae Variable of Class "Person" is Declared Here.
        self.__roll_no = roll_no           #Private Variable of Class "Person" is Declared Here.  
     
    def _details(self):                     #Protected method of Class "Student" for details of student. 
        print(f"Name of Student is {self.__name} and Roll No of Student is {self.__roll_no}")
    
one = Student("John",1)  
one._details()
'''
#Polymorphism in python: One method different functioms for diff classes.

class Animal():
    def __init__( self,name):
        self.name = name  

    def  sound(self):
        pass

class dog(Animal):
    def sound(self):
        return "Woof Woof"

class cat (Animal):
    def  sound(self):
        return "Meow Meow"

cat1 = cat("Kite")
print(cat1.sound())
