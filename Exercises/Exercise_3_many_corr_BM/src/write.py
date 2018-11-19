import pandas as pd

outputResults = {}

def write(outputFilePath, outputFileName):
    
    global outputResults
    
    brownianMotions = {}
    for key in outputResults:
        brownianMotions[key] = pd.DataFrame(outputResults[key])
    
    outputFile = outputFilePath + '\\' + outputFileName + '.xlsx'
    writer = pd.ExcelWriter(outputFile, engine='openpyxl')
    for key in brownianMotions:
        brownianMotions[key].to_excel(writer, str(key), startrow=0)
    
    writer.save()

