import pandas as pd

outputResults = {'Random_matrix': None,
                 'Brownian_motion': None}

def write(outputFilePath, outputFileName):
    
    global outputResults
    
    randomMatrix = pd.DataFrame(outputResults['Random_matrix'])
    brownianMotion = pd.DataFrame(outputResults['Brownian_motion'])
    
    outputFile = outputFilePath + '\\' + outputFileName + '.xlsx'
    writer = pd.ExcelWriter(outputFile, engine='openpyxl')
    randomMatrix.to_excel(writer, 'RandomMatrix', startrow=0)
    brownianMotion.to_excel(writer, 'BrownianMotion', startrow=0)
    
    writer.save()

