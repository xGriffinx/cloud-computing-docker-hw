import os, socket

currentDir = os.path.dirname(os.path.abspath(__file__))
dataPath = f"{currentDir}/home/data/"
output = f"{currentDir}/home/output/result.txt"
inContent = ""
fileStore = []
wordCount = []
fileNumber = 0

with open(output, "w") as outputFile:
    inContent = inContent + "Machine's IP Address: " + socket.gethostbyname(socket.gethostname()) + "\n"

    for root, dirs, files in os.walk(dataPath):
        for filename in files:
            inContent = inContent + 'File Name: ' + filename + '\n'
            fileStore.append(filename)
            inputFile = open(dataPath + filename)

            wordCount.append(len(inputFile.read().split()))
            inContent = inContent + 'Word Count: ' + str(wordCount[fileNumber]) + '\n'
            
            fileNumber=fileNumber+1

    inContent = inContent + '\nTotal Words: ' + str(sum(wordCount)) + '\nHighest Word Count: ' + str(max(wordCount))
    inContent = inContent + '\tfrom file: ' + fileStore[(wordCount.index(max(wordCount)))]

    outputFile.write(inContent)

with open(output, "r") as printOutput:
    print(printOutput.read())