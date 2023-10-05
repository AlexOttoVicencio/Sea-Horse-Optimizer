import numpy as np
import random

#----STARTING PARAMETERS

LB=-100
UB=100
Dim=30
Pop=10
popsize=30;
iterations=500   

#--------------FUNCTIONS--------------------------------------

#OBJ functions-.------

#Sphere
def sphere_optimization(seahorses_copy):

    seahorses_copy=np.power(seahorses_copy,2)
    num_rows, num_cols = seahorses_copy.shape
    minimum_result=300001
    elite_seahorse=0
    print(seahorses_copy[0,:])
    for x in range (0,num_rows):
     print(np.sum(seahorses_copy[x,:]))
     if np.sum(seahorses_copy[x,:])<minimum_result :
        minimum_result=np.sum(seahorses_copy[x,:])
        elite_seahorse=x
    print("the elite seahorse is: " , minimum_result)
    print("the index is: ",elite_seahorse)

#----------

#FIND ELITE SEAHORSE

def elite_seahorse(seahorses):
#    print("los caballos------------------")
#    print(seahorses)
#    print("-------------------------------------------------------------")
    seahorses_copy= np.copy(seahorses)
    best_seahorse=sphere_optimization(seahorses_copy)
    
    

#----------------ALGORITHM---------------------------

#initializing array and values

seahorses = np.zeros((Pop,Dim))

#Fill with values between bounds
with np.nditer(seahorses, op_flags=['readwrite']) as it:
   i=1
   for x in it:

       x[...] = random.uniform(0,1) * (UB-LB) + LB
#find elite seahores

elite_seahorse(seahorses)








