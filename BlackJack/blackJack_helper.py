import random
class Bank():
    total_amount=0
    def __init__(self, name, bank_roll):
        self.name=name
        self.bank_roll=bank_roll
class Player(Bank):
    player_total_amount=0
    def __init__(self, name, bank_roll):
        super().__init__(name, bank_roll)
    def add_player_total(self):
        Bank.total_amount+=self.bank_roll
class Computer(Bank):
    computer_total_amount=0
    def __init__(self, name, bank_roll):
        super().__init__(name, bank_roll)
    def add_computer_total(self):
        Bank.total_amount+=self.bank_roll
computer=Computer('Computer', random.randint(1,101))
player=Player('Player', int(input('Bank_roll:')))



