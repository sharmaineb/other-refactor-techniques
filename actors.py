# by Kami Bigdely
# Extract class
class Actor:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def send_hiring_email(self):
        print("Email sent to:", self.email)

actors = [
    Actor('Elizabeth', 'Debicki', 1990, ['Tenet', 'Vita & Virgina', 'Guardians of the Galaxy', 'The Great Gatsby'],
          'deb@makeschool.com'),
    Actor('Jim', 'Carrey', 1962, ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man'],
          'jim@makeschool.com')
]

for actor in actors:
    if actor.birth_year > 1985:
        print(actor.first_name, actor.last_name)
        print('Movies Played:', ', '.join(actor.movies))
        actor.send_hiring_email()
