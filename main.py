"""
A simple command line ticketing system application.

Script is intended to mimic a basic support ticketing system like ServiceNow.
It allows users to create and view support tickets and to add and search a simple Knowledge Base for solutions to common problems.

Created by : Nadia Willingham
Date: August 31, 2025

"""
import json
import os

# blueprint for single KB article
class Article:
    def __init__(self, title, solution):
        self.title = title
        self.solution = solution

#manages kb articles

class KnowledgeBase:
    def __init__(self):
        self.articles = []

    def add_article(self, title, solution):
        new_article = Article(title, solution)

        self.articles.append(new_article)
        print("Knowledge base article added successfully")

    def search_articles(self, keyword):
        print("\n--- Searching Knowledge Base ---")
        found_article = False

#go through each article

        for article in self.articles:
            #check if keyword is in title or solution
            if (keyword.lower() in article.title.lower() or
                keyword.lower() in article.solution.lower()):
                print(f"\n-- Found Article --\nTitle: {article.title}\nSolution: {article.solution}")
                found_article = True

        if not found_article:
            print("No matching articles found.")

# base for a ticket
class Ticket:
# counter belongs to the class, not to a single ticket
    ticket_counter = 1

    def __init__(self, user, description, priority):
    # - - - Values from the user - - -
        self.user = user
        self.description = description
        self.priority = priority

    # - - - Values set by the system - - -
        self.ticket_id = Ticket.ticket_counter
        self.status = "Open"
        self.notes = []

    # - - - Increase the class counter for the next ticket - - -
        Ticket.ticket_counter += 1

# this function acts like a database, uses a list to act as a container, to hold our tickets
class TicketingSystem:
    def __init__(self):
        # Create an empty list to store tickets
        self.tickets = []

    def create_ticket(self, user, description, priority):

        # check for duplicate descriptions (case-insensitive)

        for ticket in self.tickets:
            if ticket.description.lower() == description.lower() and ticket.status == "Open":
                print(f"Warning: A similar open ticket already exists (Ticket #{ticket.ticket_id})")
            response = input("Do you still want to create this ticket? (yes/no): ").strip().lower()
            if response != "yes":
                print("Ticket creation cancelled.")
                return
            break #exit the loop if user want to proceed

        # create a new ticket object using the provided info
        new_ticket = Ticket(user, description, priority)

    # add it to the list
        self.tickets.append(new_ticket)
        print(f"Ticket {new_ticket.ticket_id} created successfully")

    def view_tickets(self):
        print("\n--- All Open Tickets ---")
        # go through each ticket in the list

        for ticket in self.tickets: # check if ticket's status is "Open"

            if ticket.status == "Open": #print the details

                print(f"ID: {ticket.ticket_id}, User: {ticket.user}, Priority: {ticket.priority}, Issue: {ticket.description}")

    def close_ticket(self, ticket_id):
        # Find ticket by ID
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id and ticket.status == "Open":
                ticket.status = "Closed"
                print(f"Ticket {ticket_id} has been closed.")
                return
        print(f"Ticket {ticket_id} not found or already closed.")


    def save_tickets(self, filename="tickets.json"):
        """Save all tickets to a JSON file"""

        tickets_data = []
        for ticket in self.tickets:
            tickets_data.append({
                "ticket_id": ticket.ticket_id,
                "user": ticket.user,
                "description": ticket.description,
                "priority": ticket.priority,
                "status": ticket.status,
                "notes": ticket.notes
            })

        with open(filename, 'w') as f:
            json.dump({
                "tickets": tickets_data,
                "counter": Ticket.ticket_counter
            }, f, indent=2)
        print("Tickets saved successfully.")

    def load_tickets(self, filename="tickets.json"):
        """Load tickets from a JSON file"""
        if not os.path.exists(filename):
            return # there is no file to load
        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            # restore the ticket counter
            Ticket.ticket_counter = data.get("counter", 1)

            # Recreate tickets
            for ticket_data in data.get("tickets", []):
                ticket = Ticket(
                    ticket_data["user"],
                    ticket_data["description"],
                    ticket_data["priority"]
                )

                # override the auto-generated values
                ticket.ticket_id = ticket_data["ticket_id"]
                ticket.status = ticket_data["status"]
                ticket.notes = ticket_data["notes"]

                self.tickets.append(ticket)

                #adjust counter to avoid ID conflicts
                Ticket.ticket_counter = max(Ticket.ticket_counter, ticket.ticket_id + 1)

            print(f"Loaded {len(self.tickets)} ticket(s) from file.")
        except Exception as e:
            print(f"error loading tickets: {e}")

        print("------------------------------")

#this the start button to the program

if __name__ == "__main__":
    system = TicketingSystem()
    kb = KnowledgeBase()

    # load existing tickets
    system.load_tickets()


    #KB article for demo
    kb.add_article("How to reset password", "1. Select Password reset button. \n2. Enter your email address. \n3 Follow the instructions sent to your email. ")

    system.create_ticket("Admin", "Initial system setup", "Low")

    while True:
                print("\n--- Ticketing System Menu ---")
                print("1. Create a new ticket")
                print("2. View all open tickets")
                print("3. Close a ticket")
                print("4. Add a KB article")
                print("5. Search the Knowledge Base")
                print("6. Exit")

                choice = input("Enter your choice (1-6): ")

                if choice == "1":  #ask for the three pieces of needed info

                    # Validate user name
                    while True:
                        user = input("Enter your name: ").strip()
                        if user:  #check if not empty
                            break
                        else:
                            print("Name cannot be empty. Please try again.")

                    # Validate description
                    while True:
                        description = input("Enter the issue description: ").strip()
                        if description:
                            break
                        else:
                            print("Description cannot be empty. Please try again.")

                    allowed_priorities = ["High", "Medium", "Low"]  # implement input validation for priority of ticket using a while loop
                    while True:
                        priority = input("Enter the priority (High, Medium, Low): ").strip().capitalize()
                        if priority in allowed_priorities:
                            break #Exit the loop if input is valid
                        else:
                            print("Invalid priority. Please enter High, Medium, or Low.")

                    # Call the method with the user's input

                    system.create_ticket(user, description, priority)
                    system.save_tickets()  # saves immediately after closing

                elif choice == "2":
                    system.view_tickets()

                elif choice == "3":
                    try:
                        ticket_id = int(input("Enter ticket ID to close: "))
                        system.close_ticket(ticket_id)
                        system.save_tickets() # saves immediately after closing
                    except ValueError:
                        print("Invalid ticket ID. Please enter a number.")

                elif choice == "4":
                    title = input("Enter article title: ")
                    solution = input("Enter article solution: ")
                    kb.add_article(title, solution)
                    system.save_tickets()  # saves immediately after closing

                elif choice == "5":
                    keyword = input("Enter a search keyword: ")
                    kb.search_articles(keyword)

                elif choice == "6":
                    system.save_tickets()                #auto save when exiting.
                    print("Exiting the system. Goodbye!")
                    break

                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")