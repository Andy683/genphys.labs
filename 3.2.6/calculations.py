from math import log

r0 = 610

def f(r):
    return 1.5 * (1/2000) * (1/(r0+1000*r))

resistance = [3,3.5,4,4.5,5,6,7,10,15,20]
x = [24.5,20.6,17.8,15.6,13.9,11.4,9.7,6.1,4.5,3.2]

file = open("data_dynamic",'w')

for i in range(len(resistance)):
    file.write(str(x[i])+' '+str(round(f(resistance[i])*10**8))+'\n')
    #print(" & "+str(round(f(resistance[i])*10**8)),end="")

file.close()

file = open("data_critical",'w')

x = [[16.9 , 14.5 , 12.4 , 10.5],
     [12.7 , 10.6 , 9.0 , 7.6],
     [10.2 , 8.5 , 7.6 , 6.0],
     [8.5 , 7.1 , 6.0 , 5.1],
     [6.4 , 5.5 , 4.6 , 3.9],
     [5.2 , 4.4 , 3.8 , 3.3]]
resistance = [21,28,35,42,56,70]

for i in range(len(x)):
    s = 0.0
    for j in range(len(x[i])-1):
        s += log(x[i][j]/x[i][j+1])
    s /= float(len(x[i])-1)
    dy = round(1/(s**2),1)  # 1/theta^2
    dx = (resistance[i]*1000+r0)**2
    file.write(str(dx/10**9)+' '+str(dy)+'\n')
    
file.close()

file = open("data_ballistic",'w')

r0 = 56
resistance = [2,4,8,12,16]
x = [5.2,9.5,12,14.5,14.5]

for i in range(len(x)):
    file.write(str(round(1/(resistance[i]+r0),4))+' '+str(x[i])+'\n')

file.close()
