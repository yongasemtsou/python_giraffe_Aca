phrase = "Giraffe Academy"
# print(phrase.upper())
#print(phrase + ' is cool')
# print(phrase.isupper())
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[0])
# print(phrase.index('A'))

##########################################
# A number

#from math import *
# my_num=25
# print(sqrt(my_num))

###########################################
# Getting Imput From Users

#name = input('Enter you name: ')
#print('Hello how can I help you ? ' + name + '!')
#ask_question = input('Can I have you phone number? : ')
#print('you phone number is  ' + ask_question + '!')
#level_education = input('Enter you education level: ')
#print('you level education is  ' + level_education + '!')

####################################################################
# Building a Advanced Calculator

#num1 =  float(input('Enter first number: '))
#op = input('Enter operator: ')
#num2 =  float(input('Enter second number: '))

# if op == "+":
#   print(num1 + num2)
# elif op == "-":
#   print(num1 - num2)
# elif op == "/":
#   print(num1/num2)
# elif op == "*":
#   print(num1 * num2)
# else:
#   print("Invalid operator")

###########################################################################
# A Liste
#friends = ['kevin', 'karen','jim']
# print(friends[-1])

################################################################
# Functions
# def say_hi(name):
#print('Hello User ' + name )
# say_hi('joel')

##############################################################################
# if function statment

#is_male = True
#is_tall = True

# if is_male or is_tall:
#print('You are a male')
# else:
#print('you are not a male')

#is_male = False
#is_tall = True

# if is_male and  is_tall:
#print('You are a male')
# else:
#print('you are not a male')

#is_male = False
#is_tall = True

# if is_male and  is_tall:
#print('You are a male')
# elif is_male and not (is_tall):
#print('You are a short male')
# elif not (is_male) and is_tall:
#print('You are not a male but are tall')
# else:
#print('you are not a male')

# If statment and comparaison

# def max_num(num1, num2, num3):
# if  num1>= num2 and num1>= num3:
# return num1
# elif num2 >= num1 and num2 >= num3:
# return num2
# else:
# return num3

# print(max_num(3,40,5))


# def max_num(num1, num2, num3):
# if  num1>= num2 and num1>= num3:
# return num1
# elif num2 >= num1 and num2 >= num3:
# return num2
# else:
# return num3

# print(max_num(3,40,5))
#######################################################################################
# Dictionnary
#monthConversions = {
    #"Jan": "January", 
    #"Feb":"Febuary", 
    #"Mar": "March",
    #"Apr": "April",
    #"May": "May",
    #"Jun": "June",
    #"Jul": "July",
    #"Aug": "August",
    #"Sep": "September",
    #"Oct": "October",
    #"Nov": "November",
    #"Dec": "December",

#}

#print(monthConversions["Nov"])
#print(monthConversions.get("Nov"))
##################################################################################################
# While Loop( a structure of python)
#i =1
#while i< 10:
    #print(i)
    #i = i+1 # or i+=1
#print("Done with loop")

##########################################################################################################3
#Building a Guessing Game
#secret_word ="giraffe"
#guess = ""
#guess_count = 0
#guess_limit =3
#out_of_guesses =False

#while guess != secret_word and not (out_of_guesses):
    #if guess_count< guess_limit:
        #guess = input("Enter guess: ")
        #guess_count +=1
    #else:
        #out_of_guesses= True
#if out_of_guesses:
    #print('Out of Guesses, You lose')
#else:
    #print("You win")

############################################################################################################
#for loop
#numbers =[1,2,3,4,5,6,7,8,9,0]
#for number in numbers:
    #print(number)

#for index in range(50): # or range(3,30):
    #print(index)

#for index in range(50): # or range(3,30):
    #if index==0:
        #print('first Iteration')
    #else:
        #print('Not fisrt')
#####################################################################################################################
#exponentiel function
#def raise_to_power(base_num, pow_num):
    #result =1
    #for index in range(pow_num):
        #result = result * base_num
    #return result

#print(raise_to_power(10,76))

################################################################################################################################
#2D Lists & Nested Loops

#number_grid = [
    #[1, 2, 3],
    #[4, 5, 6],
    #[7, 8, 9],
    #[0]
#]

#for row in number_grid:
    #for col in row:
        #print(col)
############################################################################################################################################
# Build a Translator
'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation +"G"
            else:
                translation = translation + "g"
         
        else:
            translation = translation + letter
    return translation

print(translate(input('Enter a phrase: ')))   
'''
####################################################################################################################################################
#Try Except
'''
try:
    number = int(input('Enter a number: '))
    print(number)
except:
    print('Invalid Input')
    '''
#########################################################################################################
#Read File
