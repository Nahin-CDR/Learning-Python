# Nahin The Coder
# Date : 25 - 07 - 2021

print("Taking input from user horizontally : ")
size = int(input("Enter the Size of array : "))
myList = list(map(int, input("Enter Elements into list ").strip().split()))[:size]
print("Printing Elements of List : ", myList)
