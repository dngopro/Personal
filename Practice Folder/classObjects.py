import os
import json

os.system("cls")

class classicalComposer:
	type = "composer"
	
	def __init__(self, name, era, piece): 
		self.name = name
		self.era = era
		self.piece = piece
		
	def compose(self):
		return f"{self.name} composed {self.piece}."
	
	def describe(self):
		return f"{self.name} is a {self.type} from the {self.era} era."

def update_json(friends):
    data = {}
    for name, composer in friends.items():
        data[name] = {
            "name": composer.name,
            "era": composer.era,
            "piece": composer. piece
        }
    with open("friends.json", "w") as file:
        json.dump(data, file, indent=4)

def load_friends():
    if not os.path.exists("friends.json"):
         return {}
    with open("friends.json", "r") as file:
         data = json.load(file)

    friends = {} 
    for name, comp_data in data.items():
         friends[name] = classicalComposer(
              comp_data["name"],
              comp_data["era"],
              comp_data["piece"]
         )
    return friends

def add_friends(friends):
    while True:
        print("Type 'Return' at any time to exit editing.\n")
        friend = input("Enter new friend's name: \n").strip().title()
        if friend == "Return":
             return
        
        name = input("Enter the composer's name: \n").strip().title()
        if name == "Return":
             return
        
        era = input("Enter the era this composer is from: \n").strip().title()
        if era == "Return":
             return
        
        piece = input("Enter the name of a piece this composer wrote: \n")
        if piece == "Return":
             return

        os.system("cls")

        print("Here is the information you inputted. Is this correct?")
        print(f"Name: {friend}\nComposer: {name}\nEra: {era}\nPiece: {piece}")
        confirm = input("\nType 'Yes' or 'No': \n")
        
        if confirm == "Yes":
            friends[friend] = classicalComposer(name, era, piece)
            update_json(friends)
            input("\nFriend added! Press Enter to continue.")
            break
        elif confirm == "No":
            input("\nNew friend information was not added. Press Enter to continue.")
            return
        else:
            input("\nUnrecognized input. Press Enter to return.")
            return


def edit_friends(friends):
    print("Available friends:", ", ".join(friends))
    friend_to_edit = input("\nEnter the name of the friend to be edited: \n").strip().title()
    os.system("cls")

    if friend_to_edit in friends:

        while True:
            os.system("cls")
            friend_obj = friends[friend_to_edit]
            print(f"{friend_to_edit}'s favorite composer is {friend_obj.name}.")
            print(friend_obj.describe())
            print(friend_obj.compose())

            edit = input(f"\nWhich information of {friend_to_edit} would you like to edit? (Name, Era, Piece) \nType 'Return' to return to the previous page.\n").strip().title()

            if edit == "Name":
                friend_obj.name = input(f"Enter the new {edit}: \n").strip()
            elif edit == "Era":
                friend_obj.era = input(f"Enter the new {edit}: \n").strip()
            elif edit == "Piece":
                friend_obj.piece = input(f"Enter the new {edit}: \n").strip()
            elif edit == "Return":
                return
            else:
                input("Unrecognized detail. Press Enter to return.")
                return

            update_json(friends)
            os.system("cls")

            print(f"\n{friend_to_edit}'s information has been successfully edited. Here is the updated information: \n")
            print(f"{friend_to_edit}'s favorite composer is {friend_obj.name}.")
            print(friend_obj.describe())
            print(friend_obj.compose())
            again = input("\nWould you like to make any other edits? Type 'Yes' or 'No':\n").strip().title()
            
            if again == "No":
                 break

    else:
        input("Friend not found. Press Enter to return.") 


def delete_friends(friends): 
    print("Available friends:", ", ".join(friends))
    friend_to_delete = input("\nEnter the name of the friend to be deleted: \n").strip().title()
    os.system("cls")

    if friend_to_delete in friends:
        del (friends[friend_to_delete])
    
        update_json(friends)
        input("\nFriend has been successfully deleted. Press Enter to return.")

    else:
        input("Friend not found. Press Enter to return.") 

friends = load_friends()

while True:

    print("Available friends:", ", ".join(friends),"\n")
    print("Type a name to continue. Other options:\n'Add' to add a new entry.\n'Edit' to edit an existing entry.\n'Delete' to remove an entry.\n'Quit' to exit the program.\n")
    choice = input("Whose favorite composer do you want to see? \n").strip().title()
    os.system("cls")

    if choice == "Quit":
        print("\n Quitting now. Goodbye!")
        break

    elif choice == "Add":
        add_friends(friends)

    elif choice == "Edit":
        edit_friends(friends)

    elif choice == "Delete":
        delete_friends(friends)
        
    elif choice in friends:
        favComposer = friends[choice]
        print(f"{choice}'s favorite composer is {favComposer.name}.")
        print(favComposer.describe())
        print(favComposer.compose())
        choice = input("\nPress Enter to continue or 'Quit' to exit. \n")
        
    else:
        print("Friend not found.")
        choice = input("\nPress Enter to continue or 'Quit' to exit. \n")

    os.system("cls")

    if choice == "Quit":
        print("\n Quitting now. Goodbye!")
        break