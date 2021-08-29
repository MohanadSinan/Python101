def actions_list():
    print()
    print('1. Find by Phone Number')
    print('2. Find by Name')
    print('3. Add a New Phone Number')
    print('4. Quit')


phonebook = {'Amal': 1111111111, 'Mohammed': 2222222222, 'Khadijah': 3333333333, 'Abullah': 4444444444,
             'Rawan': 5555555555, 'Faisal': 6666666666, 'Layla': 7777777777}


def find_name(phone):
    key_list = list(phonebook.keys())
    val_list = list(phonebook.values())
    position = val_list.index(int(phone))
    name = key_list[position]
    return name


def find_number(name):
    return phonebook[name]


def add(name, phone):
    phonebook[name] = phone
    print('Name:', name, '\tNumber:', phone, '\tAdded Successfully!')


action = 0
while action != 4:
    actions_list()
    print()
    action = int(input("Choose your action: "))
    print()
    if action == 1:
        while True:
            try:
                number_to_find = int(input('Enter the Phone Number: '))
            except ValueError:
                print('This is invalid Number')
                continue
            if len(str(number_to_find)) != 10:
                print('This is invalid Number')
                continue
            else:
                break
        if number_to_find in phonebook.values():
            print(find_name(number_to_find))
        else:
            print('Sorry, the Number is not found')
    elif action == 2:
        name_to_find = input('Enter the Name: ')
        if name_to_find in phonebook:
            print(find_number(name_to_find))
        else:
            print('Sorry, the Number is not found')
    elif action == 3:
        name_to_add = input('Enter the Name: ')
        while True:
            try:
                phone_to_add = int(input('Enter the Phone Number: '))
            except ValueError:
                print('This is invalid Number')
                continue
            if len(str(number_to_find)) != 10:
                print('This is invalid Number')
                continue
            else:
                break
        add(name_to_add, phone_to_add)
    elif action == 4:
        print('Quitting ...')
    else:
        print("ERROR: Invalid input")
