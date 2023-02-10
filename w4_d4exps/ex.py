# ex1

def display_message():
    print("what you are learning in this course")
display_message()

# ex2

def favorite_book(title):
    print(f"One of my favorite book is {title}")
favorite_book("Wonderland")    

# ex3
def describe_city(city,country="15"):
    print(f"{city} is in {country}")
describe_city("Paris","France")
describe_city("Paris")

# ex4
import random

def compare_numbers(num):
    random_num = random.randint(1, 100)
    if num == random_num:
        print("Success! The number display is:", num)
    else:
        print("Fail. The numbers display:", num, "and", random_num)

compare_numbers(5)

# ex5
# Part 1
def make_shirt( size="large", text="I love python"):
    print(f"The size of the shirt is {size} and the text is {text}")
# make_shirt("small","Mauritius Paradise")  
# #   Part 2
make_shirt()
# Part 3
make_shirt("large","I hate js")
make_shirt("medium","I hate css")

# ex6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(name_list):
    for name in name_list:
        print(name)
show_magicians(magician_names) 
#  having an issue while calling the old function to my new function
def make_great(great_list):
    for   great in great_list:
     print(great)
    # result=show_magicians(great_list)
    # return result
# make_great(show_magicians(magician_names))
make_great( magician_names)
       






# ex7
# import random


# def get_random_temp(season_int):
#     """Generate a random float between -10 (inclusive) and 40 (inclusive/exclusive).
#     Return the generated float.
#     """

#     spring = "spring"
#     summer = "summer"
#     autumn = "autumn"
#     winter = "winter"

#     season = ""
#     if season_int >= 3 and season_int <= 5:
#         season = spring
#     elif season_int >= 6 and season_int <= 8:
#         season = summer
#     elif season_int >= 9 and season_int <= 11:
#         season = autumn
#     elif (season_int >= 1 and season_int <= 2) or season_int == 12:
#         season = winter
#     else:
#         print(f"We received a bad value for season. ({season_int})")

#     season_limits = {
#         summer: {"lower": 33, "upper": 40},
#         autumn: {"lower": 24, "upper": 33},
#         winter: {"lower": -10, "upper": 17},
#         spring: {"lower": 17, "upper": 24},
#     }

#     random_float = random.uniform(
#         season_limits[season]["lower"], season_limits[season]["upper"]
#     )
#     # Math Notation:
#     # [] Inclusive
#     # () Exclusive
#     return random_float


# def main():
#     # user_season = ""

#     # while user_season not in ["summer", "autumn", "winter", "spring"]:
#     #     user_season = input(
#     #         "Please enter the season ('summer', 'autumn', 'winter', 'spring'): "
#     #     ).lower()

#     user_season_int = 0

#     while user_season_int <= 0 or user_season_int >= 13:
#         user_season_int = int(input("Please enter the season (1-12): "))

#     random_temperature = get_random_temp(user_season_int)

#     print(f"The temperature right now is {random_temperature} degrees Celsius.")

#     if random_temperature < 0:
#         print(f"Brrr, that's freezing! Wear some extra layers today")
#     elif random_temperature >= 0 and random_temperature < 16:
#         print(f"Quite chilly! Don't forget your coat")
#     elif random_temperature >= 16 and random_temperature < 24:
#         print(f"Nice weather")
#     elif random_temperature >= 24 and random_temperature < 32:
#         print(f"It's getting hot out here")
#     elif random_temperature >= 32 and random_temperature < 40:
#         print(f"It's way too hot, I'm staying at home.")
#     else:
#         print(f"Woops, something went wrong, the temperature is way too high!")


# main()









    
