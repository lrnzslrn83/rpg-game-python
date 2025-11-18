import sqlite3

DB_PATH = "leaderboard.db" #generiamo un file .db locale

def crea_tabella():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            stanze INTEGER,
            monete INTEGER,
            arma TEXT,
            armatura TEXT,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """) #qui definiamo i parametri che ci interessano e di che tipo sono, creiamo una tabella leaderboard se non esiste  con id(numero ) nome eroe
    #numero stanze etc
    conn.commit() #conferma tutte le modifiche fatte al db nella sessione corrente
    conn.close()

def salva_partita(hero, stanza_corrente):
    arma = hero.armi.name if hero.armi else "Nessuna"
    armatura = hero.armatura.nome if hero.armatura else "Nessuna"
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO leaderboard (nome, stanze, monete, arma, armatura)
        VALUES (?, ?, ?, ?, ?)
    """, (hero.name, stanza_corrente, hero.money.get_balance(), arma, armatura))
    conn.commit()
    conn.close()
#stiamo eseguendo quindi una query che recupera dalla partita l' arma,l' armatura la stanza e quanti soldi avevamo e inserisce tutto in leaderboard

def mostra_leaderboard():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor() #creiamo un cursore che ci permette di eseguire la query
    c.execute("SELECT nome, stanze, monete, arma, armatura, data FROM leaderboard ORDER BY stanze DESC LIMIT 10") #eseguiamo la query, desc è l' ordine abbiamo limitato a 10 caratteri
    righe = c.fetchall() #fetchall restituisce tutte le righe dopo la query che comunque saranno 10 per via del limit
    conn.close()

    print("\n🏆 LEADERBOARD - Migliori 10 avventurieri:")
    print("-" * 80)
    for i, (nome, stanze, monete, arma, armatura, data) in enumerate(righe, 1): #ciclo for che fa scorrere tutti i risultati
        print(f"{i}. {nome} | Stanze: {stanze} | Monete: {monete} | Arma: {arma} | Armatura: {armatura} | {data}")
    print("-" * 80)
