===========================
  GIOCO RPG - README.txt
===========================

📌 Descrizione
-------------
Questo progetto è un mini RPG a turni sviluppato in Python.
Il giocatore impersona un eroe che affronta una serie di nemici (inclusi boss),
può acquistare equipaggiamenti, gestire il proprio inventario, e cerca di sopravvivere
il più a lungo possibile per scalare la leaderboard.

👨‍💻 Autore
---------
Lorenzo Salerno

📁 Struttura del progetto
-------------------------
- main2.py: punto di avvio del gioco
- main2.bat: avvio rapido per Windows
- GameManager.py: gestisce il flusso del gioco
- Personaggio.py: classi Hero, Enemy, Boss
- armi.py, Armatura.py, Rarità.py: classi degli oggetti equipaggiabili
- Shop.py: logica per l'acquisto di armi/armature
- Money.py: gestione soldi del giocatore
- leaderboard.py: salvataggio e visualizzazione punteggi
- healthbar.py: gestione grafica delle barre della salute
- leaderboard.db: database locale dei punteggi

▶️ Avvio del gioco
------------------
1. Assicurati di avere Python installato.
2. Esegui il file main2.bat su Windows oppure lancia:
   python main2.py

🎮 Funzionalità principali
--------------------------
- Combattimento a turni contro nemici e boss
- Equipaggiamento armi e armature
- Gestione della vita e del denaro
- Negozio con oggetti acquistabili
- Sistema di rarità
- Leaderboard salvata su database

📊 Diagrammi allegati
---------------------
- UML Class Diagram: struttura delle classi e relazioni
- Use Case Diagram: attori e funzionalità
- Sequence Diagram: flusso dettagliato dell'attacco

🛠️ Requisiti
------------
- Python 3.11+
- Nessuna libreria esterna necessaria (usa solo la libreria standard)
- (Opzionale) Estensione PlantUML per visualizzare i diagrammi
📌 Note aggiuntive
------------------
- Il gioco è interamente testabile via terminale
- Può essere esteso con nuove armi, classi o logiche di IA
