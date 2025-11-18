from GameManager import Gamemanager
from leaderboard import crea_tabella
crea_tabella()


def main():
    print("🎮 Benvenuto nel Dungeon Rogue-like!")
    nome = input("Inserisci il nome del tuo eroe: ").strip()
    if not nome:
        nome = "Eroe senza nome"

    gioco = Gamemanager(hero_name=nome)
    gioco.start()

if __name__ == "__main__":
    main()
