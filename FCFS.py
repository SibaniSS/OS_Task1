n= int(input("Enter number of processes : "))
d = dict()
 
for i in range(n):
    key = "P"+str(i+1)
    a = int(input("Enter arrival time of process"+str(i+1)+": "))
    b = int(input("Enter burst time of process"+str(i+1)+": "))
    l = []
    l.append(a)
    l.append(b)
    d[key] = l
 
d = sorted(d.items(), key=lambda item: item[1][0])
 
exitime = []
for i in range(len(d)):
    # first process
    if(i==0):
        exitime.append(d[i][1][1])
 
    # get prevET + newBT
    else:
        exitime.append(exitime[i-1] + d[i][1][1])
 
TAT = []
for i in range(len(d)):
    TAT.append(exitime[i] - d[i][1][0])
 
Waitingtime = []
for i in range(len(d)):
    Waitingtime.append(TAT[i] - d[i][1][1])
 
avg_WT = 0
for i in Waitingtime:
    avg_WT +=i
avg_WT = (avg_WT/n)
 
for i in range(n):
    print(f"Process: {d[i][0]}")
    print(f"Arrival: {d[i][1][0]}")
    print(f"Burst: {d[i][1][1]}")
    print(f"Exit: {exitime[i]}")
    print(f"Turn Around: {TAT[i]}")
    print(f"Wait: {Waitingtime[i]}")
    print("-" * 30)

print(f"Average Waiting Time: {avg_WT:.2f}")
