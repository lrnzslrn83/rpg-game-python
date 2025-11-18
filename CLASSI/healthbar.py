import os
os.system("")

class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"

    colors: dict = {
        "red": "\033[91m",
        "yellow": "\033[93m",
        "green": "\033[92m",
        "default": "\033[0m",
    }

    def __init__(self, entity, length: int = 20, is_colored: bool = True):
        self.entity = entity
        self.length = length
        self.is_colored = is_colored

    def get_color(self, ratio: float) -> str:
        if not self.is_colored:
            return ""
        if ratio > 0.6:
            return self.colors["green"]
        elif ratio > 0.3:
            return self.colors["yellow"]
        else:
            return self.colors["red"]

    def draw(self) -> None:
        """Stampa la barra visiva:
        Inizia con |
        Blocchi pieni colorati (█)
        Blocchi vuoti (_)
        Ripristina il colore con default
        Chiude con |
        """
        current = self.entity.health
        max_value = self.entity.health_max
        ratio = current / max_value
        remaining_bars = round(ratio * self.length)
        lost_bars = self.length - remaining_bars
        color = self.get_color(ratio)

        print(f"{self.entity.name}'s HEALTH: {current}/{max_value}")
        print(
            
            f"{self.barrier}"
            f"{color if self.is_colored else ''}"
            f"{self.symbol_remaining * remaining_bars}"
            f"{self.symbol_lost * lost_bars}"
            f"{self.colors['default'] if self.is_colored else ''}" 
            f"{self.barrier}"
        )



