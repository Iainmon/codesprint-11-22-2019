import random

class HistoricArray:
    
    def __init__(self, L = []):
        self.accesses = 0
        self.changes = 0
        self.items = L
        self.list_states = []
        self._save_current_list()

    def __getitem__(self, key):
        self.accesses += 1
        return self.items[key]
    
    def __setitem__(self, key, value):
        self.changes += 1
        self.items[key] = value
        self._save_current_list()

    # Saves a copy of the current list
    def _save_current_list(self):
        self.list_states.append(list(self.items))

    def print_history(self):
        for i in range(len(self.list_states)):
            print('Pass', i, self.list_states[i])

    def load_list(self, L):
        self.items = L
    
    def length(self):
        return len(self.items)
    
    def randomized(n = 0):
        r = []
        for i in range(1, n + 1):
            r.append(i)
        random.shuffle(r)
        return HistoricArray(r)


# def bubble_sort(L):
#     while True:
#         finished = True
#         for i in range(len(L.items) - 1):
#             a = L[i]
#             b = L[i+1]
#             if a > b:
#                 L[i+1] = a
#                 L[i] = b
#                 finished = False
#         if finished:
#             break
#     return L

# my_list = HistoricArray.randomized(10)
# my_list.print_history()
# my_list = bubble_sort(my_list)
# my_list.print_history()