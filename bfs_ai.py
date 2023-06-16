from queue import PriorityQueue
v = 12
graph = [[] for i in range(v)]

def best_first_search(actual_Src, target, n):
	visited = [False] * n
	pq = PriorityQueue()
	pq.put((0, actual_Src))
	visited[actual_Src] = True
	ans=[]
	while pq.empty() == False:
		u = pq.get()[1]
		# Displaying the path having lowest cost
		ans.append(u)
		if u == target:
			break

		for v, c in graph[u]:
			if visited[v] == False:
				visited[v] = True
				pq.put((c, v))
	return ans
    

# Function for adding edges to graph
def addedge(x, y, cost):
	graph[x].append((y, cost))
	graph[y].append((x, cost))


# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,heuristic cost);
addedge(0, 1, 168)
addedge(0, 2, 163)
addedge(0, 3, 189)
addedge(1, 4, 133)
addedge(2, 5, 144)
addedge(3, 6, 151)
addedge(4, 7, 90)
addedge(4, 8, 91)
addedge(5, 7, 90)
addedge(6, 9, 126)
addedge(7, 11, 0)
addedge(8, 11, 0)
addedge(9, 10, 72)
addedge(10, 11, 0)

source = 0
target = 11

d={0:'VITC',
2:'KASBAPURAM',
1:'VANDALUR',
3:'PERUMBAKKAM',
5:'SELAIYUR',
4:'TAMBARAM',
6:'MEDAVAKKAM',
7:'CHROMEPET',
8:'TIRUSULAM',
9:'KOVILAMBAKKAM',
10:'PALLAVARAM',
11:'CHENNAI_AIRPORT'}
l=best_first_search(source, target, v)
for i in l:
    print(d[i],end=' -> ')

