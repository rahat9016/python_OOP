import datetime
import os

# os.getcwd()


class LMS:
    """
        this class is used to keep record of books library 
        It has total module: "Display books", "Issue Books", "Returns Books", "Add Books"
    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}

        ID = 101
        with open (self.list_of_books) as bk:
            content = bk.readlines()
        
        for line in content:
            self.books_dict.update({str(ID): {"book_title": line.replace("\n", ""), "lender_name": "", "issue_date": "", "status": "Available"}})
            ID +=1
        
    def display_books(self):
        print("-------------------Book List-------------------")
        print("Book ID", "\t", "Title", "\t", "Status")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("book_title"), "\t", "[", value.get("status"),']')

    def issue_books(self):
        book_id = input("Enter your Book ID:-")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d - %H:%M:%S")

        if book_id in self.books_dict.keys():
            if not self.books_dict[book_id]['status'] == 'Available':
                print(f"This book already issue to {self.books_dict[book_id]['lender_name']} on {self.books_dict[book_id]['issue_date']}")
            elif self.books_dict[book_id]['status'] == 'Available':
                your_name =  input("Enter your name:-")
                self.books_dict[book_id]['lender_name'] = your_name
                self.books_dict[book_id]['issue_date'] = current_date
                self.books_dict[book_id]['status'] = "Already Issued"
                print("Book issue successfully!!!")
        else:
            print("Book id not found in book list")
    
    def add_book(self):
        new_book = input("Enter book title:-")
        if new_book == "":
            return self.add_book()
        elif len(new_book) > 25:
            print("Book title is to long. title length shoud be 20 chars.")
        else:
            with open(self.list_of_books, 'a') as bk:
                bk.writelines(f"{new_book}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1): {"book_title": new_book, "lender_name": "", "issue_date": "", "status": "Available"}})
                print(f"this book {new_book} has been added successfully.")

    def return_books(self):
        book_id = input("Enter your Book ID:-")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]["status"] == "Available":
                print("This book already available in library. Please correct Book ID")
            elif not self.books_dict[book_id]["status"] == "Available":
                self.books_dict[book_id]['lender_name'] = ""
                self.books_dict[book_id]['issue_date'] = ""
                self.books_dict[book_id]['status'] = "Available"
                print("Book return back successfully!!!")
        else:
            print("Book ID not found in book list")

    
    
try:
    myLMS = LMS("list_of_books.txt", "python")
    press_key_list = {"D": "Display Books", "I":"Issue book", "A":"Add New Book", "R":"Return Books", "Q":"Quit"}

    key_press = False
    while not (key_press == "q"):
        print(f"\n Welcome to {myLMS.library_name} library management system\n")
        for key, value in press_key_list.items():
            print(f"Press {key} To {value}")
        key_press = input("Press key:- ").lower()

        if key_press == 'i':
            print("\n Current selection : Issue book")
            myLMS.issue_books()
        elif key_press == 'a':
            print("\n Current selection : Add book")
            myLMS.add_book()
        elif key_press == 'd':
            print("\n Current selection : Display book")
            myLMS.display_books()
        elif key_press == 'r':
            print("\n Current selection : Return book")
            myLMS.return_books()
        elif key_press == 'q':
            break
        else:
            continue
except Exception as e:
    print("Something went wrong! Please try again.", e)
