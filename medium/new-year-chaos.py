def minimumBribes(q):
    # Write your code here
    swaps = 0
    for i in reversed(range(len(q))):
        if q[i] != i + 1:
            if i - 1 >= 0 and q[i - 1] == i + 1:
                q[i], q[i-1] = q[i-1], q[i]
                swaps += 1
            elif i - 2 >= 0 and q[i - 2] == i + 1:
                q[i], q[i-1], q[i-2] = q[i-2], q[i], q[i-1]
                swaps += 2
            else:
                print("Too chaotic")
                return
    print(swaps)


q = [2, 1, 5, 3, 4]

minimumBribes(q)