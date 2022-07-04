aux = dict()

key = 'Diretório'
for i in range(10):
    if key not in aux:
        aux[key] = str(i)
    else:
        aux[key] = temp, str(i)
    temp = str(i)

print(aux)