#spy number

num = int(input("Enter the number to check spy number:"))
temp = num 
sum = 0 
prod = 1
while temp > 0:
    lastdigit = temp % 10 
    sum = sum + lastdigit
    prod = prod * lastdigit
    temp = temp // 10 

print(" The sum of the digit = %d" %sum)
print("The product of the digit = %d" %prod)

if sum == prod:
    print("\n %d is a spy number" %num)
else:
    print("%d is not a spy number" %num)