minha_lista = []
trocado = True
num = int(input('quantos elementos deseja ?'))

for i in range(num):
    va1 = float(input('entre com o numero'))
    minha_lista.append(va1)
    
while trocado:
    trocado = False
    for i in range(len(minha_lista) - 1):
        if minha_lista[i] > minha_lista[i + 1]:
            trocado = True
            minha_lista[i], minha_lista[i + 1] = minha_lista[i + 10], minha_lista[i]
            
print('\nOdernado:')
print(minha_lista)