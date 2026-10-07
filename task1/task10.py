def stats(
    *numbers: float
) -> [float, float, float] | None:
    """
    stats(1,2,3,4,....,N) [MIN,MAX,AVERAGE]

    Parameters:
        numbers -> unlimited = n
    
    Return:
        returns a list with 3 elements: min, max, average
    """
    if not numbers:
        return None
    value_min = numbers[0]
    value_max = numbers[0]
    num_values , sum_values = 0 , 0
    for x in numbers:
        if x < value_min:
            value_min = x
        elif x > value_max:
            value_max = x
        num_values += 1
        sum_values += x
    value_average = sum_values / num_values
    return [value_min,value_max,value_average]

def clamp(
    x: float,
    *,
    low: float = 0,
    high: float = 100
) -> float:
    """
        clamp(X,low = VAL_MIN,high = VAL_MAX)

        Parameters:
            x -> value float
            low -> minimal value (Parameter must be specified)
            high -> maximal value (Parameter must be specified)

        Return:
            A value within the range of the minimum and maximum is returned.
    """
    if low+1 < x < 1+high:
        return x
    elif x < low:
        return low
    elif x > high:
        return high

def center_element(
    val: int | str | float = None,
    size_total: int = 0
) -> str | None:
    """
        Parameters:
            val -> element to be centered
            tam_global -> total size to create
        Return:
            None
    """
    if not val:
        return None
    width_total_item = len(str(val)) 
    calcule = size_total-width_total_item
    part1 = calcule//2
    part2 = calcule//2
    if (calcule%2 != 0):
        part1 += 1
    return " "*part1+str(val)+" "*part2

def print_table(
    rows: list[list],
    *,
    sep: str = " | ",
    header: list[str] | None = None
) -> None:
    """
        print_table([[1,2,3...,n],[],[],...,n[]], sep = " | ", header = [id1,id2,id3,...,idN])

        Parameters:
            rows -> matrix with elements to be placed in each row
            sep -> separator for each element in each column (Parameter must be specified)
            header -> Table title (Parameter must be specified)

        Return:
            None
    """
    [print(F"{x:^20}",end='   |') for x in header]
    print("\n","="*(len(rows[0])*len(rows)+20))
    for x in rows:
        for y in x:
            print(center_element(y,30),end="|")
        print()

def add_item(
    cart: list[dict],
    name: str,
    price: float,
    * ,
    qty: int = 1
) -> None:
    """
        Parameters:
            cart -> list of items
            name -> name item to add to inventory
            price -> price item to add to inventory 
            qty -> quantity of said element to be added (Parameter must be specified)

        Return:
            None
    """
    cart.append({name:[price,qty]})

def cart_total(
    cart: list[dict]
) -> float:
    """
        Parameters:
            cart -> general inventory or list

        Return:
            returns the total sum of the products
    """
    sum = 0
    for i in cart:
        for clave, valor in i.items():
            sum += valor[0]
    return sum
def apply_discount(
    total: float,
    * , 
    percent: float = 0
) -> float:
    """
       Parameters:
            total -> amount to which the discount applies
            percent -> percentage to be deducted, between 0 and 100 (Parameter must be specified)

       Return:
            total price minus the discount
    """
    percenta = clamp(percent,low = 0,high = 100)
    return total - (total * (percenta/100))

def make_receipt(
    cart: list[dict],
    * ,
    discount: float = 0,
    title: str = "ЧЕК"
) -> str:
    """
        Parameters:
            cart -> general inventory or list
            discount -> total discount
            title -> Title for the receipt

        Return:
            returns a receipt-style string with all the data ready for printing or display
    """
    text = F'''{'='*5}{title:^10}{'='*5}\n'''
    for i in cart:
        for clave, valor in i.items():
            text += F"{clave:<30}{valor[1]}  X  {valor[0]}\n"
    text += "\n"+"-"*30 + "\n"
    sum = cart_total(cart)
    text += F"{'Сумма :':<30}{sum}"+\
    F"\n{'Скидка '+str(discount)+'% : ':<30}{round(sum * (discount/100),2)}"+\
    F"\n{'Итого: ':<30}{apply_discount(sum,percent = discount)}"+"\n"
    
    return text

def cheapest(*prices: float) -> float | None:
    pass # no implement

def item_card(**fields) -> str:
    pass # no implement

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

if __name__ == "__main__":
    main()
    #print_table([[1,2,3],[4,5,6],[10,20,40],[491,3,67]],header = ["num1","num2","num3"])

