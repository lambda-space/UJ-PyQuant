from read import read
from execute import execute
from write import write
from scipy.stats import random_correlation


if __name__ == "__main__":
    
    ### Read inputs ###
    # Tasks:
    # 1 - select your input folder
    # 2 - select your input file name
    inputFilePath = ''
    inputFileName = ''
    sheetName = 'Input'
    read(inputFilePath, inputFileName, sheetName)
    
    ### Execute operations ###
    execute()
    
    ### Write output ###
    # Tasks:
    # 1 - select your output folder
    # 2 - select your output file name
    outputFilePath = ''
    outputFileName = ''
    write(outputFilePath, outputFileName)

