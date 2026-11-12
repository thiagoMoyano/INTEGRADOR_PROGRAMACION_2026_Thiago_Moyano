import Menu
import Gestion_stock

def main():
    Gestion_stock.inicializar()
    opcion = 0
    while opcion != 4:
        opcion = Menu.mostrar_menu()
        if opcion == 1:
            Gestion_stock.cargar_stock()
        elif opcion == 2:
            Gestion_stock.mostrar_stock()
        elif opcion == 3:
            categoria = input("Ingrese el tipo de prodcto que desea contar: ")
            Gestion_stock.contar(Gestion_stock.stock_cantidades[categoria])
if __name__ == "__main__":
    main()
