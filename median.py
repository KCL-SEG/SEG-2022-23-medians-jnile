"""Median calculator."""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
        break
    else:
        break

#Sort the numbers list
numbers.sort()
#find the middle number
if(len(numbers)%2 == 0):
    #2 middle numbers
    leftNo = numbers[int(len(numbers)/2 - 1)]
    rightNo = numbers[int(len(numbers)/2)]
    print((leftNo + rightNo)/2)
else:
    #1 middle number
    print(numbers[int((len(numbers)-1)/2)])
