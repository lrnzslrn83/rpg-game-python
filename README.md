# rpg-game-python
This project is a turn-based mini-RPG developed in Python. The player takes on the role of a hero who faces a series of enemies (including bosses), can purchase equipment, manage their inventory, and tries to survive as long as possible to climb the leaderboard.

Author
Lorenzo Salerno

Project Structure
main2.py: main entry point of the game
main2.bat: quick launch script for Windows
GameManager.py: handles the overall game flow
Personaggio.py: defines Hero, Enemy, and Boss classes
armi.py, Armatura.py, Rarita.py: classes for weapons, armor, and item rarity
Shop.py: shop system for purchasing equipment
Money.py: player currency and economy management
leaderboard.py: saving and displaying high scores
healthbar.py: health bar visualization
leaderboard.db: local SQLite database for the leaderboard

How to Run the Game
Make sure Python is installed on your system.
Run main2.bat on Windows
OR execute manually:
python main2.py

Main Features
Turn-based combat against enemies and bosses
Weapon and armor equipment system
Health and currency management
Shop with buyable items
Item rarity system
Persistent leaderboard stored in a local database

Included Diagrams
UML Class Diagram: class structure and relationships
Use Case Diagram: actors and main functionalities
Sequence Diagram: detailed attack/turn flow

Requirements
Python 3.11+
No external libraries required (standard library only)
Optional: PlantUML extension to view diagram files

Additional Notes
The game runs entirely in the terminal
Easily extendable with new weapons, classes, or AI logic
