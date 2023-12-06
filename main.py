#Object Oriented Prompt

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"


class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2


class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"


# Example Usage
podracer1 = Podracer(max_speed=500, condition="perfect", price=1000)
print("Podracer 1 Condition:", podracer1.condition)

anakins_pod = AnakinsPod(max_speed=700, condition="perfect", price=1500)
anakins_pod.boost()
print("Anakin's Pod Max Speed:", anakins_pod.max_speed)

sebulbas_pod = SebulbasPod(max_speed=600, condition="perfect", price=1200)
sebulbas_pod.flame_jet(podracer1)
print("Podracer 1 Condition after Sebulba's Flame Jet:", podracer1.condition)



#In thise implementaion of thise code.

#Podracer is the base class with attributes max_speed, condition, and price, along with a repair method.

#AnakinsPod is a subclass of Podracer that inherits its attributes and methods. 

#It also has an additional method boost that multiplies max_speed by 2.

#SebulbasPod is another subclass of Podracer with a method flame_jet that updates the condition of another podracer to "trashed".



#How does this solution demonstrate the four pillars of OOP?

#Encapsulation:

#Encapsulation is demonstrated through the use of classes to encapsulate related attributes and methods.

#Each class (Podracer, AnakinsPod, SebulbasPod) encapsulates its own set of attributes and methods, and their internals are hidden from the outside.

#Abstraction:

#Abstraction is achieved by defining abstract classes (like Podracer) that provide a blueprint for creating objects.
#Users interact with these classes without needing to know the intricate details of their implementation.
#The exact mechanics of repair, boost, and flame_jet are abstracted away, and users only need to know what these methods do conceptually.

#Inheritance:

#Inheritance is demonstrated through the use of subclasses AnakinsPod and SebulbasPod inheriting from the base class Podracer.
#This allows for code reuse and the creation of specialized classes that inherit attributes and behaviors from a more general class.
