# Tyler Crabtree
# Project 2
# Bitmap.py

#import needed libraries (only needed one)
import math


#functions opens a file and grabs the text
def grabText():
    f = open('animals_test.txt', 'r')
    #print f.read()
    return f.read()

#This Functions creates a bitmap
def bitmaps(text):
    text = text.split()             #splits into list of tuples
    i = 0                           #iterator
    map = ''                        #final string

    while(i < len(text)):
        tuple = text[i]                        # grab individual tuple
        input = tuple.rsplit(',', 3)           # splits into 8 segments
        animal = input[0]                      # break down each tuple
        age = input[1]
        status = input[2]
        bitmapString = ""                      # each line of bitmap

                                               # below I look at each type and assign it a value from there
                                               # I threw in x's if there were errors, but those are extra
        #######################################
        if (animal == "dog"):
            bitmapString = bitmapString + "0100"
        elif (animal == "turtle"):
            bitmapString = bitmapString + "0010"
        elif (animal == "bird"):
            bitmapString = bitmapString + "0001"
        elif (animal == "cat"):
            bitmapString = bitmapString + "1000"
        else:
            bitmapString = bitmapString + "xxxx"
        #######################################
        age = int(age)
        if ( 0<= age <= 10):
            bitmapString = bitmapString + "1000000000"
        elif ( 11<= age <= 20):
            bitmapString = bitmapString + "0100000000"
        elif ( 21<= age <= 30):
            bitmapString = bitmapString + "0010000000"
        elif ( 31<= age <= 40):
            bitmapString = bitmapString + "0001000000"
        elif ( 41<= age <= 50):
            bitmapString = bitmapString + "0000100000"
        elif ( 51<= age <= 60):
            bitmapString = bitmapString + "0000010000"
        elif ( 61<= age <= 70):
            bitmapString = bitmapString + "0000001000"
        elif ( 71<= age <= 80):
            bitmapString = bitmapString + "0000000100"
        elif ( 81<= age <= 90):
            bitmapString = bitmapString + "0000000010"
        elif (91 <= age <= 100):
            bitmapString = bitmapString + "0000000001"
        else:
            bitmapString = bitmapString + "xxxx"
        #######################################
            #######################################  Status
        if (status == "True"):
            bitmapString = bitmapString + "10"
        elif (status == "False"):
            bitmapString = bitmapString + "01"
        else:
            bitmapString = bitmapString + "xx"
        i = i + 1
        bitmapString += '\n'                    #append new line
        map = map + bitmapString                #add to map
    return map




#Oh pretty nice/short sort
def sortText():
    words = sorted( open('animals_test.txt', 'r').read().split())    #nifty python sort
    i = 0
    page = ''
    while (i < len(words)):                                         # getting the page in the right format for other functions
        page = page + words[i]+ "\n"
        i += 1
    return page

#file creation, I probably should have passed in a string to name the file
# but this works and is pretty clear
##########################################
def writeTextSorted(text):
    f = open("bitmapsSorted.txt", 'w')
    f.write(text)
def writeText(text):
    f = open("bitmaps.txt", 'w')
    f.write(text)
def writeSort(text):
    f = open("sortedText.txt", 'w')
    f.write(text)
def writeo32(text):
    f = open("CompressedOriginal32.txt", 'w')
    f.write(text)
def writes32(text):
    f = open("CompressedSorted32.txt", 'w')
    f.write(text)
def writeo64(text):
    f = open("CompressedOriginal64.txt", 'w')
    f.write(text)
def writes64(text):
    f = open("CompressedSorted64.txt", 'w')
    f.write(text)
##########################################



#This function calls all the compressions in order and writes them to the respective files
def compression(text1, text2):
    text = [int(i) for i in list(str(text1))]
    text2 = [int(i) for i in list(str(text2))]

    o32 = WAH(32, text)
    y = 0
    o32 = ''.join(map(str, o32))
    x =0
    x32 =''
    while(x < len(o32)):
        x32 = x32 + o32[x]
        x +=1
        if( x % 64 == 0):
            x32 = x32 + "\n"
    writeo32(x32)

    s32 = WAH(32, text2)
    y = 0
    s32 = ''.join(map(str, s32))
    x =0
    x32 =''
    while(x < len(s32)):
        x32 = x32 + s32[x]
        x +=1
        if( x % 64 == 0):
            x32 = x32 + "\n"
    writes32(x32)


    o32 = WAH(64, text)
    y = 0
    o32 = ''.join(map(str, o32))
    x =0
    x32 =''
    while(x < len(o32)):
        x32 = x32 + o32[x]
        x +=1
        if( x % 64 == 0):
            x32 = x32 + "\n"
    writeo64(x32)


    s32 = WAH(64, text2)
    y = 0
    s32 = ''.join(map(str, s32))
    x =0
    x32 =''
    while(x < len(s32)):
        x32 = x32 + s32[x]
        x +=1
        if( x % 64 == 0):
            x32 = x32 + "\n"
    writes64(x32)




#so this WAH compression (in progress)
'''
def WAH(wordlength, bitlist):
    compression = [bitlist[i*wordlength-1 : min((i+1)*wordlength-1, len(bitlist))]
        for i in range(0,int(math.ceil((len(bitlist)-1)/(wordlength-1))))]
    result = []
    run = 0
    rundigit = -1
    for i in compression[0:-1]:
        if sum(i) != len(i):
            if sum(i) != 0:
                if run > 0 and rundigit in [0,1]:
                    buf = binaryHelper(run, wordlength-2)
                    result = result +[1] + [rundigit] + buf
                result = result + [0] + i
                run = 0
        elif sum(i) == 0:
            run = run + 1
            rundigit = 0
        else:
            run += 1
            rundigit = 1
    if (run > 0 ):
        if (rundigit in [0,1]):
            buf = binaryHelper(run, wordlength - 2)
            result += [1] + [rundigit] + buf
    result = result + compression[-1]
    return result

def binaryHelper(run, length):
    binary = [int(i) for i in list(bin(run))[2:]]
    trim = [0]*(length-len(binary)) + binary
    return trim
'''

#nice clean main function, essentially calls functions with very little work done in main.
if __name__ == "__main__":
    text = grabText()
    bitmapsString = bitmaps(text)
    sortedWords = sortText()
    writeSort(sortedWords)
    sortedBitmapString = bitmaps(sortedWords)
    writeText(bitmapsString)
    writeTextSorted(sortedBitmapString)
    text = bitmapsString.replace('\n', '')
    text2 = sortedBitmapString.replace('\n', '')
    #compression(text, text2)














