# Hello World!
# print("Hello World!")

# Get Input from user, print it out onto terminal (Concatenation)
'''
userInput = input()
print("You said: " + userInput)
print(f"You said: {userInput}")
'''

# I am buying 32 oranges, 5 apples, and 4 bananas at the store
# Example of using an f string to optimize print statements
'''
numOranges = 32
numApples = 5
numBananas = 4


print (f"I am buying {numOranges} oranges, {numApples} apples, {numBananas} bananas at the store")
'''

# integers are whole numbers and can be negative

sampleint =-1

# doubles are decimals number

sampledouble = 6.89898979

# string
samplebool = False

#List

samplelist = [34, 165, 452, 2333, 54, 45]
try:
print (samplelist[10])
except Exception as e:
    print(e)
print(f"length of samplelist: {len(samplelist)}")
