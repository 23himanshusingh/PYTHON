from queue import PriorityQueue
pipes=PriorityQueue()
n=int(input());sum=0
for i in range(n):
    pipes.put(int(input()))
while pipes.qsize()>1:
    p1=pipes.get(0)
    P2=pipes.get(0)
    sum=sum+(p1+p2)
    pipes.put(p1+p2)
if pipes.qsize()>1:
    print(sum)
else:
    print(pipes.get(0))
