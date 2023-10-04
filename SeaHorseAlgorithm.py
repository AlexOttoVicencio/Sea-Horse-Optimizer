import numpy as np
import random

#Sphere obj funtion parameters
#falta escribir las sumatoria de la esfera
LB=-100
UB=100
Dim=30
Pop=10

popsize=30;
iterations=500   
seahorses = np.zeros((Pop,Dim))
print(seahorses)




#--------------FUNCTIONS--------------------------------------


#FIND ELITE SEAHORSE

def elite_seahorse(seahorses):
    print("los caballos")
    print(seahorses)    









#Fill with values between bounds
with np.nditer(seahorses, op_flags=['readwrite']) as it:
   i=1
   for x in it:

       x[...] = random.uniform(0,1) * (UB-LB) + LB
#find elite seahores


elite_seahorse(seahorses)


#initializing array and values





