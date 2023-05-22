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

    # each optimization variable is 1 or 0 depending on if indexed edge is in mst or not
    opts = cp.Variable(shape=(M,1), boolean=True)

    # constraints:
    # 1. sum of the optimization variables = N - 1
    # 2. this constraint would have made it exponentially slow so i'm getting rid of this lol
    # 3. for each vertex v in the graph, we make sure the sum of the optimization variables corresponding
    # to the edges attached to v is less than or equal to the bound of v
    # (4. optimization variables can only be 0 or 1. this is covered by the fact that opt variable is list of bools)
    # 5. add a constraint each time we form a cycle or something idk

    constraints = [cp.sum(opts) == N-1] # 1st constraint

    for i in range(N): # 3rd constraint
        if bounds[i] != 1:
            bound = bounds[i] - 1
        else:
            bound = bounds[i]

    node_opts = [[] for _ in range(N + 1)]

    for i, (u, v, w) in enumerate(edges):
        node_opts[u].append(opts[i])
        node_opts[v].append(opts[i])

    for u in range(1, N + 1):
        constraints.append(cp.sum(node_opts[u]) <= bounds[u - 1])
        constraints.append(cp.sum(node_opts[u]) >= 1)

    # add objective: minimize total weight
    edge_weights = [] # at index i, edge i+1 has some weight
    for i in range(M):
        edge_weights.append(edges[i][2])
    total_weight = edge_weights @ opts
    objective = cp.Minimize(total_weight)

    problem = cp.Problem(objective, constraints)
    problem.solve()

    # # now find connected components
    # mst_edges = []
    # for i in range(M):
    #     if opts.value[i] == 1.0:
    #         mst_edges.append(edges[i])
    
    # mst_edges_dict = defaultdict(list)
    # for edge in mst_edges:
    #     u, v, weight = edge[0], edge[1], edge[2]
    #     mst_edges_dict[u].append((v, weight))
    #     mst_edges_dict[v].append((u, weight))

    # unvisited = {}
    # for i in range(1, N+1):
    #     unvisited[i] = False
    # visited = {}

    # while len(unvisited) != 0:
    #     unvisited = explore(next(iter(unvisited)), mst_edges_dict, unvisited, visited)
    #     unvisited_vertex = 0
    #     if len(unvisited) == 0:
    #         break

    #     for vertex in unvisited:
    #             unvisited_vertex = vertex

    #     nodes_indices = []
    #     if unvisited_vertex != 0:
    #         for (v2, index) in edges_dict[unvisited_vertex]:
    #             if v2 in visited:
    #                 nodes_indices.append(index)
    #                 print(nodes_indices)

    #         constraints.append(cp.sum([opts[i] for i in nodes_indices]) >= 1)
    #         # add a constraint that there should be an edge from unvisited to any edge in edges reachable from initial vertex

    #         problem = cp.Problem(objective, constraints)
    #         problem.solve()
    
    for i in range(M):
        if opts.value[i] == 1.0:
            print(i+1)

# def explore(vertex, mst_edges_dict, unvisited, visited):
#     del unvisited[vertex]
#     visited[vertex] = True
#     for (v2, weight) in mst_edges_dict[vertex]:
#         if v2 in unvisited:
#             explore(v2, mst_edges_dict, unvisited, visited) 
#     return unvisited

def read_input(): # note: at index i we're looking at edge or vertex i+1
    N, M = [int(i) for i in input().split()]
    bounds = [int(input()) for _ in range(N)]
    edges = [[int(i) for i in input().split()] for _ in range(M)]

    edges_dict = defaultdict(list)
    for i in range(M):
        u, v, c = edges[i][0], edges[i][1], edges[i][2]
        edges_dict[u].append((v, i+1))
        edges_dict[v].append((u, i+1))

    return N, M, bounds, edges, edges_dict

def main():
    N, M, bounds, edges, edges_dict = read_input()
    solve(N, M, bounds, edges, edges_dict)

if __name__ == '__main__':
    main()