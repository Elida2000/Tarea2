class Ingresos:
    def __init__(self, ingresoTotal):
        self.ingresoTotal = ingresoTotal


class Egresos:
    def __init__(self, egreso):
        self.egreso = egreso


class ProyectoFinanzas:
    ingresodb = []
    egresodb = []
    proyectoFinanzasdb = []
    cuenta = 0.0

    def addEntries(self, ingreso):
        self.cuenta += ingreso.ingresoTotal
        self.ingresodb.append(ingreso.ingresoTotal)
        self.proyectoFinanzasdb.append(ingreso.ingresoTotal)

    def addExpenses(self, egreso):
        egresoDict = egreso
        self.cuenta -= egresoDict.egreso
        self.egresodb.append(egresoDict.egreso)
        self.proyectoFinanzasdb.append(egresoDict.egreso * -1)

    def getEntries(self):
        ingresos = sum(self.ingresodb)
        print(self.ingresodb)
        print()
        print("La suma de sus ingresos es: " + str(ingresos))

    def getExpenses(self):
        egresos = sum(self.egresodb)
        print(self.egresodb)
        print()
        print("La suma de sus egresos es: " + str(egresos))

    def getAllFinances(self):
        print(self.proyectoFinanzasdb)

    def totalAccount(self):
        print("Las finanzas de su cuenta son: " + str(self.cuenta))
