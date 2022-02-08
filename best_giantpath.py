# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import random
from collections import defaultdict
from simanneal import Annealer

class GiantAnnealer(Annealer):

    def move(self):
        # choose a random entry in the matrix
        i = random.randrange(len(self.state))
        j = random.randrange(len(self.state))
        self.state[i], self.state[j] = self.state[j], self.state[i]

    def energy(self):
        eval_list = [1 for _ in range(N)]
        for i in range(len(self.state)):
            eval_list[self.state[i][1]] += eval_list[self.state[i][0]]
            # print(eval_list)
        print(sum(eval_list))
        return sum(eval_list)

if __name__ == '__main__':
    N = 3
    init_state = [(a, b) for a in range(N) for b in range(N) if a != b]
    random.shuffle(init_state)
    ga = GiantAnnealer(init_state)
    order, total = ga.anneal()
    print(order)
    print("total= " + str(total))