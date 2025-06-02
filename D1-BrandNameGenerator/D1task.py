def generate_band_name(verb, city, pet):
    # Generate band names by combining the inputs in creative ways
    band_names = [
        f"The {verb.capitalize()} {city}",
        f"{city.capitalize()} {verb.capitalize()} {pet}",
        f"{pet.capitalize()} of {city}",
        f"The {city} {pet.capitalize()}",
        f"{verb.capitalize()} {pet} and the {city} Crew",
        f"{verb.capitalize()} in {city} with {pet}",
        f"The {city} {verb.capitalize()}s",
        f"{pet.capitalize()} and the {city} {verb.capitalize()}"
    ]
    
    return band_names

# Example usage
verb = input("Enter a verb: ")
city = input("Enter a city name: ")
pet = input("Enter your pet's name: ")

band_names = generate_band_name(verb, city, pet)

print("\nHere are some band name suggestions:")
for name in band_names:
    print(name)
