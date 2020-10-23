from proyecto_finanzas import ProyectoFinanzas, Ingresos, Egresos

print("Inicio ProyectoFinanzas: \n")

proyectoFinanzasObj = ProyectoFinanzas()


while True:
    print("Menu: \n")
    print("(0) salir")
    print("(1) registrar ingreso")
    print("(2) registrar egreso")
    print("(3) ver reporte de ingresos")
    print("(4) ver reporte de egresos")
    print("(5) ver reporte de todas las transacciones")
    print("(6) ver reporte total de la cuenta \n")
    option = int(input("opcion: "))
    print()

    if option == 0:
        print("Termino ProyectoFinanzas\n")
        break
    elif option == 1:
        NewEntries = float(input("Puede agregar el monto a ingresar: "))
        proyectoFinanzasObj.addEntries(Ingresos(NewEntries))
        print()
    elif option == 2:
        NewExpenses = float(input("Puede registrar su egreso: "))
        proyectoFinanzasObj.addExpenses(Egresos(NewExpenses))
        print()
    elif option == 3:
        print("Su reporte de ingresos es: ")
        proyectoFinanzasObj.getEntries()
        print()
    elif option == 4:
        print("Su reporte de egresos es: ")
        proyectoFinanzasObj.getExpenses()
        print()
    elif option == 5:
        print("Su reporte de todas las transacciones realizadas es: ")
        proyectoFinanzasObj.getAllFinances()
        print()
    elif option == 6:
        proyectoFinanzasObj.totalAccount()
        print()
    elif (
        option != 0
        or option != 1
        or option != 2
        or option != 3
        or option != 4
        or option != 5
        or option != 6
    ):
        print("Error. La opcion que desea ingresar no existe\n")
        break
