#CALCULATOR

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2 == 0:
        print("None")
    else:
        return num1 / num2
    
def calculator():
    print("==== CALCULATOR ====")
    
    print("\nSelect an option")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")    
    
    choice = input("Enter choice between 1,2,3,4: ")
    num1 = float(input("Enter the 1st number:"))
    num2 = float(input("Enter the 2nd number:"))
    
    if choice == '1':
        result = add(num1,num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = sub(num1,num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1,num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1,num2)
            
        if result != None:
            print(f"Result: {num1} / {num2} = {result}")
        
    else:
        print("Invalid choice choosen!!")

calculator() 
    