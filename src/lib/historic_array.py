import random

class HistoricArrayEntry:

    def __init__(self, new_list, key_changed = None, key_accessed = None, original_value_of_key = None, total_accesses = 0, total_changes = 0):
        self.list_snapshot = list(new_list)
        self.key_changed = key_changed
        self.key_accessed = key_accessed
        self.total_accesses = total_accesses
        self.total_changes = total_changes
        if key_changed:
            self.original_value_of_key = original_value_of_key
            self.new_value_of_key = self.list_snapshot[key_changed]

class HistoricArray:
    
    def __init__(self, L = []):
        self.accesses = 0
        self.changes = 0
        self.items = L
        self.list_states = []
        self._save_current_list()

    def __getitem__(self, key):
        self.accesses += 1
        entry = HistoricArrayEntry(self.items, key_accessed=key, total_accesses=self.accesses, total_changes=self.changes)
        self._save_current_list(entry)

        return self.items[key]
    
    def __setitem__(self, key, value):
        original_value_of_key = self.items[key]

        self.changes += 1
        self.items[key] = value

        entry = HistoricArrayEntry(self.items, key, original_value_of_key, total_accesses=self.accesses, total_changes=self.changes)
        self._save_current_list(entry)


    # Saves a copy of the current list
    def _save_current_list(self, entry = None):
        if entry:
            self.list_states.append(entry)
        else:
            self.list_states.append(HistoricArrayEntry(self.items, total_accesses=self.accesses, total_changes=self.changes))

    def print_history(self):
        for i in range(len(self.list_states)):
            entry = self.list_states[i]
            if entry.key_changed:
                print('Pass', i, entry.list_snapshot, f'[{ entry.key_changed }] { entry.original_value_of_key } -> { entry.new_value_of_key }')
            else:
                print('Pass', i, entry.list_snapshot)

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