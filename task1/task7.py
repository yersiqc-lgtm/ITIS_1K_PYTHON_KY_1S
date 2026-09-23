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

def list_from_beast_to_worst(notas: list) -> none:
    notas.reverse()
    for i in range(1,len(notas),2):
        print("\033["+str((i//2)+31)+F"m{1+(i//2)}. {notas[i]} {notas[i-1]}")

def best_student_name_score(value: list) -> str:
    return "\'{}\', {}".format(value[1],value[0])

def scores_best_student(dicc: dict,value: list) -> list:
    return dicc[value[1]]

def unique_scores(value: list) -> set:
    return set(value) 

def last_student(value: list) -> str:
    return value[-1]

journal = {
    "Иванов": [8, 9, 7, 10],
    "Петрова": [10, 10, 9, 10],
    "Сидоров": [5, 6, 4, 7],
    "Козлова": [9, 8, 10, 9],
}
notas_vistas = list()
notas = list(range(len(journal)*2))
i = 0
for clave, valor in journal.items():
    for j in valor:
        notas_vistas.append(j)
    notas[i] = clave
    notas[i+1] = sum(valor)/len(valor)
    i += 2

sort_list(notas)
list_from_beast_to_worst(notas)

print(F'''
Лучший: ('\033[0m{best_student_name_score(notas)})
Все оценки: {unique_scores(notas_vistas)}
В зоне риска: ['{last_student(notas)}']      ''')

