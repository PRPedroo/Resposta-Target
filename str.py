
def verificar_ocorrencia_letra_a(string):
	
	contador_letras = 0

	for c in string:
		if c == 'a' or c == 'A':
			contador_letras += 1

	return contador_letras


print("A palavra \"Pedro\" tem ", verificar_ocorrencia_letra_a("Pedro"), " letras a") # 0 letras a
print("A palavra \"Fabiana\" tem ", verificar_ocorrencia_letra_a("Fabiana"), " letras a") # 3 letras a
print("A palavra \"ISAbela\" tem ", verificar_ocorrencia_letra_a("ISAbela"), " letras a") # 2 letras a (a/A)
