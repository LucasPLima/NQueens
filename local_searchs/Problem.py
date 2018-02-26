import random


# def perturbate(state):
#     t = len(state)
#     c = random.randint(0, t-1)
#     state[c] = random.randint(0, t-1)
#     return state


def neighbours(current_state):
    i = 0
    n_state = current_state
    columns = len(current_state)
    n_ac = random.randint(1, columns-1) #number of altered columns
    altered_c = []

    while i < n_ac:
        c = random.randint(0, columns-1)
        if not (c in altered_c):
            n_state[c] = random.randint(0, columns-1)
            altered_c.append(c)
            i += 1
            yield current_state


def evalue(state):
    h = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if j == i:
                continue
            if state[i] == state[j]:
                h = h+1
                continue
            if state[i] + i == state[j] + j or state[i] - i == state[j] - j:
                h = h+1
    return h


def generate_state(size):
    col = []
    for i in range(size):
        col.append(random.randint(0, size-1))
    return col
