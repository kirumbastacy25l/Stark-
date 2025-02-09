print("Calculator programme")



def add(a,b ):
    print(a+b)
def sub(a,b) :
    print(a-b)
def mult(a,b):
    print(a*b)
def div(a,b) :
    print(a/b)

print("My calculator has 4 operators")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("My calc can:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
operator = input("Select an operator: (1-4)")


if operator == "1":
    add(a,b),

elif operator == "2":
    sub(a,b),

elif operator == "3" :
    mult(a,b)

elif operator == "4" :
    div(a , b)

else :
    print("operator invalid")


















