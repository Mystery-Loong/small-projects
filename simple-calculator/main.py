print("Welcome to use Simple-calcurator")
a = input("Please input the first number: ")
if not isinstance(a, int):
    print("Please input the int number!")
b = input("Please input the second number: ")
operator = input("Please input operator(+ - * /): ")
c = 0
if operator == '+':
    c = int(a) + int(b)
    print(c)

print(c)