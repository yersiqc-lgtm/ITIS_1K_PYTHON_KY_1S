def add_item(cart: list[dict], name: str, price: float, * , qty: int = 1) -> None:
    cart.append({name:[price,qty]})

def cart_total(cart: list[dict]) -> float:
    sum = 0
    for i in cart:
        for clave, valor in i.items():
            sum += valor[0]
    return sum
def apply_discount(total: float, * , percent: float = 0) -> float:
    return total - (total * (percent/100))

def make_receipt(cart: list[dict], * , discount: float = 0, title: str = "ЧЕК") -> str:
    text = F'''{'='*5}{title:^10}{'='*5}\n'''
    for i in cart:
        for clave, valor in i.items():
            text += F"{clave:<30}{valor[1]}  X  {valor[0]}"
    text += "\n"+"-"*30 + "\n"
    sum = cart_total(cart)
    text += F"{'Сумма :':<30}{sum}"+\
    F"\n{'Скидка '+str(discount)+'% : ':<30}{round(sum * (discount/100),2)}"+\
    F"\n{'Итого: ':<30}{apply_discount(sum,percent = discount)}"+"\n"
    return text

def cheapest(*prices: float) -> float | None:
    pass

def item_card(**fields) -> str:
    pass

def main() -> None:
    # tienda
    cart = []
    while(True):
        print("add item? ")
        repuest = input("(Y/N): ").lower()
        if repuest == 'n':
            break
        product = input("product : ")
        price = float(input("price : "))
        cantidad = (lambda x: 1 if x < 1 else x)(int(input("qty: ")))
        add_item(cart,product,price,qty = cantidad)
    print(make_receipt(cart,discount = 10,title="CUENTA"))
main()

