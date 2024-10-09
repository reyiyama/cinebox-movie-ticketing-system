# This is the base class for all types of customers
class Customer:
    # This method initializes a new customer with an id and name
    def __init__(self, id, name):
        self._id = id
        self._name = name

    # This is a getter for the customer's id
    def get_id(self):
        return self._id

    # This is a getter for the customer's name
    def get_name(self):
        return self._name

    # This calculates the discount for this customer (base customers get no discount)
    def get_discount(self, cost):
        return 0

    # This getter calculates the booking fee for this customer (base fee is 2 per ticket)
    def get_booking_fee(self, ticket_quantity):
        return ticket_quantity * 2

    # This method displays this customer's information
    def display_info(self):
        print(f"ID: {self._id}, Name: {self._name}")


# This is a class for a type of customer who receives a flat discount rate on all purchases
class RewardFlatCustomer(Customer):
    # This instance method initializes a new flat discount customer and it inherits id and name from the Customer class
    def __init__(self, id, name, discount_rate=0.2):  
        super().__init__(id, name)
        self.discount_rate = discount_rate  

    # This getter method calculates the discount for this customer which is a flat rate on total cost
    def get_discount(self, cost):
        return cost * self.discount_rate  

    # This method displays this customer's information and includes the discount rate
    def display_info(self):
        print(f"ID: {self.get_id()}, Name: {self.get_name()}, Discount Rate: {self.discount_rate * 100}%")  

    # This helps in changing the discount rate for this customer as per the DI-level requirements
    def set_discount_rate(self, new_rate):
        self.discount_rate = new_rate


# This is a class for a special type of customer who receives a discount only if their total cost exceeds a threshold 
class RewardStepCustomer(Customer):
    # Tgis instance class initializes a new step discount customer and it inherits id name from the Customer class, through which it adds discount rate and threshold
    def __init__(self, id, name, discount_rate=0.3, threshold=50):  
        super().__init__(id, name)
        self.discount_rate = discount_rate
        self.threshold = threshold  

    # This method calculates the discount for this customer wherein the discount is on total cost. If cost exceeds threshold, or else there is no discount.
    def get_discount(self, cost):
        return cost * self.discount_rate if cost >= self.threshold else 0  

    # This method displays this customer's information (includes discount rate and threshold)
    def display_info(self):
        print(f"ID: {self.get_id()}, Name: {self.get_name()}, Discount Rate: {self.discount_rate * 100}%, Threshold: {self.threshold}$")  

    # This helps in changing the discount threshold for this customer
    def set_threshold(self, new_threshold):  
        self.threshold = new_threshold

# This class represents a movie 
class Movie:
    # This instance method iniitializes a new movie with an id, name and number of available seats
    def __init__(self, id, name, seat_available):
        self.id = id
        self.name = name
        self.seat_available = seat_available

    # This is a getter method for the movie's id
    def get_id(self):
        return self.id

    # This is a getter method for the movie's name
    def get_name(self):
        return self.name

    # This is a getter method for the number of available seats for this movie
    def get_seat_available(self):
        return self.seat_available

    # This method helps and reduces the number of available seats by a given quantity so that more than 50 seats don't get overrun
    def decrement_seat_available(self, quantity):
        self.seat_available -= quantity

    # This method displays this specific movie's information
    def display_info(self):
        print(f"Movie ID: {self.get_id()}, Name: {self.get_name()}, Available Seats: {self.get_seat_available()}")

# This class represents a ticket 
class Ticket:
    # This instance method initializes a new ticket with an id, name, price, and an optional max_tickets parameter
    # If no max_tickets is provided, it is set to infinity this part is not really used in this program however because we handle all the discrepancies that require this method so this is solely for calculating other metrics 
    def __init__(self, id, name, price, max_tickets=None):
        self.id = id
        self.name = name
        self.price = price
        self.max_tickets = max_tickets if max_tickets is not None else float('inf')

    # This is a getter method for the ticket's id
    def get_id(self):
        return self.id

    # This is a getter metthod for the ticket's name
    def get_name(self):
        return self.name

    # This is a gettermethod for the ticket's price
    def get_price(self):
        return self.price  

    # This is a getter method for the maximum number of these tickets that can be purchased
    def get_max_tickets(self):
        return self.max_tickets

    # This method displays this ticket's information
    def display_info(self):
        print(f"Ticket ID: {self.get_id()}, Name: {self.get_name()}, Price: {self.get_price()}, Max Tickets: {self.get_max_tickets()}")

# This class exist as a way to represent a single booking made by a customer.
class Booking:
    # This instance method refers to a new booking with an assigned customer, movie, ticket type, and ticket quantity.
    def __init__(self, customer, movie, ticket, quantity):
        self.customer = customer
        self.movie = movie
        self.ticket = ticket
        self.quantity = quantity

    # This is a getter method for the booking's customer.
    def get_customer(self):
        return self.customer

    # getter method for the booking's movie.
    def get_movie(self):
        return self.movie

    # getter methord for the booking's ticket type.
    def get_ticket(self):
        return self.ticket

    # getter for the quantity of tickets in a booking made by the customer
    def get_quantity(self):
        return self.quantity

    # This method computes the cost of this booking, considering ticket cost, booking fee, and discount it also decrements the movie's available seats by the booked quantity.
    def compute_cost(self):
        self.movie.decrement_seat_available(self.quantity)
        ticket_cost = self.ticket.get_price() * self.quantity
        booking_fee = self.customer.get_booking_fee(self.quantity)
        discount = self.customer.get_discount(ticket_cost)
        return ticket_cost, booking_fee, discount


# The GroupTicket class represents a special ticket that comprises multiple ticket components it inherits a lot from the Ticket class. It is basically for the credit level of this assignment
class GroupTicket(Ticket):
    # Initializes a new group ticket with an id, name, and ticket components.
    def __init__(self, id, name, components):
        super().__init__(id, name, 0)  # Call the constructor of the superclass Ticket, price is set to 0
        self.components = components  # The components of this group ticket, which are tuples of ticket and quantity

    # Overrides the get_price method to compute the group ticket's price, which is the sum of its components' prices (with a 20% discount) or 50, whichever is greater.
    def get_price(self):
        total_price = sum(ticket.get_price() * quantity for ticket, quantity in self.components)
        return max(total_price * 0.8, 50)

    # accounts for the get_max_tickets method to compute the group ticket's maximum tickets, which is the minimum of its components' maximum tickets.
    def get_max_tickets(self):
        return min(ticket.get_max_tickets() for ticket, _ in self.components)

# This class encapsulates all the data about the cinema, including customers, movies, and tickets this includes grouped tickets.
class Records:
    # This instance method initializes a new Records object with empty lists of customers, movies, and tickets.
    def __init__(self):
        self.customers = []
        self.movies = []
        self.tickets = []

    # this reader method reads in customer data from a txt file and populates the customers list.
    def read_customers(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = [x.strip() for x in line.strip().split(',')]
                if data[0].startswith('C'):  #this refers to a Normal customer
                    self.customers.append(Customer(data[0].strip(), data[1].strip()))
                elif data[0].startswith('F'):  #this refers to a Flat discount customer
                    self.customers.append(RewardFlatCustomer(data[0].strip(), data[1].strip(), float(data[2].strip())))
                elif data[0].startswith('S'):  #refers to a Step discount customer
                    self.customers.append(RewardStepCustomer(data[0].strip(), data[1].strip(), float(data[2].strip()), float(data[3].strip())))

    # reads movie data from a txt file and populates the movies list.
    def read_movies(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.split(',')
                self.movies.append(Movie(data[0].strip(), data[1].strip(), int(data[2])))

    #reads ticket data from a txt file and populates the tickets list.
    def read_tickets(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            temp_tickets = {}  # dictionary to store individual tickets for group tickets
            group_tickets_data = []  # this is a list meant to store group ticket data for processing
            for line in lines:
                data = [x.strip() for x in line.strip().split(',')]
                if not data[0].startswith('G'):  # G means a normal grroup ticket
                    ticket = Ticket(data[0], data[1], float(data[2]), int(data[3]))
                    self.tickets.append(ticket)
                    temp_tickets[data[0]] = ticket
                else:  # this is for group tickets
                    group_tickets_data.append(data)
            for data in group_tickets_data:
                components = []
                for i in range(2, len(data), 2):  # reads the components of the group ticket
                    ticket_id = data[i]
                    quantity = int(data[i + 1])
                    ticket = temp_tickets.get(ticket_id)
                    if ticket is None:
                        print('Something is wrong with this group ticket:', data[0])
                        break
                    components.append((ticket, quantity))
                else:
                    self.tickets.append(GroupTicket(data[0], data[1], components))

    # this nethod finds a ticket in a list of tickets by its id.
    def find_ticket_in_list(self, search_value, ticket_list):
        for ticket in ticket_list:
            if ticket.get_id() == search_value:  # this is when the the ticket is found
                return ticket
        return None  # returns nothing if ticket nis ot found

    # Finds a customer by its id or name.
    def find_customer(self, search_value):
        for customer in self.customers:
            if customer.get_id() == search_value or customer.get_name() == search_value:  #  customer found
                return customer
        return None  

    # This methd is very similar to find_customer but rather, checks directly if the Customer object has _id and _name attributes.
    def find_customer_by_id_or_name(self, id_or_name):
        for customer in self.customers:
            if hasattr(customer, '_id') and customer._id == id_or_name:
                return customer
            if hasattr(customer, '_name') and customer._name == id_or_name:
                return customer
        return None

    # Finds a movie by its id or name.
    def find_movie(self, search_value):
        for movie in self.movies:
            if movie.get_id() == search_value or movie.get_name() == search_value:  #movie is found
                return movie
        return None  #no movie found

    # Finds a ticket by its id or name.
    def find_ticket(self, search_value):
        for ticket in self.tickets:
            if ticket.get_id() == search_value or ticket.get_name() == search_value:  # ticket found
                return ticket
        return None  

    # this displays information about all customers
    def display_customers(self):
        for customer in self.customers:
            customer.display_info()

    # this displays information about all the movies.
    def display_movies(self):
        for movie in self.movies:
            movie.display_info()

    # this displays information about all tickets.
    def display_tickets(self):
        for ticket in self.tickets:
            ticket.display_info()
            if isinstance(ticket, GroupTicket):  # If the tiket is a group ticket, it display its price
                print('Price:', ticket.get_price())
  
class Operations:
    #instance method like all the oness before, but in an attempt for the HD level, I also tried to add in the bookings.txt file but failed in correctly appending it
    def __init__(self):
        self.records = Records()
        self.create_data_files()
        self.load_previous_bookings('bookings.txt')
    #this method loads all the prior bookings of the ucsomter
    def load_previous_bookings(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f.readlines():
                    line = line.strip()
                    if line:  
                        self.load_booking(line.split(','))
        except FileNotFoundError:
            print('Cannot load the booking file, run as if there is no previous booking file.')
    #this loads the previous bookings
    def load_booking(self, booking_info):
        customer_id_name = booking_info[0].strip() #all of these appendages are added to ensure the booking strings are correctly parsed
        movie_id_name = booking_info[1].strip()
        customer = self.records.find_customer(customer_id_name)
        movie = self.records.find_movie(movie_id_name)
        if customer is None or movie is None: #attempted HD but failed in correctly implementing this
            #print(f"Invalid booking found for customer {customer_id_name} and movie {movie_id_name}") #still unable to parse the booking.txt file correctly hence this is going to be the first portion of the output 
            return
        booking_data = booking_info[2:-3]  
        for i in range(0, len(booking_data), 2):
            ticket_id_name = booking_data[i].strip()
            quantity = int(booking_data[i + 1].strip())
            ticket = self.records.find_ticket(ticket_id_name)
            if ticket is None:
                print(f"Invalid ticket found for booking: {ticket_id_name}") 
                return
            if movie.get_seat_available() < quantity:
                print('There are not enough available seats for the ticket type:', ticket.get_name()) #not enough seats
                return
            movie.decrement_seat_available(quantity) #decrementing movies as the bookings are getting loaded on
            discount = float(booking_info[-3].strip())
            booking_fee = float(booking_info[-2].strip())
            total_cost = float(booking_info[-1].strip())
            booking = Booking(customer, movie, ticket, quantity, discount, booking_fee, total_cost) #calls the booking class and assigns the needed quanitites
            print(f'Loaded previous booking: {booking}')
    def create_data_files(self): #this creates three data files (I was having trouble making my code work with the given files hence I created the files through my program itself)
        customers_content = """C1, Olivia
        C2, Noah
        S3, George, 0.3, 50
        S5, Florence, 0.5, 50
        F8, Amelia, 0.2
        F10, Leo, 0.2
        C11, Henry"""
        movies_content = """M1, Avatar, 50
        M2, Titanic, 50
        M3, StarWar, 50
        M4, BlackPanther, 50
        M5, Superman, 50"""
        tickets_content = """T1, adult, 25.0, 10
        T2, child, 19.5, 10
        T4, student, 20.5, 10
        T5, concession, 20.5, 10
        G6, Family3, T1, 1, T2, 2
        G7, Family4, T1, 2, T2, 2
        G8, GrandFamily, T1, 2, T4, 2, T2, 1
        G9, Friend4, T1, 4
        G10, Student4, T4, 4
        G11, Test, T1, 2"""
        with open("customers_copy1.txt", "w") as f:
            f.write(customers_content)
        with open("movies_copy1.txt", "w") as f:
            f.write(movies_content)
        with open("tickets_copy1.txt", "w") as f:
            f.write(tickets_content)              
    def run(self):
        try:
            self.records.read_customers('customers_copy1.txt')
            self.records.read_movies('movies_copy1.txt')
            self.records.read_tickets('tickets_copy1.txt')
        except FileNotFoundError as e:
            print(f'Error: {e.filename} file is missing.')
            return
        while True: #this is the menu with 8 options the first thing printed is my name, student id, and the highest attempted
            print("\n Name: Amay Viswanathan Iyer")
            print("\n Student ID: S3970066")
            print("\n Highest Level Completed: DI")
            print("\n Highest Level Attempted: HD (bookings.txt added)")
            print('\n1. Purchase a ticket\n2. Display existing customers’ information\n3. Display existing movies’ information\n4. Display existing ticket types’ information\n5. Add movies\n6. Adjust the discount rate of all RewardFlat customers\n7. Adjust the discount rate of a RewardStep customer\n8. Exit the program')
            option = input('Choose an option: ')
            if option == '1':
                self.purchase_ticket()
            elif option == '2':
                self.records.display_customers()
            elif option == '3':
                self.records.display_movies()
            elif option == '4':
                self.records.display_tickets()
            elif option == '5':
                self.add_movies()
            elif option == '6':
                self.adjust_discount_rate_interface()
            elif option == '7':
                self.adjust_step_discount_rate_interface()
            elif option == '8':
                break
            else:
                print('Invalid option.')

    def adjust_step_discount_rate(self, new_rate): #method to adjust the step discount rate
        if not isinstance(new_rate, (int, float)) or new_rate <= 0:
            raise InvalidDiscountRateError("Discount rate must be a positive number")
        for customer in self.records.customers:
            if isinstance(customer, RewardStepCustomer):
                customer.discount_rate = new_rate

    def adjust_step_discount_rate_interface(self): #adjusting the step discount rate
        while True:
            id_or_name = input("Enter the RewardStep customer's ID or name: ")
            customer = self.records.find_customer_by_id_or_name(id_or_name)
            if customer is None or not isinstance(customer, RewardStepCustomer):
                print("Invalid customer entered. Please try again.")
                continue
            while True:
                try:
                    new_rate = float(input("Enter new discount rate for this RewardStep customer: "))
                    self.adjust_step_discount_rate(new_rate)
                    print(f'Successfully updated discount rate for {customer.get_name()} to {new_rate}')
                    break
                except InvalidDiscountRateError as e:
                    print(str(e))
                except ValueError:
                    print("Invalid input. Please enter a number.")
            break

    def adjust_discount_rate(self, new_rate): #adjusting the flat discount rate
        if not isinstance(new_rate, (int, float)) or new_rate <= 0:
            raise InvalidDiscountRateError("Discount rate must be a positive number")
        for customer in self.records.customers:
            if isinstance(customer, RewardFlatCustomer):
                customer.discount_rate = new_rate
    def adjust_discount_rate_interface(self): #interface for flat discount rate adjustment
        while True:
            try:
                new_rate = float(input("Enter new discount rate for RewardFlat customers: "))
                self.adjust_discount_rate(new_rate)
                break
            except InvalidDiscountRateError as e:
                print(str(e))
            except ValueError:
                print("Invalid input. Please enter a number.")  
    def add_movies(self): #adding movies (this was taken off Project 1)
        add_movies_input = input('Do you want to add a list of movies? (y/n): ')
        if add_movies_input.lower() == 'y':
            movie_names = input('Enter the list of movies (separate by commas): ').split(',')
            for movie_name in movie_names:
                movie_name = movie_name.strip()
                if self.records.find_movie(movie_name) is None:
                    self.records.movies.append(Movie('M'+str(len(self.records.movies)+1), movie_name, 50))  
                    print(f'The movie {movie_name} has been added with 50 initial seats.')
                else:
                    print(f'The movie {movie_name} already exists.')
        else:
            print('No movies added.')
    def purchase_ticket(self): #the full purchase ticket method that takes care of the full output. moroever, the receipt is adapted from Assignment 1 which was already commented
        customer_id = input('Enter customer ID: ')
        customer = self.records.find_customer(customer_id)
        if customer is None:
            name = input('Enter customer name: ')
            rewards_program = None
            while rewards_program not in ['y', 'n']:
                rewards_program = input('Does the customer want to join the rewards program? (y/n): ')
                if rewards_program == 'y':
                    rewards_type = input('Which rewards type does the customer want to join? (F/S): ')
                    if rewards_type == 'F':
                        customer = RewardFlatCustomer(customer_id, name)
                    elif rewards_type == 'S':
                        customer = RewardStepCustomer(customer_id, name)
                    self.records.customers.append(customer)
                elif rewards_program == 'n':
                    customer = Customer(customer_id, name)
                    self.records.customers.append(customer)
        while True:  #everywhere I have a while loop I have ensured I account for the exceptions and handle the errors until the correct output is provided by the user
            movie_name = input('Enter movie name: ')  
            movie = self.records.find_movie(movie_name)  
            if movie is None or movie.get_seat_available() == 0:
                print('Invalid movie name or movie is sold out. Please try again.')  
            else:
                break
        while True:  
            ticket_ids = input('Enter ticket IDs (comma-separated, check option 4 from the menu to correctly choose ticket types): ').split(',') #this is the instance handling for entering the ticket ids
            quantities = input('Enter quantities (comma-separated): ').split(',')
            if len(ticket_ids) != len(quantities):
                print("Please enter the same number of ticket IDs and quantities.") #this is to handle the invalid iputs
                continue
            tickets = [self.records.find_ticket(ticket_id.strip()) for ticket_id in ticket_ids]
            if None in tickets:
                print("One or more ticket IDs are invalid. Please try again.") #input validation
                continue
            try:
                quantities = [int(quantity.strip()) for quantity in quantities]
            except ValueError:
                print("Invalid quantity value entered. Quantities should be integers. Please try again.") #ensuring inputs are values and not strings
                continue
            if not all(1 <= quantity <= ticket.get_max_tickets() for ticket, quantity in zip(tickets, quantities)):
                print("Invalid quantity value for one or more tickets. Please ensure quantities do not exceed available tickets and are greater than 0.") #to ensure the quantity of tickets being purchased doesn't exceed the number of seats
                continue
            break
        total_ticket_cost = 0
        total_booking_fee = 0
        total_discount = 0
        for ticket, quantity in zip(tickets, quantities): 
            if movie.get_seat_available() < quantity:
                print('There are not enough available seats for the ticket type:', ticket.get_name()) #to account and decrement the number of seats based on how many are available which is based on prior bookings
                return            
            movie.decrement_seat_available(quantity)
            booking = Booking(customer, movie, ticket, quantity)
            ticket_cost, booking_fee, discount = booking.compute_cost()
            total_ticket_cost += ticket_cost
            total_booking_fee += booking_fee
            total_discount += discount #this is partly adapted from the Assignment 1 part of the receipt
            print("-" * 54) #this is the indentation paart to ensure the receipt is output correctly in the format outlined by the professor in the assignment document
            print(f"Receipt for {customer.get_name()}".ljust(25))
            print("-" * 54)

            print(f"Movie:".ljust(25) + f"{movie.get_name()}".rjust(28))

            ticket_data = {ticket.get_name(): (ticket.get_price(), quantity)}

            for ticket_type, (ticket_unit_price, ticket_quantity) in ticket_data.items():
                print(f"Ticket type:".ljust(25) + f"{ticket_type}".rjust(28))
                print(f"Ticket unit price:".ljust(25) + f"${ticket_unit_price:.2f}".rjust(28))
                print(f"Ticket quantity:".ljust(25) + f"{ticket_quantity}".rjust(28))
                print()

            print("-" * 54)
            print(f"Discount:".ljust(25) + f"${discount:.2f}".rjust(28))
            print(f"Booking fee:".ljust(25) + f"${booking_fee:.2f}".rjust(28))
            print(f"Total cost:".ljust(25) + f"${(ticket.get_price() * ticket_quantity + booking_fee - discount):.2f}".rjust(28))
            print("-" * 54)

if __name__ == '__main__': #calling the main class Operations
    Operations().run()
