X = [1, 4, 58, 17, -9]

for i in range(len(X)):
    print(X[i])
    

for x in X:
    print(x) 
    


WM = [3.9, 2.7, 4.2, 2.5, 1.8, 4.6]

#Initialize minimum
wm_min = WM[0]

#Initialize maximum
wm_max = WM[0]

#Process all items one by one
for wm in WM:
    
    #Actualize minimum
    if wm < wm_min: 
        wm_min = wm
        
    #Actualize maximum
    if wm > wm_max:
        wm_max = wm

print('Minimum:', wm_min)    
print('Maximum:', wm_max)   

WM = [3.9, 2.7, 4.2, 2.5, 1.8, 4.6]

#Initialize minimum
wm_min = WM[0]

#Initialize maximum
wm_max = WM[0]

#Index minimum
i_min = 0
#Index maximum
i_max = 0

#Process all items one by one
for i in range(len(WM)):
    
    #Actualize minimum
    if WM[i] < wm_min: 
        wm_min = WM[i]
        i_min = i
        
    #Actualize maximum
    if WM[i] > wm_max: 
        wm_max = WM[i]
        i_max = i

print('Minimum:', wm_min)
print("Minimum_index",i_min)    
print('Maximum:', wm_max)
print("Maximum_index",i_max)    

def findMinMaxWM(WM):
    
    #Initialize minimum
    wm_min = WM[0]

    #Initialize maximum
    wm_max = WM[0]

    #Index minimum
    i_min = 0
    #Index maximum
    i_max = 0

    #Process all items one by one
    for i in range(len(WM)):
        
        #Actualize minimum
        if WM[i] < wm_min: 
            wm_min = WM[i]
            i_min = i
            
        #Actualize maximum
        if WM[i] > wm_max: 
            wm_max = WM[i]
            i_max = i

    return wm_min, wm_max, i_min, i_max

wm_min, wm_max, i_min, i_max = findMinMaxWM(WM)
print('Minimum:', wm_min)
print("Minimum_index",i_min)    
print('Maximum:', wm_max)
print("Maximum_index",i_max)  
