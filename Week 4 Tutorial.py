'''
Week 4 Tutorial
'''
import math
def sum_list(input_lyst):
    '''
    Question 1
    Write a loop that accumulates the sum of all the numbers in a list named 'Data'
    '''

    '''
    Create a variable to be returned which is the SUM of all the numbers in list
    For loop to iterate through each value in the list
    Add the value to the variable summed_values
    Print on the screen the sum of all the numbers in the list
    '''
    summed_values = 0
    for value in input_lyst:
        summed_values += value
    print('Sum of all numbers in list =', summed_values)
    return

def summ(low = 0, high = 0):
    '''
    Question 2
    Define a function named SUM, the function expects two numbers named LOW and HIGH. The function should compute the sum of all the numbers between high and low inclusive.
    '''

    '''
    Create a variable to be returned which is the SUM of all the numbers in the range from LOW to HIGH
    For loop that starts at the variable LOW and iterates through every integer between LOW and HIGH, HIGH + 1 is the upper bound so that the varaibale HIGH is included in the summation
    Add the value to the varibale nadmed summed_values
    Print on the screen the sum of all the numbers between variables LOW and HIGH inclusive of both values
    '''
    summed_values = 0
    for value in range(low, high + 1):
        summed_values += value
    print('Sum of all numbers between Low and High inclusive = ', summed_values)
    return


def dictionary_manip ():
    '''
    Question 3
    Assume that the variable 'data' refers to the dictionary {'b':20, 'a':35}. Write the expressions to that perform the following
    Replace the value at b with that value's negation
    Add the key/value pair 'c':40 to Data
    Remove the key at 'b' in data, safely
    Print the keys in alphabetical order
    '''
    '''
    Create a Dictionary data structure with the values requried
    Create a temp_value to assign the value at key 'b', use this temporary value to create the negation of the value at key 'b' without destroying it
    Crete a key/value, 'c':40 and add it to the dicitonary with data2['c'] = 40
    Use .pop('b') to remove key/value 'b':20 from the dictionary
    Create a list of keys in alphabetical order using sorted(data2) and print the list created to screen
    '''
    data2 = {'b':20, 'a':35}
    print('Dictionary :', data2)

    temp_value = data2['b']
    data2['b'] = temp_value * (-1)
    print('Dictionary :', data2)
    data2['c'] = 40
    print('Dictionary :', data2)
    data2.pop('b')
    print('Dictionary :', data2)
    data2['b'] = -20
    list_of_keys = sorted(data2)
    print(list_of_keys)
    #print(keys_alphabetical)

def find_smallest(lyst):
    '''
    Question 4
    Write a program to find the smallest number in a list
    '''
    '''
    Utilise SELECTION SORT to find the smallest value in the list
    Set the first value to the variable 'minimum' and compare it to each other value in the list. If the index'ed value is smaller than minimum, update the minimum variable
    print at the end
    '''
    index = 0
    minimum = lyst[index]
    while index < len(lyst):
        if lyst[index] < minimum:
            minimum = lyst[index]
        index += 1
    print(minimum)
    return

data1 = [1,2,3,4,5,6,7,8,9]
sublist = [19, 12, 17, 18, 14, 11, 15, 13, 16, 3]
#sum_list(data1)
#summ(5, 9)
#dictionary_manip()
find_smallest(sublist)
