#criando uma lista com elementos duplicados
lista_com_duplicatas = [1, 2, 3, 1, 4, 2, 5, 6, 3, 7, 8, 5, 9]
 #inicializando uma lista vazia para armazenar os elementos unicos
lista_sem_duplicatas = []
 
 #usando um loop while para percorrer a lista a remove  os elementos duplicatas
while lista_com_duplicatas:
    elemento = lista_com_duplicatas.pop(0) # pop e usada para remover o elemento
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)
        
print('A lista sem duplicatas é: ', lista_sem_duplicatas)