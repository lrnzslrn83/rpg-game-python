import random
from Armatura import lista_armature
from armi import armi_boss, Hero_Arms

class Shop:
    def __init__(self):
        self.items = []
        self.prices = {}

        for _ in range(3):
            scelta = random.random()
            if scelta < 0.3:
                item = random.choice(armi_boss)
                prezzo = random.randint(60, 100)
            elif scelta < 0.6:
                item = random.choice(Hero_Arms)
                prezzo = random.randint(60, 100)
            else:
                item = random.choice(lista_armature)
                prezzo = item.prezzo 

            self.items.append(item)
            self.prices[item] = prezzo

    def show_items(self):
        print("🏪 Bottega del Goblin - Oggetti disponibili:\n")
        for i, item in enumerate(self.items, 1):
            if hasattr(item, 'damage'):
                print(f"{i}. {item.name} ({item.rarita.tipo}) - Danno: {item.damage} - {self.prices[item]} monete")
            elif hasattr(item, 'difesa'):
                print(f"{i}. {item.nome} (+{item.difesa} HP) - {self.prices[item]} monete [{item.rarita}]")
            else:
                print(f"{i}. Oggetto sconosciuto")

    def buy(self, money_obj):
        self.show_items()
        try:
            choice = int(input("Scegli cosa comprare (1-3), oppure 0 per uscire: "))
            if choice == 0:
                print("Hai deciso di non acquistare nulla.")
                return None
            elif 1 <= choice <= 3:
                item = self.items[choice - 1]
                prezzo = self.prices[item]
                nome_item = getattr(item, 'name', getattr(item, 'nome', 'oggetto'))

                if money_obj.spend(prezzo):
                    print(f"✔️ Hai acquistato {nome_item}!")
                    return item
                else:
                    print("❌ Fondi insufficienti.")
                    return None
            else:
                print("❗ Scelta non valida.")
                return None
        except ValueError:
            print("❗ Inserisci un numero valido.")
            return None
