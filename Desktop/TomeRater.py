class User(object):
  #A class for our software users

  
  def __init__(self, name, email):
 #constructor takes in basic user info

    self.name = name
    self.email = email
    self.books = {}




  
  def get_email(self): #A method to obtain user email
    
    return self.email


  def change_email(self, address):
 #Implement a method allowing a specific user's email address to be updated

    self.email = address
    print("User {}\'s email address has been updated to {}.".format(self.name, self.email)
 

  def __repr__(self):
 #Defines a string representation for our user class

    return "User: {name}, email address: {email}, books read: {num_books}.".format(name=self.name, email=self.email, num_books=len(self.books))
  

  def __eq__(self, other_user):
  
    
    if self.name is other_user.name and self.email is other_user.email:
      print("User is the same as one that already exists.")

  
  def read_book(self, book, rating=None): #Implement a method to track users read books

    self.book = book
    if rating: #if user provides a rating
      self.rating=rating

    self.books[book] = rating


  def get_average_rating(self): #Implement a method to get a user's average rating they give books

    values = self.books.values()
    sum = 0
    divisor = len(list(values)) #the number of ratings

    for value in values: #add all the value together
      sum+=value

    return sum/divisor  #avg is the sum of all ratings divided by the number of ratings

#---------------------------------------------------------------------------------------------------------------------------------------------------
class Book(object): #A class for books in our system

  def __init__(self, title, isbn):

    self.title = title
    self.isbn = isbn
    self.ratings = []

  
  def get_title(self): #A method to return the title of a book
    
    return self.title


  def get_isbn(self): #A method to return the isbn number of a book

    return self.isbn

  
  def set_isbn(self, new_isbn): #Implement a method to update a book's isbn 

    self.isbn=new_isbn
    print("{}'s ISBN has been updated to {}".format(self.title, self.isbn))


  def add_rating(self, rating): #Implement a way to add a new rating for a book

    if rating >= 0 and rating <= 4: #valid rating are from 0-4
      self.ratings.append(rating)
 
    else:
      print("Invalid rating")


  def __eq__(self, other_book): #Implement a method to check for book duplicity

    if self.isbn == other_book.isbn:
      print("Books are the same")


  def get_average_rating(self): #implement a method to return the average rating a book has
 
    sum = 0
    for rating in self.ratings:
      sum+=rating

    return sum/len(self.ratings)


  def __hash__(self):

    return hash((self.title, self.isbn))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Fiction(Book): #Create a subclass of books that are fictional

  def __init__(self, title, author, isbn): 

    super().__init__(title, isbn) #Inherit the constructor from the Book class
    self.author = author


  def get_author(self): #Method to return the author
    
    return self.author


  def __repr__(self): #Method to define a string representation that returns author and title

    return "{title} by {author}".format(title=self.title, author=self.author)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Non_Fiction(Book): #Create a second subclass of Books that are non-fictional

  def __init__(self, title, subject, level, isbn):
    
    super().__init__(title, isbn) #Inherit parent's constructor
    self.subject = subject
    self.level = level


  def get_subject(self):
    
    return self.subject


  def get_level(self):

    return self.level


  def __repr__(self):
   
    return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#TOMERATER APPLICATION
#==================================================================================================================================================================

class TomeRater: #Our software for relating users and books

  def __init__(self): 
    
    self.users = {}
    self.books = {}


  def create_book(self, title, isbn): # a method to generate a book for our records

    new_book = Book(title, isbn)
    return new_book


  def create_novel(self, title, author, isbn):

    new_fiction = Fiction(title, author, isbn)
    return new_fiction



  def create_non_fiction(self, title, subject, level, isbn): 

    new_non_fiction = Non_Fiction(title, subject, level, isbn)
    return new_non_fiction


  def add_book_to_user(self, book, email, rating=None):

    if email in self.users.keys():
      user = self.users[email] #gets user associated with email
      User.read_book(book, rating)
      Book.add_rating(rating)

      if book in self.books.keys():
        self.books[book]+=1
      else:
        self.books[book] = 1

    else:
      print("No user with email {}!".format(email)


  def add_user(self, name, email, user_books=None):

    new_user = User(name, email)

    if user_books:
      for book in user_books: #loop through each book in the list
        add_book_to_user(book, email)


  def print_catalog(self):
 
    for book in self.books.keys(): #print each book in our catalog of books
      print(book) 


  def print_users(self):
  
    for user in self.users.keys():
      print(user)


  def most_read_book(self):

    reads = 0 #default starting value
    most_read = "" #default book title

    for book, times_read in self.books.items(): #self.books is a key value pair where the key is the book and the value is the #times it has been read
      
      if times_read > reads: #if the value associated with a particular book is greater than our previous reads value...
        reads = times_read #update the reads counter
        most_read = book  #update our most read title

      else:
        continue

    return most_read



  def highest_rated_book(self):


    highest= 0

    for book in self.books.keys(): #for every book in our catalog

      if book.get_average_rating() > highest:
        highest = book.get_average_rating()
      
      else:
        continue
    
    return highest


  def most_positive_user(self):

    highest = 0
    for user in self.users.keys():

      if user.get_average_rating() > highest:
        highest = user.get_average_rating()

      else:
        continue

    return highest    
    
