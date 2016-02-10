#this program implements a merge sort.

#make sure the user has the right version of python
try:
    print "Checking python version...Good."
except:
    print("Wrong version of python.")
    exit(1)

import sys

#the file name will be passed in
fileName = sys.argv[1]
myFile = None

#try to open the file
try:
    myFile = open(fileName)
except:
    print "Error: Could not open file."
    exit(1)

#collect data
print "Collecting data."
numbers = []
for num in myFile:
    numbers.append(int(num.strip()))
print "Done collecting data."

#this calls the other sort() function to do the actual sorting
def sort(array):
    mySort(array, 0, len(array)-1)

#this divides the array into two parts and sorts each of them recursively
def mySort(array, begin, end):
    if begin < end:
        middle = divide(array, begin, end)
        mySort(array, begin, middle)
        mySort(array, middle + 1, end)

#this takes an element and swaps stuff around it
def divide(array, begin, end):
    pivot = array[begin]
    indexA = begin - 1
    indexB = end + 1
    
    while indexA < indexB:
        indexA += 1
        indexB -= 1
        while array[indexA] < pivot:
            indexA += 1
        while array[indexB] > pivot:
            indexB -= 1
        if indexA < indexB:
            temp = array[indexA]
            array[indexA] = array[indexB]
            array[indexB] = temp
    return indexB

#3 2 1 go
if __name__ == "__main__":
    print "Sorting..."
    sort(numbers)
    print "done."
