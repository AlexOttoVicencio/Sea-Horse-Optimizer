import numpy as np
import random
import math
#----STARTING PARAMETERS

LB=-100
UB=100
Dim=2
Pop=5
popsize=30;
iterations=5  
current_iteration=0
#--------------FUNCTIONS--------------------------------------

#OBJ functions-.------

#Sphere
def sphere_optimization(seahorses_copy):

#elevamos los caballos y buscamos el menor
    seahorses_copy=np.power(seahorses_copy,2)
    num_rows, num_cols = seahorses_copy.shape
    minimum_result=300001
    elite_seahorse=0
    
    for x in range (0,num_rows):
     print(np.sum(seahorses_copy[x,:]))
     if np.sum(seahorses_copy[x,:])<minimum_result :
        minimum_result=np.sum(seahorses_copy[x,:])
        elite_seahorse=x
    print("the elite seahorse is: " , minimum_result)
    print("the index is: ",elite_seahorse)

    return elite_seahorse

#----------

#FIND ELITE SEAHORSE

def elite_seahorse(seahorses):

    seahorses_copy= np.copy(seahorses)
    best_seahorse=sphere_optimization(seahorses_copy)
    return best_seahorse
    
    
#-----------------------

#LEVY FUNCTION

def levy_function():
    
    lambd = 1.5
    s=0.01
    w=random.uniform(0,1)
    k=random.uniform(0,1)
    sigma=(math.gamma(lambd+1)*math.sin(math.pi*lambd))/(math.gamma((lambd+1)/2)*lambd*(pow(2,((lambd-1)/2))))
    levy_value=s*((w*sigma)/abs(pow(k,(1/lambd))))
    return levy_value
   





#----------------ALGORITHM---------------------------

#initializing array and values

seahorses = np.zeros((Pop,Dim))

#Fill with values between bounds
with np.nditer(seahorses, op_flags=['readwrite']) as it:
   i=1
   for x in it:
       
       x[...] = random.uniform(0,1) * (UB-LB) + LB


print("----------SEAHORSES-----------------")
print(seahorses)
print("-------------------------------------------")
#getting elite index and an array of fitness values

best_seahorse_index = elite_seahorse(seahorses)




while current_iteration<iterations :
    r=random.uniform(-1,1)
    
    #levy value
    step_lenght=levy_function()
    print("levy value is: ",step_lenght)

    num_rows, num_cols = seahorses.shape

#first it goes through every row and decides wether to change them with levy or the brownian movement
    
    if(r>0):
        u=0.05
        v=0.05
        theta=random.uniform(0,2*math.pi)   
        p=u*pow(math.e,(theta*v))
        x=p*math.cos(theta)
        y=p*math.sin(theta)
        z=p*theta
        print("theta: ",theta)
        print("p: " , p)
        print("x: ",x)
        print("y: ",z)
        print("z: ",z)

        #4th eq is applied
        for row in range (0,num_rows):
            for column in range (0,num_cols): 
             print("seahorse: " , seahorses[row,column])
             print("best seahorse:", seahorses[best_seahorse_index,column])
             seahorses[row,column]=(seahorses[row,column] + ((step_lenght*(seahorses[best_seahorse_index,column]-seahorses[row,column])*x*y*z)+seahorses[best_seahorse_index,column])) 
        print("----------SEAHORSES-----------------")
        print(seahorses)
        print("-------------------------------------------")
    



    current_iteration+=1





print("----------SEAHORSES-----------------")
print(seahorses)
print("-------------------------------------------")
#----TODO-----
#Terminar Primer movimiento
#terminar 2do movimiento
#caza1
#caza2
#reproduccion


