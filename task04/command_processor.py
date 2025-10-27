from error_handler import input_error

def show_help_file():
    with open("task04\\help.txt", mode="r", encoding="UTF-8") as file_object:
        help_text = file_object.read()
    return help_text

@input_error
def add_update_contact(args, allow_update, all_contacts):
    name = args[0]
    phone = args[1]
    if name in all_contacts.keys() and allow_update == False:
        raise ValueError("This name already exists")
    else:
        all_contacts[name] = phone
        if allow_update == False:
                return "Contact added"
        else:
            return "Contact updated"

@input_error
def show_phone(args, all_contacts):
    name = args[0]
    phone_number = all_contacts.get(name)
    if phone_number is None:
        raise KeyError("This name does not exist yet in contacts")
    return phone_number

@input_error
def show_all(all_contacts):
    if len(all_contacts) > 0:
        return str(all_contacts);
    else:
        raise IndexError("List of contacts is empty yet")
