from ausnahmen import*

class Math2:

    def ggt(self, zahl1, zahl2, zaehler = 0):

        aus = ausnahme_eins(zaehler, zahl1, zahl2, "ggT ist nicht berechenbar!")
        if aus != 0:

            return aus

        zahl1 = abs(zahl1)
        zahl2 = abs(zahl2)

        if zahl2 == 0:

            return zahl1

        return Math2.ggt(self, zahl2, zahl1 % zahl2, zaehler + 1)

    def kgv(self, zahl1, zahl2):

        aus = ausnahme_zwei(zahl1, zahl2, "kgV ist nicht berechenbar!")
        if aus != 0:

            return aus

        ggT = Math2.ggt(self, zahl1, zahl2)

        if ggT == "ggT ist nicht berechenbar!":

            return "kgV ist nicht berechenbar!"

        return int(abs(zahl1) / ggT * abs(zahl2))