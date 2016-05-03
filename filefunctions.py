#Author: Ben McGahee
#Title:  File Functions
#Date: 5/2/2016
#Purpose:  The file functions do various types of tasks from displaying each line of the file, splitting text in the file,
#counting the total number of words, and searching for a string in a file to see if it exists and counting how many times
#that string exists within the file.

#displayEachLine() takes in a text file name, opens the file in read only mode, and displays each line number and content in each line.
def displayEachLine(textFile):
    fileName = textFile
    lineCount = 1
    with open(fileName, 'rt') as text:
        for line in text:
            print str(lineCount) + ":", line
            lineCount += 1

#splitText() takes in a text file name, opens the file in read only mode, and splits the text into its separate strings and stores them in a list.
def splitText(textFile):
    fileName = textFile
    openFile = open(fileName, 'rt')
    message = openFile.read()
    splitMessage = message.split()
    return splitMessage

#wordCount() takes in a text file name, calls the splitText() function and counts the number of words in the file.
def wordCount(textFile):
    splitMessage = splitText(textFile)
    wordCount = len(splitMessage)
    return "There are " + str(wordCount) + " words in '" + textFile + "'."

#findString() takes in a text file and string that the user wants to find in the file and see if it exists.
#If the string exists, the function determines how many times the string occured in the file.
#Otherwise, the function will tell the user that the string does not exist.
def findString(textFile, searchString):
    message = splitText(textFile)
    size = len(message)
    searchStringCount = 0
    for i in range(0, size):
        if message[i].lower() == searchString.lower():
            searchStringCount += 1
        else:
            continue
    if searchStringCount == 0:
        return "Could not find the string '" + searchString + "'" + "."
    else:
        return "The string '" + searchString + "'" + " occured " + str(searchStringCount) + " times in '" + textFile + "'."
            
    


    
