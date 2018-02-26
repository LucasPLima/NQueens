import math
import random
import sys

from local_searchs.Problem import evalue, generate_state, neighbours


def simulated_annealing(dim, iterations, perturbations, success):
    i, j = 0, 0
    state = generate_state(dim)
    t = len(state)**2
    alpha = 0.95
    n_successes = sys.maxsize

    while i < iterations or n_successes == 0:
        n_successes = 0
        j = 0
        while (n_successes < success) or (j < perturbations):
            v1 = evalue(state)
            n_state = list(neighbours(state)).pop()
            v2 = evalue(n_state)
            if v2 == 0:
                print("Alpha: {}".format(alpha))
                print("Final iteration:{}".format(i))
                print("Final perturbation: {}".format(j))
                print("Number of successes: {}".format(n_successes))
                print("Final temperature: {}".format(t))
                print("The optimum evalue was found.")
                return n_state
            delta = v2 - v1
            if delta <= 0 or math.exp(-delta/t) > random.random():
                state = n_state
                n_successes += 1
            j += 1
        t = alpha * t
        i += 1

    print("Alpha: {}".format(alpha))
    print("Final iteration: {}".format(i))
    print("Final temperature: {}".format(t))
    print("Final evalue: {}".format(evalue(state)))
    return state
