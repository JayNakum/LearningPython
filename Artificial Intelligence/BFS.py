# adj = {
#     'a' : {'b','c'},
#     'b' : {'d','e','a'},
#     'c' : {'d','g','a'},
#     'd' : {'b','c','f'},
#     'e' : {'b'},
#     'f' : {'d','h','g'},
#     'g' : {'c','f'},
#     'h' : {'f'}
# }

adj = {
    'a' : {'b','c','d'},
    'b' : {'a','e','f'},
    'c' : {'a','g','h'},
    'd' : {'a','i'},
    'e' : {'b','j','k'},
    'f' : {'b'},
    'g' : {'c','l'},
    'h' : {'c'},
    'i' : {'d','m'},
    'j' : {'e'},
    'k' : {'e','n'},
    'l' : {'g'},
    'm' : {'i'},
    'n' : {'k'}
}

goal = 'g'

visited = {k : False for k in adj.keys()}

path = []
def calculatePath(front:int, queue:list):
    print(queue[front], end='-')
    for i in range(front, 0, -1):
        if queue[i] in adj[queue[front]]:
            path.append(queue[i])
            calculatePath(i, queue)

def BFS(start:str) -> list:
    queue = []
    front = 0

    queue.append(start)
    visited[start] = True

    while ((front >= len(queue)) or (queue[front] != goal)):
        v = queue[front]
        front += 1
        for neighbor in adj[v]:
            if (not visited[neighbor]):
                queue.append(neighbor)
                visited[neighbor] = True
    print('PATH: ', end='')
    calculatePath(front, queue)
    print(start)

BFS('a')
