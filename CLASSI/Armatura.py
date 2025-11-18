from Rarità import Rarita
class Armatura:
    def __init__(self, nome, difesa, rarita, prezzo):
        self.nome = nome
        self.difesa = difesa
        self.rarita = rarita
        self.prezzo = prezzo

    def __str__(self):
        return f"{self.nome} | Difesa: +{self.difesa} HP | Rarità: {self.rarita} | Prezzo: {self.prezzo}g"


lista_armature = [
    Armatura("Maglia di Cuoio", 37, Rarita("Rara"), 74),
    Armatura("Tunica del Cacciatore", 32, Rarita("Comune"), 64),
    Armatura("Scudo Rotto", 34, Rarita("Comune"), 68),
    Armatura("Corazza di Bronzo", 36, Rarita("Comune"), 72),
    Armatura("Armatura del Mercenario", 47, Rarita("Rara"), 94),
    Armatura("Scudo del Drago", 55, Rarita("Leggendaria"), 110),
    Armatura("Corazza d'Acciaio", 42, Rarita("Comune"), 84),
    Armatura("Mantello Incantato", 58, Rarita("Leggendaria"), 116),
    Armatura("Armatura del Cavaliere", 51, Rarita("Rara"), 102),
    Armatura("Scudo della Luce", 64, Rarita("Leggendaria"), 128),
    Armatura("Corazza del Nord", 53, Rarita("Rara"), 106),
    Armatura("Scaglie del Drago Rosso", 55, Rarita("Rara"), 110),
    Armatura("Corazza Reale", 76, Rarita("Leggendaria"), 152),
    Armatura("Armatura del Destino", 61, Rarita("Rara"), 122),
    Armatura("Scudo Eternum", 81, Rarita("Leggendaria"), 162),
    Armatura("Corazza di Mithril", 63, Rarita("Rara"), 126),
    Armatura("Vestigia Divine", 86, Rarita("Leggendaria"), 172),
    Armatura("Corazza dei Guardiani", 65, Rarita("Rara"), 130),
    Armatura("Scudo del Tempo", 88, Rarita("Leggendaria"), 176),
    Armatura("Armatura Suprema", 69, Rarita("Rara"), 138),
]