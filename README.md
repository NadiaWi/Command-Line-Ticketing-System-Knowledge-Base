# Command-Line Ticketing System

A simple, command-line-based ticketing system built in Python. This application mimics the core functionality of a support ticketing system like ServiceNow.
This tool allows users to create and manage support tickets while maintaining a searchable Knowledge Base for common solutions

## Features

Ticket Management

- Create Tickets: Submite support tickets with user name, description, and priority (High/Medium/Low)
- View Open Tickets: Display all currently open tickets with their details
- Close Tickets: Mark tickets as resolved and auto save changes
- Input validation: Prevents empty fields and validates priority levels
- Duplicate Detection: Warns users about similar open tickets (case-insensitive comparison)
- Auto-incrementing Ticket IDs: Each ticket receives a unique identifier

Knowledge Base
- Add Articles: Create knowledge base articles with titles and solutions
- Search Functionality: Search articles by keyword in both titles and solutions (case-insensitive)
- Pre-loaded Examples: Includes sample article for password reset instructions

Data Persistence

- Automatic Save/Load: All tickets are saved to a JSON file and automatically loaded on startup
- Auto-save on Actions: Changes are saved immediately when closing tickets or exiting the application
- Persistent Ticket Counter: Maintains ticket ID sequence across sessions

## Installation

1. Clone this repository:
  git clone https://github.com/NadiaWi/Command-Line-Ticketing-System-Knowledge-Base.git

2. Locate the project directory:
   cd Command-Line-Ticketing-System-Knowledge-Base

3. Run the application:
   python main.py

## Usage
When you run the application, you should see a menu with the following options:

**--- Ticketing System Menu ---**
1. Create a new ticket
2. View all open tickets
3. Close a ticket
4. Add a KB article
5. Search the knowledge Base
6. Exit

**Creating a Ticket**

1. Select option 1
2. Enter your name (required)
3. Enter issue description (required)
4. Select priority: High, Medium, or Low
5. System will warn you if a similar ticket already exists

**Closing a Ticket**

1. Select option 3
2. Enter the ticket ID number
3. Ticket will be marked as closed and changes saved automatically

**Searching the Knowledge Base**

1. Select option 5
2. Enter a keyword to search
3. System will display all matching articles from titles and solutions

**Technical Details**

Language: Python 3
Data Storage: JSON file (tickets.json)
Object-Oriented Design: Uses classes for Ticket, Article, TicketingSystem, and KnowledgeBase
No External Dependencies: Uses only Python standard library (json, os)

## Author
**Nadia Willingham** <br>
Created: August 31, 2025 <br>
Last Updated: January 16, 2026

License
This project is open source. Created for practice/training and available for educational purposes.

## Potential future updates/enhancements:
- Add ability to edit existing tickets
- ticket notes/comments functionality
- Create reporting and analytics features
- Add email notifications
- User authentication
- Save/load Knowledge Base articles to persistent storage
