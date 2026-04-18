import json

FILE = "students.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def add_student(data):
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    data.append({"name": name, "marks": marks})
    save_data(data)

def view_students(data):
    for s in data:
        print(s["name"], "-", s["marks"])

def search_student(data):
    name = input("Enter name to search: ")
    for s in data:
        if s["name"] == name:
            print("Found:", s)
            return
    print("Not found")

data = load_data()

while True:
    print("\n1.Add 2.View 3.Search 4.Exit")
    choice = input("Choice: ")

    if choice == "1":
        add_student(data)
    elif choice == "2":
        view_students(data)
    elif choice == "3":
        search_student(data)
    elif choice == "4":
        break