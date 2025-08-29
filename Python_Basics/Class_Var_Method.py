class car:
    base_price = 10000    #Global Variables can be accessed anywhere in the program
 
 # This is a class variable
    def __init__(self,model,brand):
        self.model = model #Instance Variable of Class car
        self.brand = brand
    def display ( self ):
        print(f"The Model of the car is {self.model} and the brand of the car is {self.brand} and the base price of the car is {self.base_price}")
    @classmethod
    def updated_base_price(cls,inflation):
        cls.base_price = cls.base_price + (cls.base_price *( inflation%100))
car1 =  car ( 'Ferrari', 'Fiat' )
car1.display()
car1.updated_base_price(10)
car1.display()



