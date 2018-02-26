import math
import random
import sys

from local_searchs.HillClimbing import evalue, generate_state


def simulated_annealing(dim, iterations, perturbations, success):
    i, j = 0, 0
    state = generate_state(dim)
    t = len(state)**2
    alpha = 0.2
    n_successes = sys.maxsize

    while i < iterations or n_successes == 0:
        n_successes = 0
        while n_successes <= success or j < perturbations:
            n_state = perturbate(state)
            delta = evalue(n_state) - evalue(state)
            if delta <= 0 or math.exp(-delta/t) > random.random():
                state = n_state
                n_successes += 1
            j += 1
        t = alpha * t
        i += 1

    print("Alpha: {}".format(alpha))
    print("Final temperature: {}".format(t))
    print("Final evalue: {}".format(evalue(state)))
    return state


def perturbate(state):
    t = len(state)
    c = random.randint(0, t-1)
    state[c] = random.randint(0, t-1)
    return state
