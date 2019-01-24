# python functions classwork


def main():
    #problem1()
    #problem2()
    #problem3()
    problem4()


#Create a function in your program that counts from 0 to [NUMBER]

def problem1():
    num=3
    for x in range(0,num+1):
        print(x)

def mynumbersFunction(number):
        return number

## Problem 2:
##### We will keep having this problem until EVERYONE gets it right without help
#Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.


def problem2():
    userInput=""
    while userInput.lower()!='q':
        userInput=input("enter a word\n")



### Problem 3:
#Create 4 functions called add, subtract, multiply, and divide.
# Create them to allow a user to perform the name of the function to the two numbers and return the result.


def problem3():
    userInput=int(input("Enter a number."))
    userInput2= int(input("Enter a number."))

    print(add(userInput,userInput2))
    print(subtract(userInput,userInput2))
    print(multiply(userInput,userInput2))
    print(divide(userInput,userInput2))


def add(a,b):
    return (a+b)

def subtract(x,y):
    return (x-y)

def multiply(e,m):
    return(e*m)

def divide(o,w):
    return (o/w)
    ### Problem 4:
#Create a function that will ask the user for a number.
# Use the function to get two numbers, then pass the two numbers to a function and ask a user if they want to add, subtract, multiple, or divide them.
# Return a string that prints the two numbers, which operation it did, and the result.

def problem4():
    userInput=int(input("Enter a number."))
    userInput2= int(input("Enter a number."))
    userop=input("which operation do you want?")
    if userop =="add":
        print(add(userInput,userInput2))
    elif userop =="multiply":
        print(multiply(userInput,userInput2))
    elif userop=="subtract":
        print(subtract(userInput,userInput2))
    elif userop=="divide":
        print(divide(userInput,userInput2))
    else:
        print("INVALID OPERATION")




if __name__ == '__main__':
    main()