import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

inputParameters = {'TimeHorizon': 0.0,
                   'NumberOfTimeSteps': 0,
                   'NumberOfSimulations': 0,
                   'Sigmas': None,
                   'Correlation': None}

def read(inputFilePath, inputFileName, sheetName):
    
    inputFile = inputFilePath + '\\' + inputFileName + '.xlsx'
    reader = pd.read_excel(open(inputFile, 'rb'), sheetname=sheetName)
    
    global inputParameters
    
    inputParameters['TimeHorizon'] = float(reader.iloc[10, 4])
    inputParameters['NumberOfTimeSteps'] = int(reader.iloc[11, 4])
    inputParameters['NumberOfSimulations'] = int(reader.iloc[12, 4])
    numberOfBrownianMotions = int(reader.iloc[13, 4])
    
    sigmas = []
    for i in range(0, numberOfBrownianMotions):
        sigmas.append(float(reader.iloc[15+i, 4]))
        
    inputParameters['Sigmas'] = sigmas
    
    correlationMatrix = np.zeros((numberOfBrownianMotions, numberOfBrownianMotions))
    for i in range(0, numberOfBrownianMotions):
        for j in range(0, numberOfBrownianMotions):
            correlationMatrix[i, j] = float(reader.iloc[15+i, 6+j])
    
    inputParameters['Correlation'] = correlationMatrix

