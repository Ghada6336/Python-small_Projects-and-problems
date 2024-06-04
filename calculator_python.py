# define the function needed in this calculator  [add,sub, mul,div]
# print the option to the user
def add(a, b):
    answer = a+b
    print(str(a) + "+" + str(b)+"="+str(answer))


def sub(a, b):
    answer = a-b
    print(str(a) + "-" + str(b)+"="+str(answer))


def mul(a, b):
    answer = a*b
    print(str(a) + "*" + str(b)+"="+str(answer))


def div(a, b):
    answer = a/b
    print(str(a) + "/" + str(b)+"="+str(answer))

# to stay in caluclator until exit
# while True:


print("A: Addition")
print("B: Subtraction")
print("C : Multiplication")
print("D: Division")
print("E: Exit")

choice = input("enter your choice")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    add(a, b)
elif choice == "b" or choice == "B":
    print("Subtraction")
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    sub(a, b)
elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    mul(a, b)
elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    div(a, b)
elif choice == "e" or choice == "E":
    print("Exist")
    quit()
