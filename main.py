seats = []

def creating_seats_list():
    for i in range(7):
        seats.append([])
        for j in range(i + 7):
            seats[i].append(chr(65 + i) + str((j + 1)))

def greeting_message():
    print("""
************* WELCOME TO PYTHON CENIMA ****************
We will help you in:
[1] Picking your favorite movie.
[2] Booking seats for a movie.
[3] Buying snacks to eat while watching.
""")

movie = input("Choose your movie: ")

def showing_the_hall():
    last_row_string = " ".join(seats[-1]) 
    max_width = len(last_row_string)

    print("          ----------------------")
    print("          -       SCREEN       -")
    print("          ----------------------")

    for row in seats:

        row_string = " ".join(row)
        print(row_string.center(max_width))
    print('')


number_of_people = int(input('How many seats would you like to book: '))
creating_seats_list()

showing_the_hall()

for chair in range(number_of_people):
    choice = input("Please enter the desired seat: ")

    for row in range(7):
        if choice in seats[row]:

            seat_index = seats[row].index(choice)

            seats[row][seat_index] = 'XX'

            break
    else:
        print('Invalid choice!')

    showing_the_hall()
    

    


