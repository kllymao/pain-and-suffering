def read_input():
    N, M = [int(i) for i in input().split()]
    bounds = [int(input()) for _ in range(N)]
    edges = [[int(i) for i in input().split()] for _ in range(M)]
    return N, M, bounds, edges

def main():
    N, M, bounds, edges = read_input()
    print(N, M, bounds, edges)

if __name__ == '__main__':
    main()