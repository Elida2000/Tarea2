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
        print(self.ingresodb)

    def getExpenses(self):
        print(self.egresodb)

    def getAllFinances(self):
        print(self.proyectoFinanzasdb)

    def totalAccount(self):
        print("Las finanzas de su cuenta son: " + str(self.cuenta))
