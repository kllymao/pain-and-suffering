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

    # print("\n\n\n\nHELLO YES THE ALGORITHM IS STARTING\n\n\n\n\n\n")

    touched = {}
    for key in G:
        touched[key] = 0
    num_touched = 1
    heap = []
    cost = 0
    looking = False

    used = []
            
    for edge in G[1]:
        heapq.heappush(heap, edge)
    touched[1] = 1

    while(num_touched < len):
        # print("Current heap 2", heap)
        if heap == []:
            for i in range(1, len+1): #this limit could be problematic
                if not touched[i]:
                    # print("here", i)
                    looking = True
                    touched[i] = 1
                    num_touched += 1
                    for edge in G[i]:
                        heapq.heappush(heap, edge)
                    break
            continue
        pop = heapq.heappop(heap)
        # print("\nCurrent node", pop)
        # print("Current heap", heap)
        # print("Current cost", cost)
        # print("Have visited", touched)
        # print("Used edges", used)
        # print("Limit counts", limits)
        # print(touched[pop[1]], not limits[pop[1]])
        if touched[pop[1]]:
            if looking:
                looking = False
            else: continue
        
        if not limits[pop[1]] or not limits[pop[2]]:
            continue
        num_touched += 1
        touched[pop[1]] = 1
        cost += pop[0]
        limits[pop[1]] -= 1
        limits[pop[2]] -= 1
        for edge in G[pop[1]]:
            heapq.heappush(heap, edge)
        used.append(pop[3])

    return sorted(used), cost


def solve(N, M, limits, edges):
  
  used, cost = prim(edges,limits,N)

#   print(used, cost)

  return used


def read_input():
    N, M = [int(i) for i in input().split()]
    limits = {i+1:int(input()) for i in range(N)}
    edges = defaultdict(list)
    for i in range(M):
        u, v, c = [int(i) for i in input().split()]
        # print(u,v,c)
        edges[u].append((c, v, u, i+1))
        edges[v].append((c, u, v, i+1))
    # print(N, M, limits, edges)
    
    return N, M, limits, edges


def main():
    N, M, limits, edges = read_input()
    used = solve(N, M, limits, edges)
    for edge in used:
        print(edge)


if __name__ == '__main__':
    main()
