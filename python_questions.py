#Question One
#Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.
# def hello_name(user_name):

new_user =("You must choose a new user!")
new_user+=("\nWhat is your new username? ")

user_name=input(new_user)
print("\nHello, " + user_name + "!")

#I wrote a clear prompt to tell the user the exact info I was looking for, a new username!
#My first line of code stores the message of the prompt. The second line allows the user 
#to input their username as a string and takes that string to line 9 where it will print out a message greeting the new user!



#Question Two 
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
first_odds = 0
while first_odds < 100:
        first_odds += 1
        if first_odds % 2 != 0:
                print(first_odds)                
#I first set my variable 'first_odds' equal to 0 since I will be adding one until I hit 100
#then set a while loop that allowed me to understand that while the integer is less of a 100,
#we will keep adding 1 until we hit 100. I then set a modulo operator that will divide the first_odds
#integer by two and if the remainder is not equal to 100 we will print out the first_odd integer.



#Question Three
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    maximum = a_list[0]
    for num in a_list:
        if num > maximum:
            maximum = num
    return maximum

my_list = [90, 522, 66, 8484]
maximum = max_num_in_list(my_list)
message = "\nThe maximum number in this list is"
print(message, maximum)

my_list2 = [489423121, 552, 13120, 0, 511111111454545454545]
maximum = max_num_in_list(my_list2)
print(message, maximum)
#THIS ONE TOOK ME THE LONGEST THUS FAR!!! First I wrote a function with a variable called 'maximum'
#and a value of 'a_list' that sets the the INITIAL maximum value to be the first # in the list. 
#I then enter a for loop and inside that loop there is an IF statement that basically says,
#'for every NUM in the list (a_list) that is greater than the current maximum, the maximum will be updated
#to the current value of 'num'. Then I returned the maximum to get the maximum value of the list.
#**It was also very important that I checked my indentation for this step, because at first my return value
#was inside the if loop which caused some trouble when running the code.But after working on it for a while
#and finding out what was the problem I was able to fix this** I then created a list with random numbers
#and set the maximum variable to equal to the function I created earlier which takes the current list into consideration
#I then created a message that I could use when printing the maximum value!!!



#Question Four
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    a_year = int(a_year)

    if a_year % 4 == 0:
        if a_year % 100 != 0 or a_year  % 400 ==0:
             return True
    return False

print(is_leap_year(1987))
print(is_leap_year(2004))
print(is_leap_year(1964))
print(is_leap_year(2020))
#First thing first, I wrote a function that converts 'a_year' into a string so the input is treated as a 
#integer and not another data type. In the next line, 65, I wrote an if statement basically saying, "If 
# the 'a_year is divisible by 4 then we can move it to the next if block". The following if block checks
#for two things, that the number isn't divisible by 100 yet it has be divisible by 400 in order to be considered
#a leap year. If this statement checks off, then a boolean of True will be returned, otherwise FALSE!!
#I then tested 4 different years, and got False, True, True, True 



#Question Five
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(con_list):
    if len(con_list) < 2:
         return False
    
    for i in range((len(con_list)) - 1):
         if con_list[i + 1] - con_list [i] != 1:
              return False
    return True


con_list=[15,16,17,18]
result=is_consecutive(con_list)
print(result)

con_list=[58,59,60,62]
result=is_consecutive(con_list)
print(result)
#SO first, I wrote a function that checks in the length of the list is less than 2, if it less than 2
#the code will return a boolean of False since we need at least 2 numbers to have a consecutive
#sequence. If we do have more than two numbers, then we start a for loop that runs from a variable to the
# length of the list. The next line then checks if the difference between current elements is NOT equal to 1
# If it is not equal to ONE it will return a boolean of FALSE but if it does equal to ONE then the list is
# consecutive and the boolean returned will be TRUE!!! 


#WOOOO!!!!

