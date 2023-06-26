from AuthorCRUD import AuthorCRUD
from BookCRUD import BookCRUD
from database import Database

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.211.171.57:7687", "neo4j", "journal-relief-countermeasure")

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
book_db = BookCRUD(db)
author_db = AuthorCRUD(db)

choice = input("Make your choice\n"
               "1 - Create Author\n"
               "2 - Read Author\n"
               "3 - Update Author\n"
               "4 - Delete Author\n"
               "5 - Create Book\n"
               "6 - Read Book\n"
               "7 - Update Book\n"
               "8 - Delete Book\n"
               "9 - Link book with author\n"
               "10 - Author's books\n"
               "11 - Books average pages\n"
               "0 - Exit\n"
               )

while choice != "0":

    if choice == "1":
        name = input("Author name: ")
        age = input("Author age: ")
        gender = input("Author gender: ")
        author_db.create_author(name, age, gender)

    if choice == "2":
        print("Authors")
        print("--------------------")
        author_db.get_author()
        print("--------------------\n")

    if choice == "3":
        name = input("Author name: ")
        age = input("New age: ")
        gender = input("New gender: ")
        author_db.update_author(name, age, gender)

    if choice == "4":
        name = input("Author name:")
        author_db.delete_author(name)

    if choice == "5":
        name = input("Book name: ")
        pages = input("Book pages: ")
        genre = input("Book genre: ")
        book_db.create_book(name, pages, genre)

    if choice == "6":
        print("Books")
        print("--------------------")
        book_db.get_book()
        print("--------------------\n")

    if choice == "7":
        name = input("Book name: ")
        pages = input("New pages: ")
        genre = input("New genre: ")
        book_db.update_book(name, pages, genre)

    if choice == "8":
        name = input("Book name: ")
        book_db.delete_book(name)

    if choice == "9":
        authorname = input("Author name: ")
        bookname = input("Book name: ")
        author_db.insert_author_book(authorname, bookname)

    if choice == "10":
        name = input("Author name: ")
        print(name, "books:")
        print("--------------------")
        print(author_db.get_wrote(name))
        print("--------------------\n")

    if choice == "11":
        print("--------------------")
        print("Average number of pages in books:")
        print(book_db.get_book_avg_pages())
        print("--------------------\n")


    choice = input("Make your choice\n"
                   "1 - Create Author\n"
                   "2 - Read Author\n"
                   "3 - Update Author\n"
                   "4 - Delete Author\n"
                   "5 - Create Book\n"
                   "6 - Read Book\n"
                   "7 - Update Book\n"
                   "8 - Delete Book\n"
                   "9 - Link book with author\n"
                   "10 - Author's books\n"
                   "11 - Books average pages\n"
                   "0 - Exit\n"
                   )
