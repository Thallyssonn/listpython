numeros = [10, 20, 30, 40, 50]

#inicializando a veriavel que ira armazenar o maior numero.
maior_numero = numeros[0]

#usando um loop for para percorrer a lista e encontrar o maior numero.
for numero in numeros: 
    if numero > maior_numero:
        maior_numero = numero
        
print('o maior numero na lista é: ', maior_numero)