# Loops & List with python
"""Loops make the life easier for the programmer - if you want to be lazy use your brain :-)
When we want to do the same code over and over again, we can use loops."""

# list VS range
" we have a lot of ways to create a list of numbers in python, two of them are range and list "
listOf5 = [1, 2, 3, 4, 5]
rangeOf5 = list(range(1, 6)) # The default range start with index 0, so we need to change if we want to start with 1 or else

# 3 ways to use range function
range(4)
range(1,4)
range(1,10,2) # range() function python

# Exe. 1
" use the print function & try to print those variables ^ "
" whats happen ? "

print(listOf5)
print(rangeOf5)

# For loop
" we have two mainly ways to use a loop in python, the first one is for loop "

for i in range(1,3):  # the range function is a list of numbers from 0 to number that we put in the range function
    print("This is the ", i, " iteration")

for i in listOf5:  # we can use the list that we created before
    print("This is the ", i, " iteration")

negativeAndPositiveList = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]

" we can use condition in the loops "
for index in negativeAndPositiveList:
    if negativeAndPositiveList[index] > 0:
        print(index, " is positive")
    elif negativeAndPositiveList[index] == 0:
        print(index, " is zero")
    else:
        print(index, " is negative")

# Exe. 2
" try now to print the listOf5 & rangeOf5 with for loop "
for i in listOf5:
    print(listOf5[i])

for i in rangeOf5:
    print(rangeOf5[i])

# While loop
" the second way to use a loop is while loop, we can do the same command till the condition is true "
condi = 1 > 10 # boolean variable
indexCounter = 0
while indexCounter < negativeAndPositiveList[indexCounter]:
    print("The value of the index ", indexCounter, " is a positive number ->", negativeAndPositiveList[indexCounter])
    indexCounter += 1  # indexCounter = indexCounter + 1

# Exe. 3
" try now to print the listOf5 & rangeOf5 with while loop "
# how to print all indexes in list with while loop python

# Exe. 4
"Explain why we dont see 1 & 2 values in our while loop"

# Exe. 5
"explore the range() function with different parameters -> search in google : range() function python"
"range(0,10,2)"
