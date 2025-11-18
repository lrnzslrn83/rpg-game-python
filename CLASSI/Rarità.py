import random

class Rarita:
    MOLTIPLICATORI = {
        "Comune": 1.0,
        "Rara": 1.25,
        "Leggendaria": 1.5
    }

    def __init__(self, tipo=None):
        if tipo is None:
            tipo = self.random_rarita()
        if tipo not in self.MOLTIPLICATORI:
            raise ValueError(f"Tipo di rarità non valido: {tipo}")
        self.tipo = tipo
        self.moltiplicatore = self.MOLTIPLICATORI[tipo]

    def random_rarita(self):
        return random.choices(
            ["Comune", "Rara", "Leggendaria"],
            weights=[0.5, 0.3, 0.2]
        )[0]

    def __str__(self):
        return self.tipo