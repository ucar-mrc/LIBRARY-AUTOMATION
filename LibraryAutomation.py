import os
import shutil

#FUNCTION FOR BOOKS
class Book:
    def _init_(self, barcode, bookname, author, publishing_house, release_date, inventory):
        self.barcode = barcode
        self.bookname = bookname
        self.author = author
        self.publishing_house = publishing_house
        self.release_date = release_date
        self.inventory = inventory

#FUNCTION FOR MEMBERS
class Member:
    def _init_(self, i_n, name_surname, birthdate, phone_number, address, situation):
        self.i_n = i_n
        self.name_surname = name_surname
        self.birthdate = birthdate
        self.phone_number = phone_number
        self.address = address
        self.situation = situation

# BOOK ADDITION SCREEN
def add_book():
    print("BOOK ADDITION SCREEN: ")
    barcode = int(input("BARCODE NUMBER OF THE BOOK YOU WANT TO ADD: "))
    bookname = input("ENTER THE TITLE OF THE BOOK YOU WANT TO ADD: ")
    author = input("AUTHOR OF THE BOOK YOU WANT TO ADD: ")
    publishing_house = input("PUBLISHER OF THE BOOK YOU WANT TO ADD: ")
    release_date = int(input("PUBLICATION DATE OF THE BOOK YOU WANT TO ADD: "))
    inventory = int(input("BOOK STOCK NUMBER: "))
    with open("Books.data", "a") as file:
        file.write(f"{barcode},{bookname},{author},{publishing_house},{release_date},{inventory}\n")
    print("book registration completed.")

#BOOK DELETION SCREEN
def delete_book():
    print("BOOK DELETION SCREEN: ")
    bbarcode = int(input("BARCODE NUMBER OF THE BOOK YOU WANT TO DELETE: "))
    result = 0
    try:
        with open("Books.data", "r") as file:
            lines = file.readlines()
        with open("backup.data", "w") as new_file:
            for line in lines:
                if str(bbarcode) not in line:
                    new_file.write(line)
                else:
                    result = 1
        if result == 0:
            print(f"{bbarcode} BOOK WITH BARCODE NUMBER NOT FOUND.")
        else:
            os.remove("Books.data")
            os.rename("backup.data", "Books.data")
            print(f"{bbarcode} BOOK WITH BARCODE NUMBER DELETED.")
    except FileNotFoundError:
        print("Books.data file not found.")

#BOOK OPERATIONS MENU
def book_transactions():
    print("BOOK TRANSACTIONS SCREEN: ")
    print(" 1-ADD BOOK")
    print(" 2-BOOK DELETE")
    print(" 3-LIST BOOKS")
    print(" 0-BACK TO MAIN MENU")
    selection = int(input("YOUR CHOICE: "))
    if selection == 1:
        add_book()
    elif selection == 2:
        delete_book()
    elif selection == 3:
        book_list()
    elif selection == 0:
        pass
    else:
        print("YOU HAVE MADE AN INCORRECT SELECTION. YOU ARE REDIRECTED TO THE MAIN MENU...")

#book listing function
def book_list():
    print("BOOK LIST SCREEN: ")
    number_of_books = 0
    try:
        with open("Books.data", "r") as file:
            print("%-20s%-20s%-20s%-20s%-20s%-20s" % ("BOOK-BARCODE", "BOOK-NAME", "BOOK-AUTHOR", "BOOK-PUBLISHER", "BOOK-PUBLICATION DATE", "BOOK-STOCK"))
            for line in file:
                data = line.strip().split(",")
                print("%-20s%-20s%-20s%-20s%-20s%-20s" % tuple(data))
                number_of_books += int(data[-1])
        print("\n TOTAL NUMBER OF BOOKS :", number_of_books)
    except FileNotFoundError:
        print("Books.data file not found.")

#MEMBER ADDITION FUNCTION
def add_member():
    print("MEMBER ADDITION SCREEN: ")
    i_n = input("MEMBER'S ID NUMBER: ")
    name_surname = input("ENTER MEMBER'S NAME AND SURNAME: ")
    birthdate = input("MEMBER'S DATE OF BIRTH: ")
    phone_number = input("ENTER THE MEMBER'S TELEPHONE NUMBER: ")
    address = input("MEMBER'S ADDRESS: ")
    situation = 0
    with open("members.data", "a") as file:
        file.write(f"{i_n},{name_surname},{birthdate},{phone_number},{address},{situation}\n")
    print("MEMBER REGISTRATION COMPLETED.")

#MEMBER DELETION FUNCTION
def delete_member():
    print("MEMBER DELETION SCREEN: ")
    i_n = input("ID NUMBER OF THE MEMBER YOU WANT TO DELETE: ")
    result = 0
    try:
        with open("members.data", "r") as file:
            lines = file.readlines()
        with open("backup.data", "w") as new_file:
            for line in lines:
                if i_n not in line:
                    new_file.write(line)
                else:
                    result = 1
        if result == 0:
            print(f"{i_n} NO MEMBER WITH ID NUMBER FOUND.")
        else:
            os.remove("members.data")
            os.rename("backup.data", "members.data")
            print(f"{i_n} MEMBER WITH ID NUMBER DELETED.")
    except FileNotFoundError:
        print("members.data file not found.")

#MEMBER LISTING FUNCTION
def member_list():
    print("MEMBER LIST SCREEN: ")
    number_of_members = 0
    try:
        with open("members.data", "r") as file:
            print("%-20s%-30s%-20s%-20s%-20s%-20s" % ("MEMBER IDENTIFICATION NO.", "MEMBER NAME-SURNAME", "MEMBER DATE OF BIRTH", "MEMBER PHONE NUMBER", "MEMBER ADDRESS", "MEMBER SITUATION"))
            for line in file:
                data = line.strip().split(",")
                print("%-20s%-30s%-20s%-20s%-20s%-20s" % tuple(data))
                number_of_members += 1
        print("\n TOTAL NUMBER OF MEMBERS :", number_of_members)
    except FileNotFoundError:
        print("members.data file not found.")

#MEMBER TRANSACTIONS SCREEN
def member_transactions():
    print("MEMBER TRANSACTIONS SCREEN: ")
    print(" 1-ADD MEMBER")
    print(" 2-DELETE MEMBER")
    print(" 3-LIST MEMBERS")
    print(" 0-BACK TO MAIN MENU")
    selection = int(input("YOUR CHOICE: "))
    if selection == 1:
        add_member()
    elif selection == 2:
        delete_member()
    elif selection == 3:
        member_list()
    elif selection == 0:
        pass
    else:
        print("YOU HAVE MADE AN INCORRECT SELECTION. YOU ARE REDIRECTED TO THE MAIN MENU...")

def menu():
    print("\n ** LIBRARY AUTOMATION ** ")
    print("\n 1- BOOK PROCESSING ")
    print("\n 2- MEMBER TRANSACTIONS ")
    print("\n 0- EXIT ")
    selection = int(input("\n YOUR CHOICE: "))
    return selection

def main():
    selection = menu()
    while selection != 0:
        if selection == 1:
            book_transactions()
        elif selection == 2:
            member_transactions()
        else:
            print("YOU MADE A WRONG CHOICE.")
        selection = menu()

if _name_ == "_main_":
    main()