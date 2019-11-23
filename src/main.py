import random



def rand_list(length):
    r = []
    for i in range(length):
        r.append(random.randint(1, 100))
    return r




def bubble_sort(L):
    while True:
        finished = True
        for i in range(len(L) - 1):
            a = L[i]
            b = L[i+1]
            if a > b:
                L[i+1] = a
                L[i] = b
                finished = False
        if finished:
            break
    return L


def bogo_sort(L):
    









print(bubble_sort(rand_list(10)))

