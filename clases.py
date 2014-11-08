class mascota():
	nombre = ""
	edad   = 7

	def setNombre(self, nombre):
		self.nombre = nombre





perrito = mascota()
gatito  = mascota()

perrito.setNombre("ruffo")
gatito.setNombre("ramses")

print "mi perrito se llama %s y tiene %d anos"%(perrito.nombre, perrito.edad)
print "mi gatito se llama %s y tiene %d anos"%(gatito.nombre, gatito.edad)