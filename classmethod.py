"""
Introduce instance method, class method and static method:
1. What can those method modify?
2. Can those methods be called by class and object?
3. 
"""

class Person:
	def __init__(self, a, h):
		self.age = a
		self.height = h

	# instance method
	# instance can be called by instance and class
	# self points to an instance of the class
	# instance method can freely access attributes and other methods of the same object
	# instance method can also access and modify the class state i.e self.__class__
	def method(self):
		msg1 = 'instance called ' + str(self)
		msg2 = 'class called ' + str(self.__class__)
		return msg1, msg2

	# class method marked with @classmethod decorator
	# class method can be called by instance and class
	# cls points to the class, not the object instance
	# class method  can't modify object instance state (no access to self, only cls)
	# class method can modify class state that applies across all instances of class
	@classmethod
	def classmethod(cls):
		msg = 'class called ' + str(cls)
		return msg

	# static method can neither modify class state or object state because they are not a part of the argument
	# static method can be called by object or class
	@staticmethod
	def staticmethod():
		msg = 'static method called '
		return msg

class Animal:
	# note that class method would apply the class that invoke it as first argument
	# the class invoke the class method may not be the class under the class method
	@classmethod
	def showcls(cls):
		print('The class is {cls!r}'.format(cls = cls))

class Dog(Animal):
	pass
