##this program implements a merge sort.

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


#this sorts the base cases: 0, 1, or 2 elements, or splits the array
#and sorts the sides
def sort(array):
    #if the array only has one element, just return it. it's sorted.
    if len(array) <= 1:
        return array
    #if the array only has two elements, flip if needed and return
    elif len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return array
    #otherwise, split the array in half and sort both sides, merging the results
    else:
        divIndex = len(array)/2
        return merge(sort(array[0:divIndex]), sort(array[divIndex:len(array)]))
    
#this merges two arrays, preserving the sorted order
def merge(a,b):
    iA = 0
    iB = 0
    final = []

    #go until one of the arrays has finished
    while iA < len(a) and iB < len(b):
        if a[iA] < b[iB]:
            final.append(a[iA])
            iA += 1
        else:
            final.append(b[iB])
            iB += 1

    #if a still has unused elements, put them on.
    if iA < a:
        for i in a[iA:len(a)]:
            final.append(i)

    #if b still has unused elements, put them on.
    if iB < len(b):
        for i in b[iB:len(b)]:
            final.append(i)
    return final

#3 2 1 go
if __name__ == "__main__":
    print "Sorting..."
    sort(numbers)
    print "done."

