from Rarità import Rarita

class Armi:
    def __init__(self, name, weapon_type, base_damage, value, rarita=None):
        self.name = name
        self.weapon_type = weapon_type
        self.base_damage = base_damage
        self.value = value
        self.rarita = rarita if rarita else Rarita()

    @property
    def damage(self):
        return int(self.base_damage * self.rarita.moltiplicatore)

    def __str__(self):
        return f"{self.name} ({self.rarita.tipo}) - Danno: {self.damage}"

Rusty_Sword = Armi(name="Rusty Sword", weapon_type="Spada", base_damage=5, value=10)
Silver_Sword = Armi(name="Silver Sword", weapon_type="Spada", base_damage=15, value=70)
Diamond_Sword = Armi(name="Diamond Sword", weapon_type="Spada", base_damage=25, value=150)
Platinum_Sword = Armi(name="Platinum Sword", weapon_type="Spada", base_damage=18, value=120)
Claymore_Sword = Armi(name="Claymore Sword", weapon_type="Spada", base_damage=20, value=140)

Wooden_Bow = Armi(name="Wooden Bow", weapon_type="Arco", base_damage=5, value=20)
Composite_Bow = Armi(name="Composite Bow", weapon_type="Arco", base_damage=12, value=50)
Recurve_Bow = Armi(name="Recurve Bow", weapon_type="Arco", base_damage=18, value=80)
Longbow_Elite = Armi(name="Longbow Elite", weapon_type="Arco", base_damage=25, value=100)
Royal_Bow = Armi(name="Royal Bow", weapon_type="Arco", base_damage=30, value=130)

Crossbow_Sniper = Armi(name="Crossbow Sniper", weapon_type="Balestra", base_damage=35, value=200)
Heavy_Crossbow = Armi(name="Heavy Crossbow", weapon_type="Balestra", base_damage=28, value=180)
Repeating_Crossbow = Armi(name="Repeating Crossbow", weapon_type="Balestra", base_damage=20, value=140)
Compact_Crossbow = Armi(name="Compact Crossbow", weapon_type="Balestra", base_damage=15, value=90)
Dragon_Bow = Armi(name="Dragon Bow", weapon_type="Arco", base_damage=35, value=250)

Shotgun_12Gauge = Armi(name="12 Gauge Shotgun", weapon_type="Fucile", base_damage=40, value=180)
Assault_Rifle = Armi(name="Assault Rifle", weapon_type="Fucile", base_damage=22, value=150)
Sniper_Rifle = Armi(name="Sniper Rifle", weapon_type="Fucile", base_damage=45, value=300)
Laser_Gun = Armi(name="Laser Gun", weapon_type="Fucile", base_damage=50, value=350)
Rpg = Armi(name="Rocket Propelled Grenade", weapon_type="Fucile", base_damage=100, value=500)

Battle_Axe = Armi(name="Battle Axe", weapon_type="Ascia", base_damage=30, value=120)
War_Axe = Armi(name="War Axe", weapon_type="Ascia", base_damage=35, value=150)
Double_Axe = Armi(name="Double Axe", weapon_type="Ascia", base_damage=40, value=180)
Tomahawk = Armi(name="Tomahawk", weapon_type="Ascia", base_damage=25, value=100)
Executioner_Axe = Armi(name="Executioner Axe", weapon_type="Ascia", base_damage=50, value=250)

Mace = Armi(name="Mace", weapon_type="Mazza", base_damage=28, value=110)
Morningstar = Armi(name="Morningstar", weapon_type="Mazza", base_damage=35, value=130)
Flanged_Mace = Armi(name="Flanged Mace", weapon_type="Mazza", base_damage=32, value=120)
Spiked_Mace = Armi(name="Spiked Mace", weapon_type="Mazza", base_damage=40, value=160)
Holy_Mace = Armi(name="Holy Mace", weapon_type="Mazza", base_damage=45, value=200)

Hand_Cannon = Armi(name="Hand Cannon", weapon_type="Pistola", base_damage=25, value=120)
Revolver = Armi(name="Revolver", weapon_type="Pistola", base_damage=30, value=140)
Automatic_Pistol = Armi(name="Automatic Pistol", weapon_type="Pistola", base_damage=20, value=100)
Desert_Eagle = Armi(name="Desert Eagle", weapon_type="Pistola", base_damage=40, value=180)
Silenced_Pistol = Armi(name="Silenced Pistol", weapon_type="Pistola", base_damage=20, value=130)


Hero_Arms = [
    Rusty_Sword,  
    Silver_Sword, 
    Diamond_Sword,
    Platinum_Sword, 
    Claymore_Sword, 
    Wooden_Bow, 
    Composite_Bow, 
    Recurve_Bow,  
    Longbow_Elite,  
    Royal_Bow,  
    Battle_Axe,  
    War_Axe,  
    Double_Axe,  
    Mace,
    Morningstar,  
    Hand_Cannon,  
    Revolver,  
    Desert_Eagle,
    Rpg
]

Enemy_Arms = [
    Rusty_Sword,  
    Wooden_Bow, 
    Recurve_Bow,  
    Crossbow_Sniper,  
    Hand_Cannon,  
    Mace,
    Flanged_Mace, 
    Battle_Axe,
    Tomahawk,  
    Spiked_Mace, 
]





Spada_Della_Notte = Armi(name="Spada della Notte", weapon_type="Spada", base_damage=70, value=300)
Fiamma_Eterna = Armi(name="Fiamma Eterna", weapon_type="Fucile", base_damage=60, value=200)
Pugno_di_Gelo = Armi(name="Pugno di Gelo", weapon_type="Mazza", base_damage=60, value=250)
Mazza_del_Cataclisma = Armi(name="Mazza del Cataclisma", weapon_type="Mazza", base_damage=80, value=350)
Lancia_dell_Invasione = Armi(name="Lancia dell'Invasione", weapon_type="Lancia", base_damage=70, value=300)
Ascia_della_Perdizione = Armi(name="Ascia della Perdizione", weapon_type="Ascia", base_damage=90, value=400)
Spada_Cosmica = Armi(name="Spada Cosmica", weapon_type="Spada", base_damage=100, value=450)
Cloak_of_Shadows = Armi(name="Cloak of Shadows", weapon_type="Magia", base_damage=70, value=300) 
Falcione_della_Paura = Armi(name="Falcione della Paura", weapon_type="Falcione", base_damage=60, value=350)
Mazza_dell_Oscurità = Armi(name="Mazza dell'Oscurità", weapon_type="Mazza", base_damage=75, value=375)
Artiglio_del_Drago = Armi(name="Artiglio del Drago", weapon_type="Artiglio", base_damage=60, value=500)
Furia_del_Distruttore = Armi(name="Furia del Distruttore", weapon_type="Mazza", base_damage=80, value=400)
Zanna_di_Sangue = Armi(name="Zanna di Sangue", weapon_type="Spada", base_damage=100, value=450)
Scudo_del_Titano = Armi(name="Scudo del Titano", weapon_type="Scudo", base_damage=65, value=200) 
Spada_Inferno = Armi(name="Spada Inferno", weapon_type="Spada", base_damage=75, value=500)

armi_boss = [
    Spada_Della_Notte, Fiamma_Eterna, Pugno_di_Gelo, Mazza_del_Cataclisma, 
    Lancia_dell_Invasione, Ascia_della_Perdizione, Spada_Cosmica, Cloak_of_Shadows, 
    Falcione_della_Paura, Mazza_dell_Oscurità, Artiglio_del_Drago, Furia_del_Distruttore, 
    Zanna_di_Sangue, Scudo_del_Titano, Spada_Inferno
]