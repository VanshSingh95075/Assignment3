#QUESTION1
n=int(input("Enter your number"))

d=[]

while n>0:

    k=n%2
    n=n//2
    d.append(k)
d.reverse()
print("binary code is :",d)
for i in d:
    print(i,end="")


#QUESTION2
# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
        
        
        
        
        import math

#Question3A
 print((3+4)*5)
#Question3B
 print((n*(n-1)/2))
#Question3C
 print(4*3.14*r*r)
#Question3D
 print(math.sqrt((r*(math.cos(a)))**2+math.sqrt((r*(math.cos(b)))**2))
#Question3E
 


#Question4A
for i in range(5):
 print (i)
#Question4B
for i in range(3,10):
 print (i)
#Question4C
for i in range(4,13,3):
 print (i)
#Question4D
for i in range(15,5,-2):
 print (i)
#Question4E
for i in range(5,3): 
 print (i)
 
 
#QUESTION5 
 
 a = int(input("Enter number of hydrogen"))
b = int(input("Enter number of carbon"))
c = int(input("Enter number of oxygen"))


k=a*1.00794+b*12.0107+c*15.9994

print("Molecular weight of carbohydtate is:",k)
