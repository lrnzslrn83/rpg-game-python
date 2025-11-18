import random
from Personaggio import Hero, Enemy, Boss
from Shop import Shop
from armi import Hero_Arms, Enemy_Arms, armi_boss
from leaderboard import salva_partita, mostra_leaderboard


class Gamemanager:
    def __init__(self, hero_name):
        self.room_number = 1
        self.Hero = Hero(name=hero_name, health=200)
        self.Hero.money.value = 50
        self.Hero.equip()

        self.boss_names = [
            "Bjorn, il Re delle Tenebre", "Drogor, il Signore della Fiamma", "Astra, la Regina del Gelo",
            "Sargon, il Distruttore", "Vornak, il Dio della Guerra", "Nerath, il Malvagio",
            "Zarath, il Conquistatore dei Mondi", "Thalgar, l'Oscuro Signore", "Aarav, il Padrone delle Ombre",
            "Czarina, la Signora della Morte", "Drakor, il Drago Supremo", "Kvara, la Distruttrice",
            "Vlad, il Vampiro Supremo", "Morgar, l'Invincibile", "Hades, il Re degli Inferi"
        ]

        self.enemy_pool = [
            "Goblin Selvaggio", "Orco Guerriero", "Cecchino della Foresta", "Bandito Spietato",
            "Mago Oscuro", "Stregone dei Boschi", "Sanguinario Troll", "Cavaliere Abissale",
            "Serpente Basilisco", "Vampiro della Notte", "Fenice Infernale", "Strega dei Venti",
            "Assassino Fantasma", "Lupo Mannaro", "Gigante della Montagna", "Demone della Fiamma",
            "Golem di Pietra", "Necromante Sanguinario", "Mutaforma Incantato", "Cavaliere Scheletrico",
            "Harpia dell’Incubo", "Vichingo Maledetto", "Gigante del Gelo", "Guardiano Meccanico",
            "Spettro del Dolore", "Minotauro Feroce", "Cacciatore dell’Oscurità", "Kitsune Demoniaca",
            "Ranger delle Tenebre", "Signore dei Lupi"
        ]

    def boss_spawn_chance(self):
        r = self.room_number
        if r <= 10:
            return 0.1, 0.5
        elif r <= 20:
            return 0.2, 0.75
        elif r <= 30:
            return 0.3, 1
        elif r <= 40:
            return 0.4, 1.25
        elif r <= 50:
            return 0.5, 1.5
        else:
            return 0.6, 2.0

    def next_encounter(self):
        print(f"\n🗺️ Stanza Numero {self.room_number}")
        chance, multiplier = self.boss_spawn_chance()

        if random.random() < chance:
            boss_name = random.choice(self.boss_names)
            boss_weapon = random.choice(armi_boss)
            base_health = random.randint(200, 400)
            health = int(base_health * multiplier)
            boss = Boss(name=boss_name, health=health, armi=boss_weapon)
            print(f"⚠️ È apparso il boss {boss.name} con {boss.health} HP!")
            return boss
        else:
            enemy_name = random.choice(self.enemy_pool)
            base_health = random.randint(60, 150)
            hp_multiplier = 1 + ((self.room_number - 1) // 10) * 0.25
            health = int(base_health * hp_multiplier)
            weapon = random.choice(Enemy_Arms)
            enemy = Enemy(name=enemy_name, health=health, armi=weapon)
            print(f"👾 È apparso {enemy.name} con {enemy.health} HP!")
            return enemy

    def start(self):
        while self.Hero.is_alive():
            print(f"\n🏰 {self.Hero.name} ti trovi nella stanza numero {self.room_number}")
            current_enemy = self.next_encounter()

            while current_enemy.is_alive() and self.Hero.is_alive():
                print(f"❤️ {self.Hero.name}: {self.Hero.health} HP")
                print(f"💀 {current_enemy.name}: {current_enemy.health} HP")
                if hasattr(self.Hero, 'health_bar'):
                    self.Hero.health_bar.draw()
                if hasattr(current_enemy, 'health_bar'):
                    current_enemy.health_bar.draw()

                self.Hero.attack(current_enemy)
                if current_enemy.is_alive():
                    current_enemy.attack(self.Hero)

                input("→ Premi Enter per continuare il combattimento...")

            if not self.Hero.is_alive():
                print(f"\n💀 {self.Hero.name} è morto! Game over.")
                print(f"Sei sopravvissuto fino alla stanza {self.room_number}.")
                salva_partita(self.Hero, self.room_number)
                mostra_leaderboard()
                break

            elif not current_enemy.is_alive():
                print(f"🎉 {current_enemy.name} è stato sconfitto!")
                reward = random.randint(10, 30)
                self.Hero.money.add(reward)
                self.Hero.health += 75
                self.Hero.health = min(self.Hero.health, self.Hero.health_max)
                print(f"🩹 {self.Hero.name} recupera 75 HP e ora ha {self.Hero.health} HP")
                print(f"💰 Guadagni {reward} monete. Totale: {self.Hero.money.get_balance()} monete.")
                
                

                print("\n📦 Trovi una cassa stregata al centro della stanza...")
                print("🪄 Un'incisione brillante recita:")
                print("   'Se lascerai la tua arma attuale, te ne mostrerò tre nuove... potrai sceglierne una sola.'")
                print("❗ Attenzione: se scegli 'si', dovrai per forza cambiare arma con una delle nuove proposte!")
                scelta = input("Vuoi aprire la cassa e cambiare arma? (si/no): ").strip().lower()

                if scelta == "si":
                    self.Hero.mostra_attrezzatura()
                    nuove_armi = random.sample(Hero_Arms, 3)
                    print("\n✨ Armi disponibili nella cassa:")
                    for i, arma in enumerate(nuove_armi, 1):
                        print(f"{i}. {arma.name} ({arma.rarita.tipo}) - Danno: {arma.damage}")
                    while True:
                        try:
                            scelta_index = int(input("Scegli la nuova arma (1-3): "))
                            if 1 <= scelta_index <= 3:
                                nuova = nuove_armi[scelta_index - 1]
                                self.Hero.armi = nuova
                                print(f"✔️ Hai equipaggiato: {nuova.name} ({nuova.rarita.tipo}) - Danno: {nuova.damage}")
                                break
                            else:
                                print("❗ Inserisci un numero tra 1 e 3.")
                        except ValueError:
                            print("❗ Inserisci un numero valido.")
                else:
                    print("Hai deciso di tenere l'arma attuale.")

                # SHOP
                if random.random() < 0.6:
                    print("\n🛒 Hai trovato un negozio misterioso!")
                    print(f"Hai attualmente {self.Hero.money.get_balance()} monete.")
                    decisione = input("Vuoi entrare? (si/no): ").strip().lower()
                    if decisione == "si":
                        self.Hero.mostra_attrezzatura()
                        shop = Shop()
                        nuovo_oggetto = shop.buy(self.Hero.money)
                        if nuovo_oggetto:
                            if hasattr(nuovo_oggetto, "damage"):
                                self.Hero.armi = nuovo_oggetto
                                print(f"✔️ Hai equipaggiato: {nuovo_oggetto.name} ({nuovo_oggetto.rarita.tipo}) - Danno: {nuovo_oggetto.damage}")
                            elif hasattr(nuovo_oggetto, "difesa"):
                                self.Hero.equipaggia_armatura(nuovo_oggetto)
                    else:
                        print("Hai deciso di ignorare il negozio.")

            self.room_number += 1
            input("⏩ Premi Enter per entrare nella stanza successiva...")
