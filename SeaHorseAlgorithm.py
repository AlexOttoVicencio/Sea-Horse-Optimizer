import numpy as np
import random
import math
#----STARTING PARAMETERS

LB=-100
UB=100
Dim=2
Pop=4
popsize=4;
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
     #print(np.sum(seahorses_copy[x,:]))
     if np.sum(seahorses_copy[x,:])<minimum_result :
        minimum_result=np.sum(seahorses_copy[x,:])
        elite_seahorse=x
   # print("the elite seahorse is: " , minimum_result)
    #print("the index is: ",elite_seahorse)

    return elite_seahorse

def rank_sphere_optimization(seahorses_copy):
   
   num_rows, num_cols = seahorses_copy.shape
   
   a=0
   print("ranking")
   print(seahorses_copy)
   seahorses_copy=np.power(seahorses_copy,2)
   ranked_seahorses=np.zeros((num_rows,2))
   
   for x in range (0,num_rows):
      
      ranked_seahorses[x,1]=np.sum(seahorses_copy[x,:])
      ranked_seahorses[x,0]=a
      a+=1
      #print(np.sum(seahorses_copy[x,:]))
   #print(ranked_seahorses)
   print("------RANKEADOS----------")
   
   ranked_seahorses = ranked_seahorses[::-1]
   print(ranked_seahorses)

   return ranked_seahorses

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


print("----INITIAL------SEAHORSES-----------------")
print(seahorses)
print("-------------------------------------------")
#getting elite index and an array of fitness values

best_seahorse_index = elite_seahorse(seahorses)




while current_iteration<iterations :
    print("ITERACION----------")
    r1 = np.random.randn(1, Dim)
    best_seahorse_index = elite_seahorse(seahorses)
    #levy value
    step_lenght=levy_function()
    #print("levy value is: ",step_lenght)

    num_rows, num_cols = seahorses.shape

#first it goes through every row and decides wether to change them with levy or the brownian movement


    
    #explotation part
    u=0.05
    v=0.05
        
        

    #4th eq is applied
    for row in range (0,num_rows):
        for column in range (0,num_cols): 
         #print("pasa el for valor: ",r1[0,column])
         if(r1[0,column]>0):
           #print("pasa por 1  valor:", r1[0,column])
           theta=random.uniform(0,2*math.pi)   
           p=u*pow(math.e,(theta*v))
           x=p*math.cos(theta)
           y=p*math.sin(theta)
           z=p*theta
             #print("theta: ",theta)
             #print("p: " , p)
             #print("x: ",x)
             #print("y: ",z)
             #print("z: ",z)
             #print("seahorse: " , seahorses[row,column])
             #print("sum is:", ((step_lenght*(seahorses[best_seahorse_index,column]-seahorses[row,column])*x*y*z)+seahorses[best_seahorse_index,column]) )
             #print("best seahorse:", seahorses[best_seahorse_index,column])
           seahorses[row,column]=(seahorses[row,column] + ((step_lenght*(seahorses[best_seahorse_index,column]-seahorses[row,column])*x*y*z)+seahorses[best_seahorse_index,column])) 
        else:
          l=0.05
        #exploration part
         #for row in range (0,num_rows):
            #for column in range (0,num_cols):
          #print("pasa por 2 valor:",r1[0,column])
          num=random.uniform(0,1)
          brownian=random.gauss(0,1)
           #print("the normal number is: ", brownian)
          seahorses[row,column]= seahorses[row,column]+(num*l*brownian*(seahorses[row,column]-brownian*seahorses[best_seahorse_index,column]))
       
                   
    
    #keep values from growing too much
    for row in range (0,num_rows):
        for column in range (0,num_cols):
            if(seahorses[row,column]>100):
                seahorses[row,column]=100
            if(seahorses[row,column]<-100):
                seahorses[row,column]=-100
    
    #predation
    best_seahorse_index = elite_seahorse(seahorses)
    
    for row in range (0,num_rows):
        for column in range (0,num_cols):
            r2=random.uniform(0,1) 
            rand=random.uniform(0,1) 
            alpha=(1-current_iteration/iterations)**((2*current_iteration)/iterations)
            if(r2>0.1):
               seahorses[row,column]=alpha*(seahorses[best_seahorse_index,column]-rand*seahorses[row,column])
            else:
               seahorses[row,column]=(1-alpha)*(seahorses[row,column]-rand*seahorses[best_seahorse_index,column])+alpha*seahorses[row,column]

    #keep values from growing too much
    for row in range (0,num_rows):

        for column in range (0,num_cols):
            if(seahorses[row,column]>100):
                seahorses[row,column]=100
            if(seahorses[row,column]<-100):
                seahorses[row,column]=-100

    #breeding
    #sort fitness of seahorses form best to worst in array
    seahorses_copy=seahorses.copy()
    seahorses_ranked=rank_sphere_optimization(seahorses_copy)
    
    print("Los caballos rankeados------------------")
    seahorses_temp=seahorses.copy()
    print(seahorses_ranked)
    for row in range (0,num_rows):
       seahorses[row,:]=seahorses_temp[round(seahorses_ranked[row,0]),:].copy()

    
    print("------Arrego Ordenado por fitnes-.-----------------")
    print(seahorses)
    print("-------------------------------------------")

    #make new array and breed seahorses
    children_pop=round(Pop/2)
    seahorses_children=np.zeros((children_pop,Dim))
    

    #fill children array
    for row in range (0,children_pop):
        r3=random.uniform(0,1)
        for column in range (0,Dim):
            #print("traveling r3= ",r3)
            seahorses_children[row,column]=(r3*seahorses[row,column])+((1-r3)*seahorses[children_pop+row,column])
    print("hijos")
    print(seahorses_children)
    #concatenate the children array
    expanded_seahorses=np.concatenate((seahorses,seahorses_children),axis=0)
    print("conectados------")
    print(expanded_seahorses)
    
    #order them by fitness
    expanded_copy=expanded_seahorses.copy()
    expanded_seahorses_ranked=rank_sphere_optimization(expanded_copy)
    print("------Arrego Ordenado por fitnes con hijos-.-----------------")
    print(expanded_seahorses_ranked)
    print("-------------------------------------------")

    current_iteration+=1

    

    








print("----------FINALSEAHORSES-----------------")
print(seahorses)
print("-------------------------------------------")
#----TODO-----
#Terminar Primer movimiento
#terminar 2do movimiento
#caza1
#caza2
#reproduccion


