#Ragioniamo con OOP
#Vogliamo fare cosa? Creare un personaggio, metterlo avanti a delle scelte (armi o pozioni)
#Cosa deve avere questo personaggio? Un nome (Lo imposterà l' utente), una barra delal vita e un danno
#Questi sono considerati attributi di un oggetto
#Dobbiamo ragionare su cosa può fare questo personaggio
#Curarsi o attaccare, questi sono method
import random
from armi import Hero_Arms, Enemy_Arms, armi_boss
from Money import Money
from healthbar import HealthBar

class Personaggio:
    def __init__(self, name, health, armi=None):
        self.name = name
        self.health = health
        self.health_max = health
        self.money = None  
        self.armi = armi
        self.armatura = None

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        if self.armi:
            danno = self.armi.damage
            target.health -= danno
            print(f"{self.name} attacca {target.name} con {self.armi.name} per {danno} danni!")

    def equip(self):
        print(f"{self.name} è pronto per la battaglia!")

    def equipaggia_armatura(self, nuova_armatura):
        if self.armatura: #quindi se abbiamo già un armatura andiamo a toglierla, di conseguenza togliamo gli hp e inseriamo la nuova
            self.health_max -= self.armatura.difesa
            self.health = min(self.health, self.health_max)
        
        self.armatura = nuova_armatura
        self.health_max += nuova_armatura.difesa #aggiungiamo bonus hp della nuova armatura
        self.health = min(self.health + nuova_armatura.difesa, self.health_max) #aumentiamo anche la health attuale senza modificare la health max

        print(f"🛡️ {self.name} ha equipaggiato: {nuova_armatura.nome} (+{nuova_armatura.difesa} HP)")
    
    def mostra_attrezzatura(self):
        print("\n📦 Attrezzatura attuale:")
        if self.armi:
            print(f"- Arma: {self.armi.name} ({self.armi.rarita.tipo}) - Danno: {self.armi.damage}")
        else:
            print("- Arma: Nessuna")

        if self.armatura:
            print(f"- Armatura: {self.armatura.nome} ({self.armatura.rarita.tipo}) - Difesa: +{self.armatura.difesa} HP")
        else:
            print("- Armatura: Nessuna")


class Hero(Personaggio):
    def __init__(self, name, health):
        super().__init__(name=name, health=health)
        self.money = Money()
        self.health_bar = HealthBar(self, length=20)

    def equip(self):
        print("📦 Hai trovato una cassa iniziale! Scegli la tua arma:")
        chosen_weapons = random.sample(Hero_Arms, 3)
        for i, weapon in enumerate(chosen_weapons, 1):
            print(f"{i}. {weapon.name} ({weapon.rarita.tipo}) - Danno: {weapon.damage}")

        while True:
            try:
                choice = int(input("Scegli la tua arma iniziale (1-3): "))
                if 1 <= choice <= 3:
                    self.armi = chosen_weapons[choice - 1]
                    print(f"Hai scelto: {self.armi.name} ({self.armi.rarita.tipo}) - Danno: {self.armi.damage}")
                    break
                else:
                    print("❗ Scelta non valida.")
            except ValueError:
                print("❗ Inserisci un numero valido.")


class Enemy(Personaggio):
    def __init__(self, name, health, armi=None):
        armi = armi if armi else random.choice(Enemy_Arms) #scriviamo cosi invece di armi = random.choice(enemy_arms) affinche ogni nemico abbia un arma diversa altrimenti tutti avrebbero la stessa
        super().__init__(name=name, health=health, armi=armi)
        self.health_bar = HealthBar(self, length=20)

    def attack(self, target):
        damage = int(self.armi.base_damage * self.armi.rarita.moltiplicatore)
        target.health -= damage
        target.health = max(target.health, 0)
        print(f"{self.name} infligge {damage} danni a {target.name} con {self.armi.name} ({self.armi.rarita.tipo})")


class Boss(Enemy):
    def __init__(self, name, health, armi=None):
        armi = armi or random.choice(armi_boss)
        super().__init__(name=name, health=health, armi=armi)

    def attack(self, target):
        crit = random.random() > 0.8
        multiplier = 2 if crit else 1
        damage = int(self.armi.base_damage * self.armi.rarita.moltiplicatore * multiplier)
        target.health -= damage
        target.health = max(target.health, 0)
        print(f"{self.name} infligge {damage} danni a {target.name} con {self.armi.name} ({self.armi.rarita.tipo})" +
              (" ⚔️ COLPO CRITICO!" if crit else ""))
        return crit
