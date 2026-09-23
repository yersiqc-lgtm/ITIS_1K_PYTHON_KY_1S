def sort_list(value: list):
    for i in range(1,len(value)-1,2):
        for j in range(1,len(value)-i-1,2):
            if value[j] > value[j+2]:
                aux_name = value[j-1]
                value[j-1] = value[j+1]
                value[j+1] = aux_name
                aux = value[j]
                value[j] = value[j+2]
                value[j+2] = aux

journal = {
    "Иванов": [8, 9, 7, 10],
    "Петрова": [10, 10, 9, 10],
    "Сидоров": [5, 6, 4, 7],
    "Козлова": [9, 8, 10, 9],
}
notas = list(range(len(journal)*2))
i = 0
for clave, valor in journal.items():
    notas[i] = clave
    notas[i+1] = sum(valor)/len(valor)
    i += 2
sort_list(notas)
notas.reverse()
for i in range(1,len(notas),2):
    print("\033["+str(i+31)+F"m{i//2}. {notas[i]} {notas[i-1]}")
print(F'''
Лучший: ('{notas[1]}', {notas[0]})
Все оценки: [{journal[notas[1]]}]
В зоне риска: ['{notas[-1]}']      ''')
