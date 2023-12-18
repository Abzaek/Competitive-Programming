class ATM:
    def __init__(self):
        banknote_values = [20, 50, 100, 200, 500]
        self.bank = {value: 0 for value in banknote_values}

    def deposit(self, banknotes_count):
        for value, count in zip(self.bank.keys(), banknotes_count):
            self.bank[value] += count

    def withdraw(self, amount):
        withdrew = {value: 0 for value in self.bank}
        
        for value in sorted(self.bank.keys(), reverse=True):
            withdrew[value] = min(self.bank[value], amount // value)
            amount -= withdrew[value] * value

        if amount != 0:
            return [-1]

        for value in self.bank:
            self.bank[value] -= withdrew[value]

        return [withdrew[value] for value in withdrew]
