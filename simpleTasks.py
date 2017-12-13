#! /usr/bin/env python3.4
import sys
import math

def find(pattern):
    with open('sequence.txt', 'r') as myFile:
        content = myFile.read()
    content = list(content)
    pattern = list(pattern)
    matches = []

    start = 0
    for num in content[:len(content) - len(pattern) + 1]:
        end = start + len(pattern)
        i = start
        check = True
        for digit in pattern:
            if digit == 'X' or content[i] == digit:
                i += 1
            else:
                check = False
                break
        if check == True:
            matches.append("".join(content[start:end]))
        start += 1
    return matches

def getStreakProduct(sequence, maxSize, product):
    sequence = list(sequence)
    matches = []
    i = 0
    for num in sequence[:len(sequence) - 1]:
        num = int(num)
        myProduct = num
        j = i + 1
        size = 2
        for nextNum in sequence[j:j + maxSize + 1]:
            nextNum = int(nextNum)
            myProduct *= nextNum
            if myProduct == product:
                matches.append("".join(sequence[i:i + size]))
            elif myProduct > product:
                break
            size += 1
        i += 1
    return matches

def writePyramids(filePath, baseSize, count, char):
    numSpaces = int((baseSize - 1) / 2)
    numChars = 1
    pyramidRow = []
    with open(filePath, 'w') as myFile:
        for row in range(0, int((baseSize + 1) / 2)):
            for pyramid in range(0, count):
                for space in range(0, numSpaces):
                    pyramidRow.append(" ")
                for brick in range(0, numChars):
                    pyramidRow.append(char)
                for space in range(0, numSpaces):
                    pyramidRow.append(" ")
                pyramidRow.append(" ")
            pyramidRow = "".join(pyramidRow)
            myFile.write("{}\n".format(pyramidRow))
            numSpaces -= 1
            numChars += 2
            pyramidRow = []

def getStreaks(sequence, letters):
    sequence = list(sequence)
    letters = list(letters)
    newSeq = []
    seqs = []
    n = 1
    for letter in sequence:
        if letters.count(letter) > 0:
            newSeq.append(letter)
            if n == len(sequence) or letter != sequence[n]:
                seqs.append("".join(newSeq))
                newSeq.clear()
        n += 1
    return seqs

def findNames(nameList, part, name):
    matches = []
    for word in nameList:
        word = word.split()
        firstName = word[0]
        lastName = word[1]
        if part == "L" or part == "FL":
            if lastName.lower() == name.lower():
                matches.append(" ".join(word))
                continue
        if part == "F" or part == "FL":
            if firstName.lower() == name.lower():
                matches.append(" ".join(word))
    return matches

def convertToBoolean(num, size):
    boolList = []
    if not isinstance(num, int) or not isinstance(size, int):
        return boolList
    biNum = []
    while num > 0:
        digit = num % 2
        num = math.floor(num / 2)
        biNum.append(digit)
    while len(biNum) < size:
        biNum.append(0)
    biNum.reverse()
    for biDigit in biNum:
        if biDigit == True:
            boolList.append(True)
        else:
            boolList.append(False)
    return boolList

def convertToInteger(boolList):
    if not isinstance(boolList, list):
        return None
    if not boolList:
        return None
    for element in boolList:
        if not isinstance(element, bool):
            return None
    biDigits = []
    for tf in boolList:
        if tf == True:
            biDigits.append(1)
        else:
            biDigits.append(0)
    biDigits.reverse()
    biNum = 0
    power = 0
    for digit in biDigits:
        biNum += digit * (2 ** power)
        power += 1
    return biNum

if __name__ == '__main__':
    bList = "hello"
    convertToInteger(bList)
