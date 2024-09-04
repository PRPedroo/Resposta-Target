def fibonacci(valor):
	if valor == 0 or valor == 1:
		return True
	else:
		antecessor_do_antecessor = 0
		print(antecessor_do_antecessor)
		antecessor = 1
		print(antecessor)
		numero = 1

		while numero < valor:
			numero = antecessor + antecessor_do_antecessor
			antecessor_do_antecessor = antecessor
			antecessor = numero
			print(numero)

		if valor == numero:
			return True
		else:
			return False

#testes verdadeiros

print("\n", fibonacci(21))
#print("\n", fibonacci(34))

#testes falsos

#print("\n", fibonacci(20))
#print("\n", fibonacci(31))
		