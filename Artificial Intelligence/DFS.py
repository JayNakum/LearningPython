# adj = {
#     'a' : {'e','b','g'},
#     'b' : {'a','h','g','f','c'},
#     'c' : {'b','h','d'},
#     'd' : {'c','e'},
#     'e' : {'a','d','f'},
#     'f' : {'e','b'},
#     'g' : {'a','b'},
#     'h' : {'b','c'}
# }

adj = {
    'a' : {'d','b'},
    'b' : {'f','c'},
    'c' : {'e','g','h'},
    'd' : {'f'},
    'e' : {'b','f'},
    'f' : {'a'},
    'g' : {'e','h'},
    'h' : {'a'}
}

goal = 'g'
visited = {k : False for k in adj.keys()}
path = []
stack = []

def DFS(node):
    if (node == goal):
        return path
    else:
        stack.append(node)
        if (not visited[node]):
            visited[node] = True
            path.append(node)
        print(node, end=' ')
        popCounter = 0
        for v in adj[node]:
            if (not visited[v]):
                DFS(v)
            else:
                popCounter += 1
        if (popCounter == len(adj[node])):
            stack.pop()
            DFS(stack.pop())
        
DFS('a')
print('\nPATH:', end=' ')
for p in path:
    print(p, end='-')
print(goal)
