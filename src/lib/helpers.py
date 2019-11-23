def is_list_sorted(L):
    for i in range(len(L.items)-1):
        v1 = L[i]
        v2 = L[i + 1]
        if v1 > v2:
            return False
    return True
