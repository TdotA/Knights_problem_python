test_position = [[1,1,1],[0,0,0],[0,0,0],[-1,-1,-1]]
desired  = [[-1,-1,-1],[0,0,0],[0,0,0],[1,1,1]]

def possible_moves(i,j,n,m):
    l=[]
    if i +2< n and j > 0:
        l.append((i+2, j-1))
    if i +2< n and j+1<m:
        l.append((i+2, j+1))
    if i>=2 and j > 0:
        l.append((i-2, j-1))
    if i>=2 and j+1<m:     
        l.append((i-2, j+1))  
    
    if j +2< m and i > 0:
        l.append((i-1, j+2))
    if j +2< m and i+1<n:
        l.append((i+1, j+2))
    if j>=2 and i > 0:
        l.append((i-1, j-2))
    if j>=2 and i+1<n:     
        l.append((i+1, j-2))      
    return l

def possible_moves_advanced(i,j,n,m,table):
    l =[]
    s = possible_moves(i,j,n,m)
    for i in s:
        j = i[0]
        k = i[1]
        if table[j][k]!= 0:
            continue
        else:
            l.append(i)
    return l 

def copy_matrix(mat):
    m=[]
    for i in mat:
        l = []
        for k in i: 
            l.append(k)
        m.append(l)
    return m

def moves(mat): 
    #print_board(mat)
    n = len(mat)
    m = len(mat[0])
    l = []

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                continue
            else: 
                for k in possible_moves_advanced(i,j,n,m,mat):
                    #print(k)
                    new = copy_matrix(mat)
                    val = new[i][j]
                    new[i][j] = 0
                    new[k[0]][k[1]] = val
                    l.append(new)
    return l 

def print_board(mat):
    for i in range(len(mat)):
        line= ''
        for j in range(len(mat[0])):
            
            if mat[i][j] == 1:
                line = line + 'B'
            if mat[i][j] == 0:
                line += '.'
            if mat[i][j] == -1:
                line+= 'W'
        print(line)

def tupleup(l):
    m = tuple([tuple(x) for x in l])
    return m         

def makedict(mat):
    d = {tupleup(mat):0}
    parent = {tupleup(mat): None}
    todo = [mat]
    while todo != []: 
        y = todo.pop(0)
        for x in moves(y):
            if not tupleup(x) in d:
                todo.append(x)
                d[tupleup(x)] = d[tupleup(y)]+1
                parent[tupleup(x)] = tupleup(y) 
    return d, parent

d, parent = makedict(test_position)


for i in d: 
    if i == tupleup(desired):
        print(i)
        print(d[i])

i = tupleup(desired) 

while i != tupleup(test_position):
    print_board(i)
    print()
    i = parent[i]
print_board(test_position)
    
