
# python module with function collection to print shapes 

def square():
    """Function to draw a square pattern"""
    
    print("you choosed to print SQUARE pattern..")
    n=int(input("Enter No of Rows:"))
    for i in range(n):
        print('*'*n)

        
def traingle():
    """Function to draw a triangle"""
    
    print("You choosed to print Right Angled Triangle pattern...")
    n=int(input("Enter No of Rows:"))
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()
        

def diamond():
    """Function to draw a diamond"""
    
    print("You Choosed to print Diamond pattern...")
    n=int(input("Enter n values:"))
    for i in range(n):
        print(' '*(n-i-1)+'*'*(i+1))
    for i in range(n-1):
        print(' '*(i+1)+'*'*(n-i-1))