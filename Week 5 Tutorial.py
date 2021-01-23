'''
Week 5 Tutorial
'''

'''
Question 2
Write a function that accepts a string and calculates the number of upper and lower case LETTERS
'''

def calculate_case():
    strings = input('Enter a string :')
    upper_count = 0
    lower_count = 0
    for char in strings:
        if ord(char) > 63:
            if ord(char) < 92:
                upper_count += 1
        if ord(char) > 95:
            if ord(char) < 123:
                lower_count += 1
    print('Number of Upper Case Characters: ', upper_count)
    print('Number of Lower Case Characters: ', lower_count)
    return

'''
Question 3
Write a function that takes a list and returns a new list with unique elements of the first list
'''
def return_unique(lyst):
    unique_lyst = []
    for x in range(len(lyst)):
        element = lyst[x]
        if element in unique_lyst:
            pass
        else:
            unique_lyst.append(element)
    print(unique_lyst)
    return

'''
Question 4
Try the following code and rectify the mistakes in the code
def doSum(alist):
    suval = 0
    for l in alst:
        sumval = sumval + l
    return sumval
    mylist = [1,2,3,4,5]
    print(dSum(mylist))
'''
def doSum(aList):
    sumval = 0
    for l in aList:
        sumval = sumval + l
    return sumval

myList = [1,2,3,4,5]
lyst1 = [1,2,3,3,3,3,4,5]
#calculate_case()
#return_unique(lyst1)
print(doSum(myList))
