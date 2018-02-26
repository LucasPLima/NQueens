import sys


from local_searchs.Problem import evalue, generate_state, neighbours


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