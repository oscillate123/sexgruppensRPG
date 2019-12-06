def validate_int():
    while True:
        try:
            age = int(input("Give me int : "))
        except ValueError:
            print("Wrong format, try again.")
            continue
        else:
            return age

def validate_str():
    while True:
        name = input("Give me str : ")

        if name.isalpha() or name == "":
            return name.lower().capitalize()
        else:
            print("Wrong format, try again.")
            continue

def validate_name():
    while True:
        name = input("Give me name : ")

        if name.isalpha():
            return name.lower().capitalize()
        else:
            print("Wrong format, try again.")
            continue

#TESTA
hej2 = validate_int()
hej3 = validate_str()
print(validate_name())
