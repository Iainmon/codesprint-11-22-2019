import random

class HistoricArray:
    
    def __init__(self, L = []):
        self.accesses = 0
        self.changes = 0
        self.items = L

    def __getitem__(self, key):
        self.accesses += 1
        return self.items[key]
    
    def __setitem__(self, key, value):
        self.changes += 1
        self.items[key] = value

    def load_list(self, L):
        self.items = L
    
    def randomized(n = 0):
        r = []
        for i in range(1, n + 1):
            r.append(i)
        random.shuffle(r)
        return HistoricArray(r)
