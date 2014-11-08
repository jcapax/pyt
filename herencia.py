class Animal(object):
	def __init__(self, nombre):
		self.nombre = nombre

	def printNombre(self):
		print "nombre %s"%self.nombre

class Canino(Animal):
	def __init__(self, nombre):
		super(Canino.self).__init__(nombre)
		self.raza = "pastor aleman"

perrito = Canino("ruffo")
perrito.printNombre()

