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
        print("1. Add Member")
        print("2. Remove Member")
        print("3. Update Rank")
        print("4. Display Roster")
        print("5. Search Crew")
        print("6. Filter by Division")
        print("7. Calculate Payroll")
        print("8. Count Senior Officers")
        print("9. Exit")
        print ("=================================")

        choice = input ("choose an option: ")
        return choice
display_menu()

def add_member(names, ranks, divisions, ids):
      
    name = input ("enter name: ")
    rank = input ("enter rank: ")
    division = input ("enter divisions: ")

    try:
        crew_id = int(input("enterID:"))
    except ValueError:
        print("invalid ID. Must be a number.")

        valid_ranks = ["captain", "commander", "lieutenant commander", "lieutenant", "ensign"]

        if crew_id in ids:
             print("error: invali rank.")
             return
        
        if rank not in valid_ranks:
             print("error: nvalid rank.")
             return
        
        names.append(name)
        ranks.append(rank)
        divisions.append(division) 
        ids.append(crew_id)        

        print("crew member added successfully.")