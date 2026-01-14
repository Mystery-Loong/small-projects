# to-do-list project
# function: add element, del element, view tasks, save to file 
def add_list(matter,list):
    """add element to list"""
    list.append(matter)
    print_list(list)

def del_list(delete_number, list):
    """del element to list"""
    n = int(delete_number)
    del list[n]
    print_list(list)

def print_list(list):
    """print the list"""
    print("The To-do list:")
    for index, value in enumerate(list):
        print(f"\t {index}, {value}")

def save_list(list):
    """save list to file"""

to_do_list = ["go to school", "go home", "working"]
n = ""
print("Welcome to to-do list")
while n != "q":
    print("\n\t Add the to-do matter please input: a")
    print("\t Delete the to-do matter please input: d")
    print("\t View the to-do list please input: v")
    print("\t Save the to-do list please input: s")
    print("\t Close the program please input: q or any others")
    n = input("\nPlease input you choice: ")

    if n == "a":
        to_do = input("Please input you to-do matter: ")
        add_list(to_do, to_do_list)
    elif n == "d":
        print_list(to_do_list)
        matter_number = input("Please input the delete matter number: ")
        del_list(matter_number, to_do_list)
    elif n == "v":
        print_list(to_do_list)
    else:
        n = "q"
