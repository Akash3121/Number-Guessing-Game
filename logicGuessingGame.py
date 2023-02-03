#user need to enter a number, that number we will check it.
import math
print("***Game of Guess***")
end = int(input("enter the max cap number: "))
number = int(input("enter your input numer b/w 1 and " + str(end) + ": "))

trys = 3
# check if input number is between 1 and max cap number(end)
while trys > 0 and (number > end or number < 1):
    print("Number is not in the range, please retry, tries left - " + str(trys))
    number = int(input("enter your input numer b/w 1 and " + str(end) + ": "))
    trys -= 1
    if trys == 0:
        print("sorry, your chances are completed")

# algorithm used binary search
target = number
steps = 0
start = 1
while start <= end:
    mid = start + (end - start) // 2
    if mid < target:
        start = mid + 1
        print("Guessed number " +str(mid)+ " is less than target")
    elif mid > target:
        end = mid - 1
        print("Guessed number " + str(mid) + " is greater than target")
    else:
        print("Hurray! we found")
        break
    steps += 1
    print("Steps taken: "+str(steps))
    
print("Total Steps taken: " +str(steps + 1))
# print("Binary Search" + str(math.log10((number))))
print("Exiting the game")