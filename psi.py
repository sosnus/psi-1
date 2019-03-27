import math
import numpy as np


### SETTINGS ###
np.random.seed(17503547) # Fixing random state for reproducibility
cities = 6 # how many cities
length = 100 # area where we have cities (map size)
roundCnt = 2 # round

A = np.random.randint(length, size=(cities, 2)) #generate cities
print(A)

B = np.zeros((cities, cities)) #generate array for storage length of routes


import matplotlib.pyplot as plt

plt.figure()
# Scatter plot on top of lines
plt.subplot(111)
plt.scatter(A[:,0], A[:,1], s=120, zorder=2)
plt.title('CITIES')
plt.tight_layout()
plt.savefig("test.png")


for i in range(cities):
    for j in range(i):
        B[i,j] = round(math.sqrt(math.pow((A[j,0]-A[i,0]),2)+math.pow((A[j,1]-A[i,1]),2)),roundCnt)

# show array with routes
print(B)



from queue import PriorityQueue

q=PriorityQueue();


for i in range(len(B)):
    for j in range(len(B)):
        if B[i][j] != 0:
            q.put((B[i][j], i, j))

def countNumber(b, a):
    z, x, y = list(zip(*b))
    return x.count(a) + y.count(a)


result=list();
result.append(q.get())




while not q.empty():
    tmp = q.get()


    if countNumber(result,tmp[1]) < 2  and countNumber(result,tmp[2]) < 2 :
        result.append(tmp)



s, k, l = list(zip(*result))

print(result)
print(sum(s))



plt.figure()
# Scatter plot on top of lines
plt.subplot(111)
plt.scatter(A[:,0], A[:,1], s=120, zorder=2)
for x in range(len (k)):
    plt.plot([A[k[x],0],A[l[x],0]],[A[k[x],1],A[l[x],1]])
plt.title('CITIES')
plt.tight_layout()
plt.savefig("test2.png")