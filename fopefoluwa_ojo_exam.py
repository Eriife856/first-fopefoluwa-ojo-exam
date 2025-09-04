#basic_calculation
#define the functions
def add (a ,b):
    return(a + b)

def sub (a,b):
    return(a - b)

def divide (a,b):
    if b!=0:
     return(a / b)
    else:
        print("error: divison by zero")

def multiply (a,b):
    return (a * b)

#operation function
print(" welcome to basic calculator")
print("1. Add")
print ("2. subtract")
print("3. division")
print("4. multiply")
print("0. exit")

while True:
    try:
        choice = input("kindly input 1/2/3/4/0: ")
        if choice == "0":
            print("exiting! Do have a wonderful day")
            break

        num1 = int(input("enter your first number: "))
        num2 = int(input("enter your second number: "))

        if choice == "1":
            print(f"{num1}+{num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1}-{num2} = {sub(num1, num2)}")
        elif choice == "3":
            result = divide(num1, num2)
            if result is not None:
                print(f"{num1}/{num2} = {result}")
        elif choice == "4":
            print(f"{num1}*{num2} = {multiply(num1, num2)}")
        else:
            print("Invalid input. Try again")
    except Exception as e:
        print(e)



# # Question 2
# while True:
#     user_input = input("enter a number(or type 'exit to quit):")
#     if user_input == "exit":
#         print("Goodbye!")
#     else:
#          break 
    
#     num = int(input("enter a number: "))
#     if num % 2 == 0:
#         print("The number is an even number")  
#     else:
#         print("The number is an odd number")
        
#question 3
while True:
    age = int(input("Enter your age (or type exit to quit: ") )
    try:
     if age >= 18:
        print("you can vote")
     elif age == "exit":
        print("Goodbye!")
        break
     else:
      print("You cannot vote")
    except Exception as e:
     print("Invalid input")







