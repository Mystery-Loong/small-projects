# to-do-list project
# function: add element, del element, view tasks, save to file 

from pathlib import Path


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
    to_do_string = '\n'.join(list)
    print(to_do_string)
    path.write_text(to_do_string)

path = Path('/home/loong/python/small-projects/to-do-list/to-do-list.txt')
to_do_string = path.read_text()
to_do_list = to_do_string.splitlines()
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
    elif n == "s":
        save_list(to_do_list)
    else:
        n = "q"
