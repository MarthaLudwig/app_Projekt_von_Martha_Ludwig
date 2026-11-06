# Importiere Funktionen aus den Untermoduln in den Paket-Namensraum
from .script_ggt import*
from .script_kgv import*

# Instanzen direkt ins Paket erstellen
script_ggt = Script_Ggt()
script_kgv = Script_KgV()

scriptggt = script_ggt.scriptggt()
scriptkgv = script_kgv.scriptkgv()

__all__scripte_ggt_funktionen = ["script_ggt", "scriptggt"]
__all__scripte_kgv_funktionen = ["script_kgv", "scriptkgv"]

__all__funktionen_eins = __all__scripte_ggt_funktionen + __all__scripte_kgv_funktionen

__all_scripte_funktionen = __all__funktionen_eins

__all_funktionen = __all_scripte_funktionen

__all__ = __all_funktionen