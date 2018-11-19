import numpy as np
from read import inputParameters
from write import outputResults

def execute():
    
    ### Grid ###
    global inputParameters
    timeHorizon = inputParameters['TimeHorizon']
    numberOfTimeSteps = inputParameters['NumberOfTimeSteps']
    numberOfSimulations = inputParameters['NumberOfSimulations']
    
    # Task: determine the time step dt
    dt = 0.0
    
    ### Brownian motion W ###
    sigma = inputParameters['Sigma']
    # Task: instantiate a matrix of zeros with size numberOfSimulations * (numberOfTimeSteps+1)
    brownianMotionSimulation = None
    
    ### Simulate ###
    np.random.seed(0)
    # Task: generate a normally distriuted random matrix
    Z = None
    
    for i in range(0, numberOfTimeSteps):
        # Task: write the discrete version of the stochastic differential equation
        brownianMotionSimulation[:, i+1] = None
        
    global outputResults
    outputResults['Random_matrix'] = Z
    outputResults['Brownian_motion'] = brownianMotionSimulation
    

