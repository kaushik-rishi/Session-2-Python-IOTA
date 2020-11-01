"""
First look the Person class for __init__ method
when it is not able to find the init method then it walks up the chain of inheritance until it finds and __init__ method

help() => method resolution order
- every class in python inherits from the base object class.
- methods inherited from mammal
- data and other attributes inherited from employee


- Instead of repeating the code what we are going to do is let out employee method handle the fistname, lastname and pay

# calling parents init method
super().__init__(first, last, pay)
Employee.__init__(self, first, last, pay) 
"""
 
class Mammal:
	# properties : name
	walking_speed = 30

	def __init__(self, name):
		self.name = name

	def walk(self):
		print(f"Walking at a speed of {self.walking_speed}")

# Dog
class Dog(Mammal):
	walking_speed = 60

	def __init__(self, name, nickname):
		super().__init__(name)
		# Mammal.__init__(self, name)
		self.nickname = nickname

	def run(self):
		print("Running")


d = Dog("Rusty", "Rus")
print(d.name)
print(d.nickname)
d.walk()
print(d) 

# help(d)
print(issubclass(Dog, Mammal))
