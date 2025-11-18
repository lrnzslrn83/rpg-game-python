class Money:
    def __init__(self, initial=0):  
        self.value = initial

    def add(self, amount):
        self.value += amount

    def spend(self, amount):
        if self.value >= amount:
            self.value -= amount
            return True
        return False

    def get_balance(self):
        return self.value
