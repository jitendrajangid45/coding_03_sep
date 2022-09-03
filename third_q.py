n = int(input("Enter no of element you want in array:"))
array = []
for i in range(1,n+1):
    array.append(int(input(f"Enter {i} number:")))
sum = 0
print("your array is:",array)
for i in array:
    sum = sum+i

print("SUM of all elements present in array:",sum)
