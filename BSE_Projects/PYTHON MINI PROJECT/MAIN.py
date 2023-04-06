from BOOK_FUNCTION import BookFunction
from MAGAZINE_FUNCTION import MagazineFunction
from EDUCATIONAL_DVD_FUNCTION import EducationalDVDFunction
from LECTURE_CD_FUNCTION import LectureCDFunction


book_function = BookFunction()
magazine_function = MagazineFunction()
dvd_function = EducationalDVDFunction()
cd_function = LectureCDFunction()



def main_menu():
    print("---MAIN MENU---")
    print()
    print("1 - Books")
    print("2 - Magazine")
    print("3 - Educational DVD")
    print("4 - Lecture CD")
    print("5 - Quit")

    select_option = 1
    while select_option > 0:
        select_option = int(input("\nSELECT YOUR OPTION: "))

        if select_option == 1:
            BookFunction = book_function
            book_sub_menu(BookFunction,"Book")
            
        elif select_option == 2:
            MagazineFunction = magazine_function
            magazine_sub_menu(MagazineFunction, "Magazine")
            
        elif select_option == 3:
            EducationalDVDFunction = dvd_function
            dvd_sub_menu(EducationalDVDFunction, "Educational DVD")
            
        elif select_option == 4:
            LectureCDFunction = cd_function
            cd_sub_menu(LectureCDFunction, "Lecture CD")
            
        elif select_option == 5:
            print("You are exiting...")
            quit()
            
        else:
            print("Error: Invalid Selection!")

    


def book_sub_menu(book_function, select_option):
    selected_function = 1
    while selected_function > 0:
        print("\n---THE FUNCTION LIST---")
        print()
        print(f"1 - Add a {select_option}")
        print(f"2 - Remove a {select_option}")
        print(f"3 - Show Available {select_option}")
        print(f"4 - Show Unavailable {select_option}")
        print(f"5 - Show All {select_option}")
        print(f"6 - Lend {select_option}")
        print(f"7 - Receive {select_option}")
        print(f"8 - Back to Main Menu")
        print(f"9 - Exit")
        selected_function = int(input("Please select a number from the above menu: "))

        if selected_function == 1:
            book_function.add_books()
        elif selected_function == 2:
            book_function.remove_books()
        elif selected_function == 3:
            book_function.show_available_books()
        elif selected_function == 4:
            book_function.show_unavailable_books()
        elif selected_function  == 5:
             book_function.show_all_books()
        elif selected_function == 6:  
            book_function.lend_books()
        elif selected_function == 7:
            book_function.receive_books()
        elif selected_function == 8:
            main_menu()
        elif selected_function == 9:
            print("You are exiting...")
            quit()
        else:
            print("Error: Invalid Selection!")




def magazine_sub_menu(magazine_function, select_option):
    selected_function = 2
    while selected_function > 0:
        print("\n---THE FUNCTIONS LIST---")
        print("")
        print(f"1 - Add a {select_option}")
        print(f"2 - Remove a {select_option}")
        print(f"3 - Show Available {select_option}")
        print(f"4 - Show Unavailable {select_option}")
        print(f"5 - Show All {select_option}")
        print(f"6 - Lend {select_option}")
        print(f"7 - Receive {select_option}")
        print(f"8 - Back to Main Menu")
        print(f"9 - Exit")
        selected_function = int(input("\nPlease select a number from the above menu: "))

        if selected_function == 1:
            magazine_function.add_magazines()
        elif selected_function == 2:
            magazine_function.remove_magazines()
        elif selected_function == 3:
            magazine_function.show_available_magazines()
        elif selected_function == 4:
            magazine_function.show_unavailable_magazines()
        elif selected_function  == 5:
            magazine_function.show_all_magazines()
        elif selected_function == 6:  
            magazine_function.lend_magazines()
        elif selected_function == 7:
            magazine_function.receive_magazines()
        elif selected_function == 8:
            main_menu()
        elif selected_function == 9:
            print("You are exiting...")
            quit()
        else:
            print("Error: Invalid Selection!")
           




def dvd_sub_menu(dvd_function,select_option):
    selected_function = 3
    while selected_function > 0:
        print("\n---THE FUNCTIONS LIST---")
        print("")
        print(f"1 - Add a {select_option}")
        print(f"2 - Remove a {select_option}")
        print(f"3 - Show Available {select_option}")
        print(f"4 - Show Unavailable {select_option}")
        print(f"5 - Show All {select_option}")
        print(f"6 - Lend {select_option}")
        print(f"7 - Receive {select_option}")
        print(f"8 - Back to Main Menu")
        print(f"9 - Exit")
        selected_function = int(input("\nPlease select a number from the above menu: "))

        if selected_function == 1:
            dvd_function.add_DVDs()
        elif selected_function == 2:
            dvd_function.remove_DVDs()
        elif selected_function == 3:
            dvd_function.show_available_DVDs()
        elif selected_function == 4:
            dvd_function.show_unavailable_DVDs()
        elif selected_function  == 5:
            dvd_function.show_all_DVDs()
        elif selected_function == 6:  
            dvd_function.lend_DVDs()
        elif selected_function == 7:
            dvd_function.receive_educationaldvds()
        elif selected_function == 8:
            main_menu()
        elif selected_function == 9:
            print("You are exiting...")
            quit()
        else:
            print("Error: Invalid Selection!")
       



def cd_sub_menu(cd_function, select_option):
    selected_function = 4
    while selected_function > 0:
        print("\n---THE FUNCTIONS LIST---")
        print("")
        print(f"1 - Add a {select_option}")
        print(f"2 - Remove a {select_option}")
        print(f"3 - Show Available {select_option}")
        print(f"4 - Show Unavailable {select_option}")
        print(f"5 - Show All {select_option}")
        print(f"6 - Lend {select_option}")
        print(f"7 - Receive {select_option}")
        print(f"8 - Back to Main Menu")
        print(f"9 - Exit")
        selected_function = int(input("\nPlease select a number from the above menu: "))

        if selected_function == 1:
            cd_function.add_CDs()
        elif selected_function == 2:
            cd_function.remove_CDs()
        elif selected_function == 3:
            cd_function.show_available_CDs()
        elif selected_function == 4:
            cd_function.show_unavailable_CDs()
        elif selected_function  == 5:
            cd_function.show_all_CDs()
        elif selected_function == 6:  
            cd_function.lend_CDs()
        elif selected_function == 7:
            cd_function.receive_lecturecds()
        elif selected_function == 8:
            main_menu()
        elif selected_function == 9:
            print("You are exiting...")
            quit()
        else:
            print("Error: Invalid Selection!")
            
    


print("\n")
print("--------------UNIVERSITY LIBRARY SYSTEM---------------")
print("\n")
main_menu()
