from command_processor import show_help_file, add_update_contact, show_all, show_phone
from command_parser import parse_input_data

close_commands = ("exit", "close")

def main():
    user_name = input("Enter your name >>> ")
    print(f"Welcome {user_name} to the assistant bot!")
    all_contacts = {}

    while True:
        try:
            user_data = input("Enter the command >>> ")
            command, *args = parse_input_data(user_data)
            
            if command in close_commands:
                print(f"Good bye {user_name}!")
                break

            match command:
                case "hello":
                    print("How can I help you?")
                case "add":
                    print(add_update_contact(args, False, all_contacts))
                case "change":
                    print(add_update_contact(args, True, all_contacts))
                case "phone":
                    print(show_phone(args, all_contacts))
                case "all":
                    print(show_all(all_contacts))
                case _: 
                    print("Invalid command.")
                    input_command = input("Would you like to see all commands list? Y/N >>> ").strip().lower()
                    if(input_command == 'y'):
                        print(show_help_file())
        except Exception as error:
            print("Error happened: ", error)

if __name__ == "__main__":
    main()