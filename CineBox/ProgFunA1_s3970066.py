#Name: Amay Viswanathan Iyer
#Student ID: s3970066
#Highest Part Attempted: Part 3
#this is where the Assignment starts

def movAdd(putinMov):
    #here, i am creating a list of movie names via the input string, splitting the whitespace, and splitting the names with commas
    #this function exists for option 2 in the menu
    list_Mov = [movie.strip() for movie in putinMov.split(',')]
    for movie in list_Mov:
    #in this for loop, i am iterating through every movie name i have gathered in the inputted list
        if movie in film:
            print(f"'{movie}' is an existing movie.")
            #this if statement cross checks with the list named 'film' to check if the movie is already in the roster
            #if it is already in the list, the above statement is printed
        else:
            #if the movie is not present in the list, we add it to the 'film' dictionary with 50 available seats by default
            print(f"Adding '{movie}' to the system with 50 available seats.")
            film[movie] = {"vacant": 50,
                           "sumofreturns": 0,
                           "ticket_count": {"adult": 0,
                                            "child": 0,
                                            "senior": 0,
                                            "student": 0,
                                            "concession": 0}}

def print_clients(clients):
    #this prints out all the current customers and whether or not they are registered into the rewards program
    print("\nCustomer Information:")
    #in this for loop i am iterating through the clients dictionary
    for clientname, rewards in clients.items():
        #here i am determining whether the customer is registered in the rewards program or not
        rewards_status = "Registered" if rewards else "Not Registered"
        #tthis simply prins out the customers name and their rewards status
        print(f"{clientname}: {rewards_status}")

def print_movie(film):
    #this function prints out the currently available seats for all the films in the film dictionary
    #this also takes into consideration the films added through the menu
    print("\nMovie Information:")
    #in this for loop i am iterating through every single movie in the film dictionary
    for filmname, data_film in film.items():
        #here i am printint out the movie name and the available number of vacant seats
        print(f"{filmname}: {data_film['vacant']} available seats")

def print_highest_grossing(film):
    #here i am initializing the max revenue achieved by the movies in the roster
    filmyield = 0
    #here i am initializing the most popular movies
    most_popular_film = []

    #here i am going to iterate through every single movie in the films dictionary
    for filmname, data_film in film.items():
        #i am comparing the movie's total revenue aka filmyield with the current highest value of filmyield and printing the result
        if data_film["sumofreturns"] > filmyield:
            filmyield = data_film["sumofreturns"]
            most_popular_film = [filmname]
        elif data_film["sumofreturns"] == filmyield:
            #appending the name of the film into the most popular film list
            most_popular_film.append(filmname)
    #printing out the most popular movie that has gotten the highest revenue
    print("\nMost Popular Movie(s):")
    for movie in most_popular_film:
        print(f"{movie}: ${film[movie]['sumofreturns']:.2f}")

def filmRecords(film):
    #this was probably the second most challenging part of this assignment the most challenging part was option 1 in the main while loop
    print("\nAll Time Movie Record:")

    #initializing an empty dictionary where i can store all the individual film's data values in order
    historical_film_record = {}
    #i am iterating through the values and encapsulated data of the movies in the film dictionary
    for filmname, data_film in film.items():
        #here i am creating a frequency list of the number of tickets bought as per their ticket type - student adult etc.
        ticket_count_list = [data_film["ticket_count"][client_category] for client_category in client_categories]
        #this is to obtain the revenue from the sumofreturns value initialized earlier
        revenue = data_film['sumofreturns']
        #here i am adding the ticket numbers as per their type and adding them to the historical film record dictionary
        historical_film_record[filmname] = ticket_count_list + [revenue]
    #this is calling the film tally function that outputs a fully fledged table with all the specified values as per our assignments specifications
    film_tally(historical_film_record)

def film_tally(historical_film_record):
    # this calculates the maximum width of the column consisting of movie
    filmname_colwidth = max(len(filmname) for filmname in historical_film_record.keys()) + 2
    # this variable sets the column widths for each ticket type as per revenue
    colwidths = [filmname_colwidth, 7, 7, 7, 8, 11, 12]
    # this part prints out the headers of the table as specified for part 3
    headers = ["Movie", "adult", "child", "senior", "student", "concession", "Revenue"]
    for i, header in enumerate(headers):
        print(header.ljust(colwidths[i]), end="")
    #this prints a line to separate the headers from the rows
    print("\n" + "-" * sum(colwidths))
    #this prints out the table rows
    for filmname, data_film in historical_film_record.items():
        #here i am using the ljust function with the specified column width as i print out the movie name
        print(filmname.ljust(colwidths[0]), end="")

        #here i am iterating through the number of tickets while excluding the revenue
        for i, ticket_count in enumerate(data_film[:-1]):
            
            formatted_ticket_count = str(ticket_count).rjust(colwidths[i + 1])
            print(formatted_ticket_count, end="")
            
        #here i am forrmatting the revenue and ensuring it is presented with two decimal points
        formatted_revenue = f"${data_film[-1]:,.2f}".rjust(colwidths[-1])
        print(formatted_revenue)



def menu():
    #this is just the menu that is called on the moment the program is run with all the options
    print("Name: Amay Viswanathan Iyer")
    print("Student ID: s3970066")
    print("Highest Part Attempted: Part 3")
    print("\nMenu:")
    print("1. Purchase a ticket")
    print("2. Add movie")
    print("3. Display existing customer information")
    print("4. Display existing movie information")
    print("5. Display the most popular movie")
    print("6. Display all movie record")
    print("7. Exit the program")

def print_receipt(clientname, filmname, ticket_data, dollars_saved, booking_fee, total_cost):
    #here i am printing out a separator line using the - character to make the output presentable
    #aligning the values symmetrically and making sure the math is right in this function was the third most challenging part of this assignment
    print("-" * 54)
    print(f"Receipt for {clientname}".ljust(25))
    print("-" * 54)

    #here i am printing out the movie name with left and right justification for a symmetrical presentation
    print(f"Movie:".ljust(25) + f"{filmname}".rjust(28))

    #here i am iterating through the ticket_data and printing out the type of ticket along with quantity
    #the right justification values were hard to align at first as more often than not the output was misaligned and asymmetrical
    #i chose 28 as the viable value as it aligned perfectly with the receipt separator line
    for client_category, (ticket_unit_price, ticket_quantity) in ticket_data.items():
        print(f"Ticket type:".ljust(25) + f"{client_category}".rjust(28))
        print(f"Ticket unit price:".ljust(25) + f"${ticket_unit_price:.2f}".rjust(28))
        print(f"Ticket quantity:".ljust(25) + f"{ticket_quantity}".rjust(28))
        print()

    #this prints out a separator line and breaks down the cost for the customer 
    print("-" * 54)
    print(f"Discount:".ljust(25) + f"${dollars_saved:.2f}".rjust(28))
    print(f"Booking fee:".ljust(25) + f"${booking_fee}".rjust(28))
    print(f"Total cost:".ljust(25) + f"${total_cost:.2f}".rjust(28))
    print("-" * 54)


#all of these are the data we have been asked to initialize as per assignment specifications
#all of the values are stored in their respective dictionaries
#i used a dictionary here because i feel it has a much more of a chronological feeling to it as I think using tthem for this project felt orderly

clients = {
    "Mary": True,
    "James": False
}

film = {
    "Avatar": {
        "vacant": 50,
        "sumofreturns": 0,
        "ticket_count": {
            "adult": 0,
            "child": 0,
            "senior": 0,
            "student": 0,
            "concession": 0
        }
    },
    "Titanic": {
        "vacant": 50,
        "sumofreturns": 0,
        "ticket_count": {
            "adult": 0,
            "child": 0,
            "senior": 0,
            "student": 0,
            "concession": 0
        }
    },
    "Star Wars": {
        "vacant": 50,
        "sumofreturns": 0,
        "ticket_count": {
            "adult": 0,
            "child": 0,
            "senior": 0,
            "student": 0,
            "concession": 0
        }
    }
}

client_categories = ["adult",
                     "child",
                     "senior",
                     "student",
                     "concession"]
costofticket = {
    "adult": 25.0,
    "child": 19.5,
    "senior": 17.0,
    "student": 20.5,
    "concession": 20.5
}
clients = {
    "Mary": True,
    "James": False
}

film = {
    "Avatar": {
        "vacant": 50,
        "sumofreturns": 0,
        "ticket_count": {
            "adult": 0,
            "child": 0,
            "senior": 0,
            "student": 0,
            "concession": 0
        }
    },
    "Titanic": {
        "vacant": 50,
        "sumofreturns": 0,
        "ticket_count": {
            "adult": 0,
            "child": 0,
            "senior": 0,
            "student": 0,
            "concession": 0
        }
    },
    "Star Wars": {
        "vacant": 50,
        "sumofreturns": 0,
        "ticket_count": {
            "adult": 0,
            "child": 0,
            "senior": 0,
            "student": 0,
            "concession": 0
        }
    }
}

client_categories = ["adult", "child", "senior", "student", "concession"]
costofticket = {
    "adult": 25.0,
    "child": 19.5,
    "senior": 17.0,
    "student": 20.5,
    "concession": 20.5
}


#this while loop is the backbone of this program as it dictates how the menu option choices operate
#if something was the most challenging in this project it would be this
#getting the format correct for the receipt and the table printing the all time movie records follow up from this while loop

while True:
    menu()
    choice = input("\nChoose an option: ")

    if choice == '1':
        # this promps for customer name
        clientname = input("Enter the name of the customer [e.g. Huong]: ")

        #this prompts for movie name and also validates the input by calling on the loop until a valid input is places
        while True:
            filmname = input("Enter the name of the movie [enter a valid name only, e.g. Avatar]: ")
            if filmname in film:
                break
            else:
                #i wanted to make it so that this part calls the adding movies function so that it is seamless for the user but i didn't succeed in it as i got
                #obsessed with the output format. if there is something i wish i could do better in this project it would be to fix this portion
                print(f"Movie '{filmname}' is not in the registry. Please enter a valid movie or register a valid movie record, add the movie, and try again.")

        # this prompts the ticket registrar to input the desired number of tickets and their types
        #this takes care of the ticket types and their quantities in the same while loop and keeps trying to validate the input until the user gets it right
        valid_tickinformation = False
        while not valid_tickinformation:
            client_categories_input = input("Enter a list of ticket types separated by commas [e.g. adult, child, senior]: ").split(',')
            ticket_quantities_input = input("Enter a list of ticket quantities [e.g. 2, 1, 1]: ").split(',')
            
            # this checks if the order of the ticket type separated by comma matches with the order of ticket quantity per type separated by comma
            #if it doesn't match, the prompt is called again until the order and values are correct
            if len(client_categories_input) != len(ticket_quantities_input):
                print("The number of ticket types and ticket quantities entered do not match. Please try again.")
                continue

            # Process ticket types and quantities
            tickinformation = {}
            sumTicket = 0
            wrong_typequant = False

            for i in range(len(client_categories_input)):
                client_category = client_categories_input[i].strip().lower()
                ticket_quantity_str = ticket_quantities_input[i].strip()

                if client_category not in client_categories:
                    #this part checks for the validity of the ticket types
                    print(f"Invalid ticket type '{client_category}'. Please enter valid ticket types.")
                    wrong_typequant = True
                    break

                if not ticket_quantity_str.isdigit():
                    #this checks the quantity
                    
                    print("Invalid ticket quantity. Please enter positive integers for ticket quantities.")
                    wrong_typequant = True
                    break

                ticket_quantity = int(ticket_quantity_str)
                if ticket_quantity < 1:
                    print("Invalid ticket quantity. Please enter positive integers for ticket quantities.")
                    wrong_typequant = True
                    break

                sumTicket += ticket_quantity
                tickinformation[client_category] = (costofticket[client_category], ticket_quantity)

            if wrong_typequant:
                continue

            if sumTicket > film[filmname]["vacant"]:
                #this also validates with the bound of the number of seats in the theatre as they cannot exceed 50
                #if the ticket quantity exceeds 50, the prompts are called until valid inputs with the adequate ticket seat amounts are entered
                print("The total ticket quantity entered exceeds the number of available seats which maxes out at 50. Please try again.")
                continue

            valid_tickinformation = True

        # here i check if a customer exists and if a registration to the rewards program is desired by the customer
        #the option to add a customer to the rewards program is asked in the end to ensure the discount doesn't apply for the current purchase
        if clientname not in clients:
            clients[clientname] = False
            while True:
                rewards_program_input = input("Does the customer want to join the rewards program [enter y or n]?: ").lower()
                if rewards_program_input == 'y':
                    clients[clientname] = True
                    break
                elif rewards_program_input == 'n':
                    break
                else:
                    #here i have enabled an input validattion mechanism that only ensures inputs of y for yes and n for no
                    #this prompt keeps getting called until a valid answer is given
                    print("Invalid input. Please enter y or n.")
        else:
            if clients[clientname]:
                #here i print out the customer's record with the rewards system if they are already registered
                print(f"{clientname} is already a registered rewards member.")
            else:
                while True:
                    #this is printed whenever a customer is already present in the system, but is not registered into the rewards program like
                    #the initialized customer James. in this part the registrar can onboard a customer into the rewards system
                    #this question is prompted near the end of the purchasing process to ensure the discount doesn't apply for the ticket the customer is currently purchasing
                    #however it isn't the case for this program as the moment a customer chooses to be part of the rewards program they get a discount
                    rewards_program_input = input(f"{clientname} is not in the rewards program. Does the customer want to join the rewards program [enter y or n]?: ").lower()
                    if rewards_program_input == 'y':
                        clients[clientname] = True
                        break
                    elif rewards_program_input == 'n':
                        break
                    else:
                        print("Invalid input. Please enter y or n.")

        # this portion calculates the total fees based on the full sum number of tickets bought as per their customer types and updates the roster
        #dollars saved is the discount of 20% as people who are in the rewards program get the discount for subsequent purchases 
        sumTickets = sum(ticket_unit_price * ticket_quantity for ticket_unit_price, ticket_quantity in tickinformation.values())
        dollars_saved = 0.20 * sumTickets if clients[clientname] else 0
        booking_fee = 2 * sum(ticket_quantity for _, ticket_quantity in tickinformation.values())
        total_cost = sumTickets - dollars_saved + booking_fee

        film[filmname]["vacant"] -= sum(ticket_quantity for _, ticket_quantity in tickinformation.values())
        film[filmname]["sumofreturns"] += sumTickets
        for client_category, (_, ticket_quantity) in tickinformation.items():
            film[filmname]["ticket_count"][client_category] += ticket_quantity

        # this part calls the print_receipt function and displays the receipt in a symmetrical format
        print_receipt(clientname, filmname, tickinformation, dollars_saved, booking_fee, total_cost)

    elif choice == '2':
        # this option calls the movAdd function at the start of this program film
        putinMov = input("Enter the list of movies separated by commas: ")
        movAdd(putinMov)

    elif choice == '3':
        # this displays all the customers in the system currently along with their rewards status
        print_clients(clients)

    elif choice == '4':
        # this displays all the movies running in the theatre and the available number of seats
        print_movie(film)

    elif choice == '5':
        # this calls the print highest grossing function to print out the movie that has made the theatre the most money
        print_highest_grossing(film)

    elif choice == '6':
        # this option displays all the movies, the number of tickets sold structured by the number of tickets sold per type, and the total money made from sales
        filmRecords(film)

    elif choice == '7':
        # this exists the program 
        print("Exiting the program.")
        break

    else:
        # this keeps calling on the menu over and over again until the user inputs a valid number between 1 to 7
        print("Invalid option. Please try again.")
        
        
