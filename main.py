def show_welcome():
    print("""
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║           PYTHON  PREMIERE  CINEMAS              ║
    ║         -------------------------------          ║
    ║         The Ultimate Booking Experience          ║
    ║                                                  ║
    ╠══════════════════════════════════════════════════╣
    ║                                                  ║
    ║      Welcome! Are you ready to book your         ║
    ║      tickets and have some fun!                  ║
    ║      Please follow the instructions below.       ║
    ║      LET'S GET STARTED! (Please press ENTER!)    ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    """, end = '')
    input('')

def creating_seats_list():

    global seats 
    seats = []

    for i in range(7):
        seats.append([])
        for j in range(i + 7):
            seats[i].append(chr(65 + i) + str((j + 1)))

def showing_the_hall():
    last_row_string = " ".join(seats[-1]) 
    max_width = len(last_row_string)
    print('.' * 70)
    print("          ----------------------")
    print("          -       SCREEN       -")
    print("          ----------------------")

    seats_prices = [150, 120, 90, 70, 50, 40, 30]
    for row in seats:

        row_string = " ".join(row)
        print(row_string.center(max_width) + f'  -----> {seats_prices[seats.index(row)]} SAR per seat!')

    print('.' * 70)    

def collecting_user_data():
    global the_user_name
    global number_of_people

    print("""
As you can see, this chart shows you the available seats 
and their position and price. (XX means the seat is reserved!)""")
    
    the_user_name = input("\nFirst of all, please tell me your name: ").capitalize()
    
    number_of_people = input(f'\nNice to meet you {the_user_name}. Please tell me how many seats \
would you like to book: ')
    
    while number_of_people.isdigit() == False :
        number_of_people = input('Please enter a valid whole number: ')
    
    number_of_people = int(number_of_people)

def collecting_seats_data():

    global list_of_chairs 
    global total_price

    list_of_chairs = []
    total_price = 0
    chair = 0

    while chair < number_of_people:

        seats_prices = [150, 120, 90, 70, 50, 40, 30]
        choice = input("\nPlease enter the name of the desired seat : ").upper()

        for row in range(7):
            if choice in seats[row]:

                seat_index = seats[row].index(choice)
                total_price += seats_prices[row]
                list_of_chairs.append(seats[row][seat_index])
                seats[row][seat_index] = 'XX'

                chair += 1

                break
        else:
            print('\nInvalid choice! Try again.')
    
        print('*' * 70)
        showing_the_hall()
        print(f"\nThe current total is : {total_price} SAR")
        print('*' * 70)

def handeling_users_data():

    users_information[the_user_name] = [list_of_chairs , total_price]

    if multiple_users == 'no':

        print("\nThe program has ended.")

        print("This is a summary for today's sold tickets: ")

        print("-" * 70)
        print("Name".ljust(20) + " | " + "Cost".ljust(12) + " | " + "Booked Seats")
        print("-" * 70)

        for key, value in users_information.items():
            
            name = key
            seats = " ".join(value[0])
            cost = f"{value[1]} SAR"
            
            print(name.ljust(20) + " | " + cost.ljust(12) + " | " + seats)

        print("-" * 70)

def showing_final_details():

    print("#" * 70)
    print()
    print(f'The chair(s) you have booked: {", ".join(list_of_chairs)}'.center(70))
    print(f'The total cost of your reservation is: {total_price} SAR'.center(70))
    print('Thank you for your time! Enjoy your movie!'.center(70))
    print()
    print("#" * 70)
    print()

def main():
    creating_seats_list()
    global users_information
    users_information = {}

    while True:
        show_welcome()
        showing_the_hall()
        collecting_user_data()
        collecting_seats_data()
        showing_final_details()

        global multiple_users
        multiple_users = input("Enter (Yes) to add another reservtion \
or (No) to stop the program: ").lower()

        while multiple_users != 'yes' and multiple_users != 'no':
            multiple_users = input('\nPlease choose either (Yes) or (No): ').lower()

        handeling_users_data()

        if multiple_users == 'yes':
            continue
        else:
            break    

main()
