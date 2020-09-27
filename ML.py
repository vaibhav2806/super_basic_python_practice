import numpy as np                             #lib used to handel multi-dimensional array
import pandas as pd                            #we will use panda to load the data into a dataFrame object

import matplotlib as mpl                       #used to draw graphs
import matplotlib.pyplot as plt                #plt is on object which we will use to draw graphs 

from matplotlib.animation import FuncAnimation #this module helps us to generate animation

from sklearn.datasets import load_boston       #this function load we will use to train and test our model in this project
from sklearn.metrics import mean_squared_error #this function computes the mean square error b/w predicted values and the 
                                               #true valuess the boston house price dataset
                                               #this is the data set
        
from sklearn.model_selection import train_test_split #this function takes the dataset as features and target and splits 
                                                     #them into 2 sets, a training set and a testing set
from sklearn.preprocessing import MinMaxScaler 



from IPython.display import HTML #this is used to disply results on the screen

def error(m , x , c , t):
    N = x.size
    e = sum(((m * x + c) - t ) **2)
    return e * 1/(2*N)
xtrain , xtest , ytrain , ytest = train_test_split(X , Y , test_size = 0.2)

def  update(m,x,c,t,learning_rate):
    
    #lets compute the gradient for the weight m
    #the vectorized operations provided by numpy library allows us to implement the equation in a single line insted of using a
    #for loop
    grad_m = sum(2 * ((m * x + c) - t ) * x)
    
    #lets compute the gradient for weight c
    grad_c = sum(2*((m * x + c) - t ))
    
    #now we multiply the learning rate with the grad_m and grad_c values
    m = m - grad_m * learning_rate
    c = c - grad_c * learning_rate 
    return m,c

def gradient_descent(init_m , init_c , x , t , learning_rate , iterations , error_threshold):
    
    #initialise m and c with the initial values 
    
    m = init_m
    c = init_c
    
    #lets now declare an empty list 
    
    error_values = list()
    mc_values = list()           #to store the intermittent m and c values 
    
    for i in range(iterations):
        e = error(m , x , c , t) 
        #storing errors of current iteration in variable e
        #check if the error values has fallen below the threshold value 
        
        if e < error_threshold :
            print ("Error less than the threshold. Stopping gradient descent ")
            break
        error_values.append(e)
        m,c = update(m , x , c , t , learning_rate)
        mc_values.append((m,c))
    return m, c, error_values, mc_values
    
#%%time
#we can set the slope positive or negative 

init_m = 0.9
init_c = 0

#then set the variable learning rate
#if learning_rate set above 0.0025 for this problem then it will cause overflow in weight values

learning_rate = 0.001
iterations = 250        #set the number of iterations 
error_threshold = 0.001 #set the error threshold 

#now call the gradient_descent with the correct order and type of the parameters.
#store the returned values in the same order that theywere returned from the gradient_descent function
m , c , error_values , mc_values = gradient_descent(init_m , init_c , xtrain , ytrain , learning_rate , iterations , error_threshold)

mc_values_anim = mc_values[0:250:5]
fig , ax = plt.subplots()
ln, = plt.plot([], [], 'ro-',animated = True)

def init():
    plt.scatter(xtest , ytest , color = 'g')
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 1.0)
    return ln,

def update_frame(frame_number):
    m , c = mc_values_anim[frame_number]
    x1 , y1 = -0.5, m*-.5+c
    x2 , y2 = 1.5 , m*1.5+c
    ln.set_data([x1 , x2] , [y1 , y2])
    return ln,

anim = FuncAnimation(fig , update_frame , frames = range(len(mc_values_anim)), init_func = init , blit = True)
HTML(anim.to_html5_video())
