#Graph definition
G = {
    1 : [2, 3, 5],
    2 : [1, 3, 4, 7, 8],
    3 : [1, 2, 6, 7],
    4 : [2, 9],
    5 : [1, 6],
    6 : [3, 5, 7, 8, 9],
    7 : [2, 3, 6, 8],
    8 : [2, 6, 7, 9],
    9 : [4, 6, 8]
}

#Coordinates X, Y
C = {
    1 : [95, 322],
    2 : [272, 331],
    3 : [173, 298],
    4 : [361, 299],
    5 : [82, 242],
    6 : [163, 211],
    7 : [244, 234],
    8 : [333, 225],
    9 : [412, 196]
}

def BFS(G,u):
    
    #Input data structures
    n = len(G)
    P = [-1]*(n+1)
    S = [0]*(n+1)
    Q = []
    
    #Starting node change status
    S[u] = 1
    
    #Add u to Q
    Q.append(u)
    
    # Until Q is empty
    while Q:
        # Remove first node
        u = Q.pop(0)
        S[u] = 1
        
        # Iterate through neighbours
        for v in G[u]:
            #Is node new
            if S[v] == 0:
                S[v] = 1
                P[v] = u
                Q.append(v)
                
        #Close node
        S[u] = 2
        
    return P


def DFS(G,u):
    
    #Input data structures
    n = len(G)
    P = [-1]*(n+1)
    S = [0]*(n+1)
    St = []  #Stack
    
    #Starting node change status
    S[u] = 1
    
    #Add u to St
    St.append(u)
    
    # Until Q is empty
    while St:
        # Remove first node
        u = St.pop()
        
        #Change status
        S[u] = 1
        
        # Iterate through neighbours
        for v in reversed(G[u]):

            #Is node new
            if S[v] == 0:
                S[v] = 1
                P[v] = u
                St.append(v)
                
        #Close node
        S[u] = 2
        
    return P


def rec(u,v,P):
    path = []
    
    # Path shortening
    while v != u and v !=-1:
        path.append(v)
        v = P[v]
        
    path.append(v)
    if v != u:
        print('Incorrect path')
    return (path)
  
#Run BFS
P = BFS(G, 2)    
print(P)

#Backward path reconstruction
path = rec(2, 9, P)
print(path)

P = DFS(G, 1)    
print(P)

#Backward path reconstruction
path = rec(1, 4, P)
print(path)
        
                
                
            