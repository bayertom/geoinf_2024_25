from math import *
from time import *

def loadPoints(file):
    #Load file
    X, Y, Z = [], [], [] 
    
    with open(file) as f:
        
        for line in f:
            x, y, z = line.split('\t')
            
            X.append(float(x))
            Y.append(float(y))
            Z.append(float(z))
    
    return X, Y, Z

def  getNN(xq, yq, zq, X, Y, Z):
    #Find nearest point
    dmin = inf
    xn, yn, zn = X[0], Y[0], Z[0]
    
    for i in range(len(X)):
        #Compute distance
        dx = xq - X[i]
        dy = yq - Y[i]
        dz = zq - Z[i]
        d = (dx*dx + dy*dy + dz * dz)**0.5
        
        #Actualize minimum
        if d < dmin:
            dmin = d
            xn = X[i]
            yn = Y[i]
            zn = Z[i]
    return xn, yn, zn, dmin


def initIndex(X, Y, Z, nr):
    #Extreme values 
    xmin, xmax = min(X), max(X)
    ymin, ymax = min(Y), max(Y)
    zmin, zmax = min(Z), max(Z)
    
    #Minmax box dimensions
    dx = xmax - xmin
    dy = ymax - ymin
    dz = zmax - zmin

    #Cell sizes
    bx = dx / nr
    by = dy / nr
    bz = dz / nr
    
    return xmin, ymin, zmin, dx, dy, dz, bx, by, bz    
    
def get3DIndex(x,y,z,dx,dy,dz,nr):
    #Return 3d spatial index 
    xr=(x-xmin)/dx
    yr=(y-ymin)/dy
    zr=(z-zmin)/dz

    #spatial indexes
    c = 0.99
    jx = int(c*xr*nr)
    jy = int(c*yr*nr)
    jz = int(c*zr*nr)
    
    return jx, jy, jz

def hash(jx, jy, jz, nr):
    #Convert 3D to 1D index
    return jx + jy * nr + jz * nr**2

def indexPoints(X,Y,Z,xmin,ymin,zmin,dx,dy,dz):
    #Index point cloud
    H = {}
    
    for i in range(len(X)):
        #Compute 3D index
        jx, jy, jz = get3DIndex(X[i], Y[i], Z[i], dx, dy, dz, nr)
        
        #Compute hash
        j = hash(jx, jy, jz, nr)
        
        #Add to hash table
        if j in H:
            H[j] = [i]
        else:
            H[j].append(i)
    return H


#Load points
X, Y, Z = loadPoints('points3.txt')

#Initialize index
n = len(X)
nr = int(n**(1/9))
xmin, ymin, zmin, dx, dy, dz, bx, by, bz = initIndex(X, Y, Z, nr)

#3D index
x, y, z = 500, 500, 500
jx, jy, jz = get3DIndex(x,y,z,dx,dy,dz,nr)
j = hash(jx, jy, jz, nr)
print(j)

#Index point cloud
H = indexPoints(X, Y, Z, xmin, ymin, zmin, dx, dy, dz)

#NN search, v1
for i in range(len(X)):
    xn, yn, zn, dmin = getNN(X[i], Y[i], Z[i], X, Y, Z)

#NN search, v2
for i in range(len(X)):
    #3D index
    jx, jy, jz = get3DIndex(X[i], Y[i], Z[i],dx,dy,dz,nr)
    
    #Hash
    j = hash(jx, jy, jz, nr)
    
    #Indices of points
    ixd = H[j]
    
    #Convert idx to coordinates (TBD)
    #XC = 
    #YC = 
    #ZC = 
    
    #xn, yn, zn, dmin = getNN(X[i], Y[i], Z[i], XC, YC, ZC)
    
