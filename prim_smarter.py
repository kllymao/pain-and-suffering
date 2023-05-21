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

def prim(G, limits, length, max_lim):

    # print("\n\n\n\nHELLO YES THE ALGORITHM IS STARTING\n\n\n\n\n\n")

    edges_used = 0
    touched = {}
    tree_num = {}
    for key in G:
        touched[key] = 0
        tree_num[key] = 0
    heap = []
    cost = 0
    looking = False

    edge_store = defaultdict(list)
    used = []
    # print(max_lim)
            
    for edge in G[max_lim[0][0]]:
        heapq.heappush(heap, edge)
    for edge in G[max_lim[1][0]]:
        heapq.heappush(heap, edge)
    # print(max_lim[0][0], max_lim[1][0])
    # exit()
    touched[max_lim[0][0]] = 1
    tree_num[max_lim[0][0]] = 0
    touched[max_lim[1][0]] = 1
    tree_num[max_lim[1][0]] = 1
    looking = True
    bridging = False

    while(edges_used < length-1):
        # print("edges used", edges_used)
        # print("Current heap 2", heap)
        if heap == []:
            # print(length, edges_used)
            max_lim = (0,0)
            for i in range(1, length+1): #this limit could be problematic
                if not touched[i]:
                    if limits[i] <= max_lim[1]:
                        continue
                    max_lim = (i,limits[i])
                    # print("yeah we're not ending up here", i)
                    looking = True
                    touched[i] = 1
                    # limits[i] -= 1
                    for edge in G[i]:
                        heapq.heappush(heap, edge)
            # print("yeahhhhh we're done here")
            quit()
            continue
        pop = heapq.heappop(heap)
        # print("\nCurrent node", pop)
        # print("Current heap", heap)
        # print("heap length", len(heap))
        # print("Current cost", cost)
        # print("Have visited", touched)
        # print("Used edges", used)
        # # print("Edge store", edge_store)
        # print("Limit counts", limits)
        # print("Looking", looking)
        # print(touched[pop[1]], not limits[pop[1]])
        if pop[3] in used:
            continue
        if touched[pop[1]]:
            # print("here3")
            # print("here in looking")
            if looking:
                if tree_num[pop[1]] == tree_num[pop[2]]: # if there is remarkable inefficiency the tree_num reset could be changed
                    continue
                looking = False
                bridging = True
                # print("here4")
                # print("\n\n\n\n\n\n\n\nHERE, limit is",limits[pop[1]])
                if not limits[pop[1]]:
                    # break edge
                    # print(pop[1], edge_store[pop[1]][0])
                    w,u,v,e, = edge_store[pop[1]][0]
                    print("BREAKING", edge_store[pop[1]][0])
                    # exit()
                    limits[u] += 1
                    limits[v] += 1
                    used.remove(e)
                    edge_store[pop[1]].pop(0)
                    for edge in G[pop[1]]:
                        # maybe check if edge used
                        heapq.heappush(heap, edge)
            else: continue
        if not limits[pop[1]] or not limits[pop[2]]:
            # print("here2")
            continue
        touched[pop[1]] = 1 # this could be an else condition
        cost += pop[0]
        limits[pop[1]] -= 1
        limits[pop[2]] -= 1
        for edge in G[pop[1]]:
            heapq.heappush(heap, edge)
        edge_store[pop[1]].append(pop)
        edge_store[pop[2]].append(pop)
        used.append(pop[3])
        edges_used += 1

        if bridging:
            tree_num[pop[1]] = 0 
            for k,v in tree_num.items():
                if v == 1:
                    tree_num[k] = 0
            bridging = False
        else:
            tree_num[pop[1]] = tree_num[pop[2]]

        print("CONNECTING", pop)
        # print("here")

    return sorted(used), cost


def solve(N, M, limits, edges,max_lim):
  
  used, cost = prim(edges,limits,N,max_lim)

#   print(used, cost)

  return used


def read_input():
    N, M = [int(i) for i in input().split()]
    max_lim = [(0,0), (0,0)]
    limits = {}
    for i in range(N):
        limits[i+1] = int(input())
        if limits[i+1] > max_lim[0][1]:
            max_lim[1] = max_lim[0]
            max_lim[0] = (i+1,limits[i+1])
        elif limits[i+1] > max_lim[1][1]:
            max_lim[1] = (i+1,limits[i+1])
        # print(max_lim)

    edges = defaultdict(list)
    for i in range(M):
        u, v, c = [int(i) for i in input().split()]
        # print(u,v,c)
        edges[u].append((c, v, u, i+1))
        edges[v].append((c, u, v, i+1))
    # print(N, M, limits, edges)
    
    return N, M, limits, edges, max_lim


def main():
    N, M, limits, edges, max_lim = read_input()
    used = solve(N, M, limits, edges, max_lim)
    for edge in used:
        print(edge)


if __name__ == '__main__':
    main()