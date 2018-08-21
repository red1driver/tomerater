#=====================================================================================
#   USER CLASS
#=====================================================================================

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "User: {u}; E-mail: {e}; Books read: {b}".format(u=self.name, e=self.email, b=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        return False

    def __hash__(self):
        pass
        #return hash(self.users)

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "User's email has been changed to '{a}'".format(a=address)

    def read_book(self, book, rating=None):
        self.books.update({book:rating})

    def get_average_rating(self):
        v_i = 0
        for v in self.books.values() :
            if v :
                v_i += v
            else :
                return 0
        return v_i / len(self.books.values())


"""
jason = User("Jason Bourne", "jason@blackbriar.org")
john = User("John Wick", "john@continental.net")
#john= User("Jason Bourne", "jason@blackbriar.org")

print(jason)
print(john)
print(jason==john)
"""

#=====================================================================================
#   BOOK CLASS
#=====================================================================================

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "ISBN has been changed to: {i}".format(i=self.isbn)

    def add_rating(self, rating):
        if rating != None:
            if 0 < rating < 4 :
                self.ratings.append(rating)
        else :
            return "Invalid Rating"

    def get_average_rating(self):
        if sum(self.ratings) > 0:
            return round(sum(self.ratings) / len(self.ratings), 2)
        else:
            return 0


#=====================================================================================
#   FICTION SUBCLASS
#=====================================================================================

class Fiction(Book):
    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{t} by {a}".format(t=self.title, a=self.author)

"""
book1 = Book("The Bourne Identity", "0-399-90070-5")
book2 = Fiction("The Bourne Identity", "0-399-90070-5", "Robert Ludlum")
print(book2)
"""

#=====================================================================================
#   NON-FICTION SUBCLASS
#=====================================================================================

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{t}, a {l} manual on {s}".format(t=self.title, l=self.level, s=self.subject)
"""
book3 = Non_Fiction("The Bourne Identity", "Espionage", "Expert", "0-399-90070-5")
print(book3)
"""


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        b = Book(title, isbn)
        return b

    def create_novel(self, title, isbn, author):
        return Fiction(title, isbn, author)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if not self.users[email]:
            print("No user with email {e}!".format(e=email))

        else:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1


    def add_user(self, name, email, books=None):
        u = User(name, email)
        self.users.update({email:u})
        if books:
            for b in books:
                self.add_book_to_user(b, email)
        #print(u)

# Analysis Methods

    def print_catalog(self):
       for b in self.books.keys():
            print(b)

    def print_users(self):
        for u in self.users.values():
            print(u)

    def most_read_book(self):
        most_read = 0
        for b in self.books.values():
            if b > most_read:
                most_read = b
        return most_read

    def highest_rated_book(self):
        highest_rated = {0:0}
        for b in self.books.keys():
            rating = b.get_average_rating()
            if rating > highest_rated[0]:
                highest_rated.update({b:rating})
        return highest_rated[0]

    def most_positive_user(self):
        most_pos = 0
        for u in self.users.values():
            rating = u.get_average_rating()
            if rating > most_pos:
                most_pos = rating
                return u











