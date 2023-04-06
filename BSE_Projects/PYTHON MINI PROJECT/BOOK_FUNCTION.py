from BOOK import Book

def print_book(book):
    print(f"ISBN_NO:{book.ISBN_no}, Book Title:{book.title}, Book Format:{book.format_of_book}, Book Subject:{book.subject}, Book Rental Price Per Day:{book.rental_price_per_day}, Available Book Copies:{book.no_of_copies}")

class BookFunction:
    
    def __init__(self):
        self.list_of_books = []
        self.__initial_data()


    def __initial_data(self):
        book1 = Book(ISBN_no = "ISBN1234",title = "The Solar System",format_of_book="Hardcover",subject = "Science", rental_price_per_day = 15.00, no_of_copies=5)

        book2 = Book(ISBN_no = "ISBN9876",title = "Types of Animal Species",format_of_book="Paperback",subject = "Science", rental_price_per_day= 10.00,no_of_copies=8)
        
        book3 = Book(ISBN_no = "ISBN1290",title = "Second World War",format_of_book="Hardcover",subject = "History", rental_price_per_day = 12.50 ,no_of_copies = 1)
    
        self.list_of_books.append(book1)
        self.list_of_books.append(book2)
        self.list_of_books.append(book3)

 
    def add_books(self):
        __ISBN_no = input("Enter your book ISBN number: ")
        __title = input("Enter the book title: ")
        __format_of_book = input("Enter the book format: ")
        __subject = input("Enter the book subject: ")
        __rental_price_per_day = float(input("Enter the rental price per day: "))
        __no_of_copies = int(input("Enter number of copies: "))
    
        new_book = Book(ISBN_no = __ISBN_no,
                     title = __title,
                     format_of_book = __format_of_book,
                     subject = __subject,
                     rental_price_per_day = __rental_price_per_day,
                     no_of_copies = __no_of_copies)
        
        self.list_of_books.append(new_book)
        print("Notice: The book is added to the list.")


    def remove_books(self):
        __ISBN_NO = input("Enter ISBN number: ")
        value = list(i for i in self.list_of_books if i.ISBN_no == __ISBN_NO)
        for i in value:
            self.list_of_books.remove(i)
            print("Notice:",__ISBN_NO, "book is removed from the list.")


    def show_available_books(self):
        value = list(i for i in self.list_of_books if i.no_of_copies > 0)
        for i in value:
            print_book(book=i)


    def show_unavailable_books(self):
        value = list(i for i in self.list_of_books if i.no_of_copies == 1)
        for i in value:
            print_book(book=i)

            
    def show_all_books(self):
        for i in self.list_of_books:
            print_book(book=i)


    def lend_books(self):
        __ISBN_NO = input("Enter ISBN number: ")
        __no_of_copies = int(input("Enter number of lend copies: "))
        value = list(i for i in self.list_of_books if i.ISBN_no == __ISBN_NO)
        for i in value:
            i.no_of_copies -= __no_of_copies
            print("Notice:",__ISBN_NO, "book is lent.")


    def receive_books(self):
        __ISBN_NO = input("Enter ISBN number: ")
        __no_of_copies = int(input("Enter number of received books: "))
        value = list(i for i in self.list_of_books if i.ISBN_no == __ISBN_NO)
        for i in value:
            i.no_of_copies += __no_of_copies
            print("Notice:",__ISBN_NO, "book is received.")


