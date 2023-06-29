#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
from random import randint, choice
import matplotlib.pyplot as plt
from math import dist

def tetrominoes1(grid,row,col):
    grid[row:row+4,col] = 1
def tetrominoes2(grid,row,col):
    try:
        grid[row,col] = 1
        grid[row:row+3,col+1] = 1
    except:pass
def tetrominoes3(grid,row,col):
    try:
        grid[row:row+2,col] = 1
        grid[row+1:row+3,col+1] = 1
    except: pass
def tetrominoes4(grid,row,col):
    grid[row+1,col] = 1
    grid[row:row+2,col+1] = 1

def environ(coverage):
    grid = np.zeros((128,128))  #Black originally
    final_cov = 0
    while (final_cov<coverage):
        #for i in range(int(num)):
            row = randint(0,127)
            col = randint(0,127)        
            obstacle_shape = randint(1,4)
            if obstacle_shape == 1:
                tetrominoes1(grid,row,col)
            elif obstacle_shape == 2:
                tetrominoes2(grid,row,col)
            elif obstacle_shape == 3:
                tetrominoes3(grid,row,col)
            elif obstacle_shape == 4:
                tetrominoes3(grid,row,col)
            counter = np.sum(grid)
            final_cov = ((counter)/(128*128))*100
    return grid

grid = environ(10)
plt.imshow(grid,cmap ='gray')
#plt.grid()
plt.show()


# In[31]:


def isValid(grid,vis, row, col):
   
    # If cell lies out of bounds
    if (row < 0 or col < 0 or row > 127 or col > 127):
        return False
    
    if (grid[row][col] == 1):
        return False
 
    # If cell is already visited
    if (vis[row][col]):
        return False
 
    # Otherwise
    return True

def BFS(grid,goal,row, col):
    n = 0
    dRow = [ -1, 0, 1, 0]
    dCol = [ 0, 1, 0, -1]
    vis = [[ False for i in range(len(grid))] for i in range(len((grid)))]                                                         
    # Stores indices of the matrix cells
    q = []
 
    # Mark the starting cell as visited
    # and push it into the queue
    q.append(( row, col,[]))
    vis[row][col] = True
 
    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        n += 1
        cell = q.pop(0)
        x = cell[0]
        y = cell[1]
        path = cell[2]
        
         
        #q.pop()
        if goal == [x,y]:
            return n,path
 
        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i] #neighbor
            adjy = y + dCol[i]
            if (isValid(grid,vis, adjx, adjy)):
                q.append((adjx, adjy,path + [[x,y]]))
                vis[adjx][adjy] = True
                
        #print("path",path)
    return n,None

            
goal = [127,127]
n1,path1 = BFS(grid, goal, 0, 0)
#print(path1)
path1 = np.array(path1)
plt.imshow(grid,cmap ='gray')
plt.plot(path1[:,1],path1[:,0])
plt.show()


# In[33]:


def DFS(grid,goal,row, col):
    n = 0
    dRow = [ -1, 0, 1, 0]
    dCol = [ 0, 1, 0, -1]
    vis = [[ False for i in range(len(grid))] for i in range(len((grid)))]                                                         
    # Stores indices of the matrix cells
    q = []
 
    # Mark the starting cell as visited
    # and push it into the queue
    q.append(( row, col,[]))
    vis[row][col] = True
 
    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        n += 1
        cell = q.pop()
        x = cell[0]
        y = cell[1]
        path = cell[2]
        
         
        #q.pop()
        if goal == [x,y]:
            return n,path
 
        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i] #neighbor
            adjy = y + dCol[i]
            if (isValid(grid,vis, adjx, adjy)):
                q.append((adjx, adjy,path + [[x,y]]))
                vis[adjx][adjy] = True
    return n, None
                
goal = [127,127]
n2,path2 = DFS(grid, goal, 0, 0)
path2 = np.array(path2)
plt.imshow(grid,cmap = 'gray')
plt.plot(path2[:,1],path2[:,0])
plt.show()


# In[34]:


def Dij(grid,goal,row, col):
    n = 0
    dRow = [ -1, 0, 1, 0,1,1,-1,-1]
    dCol = [ 0, 1, 0, -1,1,-1,1,-1]
    vis = [[ False for i in range(len(grid))] for i in range(len((grid)))]                                                         
    # Stores indices of the matrix cells
    q = []
 
    # Mark the starting cell as visited
    # and push it into the queue
    q.append(( row, col,[],0))
    vis[row][col] = True
 
    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        n+=1
        cell = q.pop(0)
        x = cell[0]
        y = cell[1]
        path = cell[2]
        cost = cell[3]
         
        #q.pop()
        if goal == [x,y]:
            return n,path
 
        # Go to the adjacent cells
        for i in range(8):
            adjx = x + dRow[i] #neighbor
            adjy = y + dCol[i]
            current = [x,y]
            if (isValid(grid,vis, adjx, adjy)):
                q.append((adjx, adjy,path + [[x,y]],cost + dist(current,[adjx,adjy]) ))
                q = sorted(q, key = lambda x: x[3])
                vis[adjx][adjy] = True
    return n, None

goal = [127,127]
n3,path3 = Dij(grid, goal, 10, 0)
path3 = np.array(path3)
plt.imshow(grid,cmap='gray')
plt.plot(path3[:,1],path3[:,0])
plt.show()
    
    
    


# In[35]:


def neighbors_4(grid,vis,x,y):
        neighbor = []

        if (x > 0) and (grid[x-1][y] == 0) and ([x-1,y] not in vis):
            neighbor.append([x-1, y])
        if (y > 0) and (grid[x][y-1] == 0) and ([x,y-1] not in vis):
            neighbor.append([x, y-1])
        if (x < 127) and (grid[x+1][y] == 0) and ([x+1,y] not in vis):
            neighbor.append([x+1, y])
        if (y < 127) and (grid[x][y+1] == 0) and ([x,y+1] not in vis):
            neighbor.append([x, y+1])

        return neighbor

def random_search(grid, goal, row, col):
        n = 0
        path =  []
        neighbor = [row,col]
        vis = [[ False for i in range(len(grid))] for i in range(len((grid)))]  
    
        while neighbor and n <= 128*128*2:
            n += 1
            current = neighbor
            x,y = current
            vis[x][y] = True
            path.append(current)
            if current == goal:
                return n,path

            neighbor = neighbors_4(grid,vis,x,y)
            if neighbor:
                neighbor = choice(neighbors_4(grid,vis,x,y))
            while not neighbor:
                path.pop()
                if not path:
                    break
                x,y = path[-1]
                neighbor = neighbors_4(grid,vis,x,y)
                if neighbor:
                    neighbor = choice(neighbors_4(grid,vis,x,y))

        return n,None

goal = [127,127]
n4,path4 = random_search(grid, goal, 0, 0)
path4 = np.array(path4)
plt.imshow(grid,cmap='gray')
plt.plot(path4[:,1],path4[:,0])
plt.show()


# In[22]:


size = 128
density = [*range(0,76,10)]

row = 0
col = 0
goal = [size-1, size-1]

m1 = []
m2 = []
m3 = []
m4 = []

#Plot density vs iteration

for i in range(len(density)):
    grid = environ(density[i])

    i1, path1 = DFS(grid, goal, row, col)
    i2, path2 = BFS(grid, goal, row, col)
    i3, path3 = random_search(grid, goal, row, col)
    i4, path4 = Dij(grid, goal, row, col)

    m1.append(i1)
    m2.append(i2)
    m3.append(i3)
    m4.append(i4)

plt.figure()
plt.plot(density,m1,label="DFS")
plt.plot(density,m2,label="BFS")
plt.plot(density,m3,label="Random")
plt.plot(density,m4,label="Djsktra")

plt.xlabel("Densities")
plt.ylabel("Iterations")
plt.legend(loc = "upper right")

# Paths for Density = 10 #

grid = environ(10)
i1, path1 = DFS(grid, goal, row, col)
i2, path2 = BFS(grid, goal, row, col)
i3, path3 = random_search(grid, goal, row, col)
i4, path4 = Dij(grid, goal, row, col)

plt.figure()
plt.imshow(grid, cmap='gray_r')
if path1:
    path1 = np.array(path1)
    plt.plot(path1[:,1],path1[:,0],label="DFS")
else: print("No Path found for DFS")

if path2:
    path2 = np.array(path2)
    plt.plot(path2[:,1],path2[:,0],label="BFS")
else: print("No Path found for BFS")

if path3:
    path3 = np.array(path3)
    plt.plot(path3[:,1],path3[:,0],label="Random")
else: print("No Path found for Random")

if path4:
    path4 = np.array(path4)
    plt.plot(path4[:,1],path4[:,0],label="Dijsktra")
else: print("No Path found for Dijkstra")

plt.title("Grid Coverage rate of {}".format(10))
plt.legend(loc = "upper right")

# Paths for Density = 15 #

grid = environ(15)
i1, path1 = DFS(grid, goal, row, col)
i2, path2 = BFS(grid, goal, row, col)
i3, path3 = random_search(grid, goal, row, col)
i4, path4 = Dij(grid, goal, row, col)

plt.figure()
plt.imshow(grid, cmap='gray_r')
if path1:
    path1 = np.array(path1)
    plt.plot(path1[:,1],path1[:,0],label="DFS")
else: print("No Path found for DFS")

if path2:
    path2 = np.array(path2)
    plt.plot(path2[:,1],path2[:,0],label="BFS")
else: print("No Path found for BFS")

if path3:
    path3 = np.array(path3)
    plt.plot(path3[:,1],path3[:,0],label="Random")
else: print("No Path found for Random")

if path4:
    path4 = np.array(path4)
    plt.plot(path4[:,1],path4[:,0],label="Dijsktra")
else: print("No Path found for Dijkstra")

plt.title("Grid Coverage rate of {}".format(15))
plt.legend(loc = "upper right")


# Paths for Density = 20 #

grid = environ(25)
i1, path1 = DFS(grid, goal, row, col)
i2, path2 = BFS(grid, goal, row, col)
i3, path3 = random_search(grid, goal, row, col)
i4, path4 = Dij(grid, goal, row, col)

plt.figure()
plt.imshow(grid, cmap='gray_r')
if path1:
    path1 = np.array(path1)
    plt.plot(path1[:,1],path1[:,0],label="DFS")
else: print("No Path found for DFS")

if path2:
    path2 = np.array(path2)
    plt.plot(path2[:,1],path2[:,0],label="BFS")
else: print("No Path found for BFS")

if path3:
    path3 = np.array(path3)
    plt.plot(path3[:,1],path3[:,0],label="Random")
else: print("No Path found for Random")

if path4:
    path4 = np.array(path4)
    plt.plot(path4[:,1],path4[:,0],label="Dijsktra")
else: print("No Path found for Dijkstra")

plt.title("Grid Coverage rate of {}".format(25))
plt.legend(loc = "upper right")


# In[71]:


density


# In[ ]:





# In[ ]:





# In[ ]:


def random(grid,goal,row, col):
    n = 0
    dRow = [ -1, 0, 1, 0]
    dCol = [ 0, 1, 0, -1]
    vis = [[ False for i in range(len(grid))] for i in range(len((grid)))]                                                         
    # Stores indices of the matrix cells
    q = []
 
    # Mark the starting cell as visited
    # and push it into the queue
    q.append(( row, col,[]))
    vis[row][col] = True
 
    # Iterate while the queue
    # is not empty
    while (len(q) > 0) and n < 128*128*3:
        n+=1
        cell = q.pop()
        x = cell[0]
        y = cell[1]
        path = cell[2]
    
         
        #q.pop()
        if goal == [x,y]:
            return n,path
        
        valid = True
        while valid:
            neighbor = []
            for i in range (4):
            # Go to the adjacent cells
                adjx = x + dRow[i] #neighbor
                adjy = y + dCol[i]
                neighbor.append([adjx,adjy])
            if neighbor: neighbor = choice(neighbor) 
            while not neighbor:
                path.pop()
                if not path:
                    break
                x,y = path[-1]
                for i in range (4):
                    # Go to the adjacent cells
                    adjx = x + dRow[i] #neighbor
                    adjy = y + dCol[i]
                    neighbor.append([adjx,adjy])
                if neighbor: neighbor = choice(neighbor) 

            adjx,adjy = neighbor
            if (isValid(grid,vis, adjx, adjy)):
                q.append((adjx, adjy,path + [[x,y]]))
                vis[adjx][adjy] = True
                valid = False
    return n, None
            
goal = [127,127]
n4,path4 = random(grid, goal, 10, 0)
path4 = np.array(path4)
print(path4)
plt.imshow(grid,cmap='gray')
plt.plot(path4[:,1],path4[:,0])
plt.show()


# In[ ]:


#queue = []
#visited = []

#def bfs(start,goal,grid): #function for BFS
   # visited.append(start)
   # for neighbors in range:

    #while queue:          # Creating loop to visit each node
    #    next = queue.pop(0) 
      #  print (m, end = " ") 

   # for neighbour in grid[m]:
     #   if neighbour not in visited:
   #         visited.append(neighbour)
   #         queue.append(neighbour)
  #  return 

# Driver Code
#print("Following is the Breadth-First Search")
#bfs(grid[0,0], grid[127,127], '5')    # function calling


# In[ ]:





# In[ ]:


x.grid(True)
pyplot.imshow(x)


# In[ ]:




