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
            ## 
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

LMS("list_of_books.txt", "python").display_books()