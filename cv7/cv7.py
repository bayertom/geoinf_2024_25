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