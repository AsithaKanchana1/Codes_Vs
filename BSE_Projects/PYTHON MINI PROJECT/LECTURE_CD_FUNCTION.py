from LECTURE_CD import LectureCD

def print_LectureCD(lecturecd):
    print(f"LectureCD Number:{lecturecd.CD_no}, CD Title:{lecturecd.CD_title}, CD subject:{lecturecd.CD_subject}, CD Rental Price Per Day:{lecturecd.rental_price_per_day}, Available CD copies:{lecturecd.no_of_copies}")

class LectureCDFunction:
    
    def __init__(self):
        self.list_of_lecturecds = []
        self.__initial_data()


    def __initial_data(self):
        cd1 = LectureCD(CD_no = "21",CD_title = "Basics of Western Music", CD_subject = "Music", rental_price_per_day = 1.50, no_of_copies = 11)

        cd2 = LectureCD(CD_no = "22",CD_title = "Japanese Language", CD_subject = " Foreign Languages", rental_price_per_day = 2.00, no_of_copies = 3)

        self.list_of_lecturecds.append(cd1)
        self.list_of_lecturecds.append(cd2)

 
    def add_CDs(self):
        __CD_no = input("Enter your CD number: ")
        __title = input("Enter the CD title: ")
        __subject = input("Enter the CD subject: ")
        __rental_price_per_day = float(input("Enter the rental price per day: "))
        __no_of_copies = int(input("Enter number of copies: "))
    
        new_CD = LectureCD(CD_no = __CD_no, CD_title = __title, CD_subject = __subject, rental_price_per_day = __rental_price_per_day, no_of_copies = __no_of_copies)
        
        self.list_of_lecturecds.append(new_CD)
        print("Notice: The CD is added to the list.")


    def remove_CDs(self):
        __CD_no = input("Enter CD number to remove: ")
        value = list(i for i in self.list_of_lecturecds if i.CD_no == __CD_no)
        for i in value:
            self.list_of_lecturecds.remove(i)
            print("Notice:",__CD_no, "CD is removed from the list.")


    def show_available_CDs(self):
        value = list(i for i in self.list_of_lecturecds if i.no_of_copies > 0)
        for i in value:
            print_LectureCD(lecturecd=i)


    def show_unavailable_CDs(self):
        value = list(i for i in self.list_of_lecturecds if i.no_of_copies == 1)
        for i in value:
            print_LectureCD(lecturecd=i)

            
    def show_all_CDs(self):
        for i in self.list_of_lecturecds:
            print_LectureCD(lecturecd=i)


    def lend_CDs(self):
        __CD_no = input("Enter the CD number to lend: ")
        __no_of_copies = int(input("Enter number of lend copies: "))
        value = list(i for i in self.list_of_lecturecds if i.CD_no == __CD_no)
        for i in value:
            i.no_of_copies -= __no_of_copies
            print("Notice:",__CD_no, "CD is lent.")


    def receive_lecturecds(self):
        __CD_no = input("Enter CD number to receive: ")
        __no_of_copies = int(input("Enter number of received CDs: "))
        value = list(i for i in self.list_of_lecturecds if i.CD_no == __CD_no)
        for i in value:
            i.no_of_copies += __no_of_copies
            print("Notice:",__CD_no, "CD is received.")


