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



def problem2():
    userInput=""
    while userInput.lower()!='q':
        userInput=input("enter a word\n")





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