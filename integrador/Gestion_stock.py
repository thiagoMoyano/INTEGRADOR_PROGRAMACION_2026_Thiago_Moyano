stock_productos = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}
stock_cantidades = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}

def inicializar():
    for categoria in stock_productos:
        stock_productos[categoria] = []
    for categoria in stock_cantidades:
        stock_cantidades[categoria] = []

def cargar_stock():
    try :
        categoria = input("Ingrese la categoria enlatados, frutas, congelados, panaderia: ")
    except ValueError:
        print("tipo de variable diferente, ingrese un str o una categoria existente :)")
    producto = input("Ingrese que prodcuto desea agregar: ")
    cantidad = int(input("Ingrese cunato del producto desea agregar: "))

    stock_productos[categoria].append(producto)
    stock_cantidades[categoria].append(cantidad)

def mostrar_stock():
    print("Prodcutos en stock:")
    for categoria in stock_productos:
        print(categoria, ":", stock_productos[categoria])

    print("Cantidades en stock:")
    for categoria in stock_cantidades:
        print(categoria, ":", stock_cantidades[categoria])

def contar(lista_productos):
    cantidad_productos = len(stock_productos)
    cont = 0
    for cantidad in lista_productos:
        cont = cont + cantidad

    print("Cantidad de productos que hay:", cantidad_productos)
    print("Suma de las cantidades de todos los prodcutos:", cont)
#posdata nico no me funciona lo de contar la lista de productos... no c que le pase cambio el len
#stock_productos por stock_cantidades y me sigue dande 4, ingreso un porducto y la lista dice que ingrese 4... no importa si ingreso 1 o ingreso 15
# se que no esta para un 10 pero un 8 / 9 te lo firmo, de ultima un 7 :)
