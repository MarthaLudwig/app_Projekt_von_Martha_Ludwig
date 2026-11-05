# Importiere Funktionen aus Untermoduln in den Paket_namensraum
from .ausnahmen import*

# Instasnzen direkt im Paket erstellen
ausnahmen = Ausnahmen()

ausnahme_eins = ausnahmen.ausnahme_eins
ausnahme_zwei = ausnahmen.ausnahme_zwei
ausnahme_drei = ausnahmen.ausnahme_drei
ausnahme_vier = ausnahmen.ausnahme_vier
ausnahme_fuenf = ausnahmen.ausnahme_fuenf
ausnahme_sechs = ausnahmen.ausnahme_sechs

__all__ausnahmen_funktionen = ['ausnahmen', 'ausnahme_eins', 'ausnahme_zwei', 'ausnahme_drei', 'ausnahme_vier', 'ausnahme_fuenf', 'ausnahme_sechs']

__all__funktionen = __all__ausnahmen_funktionen

__all__ = __all__funktionen

