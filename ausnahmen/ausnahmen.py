import numpy as np

class Ausnahmen:

    def ausnahme_eins(self, zahl1, zahl2, zahl3, ausnahme_Text):

        if zahl1 == 0 and (zahl2 == 0 or zahl3 == 0):

            return ausnahme_Text

        return 0

    def ausnahme_zwei(self, zahl1, zahl2, ausnahme_Text):

        if zahl1 == 0 or zahl2 == 0:

            return ausnahme_Text

        return 0

    def ausnahme_drei(self, dateinahme):

        if not exit(dateinahme):

            return "Hinweis: Die Datei existiert nicht!"

        with open(dateinahme, 'r', encoding = 'utf-8') as f:

            text = f.read()
            if not text:

                text = "Hinweis: Die Datei ist leer!"

            return text

    def ausnahme_vier(self, zahl1, zahl2, ausnahme_Text):

        if zahl1 == 0 and zahl2 == 0:

            return ausnahme_Text

        return 0

    def ausnahme_fuenf(self, zahl, ausnahme_Text):

        if not isinstance(zahl, (int, float, np.float64)):

            return ausnahme_Text

        return 0

    def ausnahme_sechs(self, zahl, ausnahme_Text):

        if zahl == 0:

            return ausnahme_Text

        return 0