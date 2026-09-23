import random

def promedio(puntuaciones: list[int]) -> float:
    if not puntuaciones:
        return 0.0
    return round(sum(puntuaciones) / len(puntuaciones), 2)

def clasificacion(diario: dict) -> list[tuple[str, float]]:
    lista_tuplas = []
    for apellido, notas in diario.items():
        lista_tuplas.append((apellido, promedio(notas)))
    return sorted(lista_tuplas, key=lambda x: x[1], reverse=True)

def mejor_estudiante(diario: dict) -> tuple[str, float]:
    lista_ordenada = clasificacion(diario)
    if not lista_ordenada:
        return ("", 0.0)
    return lista_ordenada[0]

def puntuaciones_unicas(diario: dict) -> set[int]:
    conjunto_notas = set()
    for notas in diario.values():
        conjunto_notas.update(notas)
    return conjunto_notas

def agregar_puntuacion(diario: dict, nombre: str, puntuacion: int) -> None:
    if puntuacion < 0 or puntuacion > 10:
        print("Ошибка: оценка должна быть от 0 до 10!")
        return
    if nombre not in diario:
        diario[nombre] = []
    diario[nombre].append(puntuacion)

journal = {
    "Иванов": [8, 9, 7, 10],
    "Петрова": [10, 10, 9, 10],
    "Сидоров": [5, 6, 4, 7],
    "Козлова": [9, 8, 10, 9],
}

print("Рейтинг:")
ranking = clasificacion(journal)
for i, (nombre, nota) in enumerate(ranking, 1):
    print("\t\033["+str(random.randint(31,38))+"m"+f"{i}. {nombre} {nota}")

mejor = mejor_estudiante(journal)
print(f"\033[0mЛучший: {mejor}")

unicas = puntuaciones_unicas(journal)
print(f"Все оценки: {unicas}")

en_riesgo = []
for nombre, notas in journal.items():
    for nota in notas:
        if nota < 5:
            en_riesgo.append(nombre)
            break

# RSIK ZONE
print(f"В зоне риска: {en_riesgo}")

print("\nТипы промежуточных результатов и объяснение выбора коллекций:")
print(f"Тип рейтинга: {type(ranking)}.")
print(f"Тип элемента рейтинга: {type(ranking[0])}.")
print(f"Тип лучшего студента: {type(mejor)}.")
print(f"Тип уникальных оценок: {type(unicas)}.")
print(f"Тип зоны риска: {type(en_riesgo)}.")
