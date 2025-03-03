current_movies = {
    'The Grinch': '11:00am',
    'Rudolph': '1:00pm',
    'Frosty the Snowman': '3:00pm',
    'Christmas Vacation': '5:00pm'
}

print("We're showing the following movies:")
print(", ".join(current_movies.keys()))  # More compact display

movie = input('What movie would you like the showtime for?\n').strip()

# Normalize input for case-insensitive matching
showtime = current_movies.get(movie.title())

if not showtime:
    print("Requested movie isn't playing")
else:
    print(f"{movie} is playing at {showtime}")
