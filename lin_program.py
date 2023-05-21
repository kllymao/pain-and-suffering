'''
    first create the linear optimization problem
    then solve the linear optimization problem
    then take the array of solutions [{1,0}...] (1 if indexed edge is in mst and 0 if not)
    and process them to print the lines
'''

from collections import defaultdict
import heapq
import cvxpy as cp

def solve(N, M, bounds, edges, edges_dict):
    # CREATE LINEAR OPTIMIZATION PROBLEM!

    # an array of optimization variables:
    # each optimization variable is 1 or 0 depending on if indexed edge is in mst or not
    opts = cp.Variable(M, boolean=True)

    # constraints
    # 1. sum of the optimization variables = N - 1
    # 2. for all edges in a subset S = (V', E') of G (for all subsets)
    # (yikes! this is a LOT of subsets! might have to make it smaller in some way),
    # make sure sum of optimization variables = |V'| - 1
    # 3. for each vertex v in the graph, we make sure the sum of the optimization variables corresponding
    # to the edges attached to v is less than or equal to the bound of v
    # (4. optimization variables can only be 0 or 1. this is covered by the fact that opt variable is list of bools)

    constraints = [cp.sum(opts) == N-1] # 1st constraint

    # 2nd constraint is: hard. see if this runs without it or if we can choose better subgraphs
    # maybe choose a proportional number of random subgraphs and see if this property holds?

    for i in range(N): # 3rd constraint
        bound = bounds[i]
        i_edges = [] # at index j: 1 if edge j+1 connects to vertex i, 0 otherwise
        for j in range(M):
            if edges[j+1][0] == i or edges[j+1][1] == i:
                i_edges.append(1)
            else:
                i_edges.append(0)
        degree_vertex = i_edges @ opts
        constraints.append(degree_vertex <= bound)

    # add objective
    # objective: for each edge in E, we add to our total weight the weight of that edge 
    # multiplied by the optimization variable corresponding to that edge
    # minimize this total weight
    edge_weights = [] # at index i, edge i+1 has some weight
    for i in range(M):
        edge_weights.append(edges[i+1][2])
    total_weight = edge_weights @ opts
    objective = cp.Minimize(total_weight)
    

    # SOLVE LINEAR OPTIMIZATION PROBLEM ITERATIVELY!

    return 0
        


def read_input():
    N, M = [int(i) for i in input().split()]
    bounds = [int(input()) for _ in range(N)]
    bounds.insert(0, None)
    edges = [[int(i) for i in input().split()] for _ in range(M)]
    edges.insert(0, None)

    edges_dict = defaultdict(list)
    for i in range(M):
        u, v, c = edges[i+1][0], edges[i+1][1], edges[i+1][2]
        edges_dict[u].append((v, c))
        edges_dict[v].append((u, c))

    print(bounds, edges)

    return N, M, bounds, edges, edges_dict

def main():
    N, M, bounds, edges, edges_dict = read_input()
    total_cost = solve(N, M, bounds, edges, edges_dict)
    print(total_cost)

if __name__ == '__main__':
    main()