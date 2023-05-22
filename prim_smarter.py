"""
Prim's Algorithm for Bounded MSTs with some additional modifications
"""

from collections import defaultdict
import heapq

def prim(G, limits, length, max_lim):

    # print("\n\n\n\nHELLO YES THE ALGORITHM IS STARTING\n\n\n\n\n\n")

    edges_used = 0
    touched = {}
    for key in G:
        touched[key] = 0
    heap = []
    cost = 0
    looking = False

    edge_store = defaultdict(list)
    used = []
            
    for edge in G[max_lim[0]]:
        heapq.heappush(heap, edge)
    touched[max_lim[0]] = 1

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
        # print("Limit counts", limits)
        # print("Looking", looking)
        # print(touched[pop[1]], not limits[pop[1]])
        if touched[pop[1]]:
            # print("here3")
            # print("here in looking")
            if looking:
                looking = False
                # print("here4")
                # print("\n\n\n\n\n\n\n\nHERE, limit is",limits[pop[1]])
                if not limits[pop[1]]:
                    # break edge
                    w,u,v,e, = edge_store[pop[1]][0]
                    # print("BREAKING", u,v,e)
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
        # print("here")

    return sorted(used), cost


def solve(N, M, limits, edges,max_lim):
  
  used, cost = prim(edges,limits,N,max_lim)

#   print(used, cost)

  return used


def read_input():
    N, M = [int(i) for i in input().split()]
    max_lim = (0,0)
    limits = {}
    for i in range(N):
        limits[i+1] = int(input())
        if limits[i+1] > max_lim[1]:
            max_lim = (i+1,limits[i+1])

    edge_count = {}
    for i in range(N):
        edge_count[i+1] = 0

    edges = defaultdict(list)
    for i in range(M):
        u, v, c = [int(i) for i in input().split()]
        # print(u,v,c)
        edges[u].append((c, v, u, i+1))
        edges[v].append((c, u, v, i+1))
        edge_count[u] += 1
        edge_count[v] += 1
    # print(N, M, limits, edges)

    max_ratio = (0,0)

    for i in range(1,N):
        ratio = edge_count[i] * limits[i]
        # print(ratio)
        if ratio > max_ratio[1]:
            max_ratio = (i,ratio)

    # print(max_ratio)


    
    return N, M, limits, edges, max_ratio


def main():
    N, M, limits, edges, max_lim = read_input()
    used = solve(N, M, limits, edges, max_lim)
    for edge in used:
        print(edge)


if __name__ == '__main__':
    main()