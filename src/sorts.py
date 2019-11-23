import random
from src.lib.helpers import *
import matplotlib.pyplot as plt


def rand_list(length):
    r = []
    for i in range(1, length + 1):
        r.append(i)
    random.shuffle(r)
    return r


def bubble_sort(L):
    while True:
        finished = True
        for i in range(len(L.items) - 1):
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
    while True:
        random.shuffle(L.items)
        if is_list_sorted(L.items):
            return L
    




