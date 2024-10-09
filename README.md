# CineBox: Python-Powered Movie Ticketing

## Introduction
Welcome to **CineBox**, a Python-based movie ticketing system designed to streamline ticket purchases for box office cashiers or managers. This system allows users to easily manage ticket sales, handle customer rewards, and keep track of available seats for different movies.

Developed as an assignment for RMIT's COSC2531 course, CineBox implements fundamental programming concepts, emphasizing modularity, data handling, and interactive features. The project was completed with a perfect score, meeting all required criteria. This repository includes a single Python file (`ProgFunA1_s3970066.py`) containing the full implementation.

## Features
CineBox provides a rich set of functionalities, covering different aspects of a movie ticketing system:

1. **Ticket Purchase**: Handles customer names, movie names, ticket types, and quantities.
2. **Discounts for Rewards Members**: Applies a discount for customers who are part of the rewards program.
3. **Menu System**: Operates through an interactive menu to choose tasks such as purchasing tickets, adding movies, or viewing customer information.
4. **Dynamic Updates**: Tracks the number of available seats for each movie.
5. **Multiple Ticket Types**: Allows customers to buy different ticket types within a single order.
6. **Movie Records**: Displays a detailed history of movie sales, including revenue per movie.

## Getting Started
### Prerequisites
- **Python 3.x**: Make sure Python 3 is installed on your system. CineBox has been tested on Python 3.9+, but other versions should also work.
- **Command Line Interface**: The program is designed to run from a terminal or command prompt.

### Installation
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/reyiyama/cinebox-movie-ticketing-system.git
   ```

2. **Navigate to Project Directory**:
   ```sh
   cd CineBox
   ```

## Running the Program
The program is contained in a single Python file. To run it, follow these steps:

1. **Launch the Program**:
   ```sh
   python ProgFunA1_s3970066.py
   ```

2. **Using the Program**: Upon running the script, the program will display a menu of options:
   - **Purchase a Ticket**: Guides you through selecting a customer, movie, ticket type, and quantity, then displays the calculated total cost.
   - **Add Movies**: Allows you to add new movies to the system, initialized with 50 available seats each.
   - **View Customers**: Displays all existing customers and whether they are part of the rewards program.
   - **View Movies**: Shows all movies along with the number of seats still available.
   - **Exit**: Exits the program.

### Example Usage
Here is an example of how the program can be used:

1. **Purchase a Ticket**:
   - Enter customer name: *John Doe*
   - Select a movie: *Avatar*
   - Choose ticket type: *Adult*
   - Enter ticket quantity: *2*
   - Join rewards program: *y/n*
   - The system will calculate the total cost, apply any discounts, add booking fees, and display a detailed receipt.

2. **Add Movies**:
   - Add movies like: *Frozen, Inception, Avengers*
   - Each movie will be initialized with 50 seats.

3. **View Records**: Display the most popular movie or see all past purchases.

## Code Structure
The code is structured into several modular functions to ensure clarity and maintainability. Each function handles a distinct task, such as:

- **Main Menu Loop**: Provides users with options to navigate.
- **Ticket Purchase Process**: Takes care of selecting movies, ticket types, and quantities, while validating user input.
- **Adding Movies and Viewing Information**: Functions dedicated to expanding the movie list and displaying the current state of customers or movies.

The system utilizes Python's list and dictionary data types to store relevant information, making it easy to manage and retrieve data during runtime.

## Important Considerations
- **Data Persistence**: The current version of CineBox is a command-line program and does not save data between sessions. All data is lost once the program ends.
- **Error Handling**: Input validation is included for various user inputs, ensuring robust interaction.
- **Documentation**: The code is well-documented, with comments describing each function, logic flow, and important decision points.

## Future Enhancements
There are several features that could be added to improve CineBox:
- **Database Integration**: Implementing a database to persist data across sessions.
- **Graphical User Interface (GUI)**: Developing a GUI using frameworks like Tkinter or PyQt.
- **Online Ticketing**: Expanding the program to handle online reservations, integrating a payment gateway.

## Credits
- **Author**: Amay (s3970066)
- **Course**: RMIT - Programming Fundamentals (COSC2531)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Feedback
If you have any questions, suggestions, or would like to contribute to this project, feel free to open an issue or submit a pull request.

