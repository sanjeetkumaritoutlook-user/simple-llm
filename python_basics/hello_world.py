"""Variables"""
# intVal = 7
# floatVal = 3.91
# boolVal = True
# #print(boolVal)
#
# boolVal = False
#print(intVal, floatVal, boolVal)

"""testing comments"""

"""So multiple line comments
need 3 quotation marks"""

"""Math operators:"""
# operator1 = 2
# operator1 //= 0.5
#print (operator1)

"""#Strings and Print"""

# print("test")
# print("this should be \"in quotes\"")
# var = "Alligator"
# print(var[5])
# print(var[:4])
# print(var[4:7])
# print(var[6:])
# len(varName) Gives length of variable:
# print(len(var))
# print(var.upper())
#To convert any variable to a string: use varName(num)
# print(len("Manchester United"))
# int = 12345
# int = str(int)
# print(int[2])
# print("albania".upper())
# print("BELGIUM".lower())

"""Print input/output:"""
# name = input("What is your name?")
# print("Your name is %s" % (name))
#the %s concatenation is used to place variables inside strings


"""the else if statement (from JavaScript) is elif statement in Python:"""
# num1 = 1
# num2 = 2
# if num1 > num2 :
#     print("%s is larger than %s" % (num1, num2))
# elif num1 == num2:
#     print("%s is equal to %s" % (num1, num2))
# else:
#     print("%s is smaller than %s" % (num1, num2))

# name = input("What's your name?")
# nameLength = len(name)
# if nameLength < 4 :
#     print("%s is less than 4 characters" % (name))
# elif (nameLength >= 4) and (nameLength < 10) :
#     print("%s is at least 4 but less than 10 characters" % (name))
# else:
#     print("%s is a very long name." % (name))

"""Functions"""
# def ex():
#     print("hello world")
# ex()
#
# def singleParameter(n):
#     print(n)
# singleParameter(3)
#
# def multiplication(a,b,c):
#     d = a * c
#     print(d,b,d+b)
# multiplication(2,5,3)
#
# def intPar(intVal):
#     return intVal * 2
# def takesTwo(int1,int2):
#     return int1 * int2
# def functionInside(a,b,c):
#     output = takesTwo(intPar(a), b) * c
#     print(output)
# functionInside(7,4,2)

"""Module imports"""
# import random
# print(random.randint(1,10))
# from random import randint
# print(randint(10,20))
# from random import *
# print(random())

# import random
# from random import randint
# from math import *
# print(randint(5,10))
# print(factorial(4))
# print(random.random())

"""Built-in functions"""
# example1 = abs(-3) #results in absolute value: output 3
# example2 = type("example") #results in type of the value (int, float, string, bool etc)
# example3 = max(1.7, 9.2434, 13.3, 2.6) #gives the maximum of the values, also works for letters:
# example4 = min("f", "a", "y", "h", "z", "r") #returns the smallest of numbers/letters
# print(example1, example2, example3, example4)

"""Lists, tuples, dictionaries"""
# list: [], tuple: (), dictionary: {}
# List is an array! Accessible by index
# colors = ["green", "blue", "red", "purple", "orange"]
# print(colors)
# print(len(colors), len(colors[3]), colors[3]) #shows length of list (5 objects) and of 4th object in the list (starting at 0!)
# colors[3] = "yellow" #re-assign a specific object in a list to a new value
# print(colors)
# colors.append("pink") #append list with a new value at the end
# print(colors)
# blackWhite = ["black", "black", "white", "black", "white", "white"]
# firstWhite = blackWhite.index("white") #index gives location in array of when a value is first seen in the list
# print(firstWhite, blackWhite[firstWhite]) #white is on array position 2 (counting 0, 1, 2)
# colors.insert(5,"purple") #inserts value into existing list on location 5 of index
# print(colors)
# colors.remove(colors[2]) #remove a value from a list, exact value works too: colors.remove("red") results in same
# print(colors)
# oneColor = colors.pop(4) #pops one value from the list at location 4 (purple) into a new variable
# print(colors)
# print("Popped: " + oneColor)
"""list exercises"""
# numbers = [1, 2, 3, 4, 4, 6]
# print(numbers)
# numbers[4] = 5
# print(numbers)
# numbers.append(7)
# print(numbers)
# print(numbers[0:4])
# print(numbers[2:5])
# print(numbers[5:])
# index7 = numbers.index(7)
# print(index7)
# numbers.insert(0, 0)
# print(numbers)
# numbers.remove(3)
# print(numbers)
# print(numbers.pop())
# print(numbers)
"""For loops and tuples (list with various data types)"""
# tup = ("Let", "it", "be", "by", "The", "Beatles")
# song = ""
# for words in tup: #words is the custom 'object name' for objects inside of the list/tuple
#     song += words + " "
#     # song.append(words + " ") #will only work if both Tup and Song are arrays/lists instead of tuple! thus with []
# print(song)

# Exercises:
# tupVar = (1, 2, 3, 4)
# print(tupVar[1])
# print(tupVar[0:2])
# print(tupVar[1:3])
# print(tupVar[2:])
# for numbers in tupVar:
#     print(numbers)
"""dictionaries:"""
# # accessed by "keys" (could be string or integer) instead of index to make 'key-value pairs'
# provinces = {1: "Noord-Holland", 2: "Zuid-Holland", 3: "Utrecht", 4: "Noord-Brabant", "vijf": "Gelderland", 6: "Limburg", 7: "Groningen", 8: "Friesland", 9: "Flevoland"}
# print(provinces["vijf"])
# provinces[10] = "Overijssel" #add new key to dictionary
# print(provinces[10])
# print("Length:", len(provinces)) #length can be counted just like with lists/tuples
# del provinces[4] #deleting a key from a dictionary
# print(provinces)

#dictionary exercises:
# emp = {}
# emp["first"] = "car"
# emp["second"] = "bike"
# emp["third"] = "boat"
# print(emp)
# empLength = len(emp)
# print(empLength)
# print(emp["third"])
# emp["third"] = "plane"
# print(emp["third"],emp)
# del emp["third"]
# print(emp)

"""functions with lists - Exercises"""
# myList = ["one", "two", "three"]
# def listFunction(li):
#     print(li[1])
#     print(li[2] + " frogs")
#     li.remove(li[0])
#     print(li)
# # listFunction(myList)
#
# def printListItems(a):
#     for items in a:
#         print(items)
# printListItems(myList)

#using range function to create a number list: range(start, stop, step)
# var1 = list(range(1, 25, 2))
# print(var1)

#using multiple lists in functions:
# exList = [2, 4, 6, 8]
# def printList(a):
#     for items in a:
#         print(items)
# printList(exList)

# list1 = list(range(0,3)) #prints 0, 1, 2
# list2 = list(range(2,5)) #prints 2, 3, 4
# list3 = list(range(2,13,5)) #prints 2, 7, 12
#
# def sumLists(a,b,c):
#     summedList = []
#     for x in range(0,len(a)): #iterate total times of the length of the list
#         summedList.append((a[x] + b[x] + c[x])) #new variable to add the sums of each xth element
#     print(summedList)
# sumLists(list1, list2, list3)
#
# combinedLists = [[1,2],[0,1],[3,4]]
# def listOfLists(a):
#     singleList = []
#     for item in a:
#         for element in item:
#             singleList.append(element)
#     print(singleList)
#
# listOfLists(combinedLists)

"""While loops: same as if-statement but continues until while loop is not true anymore"""
# from random import randint
# counter = 5
# while counter < 15: #continue until number 15 is reached
#     print(counter)
#     if counter == 7:
#         print("Counter is equal to 7.")
#         break #print statement on nr 7 and stop loop with break
#     counter = randint(5, 15) #if not 7, create new random integer between 5-15 and start again
# else: #once number 15 is reached (counter is not smaller than 15):
#     print("Counter is equal to fifteen.")

#for loops with strings:
# exampleString = "example"
# for char in range(len(exampleString)):
#     print(exampleString[char], end=" ")

# def lineByLine(a):
#     for char in range(len(a)):
#         print(a[char])
# lineByLine(exampleString)

# exampleDict = {"first": 1, "second": 2, "third": 3}
# for key in exampleDict:
#     print(key + ": " + str(exampleDict[key]))

#zip function: for comparing items from two lists
# list1 = [4,2,8,12]
# list2 = [5,2,7,10]
#
# for items1, items2 in zip(list1, list2):
#     if items1 >= items2:
#         print(items1)
#     elif items1 < items2:
#         print(items2)

#for loop exercises:
# stringVar = "practice"
# intList1 = [0,2,3,6,9,12]
# intList2 = [2,6,1,7,10,11]
# dictVar = {1: "one", 2: "two", 3: "three", 4: "four"}
#
# # for char in range(len(stringVar)):
# #     print(stringVar[char])
#
# for item in intList1:
#     print(item, end = " ")
# else:
#     print(14)

# for key in dictVar:
#     print(dictVar[key])

# for items1, items2 in zip(intList1,intList2):
#     if items1 >= items2:
#         print(items1)
#     else:
#         print(items2)


"""List comprehension"""
#creating a list with a for / range function
# list1 = [num1 for num1 in range(10)] #print from 0 to 9
# list2first = [num2 for num2 in range(1,11,2)] #print 1, 3, 5, 7, 9
# list2 = [num2 * 3 for num2 in range(1,11,2)] #print above list values * 3
# #you can also use an 'if' statement in this list:
# list3 = [num1 for num1 in range(0,100) if num1 % 5 == 0]
# print(list3)

#exercises with list comprehension:
# list1 = [num1 for num1 in range(1,10,2)]
# print(list1)
# list2 = [num1 for num1 in range(3,8)]
# print(list2)
# list3 = [num1 for num1 in range(10) if num1 % 2 == 1]
# print(list3)
# list4 = [num1 for num1 in range(8) if (num1 > 2)]
# print(list4)

"""Slicing lists using stride"""
# numList = [1,2,3,4,5,6,7,8,9,10]
# reverseList = numList[::-1]
# evenList = numList[1:11:2] #first = start, second = stop, third = step
# unevenList = numList[:11:2]
# print(numList, reverseList, evenList, unevenList)

# longList = []
# counter = 1
# while counter <= 20:
#     longList.append(counter)
#     counter += 1
# print(longList)
#
# print(longList[1:19:2])
# print(longList[::5])
# print(longList[11:1:-3])
# print(longList[::-1])

"""Try and except-statements: avoid crashing the program"""
# ex1 = input("What is my favourite integer?")
# try:
#     if int(ex1) == 7:
#         print("Indeed, 7 is my favourite integer!")
#     else:
#         print("That is not my favourite integer")
# except: #if no integer is entered (e.g. a string/float variable), the program would normally crash, but not with 'except' statement.
#     print("Please re-run the program and enter an integer.")

# Exercises:
from random import randint
randomInt = randint(0, 5)
print(randomInt)
userInt = input("enter an integer.")

try:
    if int(userInt) > randomInt:
        print(userInt, "- your integer is larger than the random integer:", randomInt)
    elif int(userInt) < randomInt:
        print(randomInt, "- the random integer is larger than", userInt)
    else:
        print("Both integers are the same:", randomInt)
except:
    print("Please run the program again and enter an integer.")