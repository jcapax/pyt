class animal:

	def __init__(self, nombre, edad, tipo):
		self.nombre = nombre
		self.edad = edad
		self.tipo = tipo

x = animal("ruffo",5,"canino")
y = animal("cleo",7,"felino")

print x.nombre, x.edad, x.tipo
print y.nombre, y.edad, y.tipo