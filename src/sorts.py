import random
from src.lib.helpers import *
import matplotlib.pyplot as plt
import time

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


def bogo_sort(L):
    while True:
        random.shuffle(L.items)
        if is_list_sorted(L):
            return



def insertion_sort(L):
    i = 1
    while i < len(L.items):
        j = i
        while j > 0 and L[j-1] > L[j]:
            a = L[j]
            b = L[j-1]
            L[j] = b
            L[j-1] = a
            j = j - 1
        i = i + 1




def quantum_sort(L):
    if is_list_sorted(L):
        return
    else:
        while True:
            #todo: destroy current universe
            continue




def entropy_sort(L):
    while True:
        if is_list_sorted(L):
            return
        time.sleep(5)


def fast_sort(L):
    for i in range(len(L.items)):
        L[i] = i + 1







