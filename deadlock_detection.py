def find_safe_sequence():
    # P0, P1, P2, P3, P4 are the Process names here

    n = int(input("Enter the number of processes")) # Number of processes
    m = int(input("Enter the number of resources"))# Number of resources
    # Total Number of Resources
    r = []
    for i in range(m):
        r.append(int(input(f"Total Amount of the Resource R{i+1}: ")))
    
    # Allocation Matrix
    alloc = []
    print("\nEnter the allocation matrix:")
    for i in range(n):
        alloc.append([int(x) for x in input().split()])
    # MAX Matrix
    max_need = []
    print("\nEnter the Maximum matrix:")
    for i in range(n):
        max_need.append([int(x) for x in input().split()])
    # Available Resources
    avail = r[:]
    for i in range(n):
        for j in range(m):
            avail[j] -= alloc[i][j]

    f = [0] * n
    ans = [-1] * n
    ind = 0

    # Calculate Need Matrix
    need = [[max_need[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            if f[i] == 0:
                flag = True
                for j in range(m):
                    if need[i][j] > avail[j]:
                        flag = False
                        break

                if flag:
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1

    safe_sequence = all(f[i] == 1 for i in range(n))

    if not safe_sequence:
        print("DEADLOCK POSSIBLE")
    else:
        print("Following is the SAFE Sequence")
        print(" -> ".join(f"P{ans[i]}" for i in range(n)))
        print("So deadlock is not possible")

if __name__ == "__main__":
    find_safe_sequence()
