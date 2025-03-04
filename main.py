
# Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    return (a + b)
    
def sub(a,b):
    return(b-a)
    
def mul(a,b):
    return(a*b)
    
def div(a,b):
    return(b/a)
    
i=0
while(i!=5):
    print("Hello, Welcome to Calculator")
    print("What do you want to do?")
    print("1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Exit")
    i=int(input("Enter your Choice {1|2|3|4|5} : "))
    if(i==1):
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
        print(f'Sum of {a} and {b} is {sum(a, b)}')
    elif(i==2):
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
        print(f'Difference of {a} from {b} is {sub(a, b)}')
    elif(i==3):
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
        print(f'Multiplication of {a} and {b} is {mul(a, b)}')
    elif(i==4):
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
        print(f'Division of {b} by {a} is {div(a, b)}')
    elif(i==5):
        print("Thank You for using Calculator")
        quit()
    else:
        print("Invalid Input, Please Try Again")
    
