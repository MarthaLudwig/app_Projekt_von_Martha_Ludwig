# Imprtiere Funktionen aus den Untermoduln in den Paket-Nsamensrau
from .math2 import*

# Instanzen direkt ins Paket erstellen
math2 = Math2()

ggt = math2.ggt
kgv = math2.kgv

__all__math2_funktionen = ['math2', 'ggt', 'kgv']

__all__funktionen_eins = __all__math2_funktionen

__all_funktionen = __all__funktionen_eins

__all__ = __all_funktionen