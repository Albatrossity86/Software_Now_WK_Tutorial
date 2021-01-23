'''
Week 2 Tutorial Questions
'''
#Question 1
#Write a program to find the smallest and largest of three numbers
def small_large():
    number = []
    for i in range(3):
        value_number = int(input('Enter a number: '))
        number.append(value_number)
        #print(number[i])
    smallest = min(number)
    largest = max(number)
    print('Smallest Value:', smallest, 'Largest Value:', largest)
    return


#Question 2
#Write a program that will accept 10 numbers from the user and output the sum of the broken_numbers
def ten_summed_numbers():
    numbers = []
    numbers_left = 10
    summed_numbers = 0
    for i in range(0, numbers_left):
        user_number = int(input('Enter a number : '))
        numbers.append(user_number)
        numbers_left -= i
    for i in range(0, 10):
        summed_numbers = numbers[i] + summed_numbers
    print(summed_numbers)
    return

#Question 3
#Write a program that will print the number of days if the user inputs the month name
def number_days():
    days_30 = ['september', 'april', 'november', 'june']
    days_28 = ['february']
    days_31 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
    user_input = str(input('Enter a month in lower case : '))
    if user_input in days_30:
        print(user_input, 'Has 30 Days')
    if user_input in days_28:
        print(user_input, 'Has 28 Days')
    if user_input in days_31:
        print(user_input, 'Has 31 days')
    else:
        print('That is not a valid month.')
        return number_days()
    run_again = input('Do you want to go again? Y to go again or press ENTER to exit ')
    if run_again:
        return number_days()
    else:
        return

#small_large()
#ten_summed_numbers()
#number_days()
