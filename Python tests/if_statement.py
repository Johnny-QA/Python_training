# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")

# if person in known_people:
#     print("You know {}".format(person))
# else:
#     print("You don`t know {}".format(person))


## Exercise

def who_do_you_know():
    people = input("Enter the names of people you know, separated by commas: ")
    people_list = people.split(",")
    normal_list = [person.strip().lower() for person in people_list]
    return normal_list

    # people_list_without_spaces = []
    # for person in people_list:
    #     people_list_without_spaces.append(person.strip())

    # return people_list_without_spaces

def ask_user():
    person = input("Enter a name of someone you know: ")
    if person.lower() in who_do_you_know():
        return print("You know {}!".format(person))
    else:
        return print("You don`t know {}!".format(person))

ask_user()