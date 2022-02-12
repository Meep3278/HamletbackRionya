# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import random
from collections import defaultdict
from simanneal import Annealer
import sys
import numpy as np
from numpy.linalg import multi_dot

def evaluate_ordering(ordering):
    return multi_dot(ordering)
def to_slots(ordering, N_in):
    slots = []
    for array in ordering[1:]:
        slots += [(sum(np.dot(np.arange(N_in), array - np.identity(N_in))), sum(np.dot(array- np.identity(N_in), np.arange(N_in))))]
    return(slots)

class GiantAnnealer(Annealer):

    def move(self):
        # choose a random entry in the matrix
        i = random.randrange(1, len(self.state)-1)
        self.state[i], self.state[i+1] = self.state[i+1], self.state[i]

    def energy(self):
        # print("evaluating:")
        # print(evaluate_ordering(self.state))
        return -sum(evaluate_ordering(self.state))

if __name__ == '__main__':
    N = sys.argv
    if len(N) != 2:
        raise ValueError("Oops!  That was the wrong input.  Try again...")
    N = int(N[1])
    init_state = [np.identity(N) + np.array([[0 if a != c or b != d else 1 for c in range(N)] for d in range (N)]) for a in range(N) for b in range(N) if a != b]
    random.shuffle(init_state)
    init_state = [np.ones(N)] + init_state
    print(to_slots(init_state, N))
    ga = GiantAnnealer(init_state)
    ga.steps = 100000
    order, total = ga.anneal()
    print(order)
    print(evaluate_ordering(order))
    print(to_slots(order, N))
    print("total=" + str(-total))