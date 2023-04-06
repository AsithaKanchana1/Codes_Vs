from EDUCATIONAL_DVD import EducationalDVD

def print_EducationalDVD(educationaldvd):
    print(f"EducationalDVD Number:{educationaldvd.DVD_no}, DVD Title:{educationaldvd.DVD_title}, DVD subject:{educationaldvd.DVD_subject}, DVD Rental Price Per Day:{educationaldvd.rental_price_per_day}, Available DVD copies:{educationaldvd.no_of_copies}")

class EducationalDVDFunction:
    
    def __init__(self):
        self.list_of_educationaldvds = []
        self.__initial_data()


    def __initial_data(self):
        dvd1 = EducationalDVD(DVD_no = "10",DVD_title = "Birth of the Solar System", DVD_subject = "Astronomy", rental_price_per_day = 2.50, no_of_copies = 10)

        dvd2 = EducationalDVD(DVD_no = "11",DVD_title = "Pythagoras Theorem", DVD_subject = "Math", rental_price_per_day = 1.00, no_of_copies = 50)

        self.list_of_educationaldvds.append(dvd1)
        self.list_of_educationaldvds.append(dvd2)

 
    def add_DVDs(self):
        __dvd_no = input("Enter your DVD number: ")
        __title = input("Enter the DVD title: ")
        __subject = input("Enter the DVD subject: ")
        __rental_price_per_day = float(input("Enter the rental price per day: "))
        __no_of_copies = int(input("Enter number of copies: "))
    
        new_dvd = educationaldvd(DVD_no = __dvd_no,
                                 DVD_title = __title,
                                 DVD_subject = __subject,
                                 rental_price_per_day = __rental_price_per_day,
                                 no_of_copies = __no_of_copies)
        
        self.list_of_educationaldvds.append(new_dvd)
        print("Notice: The DVD is added to the list.")


    def remove_DVDs(self):
        __dvd_no = input("Enter DVD number to remove: ")
        value = list(i for i in self.list_of_educationaldvds if i.DVD_no == __dvd_no)
        for i in value:
            self.list_of_educationaldvds.remove(i)
            print("Notice:",__dvd_no, "DVD is removed from the list.")


    def show_available_DVDs(self):
        value = list(i for i in self.list_of_educationaldvds if i.no_of_copies > 0)
        for i in value:
            print_EducationalDVD(educationaldvd=i)


    def show_unavailable_DVDs(self):
        value = list(i for i in self.list_of_educationaldvds if i.no_of_copies == 1)
        for i in value:
            print_EducationalDVD(educationaldvd=i)

            
    def show_all_DVDs(self):
        for i in self.list_of_educationaldvds:
            print_EducationalDVD(educationaldvd=i)


    def lend_DVDs(self):
        __dvd_no = input("Enter the DVD number to lend: ")
        __no_of_copies = int(input("Enter number of lend copies: "))
        value = list(i for i in self.list_of_educationaldvds if i.DVD_no == __dvd_no)
        for i in value:
            i.no_of_copies -= __no_of_copies
            print("Notice:",__dvd_no, "DVD is lent.")


    def receive_educationaldvds(self):
        __dvd_no = input("Enter DVD number to receive: ")
        __no_of_copies = int(input("Enter number of received DVDs: "))
        value = list(i for i in self.list_of_educationaldvds if i.DVD_no == __dvd_no)
        for i in value:
            i.no_of_copies += __no_of_copies
            print("Notice:",__dvd_no, "DVD is received.")


