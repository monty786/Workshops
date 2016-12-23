__author__ ="jc449735"

# Initialize the constants
BOOK_FILE = "books.csv"

def main():
    print("Reading List 1.0 - by Upendra B Thapa")
    book_list=[]
    load_books(book_list)
    display_menu()
    choice=input(">>>").upper()

    while choice !='Q':
        if choice == 'R':
            list_required_books(book_list)
        elif choice =='C':
            list_complete_book(book_list)
        elif choice =='A':
            list_add_new_book(book_list)
        elif choice =='M':
            list_mark_a_book(book_list)
        else:
            print("please enter only the following Alphabets to carry on R,C,A,M")
        choice=input(">>>".upper())
    print("have a great day fudge")



    # end of main()

def load_books(book_list):
    """

    """
    print("load books")

    # end of load_books()
def display_menu():
    print('Menu:')
    print('R - List required books')
    print('C - List completed books')
    print('A - Add new book')
    print('M - Mark a book as completed')
    print('Q - Quit')

def list_required_books(book_list):
    print("required books")

def list_complete_book(book_list):
    print("complete books")

def list_add_new_book(book_list):
    print("add new book to the fray")

def list_mark_a_book(book_list):
    print("mark a book for your likings")

def complete_a_book(book_list):
    """

    """
    print("complete a book")

# end of complete_a_book()

# Start the program
main()