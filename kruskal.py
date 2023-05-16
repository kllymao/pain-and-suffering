from collections import defaultdict
import heapq as hq


def find(index, back_tree):
    while back_tree[index] != None:
        index = back_tree[index]
    return index


def kruskal(N, M, bounds, edges):
    frontier = []
    hq.heapify(frontier)
    visited = set([])
    total_cost = 0
    back_tree, degree_counter = [None], [None]
    for i in range(1, M+1):
        _, _, cost = edges[i]
        hq.heappush(frontier, (cost, i))
    for j in range(1, N+1):
        back_tree.append(None)
        degree_counter.append(0)
    while(len(frontier) > 0):
        (cost, edge_index) = hq.heappop(frontier)
        u, v, _ = edges[edge_index]
        if (degree_counter[u] >= bounds[u]) or (degree_counter[v] >= bounds[v]):
            continue
        fu = find(u, back_tree)
        if fu == find(v, back_tree):
            continue
        visited.add(edge_index)
        degree_counter[u], degree_counter[v] = degree_counter[u]+1, degree_counter[v]+1
        back_tree[fu] = v
        total_cost += cost
    if len(visited) < N-1:
        return -1, "Dead End :("
    return total_cost, sorted(list(visited))


def read_input():
    N, M = [int(i) for i in input().split()]
    bounds = [None] + [int(input()) for _ in range(N)]
    edges = [(-1, -1, -1)]
    for i in range(M):
        u, v, c = [int(i) for i in input().split()]
        edges.append((u, v ,c))
    return N, M, bounds, edges


def print_output(mst):
    for edge in mst:
        print(edge)


def main():
    N, M, bounds, edges = read_input()
    cost, mst = kruskal(N, M, bounds, edges)
    # print(cost)
    print_output(mst)


if __name__ == '__main__':
    main()
