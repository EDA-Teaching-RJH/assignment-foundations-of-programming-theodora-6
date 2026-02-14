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
    division = input ("enter division: ")

    try:
        crew_id = int(input("enterID:"))
    except ValueError:
        print("invalid ID. Must be a number.")

        valid_ranks = ["captain", "commander", "lieutenant commander", "lieutenant", "ensign"]

        if crew_id in ids:
             print("error: rank already exists.")
             return
        
        if rank not in valid_ranks:
             print("error: invalid rank.")
             return
        
        names.append(name)
        ranks.append(rank)
        divisions.append(division) 
        ids.append(crew_id)        

        print("crew member added successfully.")

def remove_member(names, ranks, divisions, ids):
             
             remove_id = input("enter ID to remove: ")

             if remove_id in ids:
                  index = ids.index(remove_id)

                  names.pop(index)
                  ranks.pop(index)
                  divisions.pop(index)
                  ids.pop(index)

                  print("crew member re,oved successfully.")
             else:
                  print("error: ID not found.")
                
def update_rank(names, ranks, ids):
      
    update_ids = input("enter ID to update rank: ")

    if update_ids in ids:
          index = ids.index(update_ids)
          new_rank = input("enter new rank: ")
          ranks[index] = new_rank
          print("rank updated successfully")
    else:
          print("Error ID not found.")

def display_roster(names, ranks, divisions, ids):
      
      print("\n===== Crew Roster =====")
      print(f"{'ID':<6} {'name':<25} {'rank':<20} {'division':<15}")
      print("-" * 70)

      for i in range(len(names)):
            print(f"{ids[i]<6} {names[i]:<25} {ranks[i]:<20} {divisions[i]:<15}")

def search_crew(names, ranks, divisions, ids):
      
      term = input("enter name search term: ").lower()
      found = False

      for i in range(len(names)):
            if term in names[i].lower():
                  print (f"found: {names[i]} | {ranks[i]} | {divisions[i]} | {ids[i]}")
                  found = True
        
            if not found: 
                print("no matching crew members found.")

def filter_by_division(names, divisions):

      division = input("enter division (command, operations, sciences): ")

      print(f"/nMembers in {division} Division: ")
      for i in range(len(names)):
            if divisions[i] == division:
                  print(names[i])

def calculate_payroll(ranks):
      
      pay = {"captain": 1000, "commander": 800, "lieutenant commander": 600, "lieutenant": 400, "ensign": 200}

      total = 0

      for rank in ranks:
            total += pay.get(rank, 0)

      return total

def count_officers(ranks):
      
      count = 0

      for rank in ranks:
            if rank == "captain" or rank == "commander":
                  count+= 1

      return count