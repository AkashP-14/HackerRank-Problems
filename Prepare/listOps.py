N = int(input())
liSt = list()
for _ in range(N):
    command = input().strip().split(" ")
    if command[0]=="insert":
        liSt.insert(int(command[1]),int(command[2]))
    if command[0]=="print":
        print(liSt)
    if command[0]=="remove":
        liSt.remove(int(command[1]))
    if command[0]=="append":
        liSt.append(int(command[1]))
    if command[0]=="sort":
        liSt.sort()
    if command[0]=="pop":
        liSt.pop()
    if command[0]=="reverse":
        liSt.reverse()