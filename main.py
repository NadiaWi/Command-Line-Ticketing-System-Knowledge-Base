"""
A simple command line ticketing system application.

Script is intended to mimic a basic support ticketing system like ServiceNow.
It allows users to create and view support tickets and to add and search a simple Knowledge Base for solutions to common problems.

Created by : Nadia Willingham
Date: August 31, 2025

"""

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
            #check if keyword (case-insensitive) is in the title
            if keyword.lower() in article.title.lower():
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

        print("------------------------------")

        #this the start button to the program

if __name__ == "__main__":
    system = TicketingSystem()
    kb = KnowledgeBase()

    #KB article for demo
    kb.add_article("How to reset password", "1. Select Password reset button. \n2. Enter your email address. \n3 Follow the instructions sent to your email. ")

    system.create_ticket("Admin", "Initial system setup", "Low")

    while True:
                print("\n--- Ticketing System Menu ---")
                print("1. Create a new ticket")
                print("2. View all open tickets")
                print("3. Add a KB article")
                print("4. Search Knowledge Base")
                print("5. Exit")

                choice = input("Enter your choice (1-5): ")

                if choice == "1":  #ask for the three pieces of needed info

                    user = input("Enter your name: ").strip()
                    description = input("Enter the issue description: ").strip()

                    allowed_priorities = ["High", "Medium", "Low"]  # implement input validation for priority of ticket using a while loop
                    while True:
                        priority = input("Enter the priority (High, Medium, Low): ").strip().capitalize()
                        if priority in allowed_priorities:
                            break #Exit the loop if input is valid
                        else:
                            print("Invalid priority. Please enter High, Medium, or Low.")

                    # Call the method with the user's input

                    system.create_ticket(user, description, priority)

                elif choice == "2":
                    system.view_tickets()

                elif choice == "3":
                    title = input("enter article title: ")
                    solution = input("Enter article solution: ")
                    kb.add_article(title, solution)

                elif choice == "4":
                    keyword = input("Enter a search keyword: ")
                    kb.search_articles(keyword)

                elif choice == "5":
                    print("Exiting the system. Goodbye!")
                    break

                else:
                    print("Invalid choice, Please enter a number between 1 and 3.")