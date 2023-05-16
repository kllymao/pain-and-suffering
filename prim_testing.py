"""
Teleporters

Incoming Dean of the College, Melina Hale, has decided that winters have gotten too long and by next winter, the beloved tunnels connecting the entire campus should be accessible once again. Unfortunately, all the old tunnels running under the quad have become unusable and new ones need to be built. Of course, this should be kept economical and financially responsible. An engineering firm has provided all possible tunnels that could be dug, and of course the price tag for each of them. In a wild revelation, Fermilab announced that they now have a working teleporter, but it only works for short distances. The engineering firm has provided estimates for installing these teleporters in various building around campus (but not all). The dean wants all buildings to be connected by at least one path, but also for the entire project to cost as low as possible. To that end, you need to find the best set of tunnels and (maybe) teleporters to connect the entire campus for the next winter.

Input: In the first line there are three integers $N$, $K$, $M$, which correspond to the number of buildings, the number of buildings where a teleporter can be installed and the number of possible tunnels between buildings.
In the next $K$ lines there are two integers, $i$ and $B[i]$, meaning that a teleporter can be installed in building $i$ with cost $B[i]$.
Finally, the next $M$ lines contain three integers $i$, $j$, $c[i, j]$, which denote that there is a proposed tunnel between buildings $i$ and $j$ with cost $c[i, j]$.

Output: One line with a single integer, the minimum cost for the entire network.
"""

from collections import defaultdict
import heapq

def prim(G, limits, len):

    touched = {}
    for key in G:
        touched[key] = 0
    num_touched = 1
    heap = []
    cost = 0
            
    for edge in G[1]:
        heapq.heappush(heap, edge)
    touched[1] = 1
    limits[1] -= 1

    while(num_touched < len):
        pop = heapq.heappop(heap)
        print("\nCurrent node", pop)
        print("Current heap", heap)
        print("Current cost", cost)
        print("Have visited", touched)
        print("Limit counts", limits)
        if touched[pop[1]] or not limits[pop[1]]:
            continue
        num_touched += 1
        touched[pop[1]] = 1
        cost += pop[0]
        limits[pop[1]] -= 1
        for edge in G[pop[1]]:
            heapq.heappush(heap, edge)


    return cost


def solve(N, M, limits, edges):
  
  mst1 = prim(edges,limits,N)

#   print(mst1, mst2)

  return mst1


def read_input():
    N, M = [int(i) for i in input().split()]
    limits = [int(input()) for _ in range(N)]
    limits.insert(0, None)
    edges = defaultdict(list)
    for i in range(M):
        u, v, c = [int(i) for i in input().split()]
        # print(u,v,c)
        edges[u].append((c, v))
        edges[v].append((c, u))
    print(N, M, limits, edges)
    
    return N, M, limits, edges


def main():
    N, M, limits, edges = read_input()
    cost = solve(N, M, limits, edges)
    print(cost)


if __name__ == '__main__':
    main()
