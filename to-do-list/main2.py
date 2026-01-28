# to-do-list project
# function: add element, del element, view tasks, save to file 

from pathlib import Path
import csv


def add_list(id, matter, list):
    """add element to list"""
    matter = {
        'id': id,
        'description': matter,
        'completed': 'False'
    }
    list.append(matter)
    print_list(list)

def mark_list(mark_number, list):
    """mark element to list"""
    n = int(mark_number)
    try:
        list[n]
    except IndexError:
        if not list:
            print("The list is empty!")
        else:
            print("There is not such number!")
        pass
    else:
        list[n]['completed'] = 'True'
        print_list(list)

def delete_list(delete_number, list):
    """del element to list"""
    n = int(delete_number)
    try:
        del list[n]
    except IndexError:
        if not list:
            print("The list is empty!")
        else:
            print("There is not such number!")
        pass
    else:
        print_list(list)

def print_list(list):
    """print the list"""
    print("The To-do list:")
    for index, values in enumerate(list):
        if values['completed'] == 'True':
            print(f"\t[✅] {index}, {values['description']}")
        else:
            print(f"\t[  ] {index}, {values['description']}")

def save_list(list):
    """save list to file"""
    with open("to-do-list.csv", "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'description', 'completed'])
        writer.writeheader()
        writer.writerows(list)

path = Path('/home/loong/python/small-projects/to-do-list/to-do-list.csv')
try:
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        to_do_string = list(reader)
except FileNotFoundError:
    to_do_list = []
    pass
else:
    to_do_list = to_do_string
n = ""
print("Welcome to to-do list")
while n != "q":
    print("\n\t Add the to-do matter please input: a")
    print("\t Mark the to-do matter please input: m")
    print("\t Del the to-do matter please input: d")
    print("\t View the to-do list please input: v")
    print("\t Save the to-do list please input: s")
    print("\t Close the program please input: q or any others input")
    n = input("\nPlease input you choice: ")

    if n == "a":
        to_do = input("Please input you to-do matter: ")
        id = len(to_do_list)
        add_list(id, to_do, to_do_list)
    elif n == "m":
        print_list(to_do_list)
        matter_number = input("Please input the mark matter number: ")
        mark_list(matter_number, to_do_list)
    elif n == 'd':
        print_list(to_do_list)
        delete_number = input("Please input the delete matter number: ")
        delete_list(delete_number, to_do_list)
    elif n == "v":
        print_list(to_do_list)
    elif n == "s":
        save_list(to_do_list)
    else:
        n = "q"
