def is_number_integer(value: str) -> bool:
    cantidad = len(value)
    contador = 0
    for i in value:
        if ord(str(i)) in range(48,57+1):
            contador += 1
    return True if cantidad == contador else False
def is_number_float(value: str) -> bool:
    cantidad = len(value)
    contador = 0
    for i in value:
        if is_number_integer(i) or ord(i) == 46:
            contador += 1
    return True if cantidad == contador else False
def is_boolean(value: str) -> bool:
    if value.lower() == "true" or value.lower() == "false":
        return True
    else:
        return False
def detect_type(value: str) -> str:
    valorN = value.strip()
    if is_number_integer(valorN):
        return F"\033[33m{valorN} -> <class 'int'>"
    elif is_number_float(valorN):
        return F"\033[32m{valorN} -> <class 'float'>"
    elif is_boolean(valorN):
        return F"\033[35m{valorN} -> <class 'bool'>"
    else:
        return F"\033[38m{valorN} -> <class 'str'>"

while(True):
    value = input("\033[0mВведите значение: ")
    print(detect_type(value))
    if value == "стоп":
        print("\033[0mПока!")
        break
