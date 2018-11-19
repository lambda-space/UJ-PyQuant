import numpy as np
import scipy.linalg
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
    sigmas = inputParameters['Sigmas']
    numberOfBrownianMotions = len(sigmas)
    correlatedRandomMatrices = {}
    brownianMotionSimulations = {}
    for i in range(0, numberOfBrownianMotions):
        # Tasks:
        # 1 - create matrix to contain a correlated random matrix of size numberOfSimulations * numberOfTimeSteps
        # 2 - create matrix to contain a Brownian motions simulation of size numberOfSimulations * (numberOfTimeSteps+1)
        correlatedRandomMatrices[i] = None
        brownianMotionSimulations[i] = None
 
    ### Cholesky decomposition ###
    correlationMatrix = inputParameters['Correlation']
    # Task: call the cholesky method on the appropriate matrix
    cholesky = scipy.linalg.cholesky(??????????????, lower=True)
    
    ### Generate random matrices ###
    np.random.seed(0)
    for i in range(0, numberOfSimulations):
        for j in range(0, numberOfTimeSteps):
            # Task: generate a random vector of size numberOfBrownianMotions * 1
            randomVector = None
            # Task: generate a correlated random vector using the np.matmul() function
            correlatedRandomVector = None
            for k in range(0, numberOfBrownianMotions):
                # Task: fill a correlated random matrix with the appropriate random number
                correlatedRandomMatrices[k][i ,j] = None

    ### Simulate Brownian motions ###    
    for j in range(0, numberOfBrownianMotions):
        for i in range(0, numberOfTimeSteps):
            # Task: generate the brownian motion simulation using 'correlatedRandomMatrices'
            brownianMotionSimulation[j][:, i+1] = None
            
    global outputResults
    for i in range(0, numberOfBrownianMotions):
        outputResults[i] = brownianMotionSimulations[i]
    

