from collections import deque

def an_ancient_ordering():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        words.append(word)


    used = set()
    for i in words:
        for j in i:
            used.add(j)

    adj = [[] for i in range(26)]
    indeg = [0] * 26

    for i in range(n-1):
        w1, w2 = words[i], words[i+1]
        minlen = min(len(w1), len(w2))
        found = False
        for j in range(minlen):
            if w1[j] != w2[j]:
                u, v = ord(w1[j])-ord('a'), ord(w2[j])-ord('a')
                if v not in adj[u]:
                    adj[u].append(v)
                    indeg[v] += 1
                found = True
                break
        if not found and len(w1) > len(w2):
            print(-1)
            return


    result = []
    used_idx = []
    for c in used:
        used_idx.append(ord(c)-ord('a'))
    used_idx.sort()


    queue = deque()
    for i in used_idx:
        if indeg[i] == 0:
           queue.append(i)

    while queue:
        temp = queue.popleft()
        result.append(chr(temp + ord('a')))
        for neighbour in adj[temp]:
            indeg[neighbour] -= 1
            if indeg[neighbour] == 0:
                queue.append(neighbour)
        queue = deque(sorted(queue))

    if len(result) != len(used):
        print(-1)
    else:
        print("".join(result))

an_ancient_ordering()
