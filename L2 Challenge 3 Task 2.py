def readable(data):
    people = []
    for first_name, details in data.items():
        person_info = f"""Name: {first_name} {details.get("Surname")}
Age: {details.get("Age")}
Employed: {details.get("Employed")}\n"""
        people.append(person_info)
    return "\n".join(people)


def add_person(data):
    name = input("Please enter your full name: ")
    first_name = name.split(" ")[0].capitalize()
    surname = name.split(" ")[1].capitalize()
    age = input("Please enter your age: ")
    employed = input(
        "Please enter a Yes if you're employed or a No if you're not: ").capitalize()
    data[first_name] = {"Surname": surname,
                        "Age": int(age), "Employed": employed}
    choice = input("Is that the only person you wanted to add? ")
    if choice.capitalize() == "Yes":
        return readable(data)
    else:
        return add_person(data)


def remove_person(data):
    name = input("Please enter a name: ")
    first_name = name.split(" ")[0].capitalize()
    if first_name in data:
        data.pop(first_name)
        choice = input(("Is that the only person you wanted to remove? "))
        if choice.capitalize() == "Yes":
            return readable(data)
        else:
            return remove_person(data)
    else:
        return "That person is not in the dictionary"


people = {"Jane": {"Surname": "Doe", "Age": 42, "Employed": "Yes"},
          "Tom": {"Surname": "Smith", "Age": 18, "Employed": "Yes"},
          "Mariam": {"Surname": "Coulter", "Age": 66, "Employed": "No"},
          "Gregory": {"Surname": "Tims", "Age": 8, "Employed": "No"}}

user_input = input("Do you want to Add or Remove: ").capitalize()
if user_input == "Add":
    print(add_person(people))
elif user_input == "Remove":
    print(remove_person(people))
else:
    print("Value entered was not Add or Remove")
