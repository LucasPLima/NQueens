import numpy as np
from HillClimbing import i_hill_climbing
from SimulatedAnnealing import simulated_annealing

n = int(input("Input the board's size:"))


def n_queens():
    if n < 4:
        print("The solution doesn't exist.")
        quit()
    iterations = int(input("Input the max iterations:"))
    al = int(input("Select the algorithm of local search : 1 -Iterative Hill Climbing | 2 - Simulated Annealing:\t"))
    solution = []
    if al == 1:
        solution = i_hill_climbing(iterations, n)
    elif al == 2:
        p = int(input("Input the maximum of perturbations per iteration:"))
        scs = int(input("Input the maximum of successes per iteration:"))
        solution = simulated_annealing(n, iterations, p, scs)
    else:
        print('Invalid Option! Try Again.')

    return solution


def print_board(sol, dim):
    board = np.array([['| |'] * dim] * dim)
    for i in range(len(sol)):
        board[sol[i], i] = '|Q|'
    print(board)


if __name__ == '__main__':
    s = n_queens()
    print("The solution is:{}".format(s))
    print_board(s, n)
