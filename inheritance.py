"""
Introduce inheritance in Python
- How the inheritance work?
- What is overloading and overriding
"""

# Python support multiple inheritance
# A class can inherit attributes and methods from another class
# A class which inherits from a superclass is called subclass/ child class
class Person:
	def __init__(self, first, last):
		self.firstname = first
		self.lastname = last
	# print() method
	def __str__(self):
		return self.firstname + ' ' + self.lastname

class Employee(Person):
	def __init__(self, first, last, id):
		# Person instance is invoked when employee instance is initiated
		# equivalent to super().__init__(first, last)
		# super() refers to superclass
		Person.__init__(self, first, last)
		self.staffid = id
	def __str__(self):
		# override the print() method from superclass
		# rmb to add __str__()
		return super().__str__() + ', ' + str(self.staffid) 
