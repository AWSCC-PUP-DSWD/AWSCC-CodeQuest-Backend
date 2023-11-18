import json
import os

def print_menu():
    menu = ["1 - Add Username and Password",
            "2 - View",
            "3 - Search",
            "4 - Delete",
            "5 - Update",
            "6 - Exit"]
    
    for i in menu:
        print(i)

def check_input(_input):
    global running

    if _input == "1":
        add()
    elif _input == "2":
        view()
    elif _input == "3":
        website = input("Enter website: ")
        search(website)
    elif _input == "4":
        existing = False
        while not existing:
            website = input("Enter website: ")
            existing = is_existing(website)
        delete(website)
    elif _input == "5":
        existing = False
        while not existing:
            website = input("Enter website: ")
            existing = is_existing(website)
        update(website)
    elif _input == "6":
        running = False

def is_existing(website):
    with open('data.json', 'r') as f:
        data = json.load(f)
        if website in data:
            return True
        return False

def add():
    website = input("Enter website: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    new_data = {
        website: [{
            'email': email,
            'password': password
        }]
    }

    with open('data.json', 'r') as f:
        data = json.load(f)
    
    if website in data:
        data[website].append({'email': email, 'password': password})
    else:
        data.update(new_data)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    os.system('cls')
    print("Successfully added!")
    
def view():
    os.system('cls')
    with open('data.json', 'r') as f:
        data = json.load(f)
        for key, val in data.items():
            print(f"Website: {key}")
            for i in range(len(val)):
                print(f"    Email: {val[i]['email']}")
                print(f"    Password: {val[i]['password']}\n")

def search(website):
    with open('data.json', 'r') as f:
        data = json.load(f)
        for key, val in data.items():
            if key == website:
                print(f"Website: {key}")
                for i in range(len(val)):
                    print(f"    {i+1} Email: {val[i]['email']}")
                    print(f"      Password: {val[i]['password']}\n")
                return True
            
        print("No websites found.")
        return 
    
def delete(website):
    with open('data.json', 'r') as f:
        data = json.load(f)
        search(website)

        valid_idx = False
        while not valid_idx:
            num = int(input("Enter the number you want to delete: "))
            valid_idx = 0 <= num-1 < len(data[website])
    
        data[website].pop(num-1)

        if len(data[website]) == 0:
            data.pop(website)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Successfully removed.")

def update(website):
    with open('data.json', 'r') as f:
        data = json.load(f)
        search(website)

        valid_idx = False
        while not valid_idx:
            num = int(input("Enter the number you want to update: "))
            valid_idx = 0 <= num-1 < len(data[website])

        to_update = input("'email' or 'password': ").lower()
        new_val = input(f"Enter your new {to_update}: ")
        data[website][num-1][to_update] = new_val

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Successfully updated!")

running = True

while running:
    print("=======PASSWORD MANAGER=======")
    print_menu()
    user_input = input("Enter a number: ")
    check_input(user_input)