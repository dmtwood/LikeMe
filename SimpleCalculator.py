class AritmNr:


    def __init__(self, nr1):
        self.nr = nr1

    def add(self, nr1):
         self.nr = self.nr + nr1

    def multiply(self, nr1):
        self.nr = self.nr * nr1

    def toPower(self, nr1):
        self.nr = pow(self.nr, nr1)
        # OR self.nr ** nr1

nr = AritmNr(10)

nr.add(20)
print(nr.nr)

nr.multiply(2)
print(nr.nr)

nr.toPower(2)
print(nr.nr)


