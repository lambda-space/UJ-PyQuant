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
    
    ### First Brownian motion W_1 ###
    sigma_1 = inputParameters['Sigma_1']
    # Task: instantiate a matrix of zeros with size numberOfSimulations * (numberOfTimeSteps+1)
    brownianMotionSimulation_1 = None
    
    ### Second Brownian motion W_2 ###
    sigma_2 = inputParameters['Sigma_2']
    # Task: instantiate a matrix of zeros with size numberOfSimulations * (numberOfTimeSteps+1)
    brownianMotionSimulation_2 = None
    
    ### Simulate ###
    np.random.seed(0)
    # Task: generate two normally distriuted random matrices
    Z_1 = None
    X_1 = None
    
    correlation = inputParameters['Correlation']
    # Task: correlate the two independent matrices to generate a third one correlated to Z_1
    Z_2 = None
    
    for i in range(0, numberOfTimeSteps):
        # Task: write the discrete version of the stochastic differential equation
        # Uwaga: choose the random matrices correctly!
        brownianMotionSimulation_1[:, i+1] = None
        brownianMotionSimulation_2[:, i+1] = None
        
    global outputResults
    outputResults['First_random_matrix'] = Z_1
    outputResults['Second_random_matrix'] = Z_2
    outputResults['First_brownian_motion'] = brownianMotionSimulation_1
    outputResults['Second_brownian_motion'] = brownianMotionSimulation_2
    

