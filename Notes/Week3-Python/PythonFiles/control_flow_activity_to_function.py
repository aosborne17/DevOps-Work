name = input("Hi there, what's your name? ")


"""
Try adding in TRY and EXCEPT to stop my program crashing when the user
uses an invalid input.
"""

def cinema_restriction():
    while True:
        try:
            age = int(input("How old are you {} ? ".format(name)))
            # 18, 15, 12, PG, U
            if age >= 18:
                print("You can watch all of today's movies, enjoy!")
            elif 15 <= age < 18:
                print("You can watch the 15, 12, PG and U rated movies, enjoy!")
            elif 12 <= age < 15:
                print("You can watch the 12, PG and U rated movies, enjoy!")
            else:
                print("Sorry lil kid, you can only watch the PG and U rated movies, enjoy!")
            break
        except ValueError:
            print("Ohh noo you've entered an invalid value! Please try again using a number")


cinema_restriction()