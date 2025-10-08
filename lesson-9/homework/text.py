#1-task
import math 
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(round(math.pi * self.radius**2))
    def perimetr(self):
        print(round(2 * math.pi * self.radius))
circle1=circle(10)
circle1.area()
circle1.perimetr()
#2task
#  from datetime import datetime
# class person:
#     def __init__(self,name,country,datebirth):
#         self.name=name
#         self.country=country
#         self.datebirth = datetime.strptime(datebirth, "%d-%m-%Y")
#     def age(self):
#         today=datetime.today()
#         years=today.year-self.datebirth.year
#         if (today.month, today.day) < (self.datebirth.month, self.datebirth.day):
#             years -= 1
#         print(f"{self.name} {years} yoshda")
# person1=person('Elshod','Uzbekistan','16-08-2007')
# person1.age()
#3-task
class calculator:
    def __init__(self,ason,bson):
        self.ason=ason
        self.bson=bson
    def addition(self):
        print(self.ason-self.bson)
    def substraction(self):
        print(self.ason-self.bson)
    def division(self):
        print(self.ason/self.bson)
    def power(self):
        print(self.ason*self.bson)
calc=calculator(100,10)
calc.addition()
calc.substraction()
calc.division()
calc.power()

#4-task
class shape():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        print(self.a*self.b)
    def perimetr(self):
        print(2*(self.a+self.b))
square=shape(10,8)
square.area()
square.perimetr()

#6-task
class stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.items:
            return None
        return self.items.pop()
i1=stack(10)
i1=stack(20)
print(i1.pop())
print(i1.pop())

class ShoppingCart:
    def __init__(self):
        # Mahsulotlar nomi, narxi va miqdorini saqlash uchun lug‘at
        self.items = {}

    def add_item(self, item, price):
        """Savatga mahsulot qoshish"""
        if item in self.items:
            self.items[item]['quantity'] += 1
        else:
            self.items[item] = {'price': price, 'quantity': 1}

    def remove_item(self, item):
        """Savatdan mahsulotni ochirish"""
        if item in self.items:
            if self.items[item]['quantity'] > 1:
                self.items[item]['quantity'] -= 1
            else:
                del self.items[item]
        else:
            print(f"{item} savatda yoq.")

    def total_price(self):
        """Jami narxni hisoblash"""
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total

    def display(self):
        """Savatdagi mahsulotlarni korsatish"""
        if not self.items:
            print("Savat bosh.")
        else:
            print(" Savatchadagi mahsulotlar:")
            for name, info in self.items.items():
                print(f"{name} - {info['quantity']} dona, narxi: {info['price']} som")
            print(f"Jami summa: {self.total_price()} so‘m")


# Sinov uchun
cart = ShoppingCart()
cart.add_item("Olma", 5000)
cart.add_item("Banan", 7000)
cart.add_item("Olma", 5000)  # Olma soni 2 bo‘ladi
cart.display()

cart.remove_item("Olma")
cart.display()

cart.remove_item("Banan")
cart.display()


