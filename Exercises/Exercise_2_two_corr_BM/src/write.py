import pandas as pd

outputResults = {'First_random_matrix': None,
                 'Second_random_matrix': None,
                 'First_brownian_motion': None,
                 'Second_brownian_motion': None}

def write(outputFilePath, outputFileName):
    
    global outputResults
    
    firstRandomMatrix = pd.DataFrame(outputResults['First_random_matrix'])
    secondRandomMatrix = pd.DataFrame(outputResults['Second_random_matrix'])
    firstBrownianMotion = pd.DataFrame(outputResults['First_brownian_motion'])
    secondBrownianMotion = pd.DataFrame(outputResults['Second_brownian_motion'])
    
    outputFile = outputFilePath + '\\' + outputFileName + '.xlsx'
    writer = pd.ExcelWriter(outputFile, engine='openpyxl')
    firstRandomMatrix.to_excel(writer, 'First_RM', startrow=0)
    secondRandomMatrix.to_excel(writer, 'Second_RM', startrow=0)
    firstBrownianMotion.to_excel(writer, 'First_BM', startrow=0)
    secondBrownianMotion.to_excel(writer, 'Second_BM', startrow=0)
    
    writer.save()

