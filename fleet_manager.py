def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "commander"]
    divisions = ["Command", "Command", "Operations", "Security", "sciences"]
    ids = ["1701", "1702", "1703", "1704", "1705"]

init_database()

def display_menu():

        student = input("\nEnter your full name: ")

        print ("\n=================================")
        print (f"logged in as: {student}")
        print ("starfleet crew manager")
        print ("=================================")
        print ("1. Add member")
        print ("2. Remove member")
        print ("3. Update rank")
        print ("5. Exit")
        print ("=================================")

        choice = input ("choose an option: ")
        return choice
display_menu()