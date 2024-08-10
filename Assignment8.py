#Largest cities in China. What would NYC be like if it had the population of Shanghai?
myList = ["Shanghai","Beijing","Guangzhou","Chongqing","Chengdu","Tianjin","Shenzhen","Harbin"] 
print(myList)

myList2 = myList[1:]
print(myList2)

myList2.append("Wuhan")
print(myList2)

myList3 = myList2.pop(2)
print(myList3)

#Count - A function to count the number of occurrences of a substring in a string.
txt = " The largest city in China is Shanghai with a population several times that of New York City. " 
countResult = txt.count("c",0,30)

#The count function is case sensitive so it only returns a result of 1.
print(countResult)

#Function to check if a string ends with the punctuation sign passed to the function.
endsWithResult = txt.endswith(".")
print(endsWithResult)

#Function to find the first occurrence of a specified value and returns the index. 
# Index is similar but returns an exception if the value is not found rather than -1.
findResult = txt.find("with")
print(findResult)

#Function to join all the elements of an iterable into a string, 
# using a specified character as a separator.
joinResult = " ".join(myList)
print(joinResult)

#Function to create a string where one value has been replaced with another.
replaceResult = joinResult.replace("Beijing","Replaced")
print(replaceResult)

#Function to turn a string into a list using a specified value as a delimiter. 
#For this I will use the default value of a space.
splitResult = joinResult.split()
print(splitResult)

#Function to split a string into a list at the line breaks.
txt2 = "Thanks for the memories, even though they weren't so great.\n -Fallout Boy"
splitlinesResult = txt2.splitlines()
print(splitlinesResult)

#Function to check if a string starts with a specified value. 
# The default action is start at the beginning of a string, but you can specify a 
# start and end position.
startswithResults = txt2.startswith("Thanks")
startswithResults2 = txt2.startswith("anks", 2, 30)
print(startswithResults)
print(startswithResults2)

#Function to strip either leading and trailing spaces from a string, 
# or specified characters.
print(txt)
stripResults = txt.strip()
print(stripResults)
stripResults2 = txt.strip(" T,. ")
print(stripResults2)

#Function to test if a number is prime.

def testIfPrime(testNumber):
    if testNumber > 1: #Make sure number isn't equal to one, as one is prime.
        for i in range(2, (testNumber//2)+1): 
            if (testNumber % i) == 0: #Make sure the remainder of a number is not equal to zero.
                print(testNumber, "is not a prime number")
                break
        else:
            print(testNumber, "is a prime number")
    else:
        print(testNumber, "is not a prime number")


testNumber = int(input("Enter a number to test if it is prime."))

testIfPrime(testNumber)

#Function which can take a variable number of arguments

def disStuInfo(schoolID, *firstName, **lastEmail):
    schoolIDFun = schoolID
    firstNameFun = firstName
    lastEmailKeys = lastEmail.keys()
    lastEmailValues = lastEmail.values()
    
    for i in firstNameFun:
        for x in lastEmailKeys:
            for y in lastEmailValues:
                print(schoolIDFun)
                print(i)
                print(x)
                print(y)
                print("\n")
            #print(x, y)
    
disStuInfo(10001,'John','Petter', Smith='jSmith@gmail.com',Potter="Petter@yahoo.com",Doe="j@gmail.com")
            