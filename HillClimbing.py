import sys
import random


def i_hill_climbing(iterations, dim):
    best_value = sys.maxsize
    best_state = []
    for i in range(iterations):
        state = generate_state(dim)
        h_c_solution = hill_climbing(state)
        e_hc = evalue(h_c_solution)
        if e_hc == 0:
            print("The optimum evalue was found.")
            return h_c_solution
        elif e_hc < best_value:
            best_state = h_c_solution
            best_value = e_hc
    print("The lowest evalue found was: {}".format(best_value))
    return best_state


def hill_climbing(state):
    best_evalue = sys.maxsize
    new_state = []

    for e in neighbours(state):
        val = evalue(e)
        if val < best_evalue:
            new_state = e
            best_evalue = evalue(new_state)

    if evalue(state) < best_evalue:
        return state

    return new_state


def neighbours(current_state):
    for i in range(len(current_state)):
        n_state = generate_state(len(current_state))
        yield n_state


def evalue(state):
    h = 0
    for i in range(len(state)):
        for j in range(len(state)):
            if j == i:
                continue
            if state[i] == state[j]:
                h = h+1
                continue
            if state[i] + i == state[j] + j or state[i] - i == state[j] - j:
                h = h+1
    return round(h/2)


def generate_state(size):
    col = []
    for i in range(size):
        col.append(random.randint(0, size-1))
    return col