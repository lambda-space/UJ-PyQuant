import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

inputParameters = {'TimeHorizon': 0.0,
                   'NumberOfTimeSteps': 0,
                   'NumberOfSimulations': 0,
                   'Sigma_1': 0.0,
                   'Sigma_2': 0.0}

def read(inputFilePath, inputFileName, sheetName):
    
    inputFile = inputFilePath + '\\' + inputFileName + '.xlsx'
    reader = pd.read_excel(open(inputFile, 'rb'), sheetname=sheetName)
    
    global inputParameters
    
    inputParameters['TimeHorizon'] = float(reader.iloc[10, 4])
    inputParameters['NumberOfTimeSteps'] = int(reader.iloc[11, 4])
    inputParameters['NumberOfSimulations'] = int(reader.iloc[12, 4])
    inputParameters['Sigma_1'] = float(reader.iloc[14, 4])
    inputParameters['Sigma_2'] = float(reader.iloc[15, 4])

