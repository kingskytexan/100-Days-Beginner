# A simple band name generator selecting the city you grew up in and the name of a pet
#   to create a basic band name, in case you needed one.
#   Project based on - strings, variables, and user input

print("Welcome to the Band Name Generator!! Design the band name of your dreams")

# User input for the city the user grew up in and a name of a pet
city = input("What city did you grow up in? ")
pet_name = input("What is the name of your name? ")
band_name = city + " " + pet_name

# Output for the new band name
print(f"This is your band name: {band_name}!!")
