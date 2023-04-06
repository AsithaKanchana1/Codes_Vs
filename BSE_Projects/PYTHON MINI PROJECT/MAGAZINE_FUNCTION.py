from MAGAZINE import Magazine

def print_magazine(magazine):
    print(f"Magazine Number:{magazine.magazine_no}, Magazine Title:{magazine.title},  Magazine Color:{magazine.color}, Magazine Subject:{magazine.subject}, Magazine Rental Price Per Day:{magazine.rental_price_per_day}, Available magazine copies:{magazine.no_of_copies}")

class MagazineFunction:
    
    def __init__(self):
        self.list_of_magazines = []
        self.__initial_data()


    def __initial_data(self):
        magazine1 = Magazine(magazine_no = "01",title = "History of Cricket", color="color",subject = "Sports", rental_price_per_day = 5.00, no_of_copies = 7)

        magazine2 = Magazine(magazine_no = "02",title = "Evolution of the Computer", color=" black&white",subject = "Technology", rental_price_per_day = 3.00, no_of_copies = 21)        

        self.list_of_magazines.append(magazine1)
        self.list_of_magazines.append(magazine2)

 
    def add_magazines(self):
        __magazine_no = input("Enter your Magazine number: ")
        __title = input("Enter the Magazine title: ")
        __color = input("Enter the Magazine color: ")
        __subject = input("Enter the Magazine subject: ")
        __rental_price_per_day = float(input("Enter the rental price per day: "))
        __no_of_copies = int(input("Enter number of copies: "))
    
        new_magazine = Magazine(magazine_no = __magazine_no,
                     title = __title,
                     color = __color,
                     subject = __subject,
                     rental_price_per_day = __rental_price_per_day,
                     no_of_copies = __no_of_copies)
        
        self.list_of_magazines.append(new_magazine)
        print("Notice: The magazine is added to the list.")


    def remove_magazines(self):
        __magazine_no = input("Enter magazine number to remove: ")
        value = list(i for i in self.list_of_magazines if i.magazine_no == __magazine_no)
        for i in value:
            self.list_of_magazines.remove(i)
            print("Notice:",__magazine_no, "magazine is removed from the list.")


    def show_available_magazines(self):
        value = list(i for i in self.list_of_magazines if i.no_of_copies > 0)
        for i in value:
            print_magazine(magazine=i)


    def show_unavailable_magazines(self):
        value = list(i for i in self.list_of_magazines if i.no_of_copies == 1)
        for i in value:
            print_magazine(magazine=i)

            
    def show_all_magazines(self):
        for i in self.list_of_magazines:
            print_magazine(magazine=i)


    def lend_magazines(self):
        __magazine_no = input("Enter magazine number to lend: ")
        __no_of_copies = int(input("Enter number of lend copies: "))
        value = list(i for i in self.list_of_magazines if i.magazine_no == __magazine_no)
        for i in value:
            i.no_of_copies -= __no_of_copies
            print("Notice:",__magazine_no, "magazine is lent.")


    def receive_magazines(self):
        __magazine_no = input("Enter magazine number to receive: ")
        __no_of_copies = int(input("Enter number of received magazines: "))
        value = list(i for i in self.list_of_magazines if i.magazine_no == __magazine_no)
        for i in value:
            i.no_of_copies += __no_of_copies
            print("Notice:",__magazine_no, "magazine is received.")


